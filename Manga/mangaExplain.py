import cv2
import numpy as np 
from googletrans import Translator
import pyttsx3
from gtts import gTTS
import easyocr
import os
import torch
print(torch.cuda.is_available())  # Should return True if CUDA is enabled
print(torch.cuda.device_count())  # Number of available GPUs
print(torch.cuda.get_device_name(0))  # Name of your GPU


def extract_text(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply adaptive threshold to highlight panel boundaries
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                   cv2.THRESH_BINARY, 11, 2)

    # Find contours (possible panels)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    panel_texts = []
    reader = easyocr.Reader(['en', 'ja'])  # Add Japanese if needed

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if w > 50 and h > 50:  # Ignore small noise
            panel = image[y:y+h, x:x+w]  # Crop panel
            text = reader.readtext(panel)
            extracted_text = " ".join([res[1] for res in text])
            panel_texts.append(extracted_text)

    return panel_texts

def tranaslate_text(text, target_language='en'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

def text_to_speech(text, save_path='output.mp3', use_gtts=False):
    if use_gtts:
        tts = gTTS(text, lang='en')
        tts.save(save_path)
        os.system(f"start {save_path}")
    else:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        
def process_manga(image_path):
    print("Extracting text from image...")
    extracted_text = extract_text(image_path)
    
    if not extracted_text:
        print("No text found!")
        return None

    extracted_text = " ".join(extracted_text)  # Convert list to a single string
    print("Extracted text:", extracted_text)
    
    print("Translating text...")
    try:
        translated_text = tranaslate_text(extracted_text)  # Translate full text at once
    except Exception as e:
        print("Translation Error:", str(e))
        translated_text = "Translation failed."
    
    print("Translated text:", translated_text)
    
    print("Generating speech...")
    text_to_speech(translated_text)
    
    return translated_text



if __name__ == "__main__":
    image_path = "page1.PNG"
    process_manga(image_path)