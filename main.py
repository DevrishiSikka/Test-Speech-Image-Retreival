import os
import torch
import requests
import json
import pandas as pd
import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
from diffusers import StableDiffusionPipeline
import openpyxl

# Directories to store output files
BASE_DIR = "output"
TTS_DIR = os.path.join(BASE_DIR, "tts")
STT_DIR = os.path.join(BASE_DIR, "stt")
IMG_DIR = os.path.join(BASE_DIR, "images")
JSON_FILE = os.path.join(BASE_DIR, "file_mapping.json")

# Ensure directories exist
os.makedirs(TTS_DIR, exist_ok=True)
os.makedirs(STT_DIR, exist_ok=True)
os.makedirs(IMG_DIR, exist_ok=True)

# ========== 1. Text-to-Speech (Offline) ==========
def text_to_speech(text, output_audio):
    print(f"Generating speech for: {text}")
    tts = gTTS(text=text, lang="en", slow=False)
    tts.save(output_audio)
    print(f"Audio saved as {output_audio}")

# ========== 2. Speech-to-Text (Offline) ==========
def speech_to_text(audio_file):
    print(f"Converting speech to text from {audio_file}...")
    recognizer = sr.Recognizer()

    # Convert MP3 to WAV (SpeechRecognition works better with WAV)
    if audio_file.endswith(".mp3"):
        wav_file = audio_file.replace(".mp3", ".wav")
        AudioSegment.from_mp3(audio_file).export(wav_file, format="wav")
        audio_file = wav_file

    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data)
        print(f"Transcribed Text: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand the audio")
    except sr.RequestError:
        print("Could not request results, check your internet connection")
    
    return ""

# ========== 3. Text-to-Image (Local Stable Diffusion) ==========
def generate_image_from_text(text, output_image):
    print(f"Generating image for: {text}")
    # Load Stable Diffusion model (use a lightweight model for efficiency)
    model_id = "runwayml/stable-diffusion-v1-5"
    pipeline = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    pipeline.to("mps")  # Use Metal acceleration on Apple M-series chips

    # Generate the image
    image = pipeline(text).images[0]
    image.save(output_image)
    print(f"Image saved as {output_image}")

# ========== 4. Process Multiple Prompts from Excel ==========
def process_prompts_from_excel(excel_file):
    # Load prompts from Excel
    df = pd.read_excel(excel_file, engine="openpyxl")
    prompts = df['prompts'].tolist()

    file_mapping = {}  # Dictionary to store file paths for each prompt

    # Process each prompt
    for idx, prompt in enumerate(prompts):
        prompt_key = f"prompt_{idx + 1}"
        print(f"Processing {prompt_key}: {prompt}")

        # 1. Text-to-Speech
        tts_file = os.path.join(TTS_DIR, f"tts_{prompt_key}.mp3")
        text_to_speech(prompt, tts_file)

        # 2. Speech-to-Text
        stt_file = os.path.join(STT_DIR, f"stt_{prompt_key}.wav")
        transcribed_text = speech_to_text(tts_file)

        if transcribed_text:
            # 3. Text-to-Image
            img_file = os.path.join(IMG_DIR, f"image_{prompt_key}.png")
            generate_image_from_text(transcribed_text, img_file)

            # Add file paths to mapping
            file_mapping[prompt_key] = {
                "prompt": prompt,
                "tts": tts_file,
                "stt": stt_file,
                "image": img_file
            }

    # Save the file mapping as JSON
    with open(JSON_FILE, "w") as json_file:
        json.dump(file_mapping, json_file, indent=4)

    print(f"Processing complete! JSON file created at {JSON_FILE}")

# ========== Run the Full Pipeline ==========
process_prompts_from_excel("prompts.xlsx")
