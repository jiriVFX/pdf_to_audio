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
# pdf_reader.read_pdf("test.pdf")
text = pdf_reader.get_page(4)[0:500]
#print(text)

# Speech synthesis -----------------------------------------------------------------------------------------------------

text_to_speech = TextToSpeech()
#text_to_speech.list_voices()
text_to_speech.text_to_audio(text)
