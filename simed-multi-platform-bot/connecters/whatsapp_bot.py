"""
WhatsApp connector for SimEd Studio Bot (Twilio)
"""

from core.agent import SimEdAgent
from flask import Flask, request
from twilio.rest import Client

app = Flask(__name__)
agent = SimEdAgent()

# Twilio credentials
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_client = Client(account_sid, auth_token)


@app.route("/whatsapp", methods=["POST"])
def whatsapp_webhook():
    """Handle incoming WhatsApp messages"""
    incoming_msg = request.values.get("Body", "").strip()
    sender = request.values.get("From", "")

    user_id = sender.replace("whatsapp:", "")
    response = agent.process_message(user_id, incoming_msg)

    message = twilio_client.messages.create(
        from_=f"whatsapp:{os.getenv('TWILIO_WHATSAPP_NUMBER')}",
        body=response,
        to=sender,
    )

    return str(message.sid)


def run_whatsapp(port: int = 5000):
    """Start WhatsApp bot"""
    print(f"✅ WhatsApp bot listening on port {port}")
    app.run(port=port, debug=False)
