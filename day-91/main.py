import PyPDF2
from google.cloud import texttospeech
from dotenv import load_dotenv
import os

load_dotenv()

def pdf_to_text(path, output):
    with open(path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(path)
        text = ''

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    cleaned_text = text.replace('\n', ' ').strip()

    client = texttospeech.TextToSpeechClient.from_service_account_file(os.environ['file_path'])

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=cleaned_text)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # The response's audio_content is binary.
    with open("output.mp3", "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')

if __name__ == '__main__':
    pdf_path = 'test-1.pdf'
    output_txt = 'test.txt'
    pdf_to_text(pdf_path, output_txt)
    print("PDF converted to text successfully!")