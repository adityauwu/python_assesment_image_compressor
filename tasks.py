import csv
import os
import time
from utils import download_and_compress_images, update_csv_with_output_image_paths, update_tracking_status

def process_images(request_id):
    print(f"Processing {request_id} : the CSV file in background!!")
    csv_path = os.path.join('uploads', f'{request_id}.csv')
    
    with open(csv_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        entries = list(reader)
    
    # Ensure 'Output Image Urls' column is added to each entry
    for entry in entries:
        entry['Output Image Urls'] = ''
    
    for entry in entries:
        product_name = entry['Product Name']
        image_urls = entry['Input Image Urls'].split(',')
        local_image_paths = []
        for url in image_urls:
            try:
                local_path = download_and_compress_images(url.strip(), request_id, product_name)
                print(f"the path for image is : {local_path}")
                local_image_paths.append(local_path)
            except Exception as err:
                print(f"Error processing image {url}: {err}")
                continue
        
        if local_image_paths:
            entry['Output Image Urls'] = ','.join(local_image_paths)
        else:
            print("error processing image")
            entry['Output Image Urls'] = 'Error processing images'
    
    # Write updated entries back to the CSV
    with open(csv_path, 'w', newline='') as csv_file:
        fieldnames = list(entries[0].keys())
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(entries)
    time.sleep(3) 
    update_tracking_status(request_id, "completed", csv_path)