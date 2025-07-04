from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse
from language_flow import process_input

app = Flask(__name__)

@app.route("/voice", methods=['POST'])
def voice():
    speech_input = request.form.get("SpeechResult", "")
    response = VoiceResponse()
    reply = process_input(speech_input)
    response.say(reply, voice='alice', language="en-US")
    return str(response)

@app.route("/")
def home():
    return "✅ Guru AI Demo VoiceBot is running!"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
