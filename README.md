# python_assesment_image_compressor


Image Processing Application Documentation and API Guide
Overview
This Flask application facilitates the asynchronous processing of image data from CSV files. It allows users to upload CSV files containing image URLs, compresses the images, stores them locally, and tracks the processing status.

Routes and Endpoints
Homepage

**Route: /**
Method: GET
Description: Renders the main page of the application where users can upload CSV files.


**Route: /online**
Method: GET
Description: Checks if the server is up and running.
Upload CSV File

**Route: /upload_csv**
Method: POST
Description: Uploads a CSV file containing image data. Initiates asynchronous processing of images.
Check Processing Status

**Route: /status/<request_id>**
Method: GET
Parameters:
<request_id>: Unique identifier for the request.
Description: Retrieves the current processing status and CSV file location for a given request ID.
![image](https://github.com/adityauwu/python_assesment_image_compressor/assets/64534738/2c94dd78-77c1-4919-aa61-64732fa2090d)
![image](https://github.com/adityauwu/python_assesment_image_compressor/assets/64534738/1e4dc496-828c-47dc-93bc-d79491554ce8)
![image](https://github.com/adityauwu/python_assesment_image_compressor/assets/64534738/79859241-7ada-408e-811e-ae4b1e48cea1)




**Installation and Setup**



git clone <repo>

pip install -r requirements.txt

python app.py


Open a web browser and go to http://localhost:5000/ to access the application.
