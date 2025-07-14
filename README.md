# A.L.I.S.A. – Artificial Language Intelligence for Speech Assistance

**A.L.I.S.A.** is an AI-powered tool that helps users improve their spoken English by analyzing their pronunciation at the word level. It transcribes speech, compares it against an expected sentence, and identifies specific pronunciation mistakes — especially helpful for Indian learners dealing with Mother Tongue Influence (MTI).

---

## 📌 About

This component is a **primitive prototype** of A.L.I.S.A. It:

- Transcribes spoken English from an audio file using OpenAI's Whisper model.
- Compares the transcribed sentence with a reference sentence.
- Identifies mispronounced or mismatched words.
- Provides feedback like:
  ```
  1. You mispronounced "car" as "cars"
  ```

---

## ⚙️ How It Works

1. **Audio Input**: User speaks a given sentence and saves it as an audio file (e.g., `sample.mp3`).
2. **Transcription**: Whisper converts the audio to text.
3. **Sentence Matching**: It checks how closely the spoken sentence matches the expected one.
4. **Pronunciation Feedback**: If the sentence is correct, it checks each word and reports incorrect pronunciations.

---

## 🧰 Requirements

### Python

- Python 3.8 or higher

### Python Packages

Install all required packages:

```bash
pip install -r requirements.txt
```

#### `requirements.txt` content:
```
openai-whisper
fuzzywuzzy
python-Levenshtein
torch
```

### FFmpeg

Whisper requires **FFmpeg** to process audio.

#### ✅ Windows Installation:

1. Download FFmpeg from: https://www.gyan.dev/ffmpeg/builds/
2. Extract the ZIP file.
3. Copy the path to the `bin` folder inside the extracted folder.
4. Add it to your system’s `Environment Variables > Path`.
5. Restart terminal and verify:

```bash
ffmpeg -version
```

---

## 🛠️ Local Setup Instructions

1. **Clone the repository**:

```bash
git clone https://github.com/compactcoders/A.L.I.S.A.git
cd A.L.I.S.A
```

2. **Create and switch to your branch** (optional):

```bash
git checkout -b RameshV1
```

3. **Place your audio file** in a folder named `audios/`, e.g.:

```
A.L.I.S.A/
├── audios/
│   └── car (wrong).mp3
```

4. **Update `app.py`** with the audio file name and target sentence:

```python
expected_sentence = "I was driving my car this evening"
audio_file = "audios/car (wrong).mp3"
```

5. **Run the script**:

```bash
python app.py
```

---

## ✅ Sample Output

```
Looking for: audios/car (wrong).mp3 in ...
File found.
Transcribing: audios/car (wrong).mp3
Transcribed Text: I was driving my cars this evening.
Sentence similarity: 99%
Pronunciation issues found:
1. You mispronounced "car" as "cars"
```

---

## 🔍 Notes

- Works with `.mp3`, `.wav`, `.m4a`, etc.
- First-time Whisper usage will automatically download the model (~75MB for `tiny`).
- You can change the model (`tiny`, `base`, `small`, etc.) depending on accuracy and performance needs.

---
