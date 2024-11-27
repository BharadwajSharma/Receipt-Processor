from flask import Flask, request, jsonify
import uuid
import re

app = Flask(__name__)

receipts = {}

def calculate_points(receipt):
    points = 0
    points += sum(1 for c in receipt["retailer"] if c.isalnum())
    
    total = float(receipt["total"])
    if total.is_integer():
        points += 50

    if total % 0.25 == 0:
        points += 25

    points += (len(receipt["items"]) // 2) * 5

    for item in receipt["items"]:
        if len(item["shortDescription"].strip()) % 3 == 0:
            points += int(float(item["price"]) * 0.2 + 0.99) 

    day = int(receipt["purchaseDate"].split("-")[2])
    if day % 2 == 1:
        points += 6

    time = receipt["purchaseTime"]
    hour, minute = map(int, time.split(":"))
    if 14 <= hour < 16:
        points += 10

    return points

@app.route('/receipts/process', methods=['POST'])
def process_receipt():
    try:
        receipt = request.get_json()
        receipt_id = str(uuid.uuid4())
        points = calculate_points(receipt)
        receipts[receipt_id] = {"receipt": receipt, "points": points}
        return jsonify({"id": receipt_id})
    except Exception as e:
        return jsonify({"error": "Invalid receipt"}), 400

@app.route('/receipts/<receipt_id>/points', methods=['GET'])
def get_points(receipt_id):
    if receipt_id in receipts:
        return jsonify({"points": receipts[receipt_id]["points"]})
    return jsonify({"error": "Receipt not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)