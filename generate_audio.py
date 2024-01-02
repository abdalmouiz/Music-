import pyaudio
import wave

# Define the notes and durations of the song
notes = [
    "G", "D", "G", "D",
    "Em", "C", "D", "G",
    "G", "D", "G", "D",
    "Em", "C", "D", "G",
    "Em", "C", "D", "G",
    "G", "D", "G", "D"
]
durations = [
    0.5, 0.5, 0.5, 0.5,
    0.5, 0.5, 0.5, 0.5,
    0.5, 0.5, 0.5, 0.5,
    0.5, 0.5, 0.5, 0.5,
    0.5, 0.5, 0.5, 0.5,
    0.5, 0.5, 0.5, 0.5
]

# Create a PyAudio object
p = pyaudio.PyAudio()

# Open a stream to write the audio to
stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=True)

# Create a function to generate a note
def generate_note(note, duration):
    frequency = 440 * pow(2, (note - 69) / 12)
    sine_wave = [math.sin(2 * math.pi * frequency * t / 44100) for t in range(int(duration * 44100))]
    return sine_wave

# Generate the notes of the song
notes_generated = [generate_note(note, duration) for note, duration in zip(notes, durations)]

# Combine the notes into a single audio signal
audio_signal = sum(notes_generated)

# Write the audio signal to the stream
stream.write(audio_signal.tobytes())

# Close the stream
stream.close()

# Close PyAudio
p.terminate()
pip install pyaudio
python generate_audio.py
