from flask import Flask, render_template, request
from googletrans import Translator
from gtts import gTTS
import os

app = Flask(__name__)
translator = Translator()

@app.route("/", methods=["GET", "POST"])
def index():
    sinhala_output = ""
    if request.method == "POST":
        english_text = request.form["english_text"]
        try:
            translated = translator.translate(english_text, dest='si')
            sinhala_output = translated.text

            # Create TTS audio from Sinhala text
            tts = gTTS(text=sinhala_output, lang='si')
            audio_path = os.path.join("static", "sinhala_audio.mp3")
            tts.save(audio_path)

        except Exception as e:
            sinhala_output = f"[Error] {e}"

    return render_template("index.html", sinhala_output=sinhala_output)

if __name__ == "__main__":
    app.run(debug=True)
