import cv2
import pytesseract
from googletrans import Translator
import speech_recognition as sr
from gtts import gTTS
import os

# Configure Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Adjust path if needed

def image_to_text(image_path):
    img = cv2.imread(image_path)
    text = pytesseract.image_to_string(img)
    return text

def translate_text(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except Exception as e:
        return f"Error: {e}"

def text_to_speech(text, language='en'):
    tts = gTTS(text=text, lang=language)
    output_file = "output.mp3"
    tts.save(output_file)
    os.system(f"start {output_file}")

def main():
    print("Choose an option:")
    print("1. Translate text from an image")
    print("2. Translate speech")
    print("3. Translate typed text")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        image_path = input("Enter the image path: ")
        extracted_text = image_to_text(image_path)
        print(f"Extracted Text: {extracted_text}")
        target_lang = input("Enter target language (e.g., 'en' for English, 'fr' for French): ")
        translation = translate_text(extracted_text, target_lang)
        print(f"Translated Text: {translation}")
        text_to_speech(translation, language=target_lang)

    elif choice == "2":
        print("Listening...")
        spoken_text = speech_to_text()
        print(f"Recognized Speech: {spoken_text}")
        target_lang = input("Enter target language (e.g., 'en' for English, 'fr' for French): ")
        translation = translate_text(spoken_text, target_lang)
        print(f"Translated Text: {translation}")
        text_to_speech(translation, language=target_lang)

    elif choice == "3":
        text = input("Enter the text to translate: ")
        target_lang = input("Enter target language (e.g., 'en' for English, 'fr' for French): ")
        translation = translate_text(text, target_lang)
        print(f"Translated Text: {translation}")
        text_to_speech(translation, language=target_lang)

    else:
        print("Invalid choice! Exiting.")

if __name__ == "__main__":
    main()
