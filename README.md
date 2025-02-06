Here is the updated `README.md` without the **File Structure** section:

---

# Speech to Text, Text to Speech, and Image Generation Pipeline

This project allows you to automate the process of converting text to speech (TTS), speech to text (STT), and generate images from text using Stable Diffusion. The pipeline processes multiple prompts stored in an Excel file, generating results in separate folders.

### Table of Contents
- [Requirements](#requirements)
- [Setting Up the Environment](#setting-up-the-environment)
- [Running the Code](#running-the-code)
- [Creating the Prompts Excel File](#creating-the-prompts-excel-file)

## Requirements

- Python 3.7+
- `virtualenv` (for creating isolated Python environments)
- Python dependencies:
  - `gTTS` (Google Text-to-Speech)
  - `speech_recognition` (Speech-to-Text conversion)
  - `diffusers` (for image generation using Stable Diffusion)
  - `pydub` (for audio processing)
  - `pandas` (for handling Excel files)
  - `torch` (for PyTorch)
  - `openai` (optional for text generation, if needed)

## Setting Up the Environment

1. **Create a Virtual Environment**

   First, ensure that `virtualenv` is installed. If not, you can install it using pip:

   ```bash
   pip install virtualenv
   ```

   Then, create a virtual environment for the project:

   ```bash
   virtualenv venv
   ```

2. **Activate the Virtual Environment**

   - On **Windows**:
     ```bash
     .\venv\Scripts\activate
     ```

   - On **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

3. **Install Required Dependencies**

   After activating the virtual environment, install all the required Python packages by running:

   ```bash
   pip install gTTS speech_recognition diffusers torch pydub pandas openai
   ```

4. **Install ffmpeg for Audio Processing**

   The `pydub` library requires `ffmpeg` for audio file conversion (MP3 to WAV). You can install `ffmpeg` using the following methods:

   - **On macOS** (using Homebrew):
     ```bash
     brew install ffmpeg
     ```

   - **On Windows**:
     - Download the ffmpeg executable from [FFmpeg official site](https://ffmpeg.org/download.html).
     - Add the `bin` folder containing `ffmpeg.exe` to your system’s PATH.

   - **On Linux** (Ubuntu/Debian):
     ```bash
     sudo apt-get install ffmpeg
     ```

## Running the Code

1. **Create Prompts Excel File**

   If you don't already have an Excel file with prompts, you can generate one using the provided script `generate_excel.py`. Run the following command to create the `prompts.xlsx` file:

   ```bash
   python generate_excel.py
   ```

   This will generate an Excel file with sample prompts. You can edit this file to add more custom prompts.

2. **Run the Main Script**

   Once the `prompts.xlsx` file is ready, run the main Python script to process the prompts:

   ```bash
   python main.py
   ```

   The script will generate:
   - TTS audio files in the current directory (e.g., `tts_1.mp3`, `tts_2.mp3`, ...).
   - Transcribed text files (e.g., `stt_1.txt`, `stt_2.txt`, ...).
   - Generated images (e.g., `image_1.png`, `image_2.png`, ...).
   - A `results.json` file containing the mappings between prompts and the generated files.

3. **View Results**

   After running the script, you will find the generated audio files, transcriptions, images, and a `results.json` file in the same directory.
