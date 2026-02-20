import subprocess
import sys

def speak(text):
    """
    Raspberry Pi Hindi TTS using espeak-ng.
    Optimized to use stdin pipe (no temporary files).
    """
    try:
        # Launch espeak-ng directly
        process = subprocess.Popen(
            ["espeak-ng", "-v", "hi", "-s", "130"],  # -s 130 = speech speed (adjustable)
            stdin=subprocess.PIPE,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            text=True,
            encoding="utf-8"
        )

        # Send text to espeak-ng
        process.communicate(input=text)

    except Exception as e:
        print(f"⚠️ TTS Error: {e}")
