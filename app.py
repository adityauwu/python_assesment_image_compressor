from flask import Flask, request, jsonify , render_template
import uuid
import os
from concurrent.futures import ThreadPoolExecutor
from utils import save_csv, validate_csv, get_processing_status
from tasks import process_images

app = Flask(__name__)
app.config.from_object('config')

executor = ThreadPoolExecutor(max_workers=4)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/online', methods=['GET'])
def status():

    return "Server is up"


@app.route('/upload_csv', methods=['POST'])
def upload_csv():
    file = request.files['file']
    if not validate_csv(file):
        return jsonify({"error": "Invalid CSV format"}), 400

    request_id = str(uuid.uuid4())
    save_csv(file, request_id)
    executor.submit(process_images, request_id)
    return jsonify({"request_id": request_id})

@app.route('/status/<request_id>', methods=['GET'])
def check_status(request_id):
    status, csv_location = get_processing_status(request_id)
    return jsonify({"status": status, "csv_location": csv_location})

if __name__ == '__main__':
    app.run(debug=True)
