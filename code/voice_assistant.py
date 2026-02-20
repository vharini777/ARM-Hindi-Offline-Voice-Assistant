import os
os.environ["OPENBLAS_CORETYPE"] = "ARMV8"

import json
import time
import threading
import numpy as np
import sounddevice as sd
import onnxruntime as ort
from rapidfuzz import fuzz
from transformers import Wav2Vec2Processor
from least import speak
from actions import handle_intent

# ======================
# CONFIG
# ======================
MODEL_DIR = "hindi_onnx_model"
ONNX_PATH = os.path.join(MODEL_DIR, "model.onnx")
SAMPLE_RATE = 16000
is_speaking = False

# ======================
# LOAD ASR MODEL
# ======================
print("🚀 Loading ONNX ASR Model...")

sess_options = ort.SessionOptions()
sess_options.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL
sess_options.intra_op_num_threads = 2  # Pi 4 friendly

processor = Wav2Vec2Processor.from_pretrained(MODEL_DIR)
asr_session = ort.InferenceSession(
    ONNX_PATH,
    sess_options,
    providers=["CPUExecutionProvider"]
)

# ======================
# LOAD INTENTS
# ======================
with open("intent.json", "r", encoding="utf-8") as f:
    INTENTS = json.load(f)

def detect_intent_fuzzy(text):
    best_intent = "GREETING"
    highest_score = 0

    for intent_name, data in INTENTS.items():
        for kw in data.get("keywords", []):
            score = fuzz.partial_ratio(kw, text)
            if score > highest_score:
                highest_score = score
                best_intent = intent_name

    return best_intent if highest_score > 60 else "GREETING"

# ======================
# RECORD AUDIO UNTIL SILENCE
# ======================
def record_until_silence():
    CHUNK = 1024
    THRESHOLD = 0.02
    SILENCE_LIMIT = 15

    audio_buffer = []
    speech_started = False
    silence_chunks = 0

    try:
        with sd.InputStream(
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype="float32",
            blocksize=CHUNK
        ) as stream:
            while True:
                if is_speaking:
                    return None

                data, _ = stream.read(CHUNK)
                data = data.flatten()
                rms = np.sqrt(np.mean(data**2))

                if rms > THRESHOLD:
                    speech_started = True
                    audio_buffer.append(data.copy())
                    silence_chunks = 0
                elif speech_started:
                    silence_chunks += 1
                    audio_buffer.append(data.copy())
                    if silence_chunks > SILENCE_LIMIT:
                        break
    except Exception as e:
        print(f"⚠️ Audio Stream Error: {e}")
        return None

    if audio_buffer:
        return np.concatenate(audio_buffer).astype(np.float32)
    return None

# ======================
# SPEAK WRAPPER
# ======================
def speaking_wrapper(text):
    global is_speaking
    is_speaking = True
    speak(text)
    time.sleep(0.3)
    is_speaking = False

# ======================
# MAIN LOOP
# ======================
print("\n🔥 Raspberry Pi Assistant Active\n")

while True:
    try:
        if is_speaking:
            time.sleep(0.1)
            continue

        audio = record_until_silence()
        if audio is None:
            continue

        start_time = time.time()

        inputs = processor(audio, sampling_rate=SAMPLE_RATE, return_tensors="np")
        logits = asr_session.run(
            None,
            {asr_session.get_inputs()[0].name: inputs.input_values}
        )[0]

        predicted_ids = np.argmax(logits, axis=-1)
        text = processor.decode(predicted_ids[0]).strip()

        if not text or len(text) < 2:
            continue

        print(f"🎤 Heard: {text}")

        intent = detect_intent_fuzzy(text)
        response = handle_intent(intent, text)

        # Start speaking in a separate daemon thread
        threading.Thread(target=speaking_wrapper, args=(response,), daemon=True).start()

        print(f"🎯 Intent: {intent}")
        print(f"🗣️ AI: {response}")
        print(f"🕒 Latency: {time.time() - start_time:.2f}s")
        print("-" * 30)

    except KeyboardInterrupt:
        print("\nStopping Assistant...")
        break
    except Exception as e:
        print(f"⚠️ Error: {e}")
