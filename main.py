import os
from text_to_speech import TextToSpeech
from pdf_to_text import PdfToText

# Google Cloud Key -----------------------------------------------------------------------------------------------------

# Path to your Google Cloud Key
path_to_your_key = "google_cloud_key.json"
# Set the key environment variable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = path_to_your_key

# Reading PDF ----------------------------------------------------------------------------------------------------------

pdf_reader = PdfToText()
# Enter the path to your PDF file
pdf_reader.read_pdf("scandal_in_bohemia.pdf")
# Get first 500 characters from 5th page of the document (pages start at 0 - like lists)
text = pdf_reader.get_page(4)[0:500]

# Speech synthesis -----------------------------------------------------------------------------------------------------

# Create TextToSpeech object with correct language code in the constructor
# https://cloud.google.com/text-to-speech/docs/voices
text_to_speech = TextToSpeech("en-US")

# Print list of all available languages
# text_to_speech.list_voices()

# Convert the text to audio
# result is saved as an MP3 file in the project folder, named in format "YYYY-MM-DD_HH-MM-SS.mp3"
text_to_speech.text_to_audio(text)
