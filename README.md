# python_assesment_image_compressor


Image Processing Application Documentation and API Guide
Overview
This Flask application facilitates the asynchronous processing of image data from CSV files. It allows users to upload CSV files containing image URLs, compresses the images, stores them locally, and tracks the processing status.

Routes and Endpoints
Homepage

Route: /
Method: GET
Description: Renders the main page of the application where users can upload CSV files.
Check Server Status

Route: /online
Method: GET
Description: Checks if the server is up and running.
Upload CSV File

Route: /upload_csv
Method: POST
Description: Uploads a CSV file containing image data. Initiates asynchronous processing of images.
Check Processing Status

Route: /status/<request_id>
Method: GET
Parameters:
<request_id>: Unique identifier for the request.
Description: Retrieves the current processing status and CSV file location for a given request ID.
Installation and Setup
Prerequisites

Python 3.x installed on your system.
Pip (Python package installer) installed.
Clone the Repository

bash
Copy code
git clone <repository_url>
cd image_processor
Install Dependencies

bash
Copy code
pip install -r requirements.txt
Configure the Application

Modify config.py as per your requirements (e.g., upload folder path).
Run the Application

bash
Copy code
python app.py
This starts the Flask development server.
Access the Application

Open a web browser and go to http://localhost:5000/ to access the application.