# MangaPanel OCR, Translate & Text-to-Speech

Process manga/comic pages: automatically extract panel text, translate (e.g., Japanese to English), and generate speech audio.

## Features

- **Text extraction** from manga/comic image panels (supports English & Japanese by default).
- **Automatic translation** of extracted text to English (customizable).
- **Text-to-speech**: convert translated text to spoken audio (supports offline and online engines).
- **GPU detection/diagnostics** (PyTorch) for CUDA-enabled systems.

## Requirements

Before running, install all dependencies:

```bash
pip install opencv-python-headless numpy googletrans==4.0.0-rc1 pyttsx3 gTTS easyocr torch
```

- *Note:* `opencv-python-headless` avoids GUI dependencies.
- Make sure you have Python 3.6 or newer.
- GPU is optional but recommended for faster OCR with EasyOCR.

## Usage

1. **Place your manga/comic page image** in the project directory (e.g., `page1.PNG`). Update the path if needed.
2. **Run the script:**

   ```bash
   python script_name.py
   ```

   - The script will:
     - Detect your GPU (if available),
     - Extract text from detected panels,
     - Translate text to English,
     - Read out the translation aloud and optionally save audio as `output.mp3`.

## Customization

- **Languages for OCR:**  
  Edit the languages in `easyocr.Reader(['en', 'ja'])` in the `extract_text()` function for other languages (see EasyOCR docs for codes).
- **Target translation language:**  
  Change `target_language='en'` in `tranaslate_text()` to another language code if needed.
- **Text-to-speech engine:**  
  Use `use_gtts=True` in `text_to_speech()` for Google TTS (requires internet), or leave as `False` for `pyttsx3` (offline).

## Example

Basic usage with default image:

```python
if __name__ == "__main__":
    image_path = "page1.PNG"
    process_manga(image_path)
```

## Project Structure

| File/Folder        | Purpose                                  |
|--------------------|------------------------------------------|
| `script_name.py`   | Main script for OCR, translation, TTS    |
| `page1.PNG`        | Example manga/comic page image           |
| `output.mp3`       | (Generated) Audio of translated text     |

## Troubleshooting

- If GPU is not detected, script still works on CPU (may be slower).
- EasyOCR downloads model files on first run.
- Translation service (`googletrans`) may hit rate limits; use sparingly.
- For gTTS audio on Linux/macOS, change `os.system(f"start {save_path}")` to use `open` (macOS) or `xdg-open` (Linux).

## License

MIT License (add your preferred license information here).

## Credits

- [EasyOCR](https://github.com/JaidedAI/EasyOCR)
- [googletrans](https://pypi.org/project/googletrans/)
- [gTTS](https://pypi.org/project/gTTS/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [PyTorch](https://pytorch.org/)
- [OpenCV](https://opencv.org/)
