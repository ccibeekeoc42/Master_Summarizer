from gtts import gTTS
from io import BytesIO


def text2voice(text):
    """Converts text to an audio file using gTTS and returns the audio file as binary data"""
    audio_bytes = BytesIO()
    tts = gTTS(text, lang='en')
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)
    return audio_bytes.read()
   