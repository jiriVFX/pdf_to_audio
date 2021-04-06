from google.cloud import texttospeech
from datetime import datetime
import os
from constants import *


class MaxCharsExceeded(Exception):
    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)


class TextToSpeech(texttospeech.TextToSpeechClient):
    def __init__(self):
        # Initialize TextToSpeechClient
        super().__init__()
        #es-ES
        #cs-CZ
        self.voice = texttospeech.VoiceSelectionParams(language_code="en-US",
                                                       ssml_gender=texttospeech.SsmlVoiceGender.FEMALE)
        self.audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

    def text_to_audio(self, text):
        """Sends the text input to Google Text-To-Speech synthesizer and saves the response to audio file.
        :type text: str"""
        if len(text) <= MAX_CHARACTERS:
            response = self.synthesize_speech(
                input=texttospeech.SynthesisInput(text=text),
                voice=self.voice,
                audio_config=self.audio_config
            )
            self.save_audio_file(response)
        else:
            raise MaxCharsExceeded(f"text_to_audio: "
                                   f"Number of characters in 'text' is {len(text)},"
                                   f" but MAX_CHARACTERS is set to {MAX_CHARACTERS}.")

    def save_audio_file(self, response):
        """Saves response to MP3 file in the format YYYY-MM-DD_HH-MM-SS.mp3.
        :type response: binary"""
        file_name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        # The response's audio_content is binary.
        with open(f"{file_name}.mp3", "wb") as file:
            # Write the response to the output file.
            file.write(response.audio_content)
            print(f"Audio content written to file '{file_name}.mp3'")

    def list_voices(self):
        """Lists the available voices.
        Adapted from the original API example https://cloud.google.com/text-to-speech/docs/list-voices"""
        # Performs the list voices request
        client = texttospeech.TextToSpeechClient()

        # Performs the list voices request
        voices = client.list_voices()

        for voice in voices.voices:
            # Display the voice's name. Example: tpc-vocoded
            print(f"Name: {voice.name}")

            # Display the supported language codes for this voice. Example: "en-US"
            for language_code in voice.language_codes:
                print(f"Supported language: {language_code}")

            ssml_gender = texttospeech.SsmlVoiceGender(voice.ssml_gender)

            # Display the SSML Voice Gender
            print(f"SSML Voice Gender: {ssml_gender.name}")

            # Display the natural sample rate hertz for this voice. Example: 24000
            print(f"Natural Sample Rate Hertz: {voice.natural_sample_rate_hertz}\n")
