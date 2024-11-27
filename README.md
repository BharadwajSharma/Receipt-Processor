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
