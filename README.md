# Receipt Processor API

## Overview

The **Receipt Processor API** is a simple web service built using **Flask** (Python) that allows users to submit receipt data in JSON format and calculates reward points based on the total amount spent. The service processes receipts, assigns reward points, and returns the results for further use. This project is designed to demonstrate the functionality of building APIs using Flask, handling JSON data, and processing requests and responses.

## Features

- **POST /receipts/process**: Submit receipt data to calculate reward points.
- **GET /receipts/{receipt_id}**: Retrieve the reward points for a specific receipt based on a unique receipt ID.

## Technologies

- **Python**: Backend programming language.
- **Flask**: Web framework to build the API.
- **Docker**: For easy deployment and containerization.
- **Postman or cURL**: For API testing.

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/receipt-processor.git
   cd receipt-processor

2. Install dependencies:

Make sure you have Python installed, then install the required Python libraries

3. Run the application:

Start the Flask app by running the following command:
flask run

API Endpoints
1. POST /receipts/process
Description: Submit a receipt in JSON format to calculate reward points based on the total amount.

2. GET /receipts/{receipt_id}
Description: Retrieve the reward points for a given receipt ID.

How to Test
You can test the API using Postman or cURL by sending POST and GET requests to the relevant endpoints:

POST Request: Submit receipt data to /receipts/process.
GET Request: Retrieve the reward points for a specific receipt using /receipts/{receipt_id}.
For example, to test with Postman:

Send a POST request to http://127.0.0.1:5000/receipts/process with the receipt data.
Use the receipt_id returned from the POST response to make a GET request to http://127.0.0.1:5000/receipts/{receipt_id} to get the calculated reward points.

Dockerization
To containerize the application, the following steps are used:

1.Dockerfile: Defines the environment, installs dependencies, and runs the Flask app.

2.Build the Docker image.

Run the Docker container.This will start the app inside a Docker container, accessible at http://127.0.0.1:5000.
