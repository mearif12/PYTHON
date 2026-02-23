import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# ----------------------------
# Load speech signal
# ----------------------------
fs, signal = wavfile.read("anger.wav")  # Replace with your file

# If stereo, convert to mono
if len(signal.shape) > 1:
    signal = signal.mean(axis=1)

signal = signal.astype(float)

# ----------------------------
# Framing parameters
# ----------------------------
frame_size_ms = 25      # 25 ms
frame_shift_ms = 10     # 10 ms

frame_length = int(fs * frame_size_ms / 1000)
frame_step = int(fs * frame_shift_ms / 1000)

signal_length = len(signal)

# ----------------------------
# Compute total number of frames
# ----------------------------
num_frames = int(np.ceil((signal_length - frame_length) / frame_step)) + 1

# Zero padding (if needed)
pad_length = num_frames * frame_step + frame_length
z = np.zeros(pad_length - signal_length)
padded_signal = np.append(signal, z)

# ----------------------------
# Create frames
# ----------------------------
frames = np.zeros((num_frames, frame_length))

for i in range(num_frames):
    start = i * frame_step
    end = start + frame_length
    frames[i] = padded_signal[start:end]

print("Total number of frames:", num_frames)

# ----------------------------
# Apply Hamming window
# ----------------------------
hamming_window = np.hamming(frame_length)
windowed_frames = frames * hamming_window

# ----------------------------
# Plot two sample frames
# ----------------------------
frame_index = 10  # You can change this


plt.figure(figsize=(10,4))
plt.plot(frames[frame_index])
plt.title("Original Frame")

plt.figure(figsize=(10,4))
plt.plot(windowed_frames[frame_index])
plt.title("Windowed Frame (Hamming)")

plt.figure(figsize=(10,4))
plt.plot(hamming_window)
plt.title("Hamming Window")
plt.xlabel("Sample Index")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()
