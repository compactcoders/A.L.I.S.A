import whisper
from fuzzywuzzy import fuzz
import os
import warnings
import logging

# Suppress warnings and logs
warnings.filterwarnings("ignore")
logging.getLogger().setLevel(logging.ERROR)
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

# Set expected sentence and audio file
expected_sentence = "I was driving my car this evening."
audio_file = "audios/car (correct).mp3"

print(f"Looking for: {audio_file} in {os.getcwd()}")
if not os.path.exists(audio_file):
    print("File not found.")
    exit()
else:
    print("File found.")

# Load Whisper model
model = whisper.load_model("tiny")

# Transcribe the audio
def transcribe_audio(file_path):
    print(f"Transcribing: {file_path}")
    result = model.transcribe(file_path)
    transcribed = result["text"].strip()
    print(f"Transcribed Text: {transcribed}")
    return transcribed

# Check if sentences are similar
def is_sentence_match(expected, actual, threshold=85):
    similarity = fuzz.token_set_ratio(expected.lower(), actual.lower())
    print(f"Sentence similarity: {similarity}%")
    return similarity >= threshold, similarity

# Word-level pronunciation comparison
def compare_sentences(expected, actual):
    expected_words = expected.lower().split()
    actual_words = actual.lower().split()
    mismatches = []

    for i, expected_word in enumerate(expected_words):
        if i >= len(actual_words):
            mismatches.append((expected_word, "missing"))
            continue

        actual_word = actual_words[i]
        similarity = fuzz.ratio(expected_word, actual_word)

        if similarity < 100:  # catch small changes like "car" vs "cars"
            mismatches.append((expected_word, actual_word))

    return mismatches

# Print feedback
def provide_feedback(mismatches):
    if not mismatches:
        print("You passed the pronunciation check.")
    else:
        print("Pronunciation issues found:")
        for idx, (expected, actual) in enumerate(mismatches, start=1):
            print(f'{idx}. You mispronounced "{expected}" as "{actual}"')

# Main logic
if __name__ == "__main__":
    try:
        transcribed_text = transcribe_audio(audio_file)
        is_match, sim_score = is_sentence_match(expected_sentence, transcribed_text)

        if not is_match:
            print(f'Your sentence "{transcribed_text}" does not match the given sentence "{expected_sentence}".')
        else:
            mismatches = compare_sentences(expected_sentence, transcribed_text)
            provide_feedback(mismatches)

    except Exception as e:
        print(f"Error: {str(e)}")
