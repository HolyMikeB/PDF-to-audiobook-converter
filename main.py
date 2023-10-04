import PyPDF2
from google.cloud import texttospeech
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

Tk().withdraw()

pdf_file = askopenfilename()

with open(pdf_file, 'rb') as f:
    pdf = PyPDF2.PdfReader(f)

    pages = pdf.pages
    text = pages[0].extract_text()

client = texttospeech.TextToSpeechClient()

synthesis_input = texttospeech.SynthesisInput(text=text)

voice = texttospeech.VoiceSelectionParams(language_code='en-GB',
                                          name='en-GB-News-K',
                                          ssml_gender=texttospeech.SsmlVoiceGender.MALE)

audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

with open(f"{asksaveasfilename()}.mp3", 'wb') as out:
    out.write(response.audio_content)



