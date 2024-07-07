import csv
import os
import requests
from PIL import Image
from io import BytesIO
import pandas as pd
from config import TRACKING_FILE

def save_csv(file, request_id):
    os.makedirs('uploads', exist_ok=True)
    save_path = os.path.join('uploads', f'{request_id}.csv')

    # Read the CSV file into a DataFrame
    df = pd.read_csv(file, header=None)
    
    # Set the column names
    df.columns = ['S. No.', 'Product Name', 'Input Image Urls']
    
    # Save the DataFrame to a CSV file
    df.to_csv(save_path, index=False)
    
    log_request(request_id, save_path)

def validate_csv(file):
    try:
        # Read the first few lines to sniff the dialect and check the header
        sample = file.read(1024).decode('utf-8')
        dialect = csv.Sniffer().sniff(sample)
        file.seek(0)
        
        # Create a CSV reader object
        reader = csv.reader(file, dialect)
        
        # Get the header row
        header = next(reader)
        
        # Define the required columns
        required_columns = ["S. No.", "Product Name", "Input Image Urls"]
        
        # Check if all required columns are present
        if all(column in header for column in required_columns):
            return True
        else:
            print("columns missing")
            return False
    except (csv.Error, UnicodeDecodeError):
        return csv.Error

def download_and_compress_images(url, request_id, product_name):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = img.convert("RGB")
    
    output_folder = os.path.join('compressed_images', request_id)
    os.makedirs(output_folder, exist_ok=True)
    
    image_name = f"{product_name}_{os.path.basename(url)}"
    compressed_path = os.path.join(output_folder, image_name)
    
    img.save(compressed_path, "JPEG", quality=50)
    return compressed_path

def update_csv_with_output_image_paths(entries, csv_path):
    fieldnames = entries[0].keys()
    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(entries)

def log_request(request_id, csv_path):
    os.makedirs(os.path.dirname(TRACKING_FILE), exist_ok=True)
    if not os.path.exists(TRACKING_FILE):
        with open(TRACKING_FILE, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["request_id", "csv_path", "status"])

    with open(TRACKING_FILE, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([request_id, csv_path, 'processing'])

def update_tracking_status(request_id, status, csv_location=None):
    rows = []
    with open(TRACKING_FILE, 'r') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

    with open(TRACKING_FILE, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in rows:
            if row[0] == request_id:
                row[2] = status
                if csv_location:
                    row[1] = csv_location
            writer.writerow(row)

def get_processing_status(request_id):
    with open(TRACKING_FILE, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == request_id:
                return row[2], row[1]
    return 'not found', None
