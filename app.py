from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send-alert', methods=['POST'])
def send_alert():
    data = request.json
    location = data.get('location')
    contact = data.get('contact')

    print("🚨 ALERT SENT")
    print("📞 Contact:", contact)
    print("📍 Location:", location)

    return {"status": "ok"}

if __name__ == "__main__":
    app.run()