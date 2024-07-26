from Flask import Flask, request, jsonify

app1 = Flask(__name__)

@app1.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Received webhook data:", data)
    # Process the received data as needed
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app1.run(port=5000)
