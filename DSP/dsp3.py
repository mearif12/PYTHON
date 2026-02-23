import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# ----------------------------
# Load speech signal
# ----------------------------
fs, signal = wavfile.read("anger.wav")  # Replace with your file

# Convert to mono if stereo
if len(signal.shape) > 1:
    signal = signal.mean(axis=1)

signal = signal.astype(float)

# ----------------------------
# Framing parameters
# ----------------------------
frame_size_ms = 25
frame_shift_ms = 10

frame_length = int(fs * frame_size_ms / 1000)
frame_step = int(fs * frame_shift_ms / 1000)

signal_length = len(signal)

# Compute number of frames
num_frames = int(np.ceil((signal_length - frame_length) / frame_step)) + 1

# Zero padding
pad_length = num_frames * frame_step + frame_length
padded_signal = np.append(signal, np.zeros(pad_length - signal_length))

# Create frames
frames = np.zeros((num_frames, frame_length))
for i in range(num_frames):
    start = i * frame_step
    frames[i] = padded_signal[start:start + frame_length]

# ----------------------------
# Apply Hamming Window
# ----------------------------
window = np.hamming(frame_length)
windowed_frames = frames * window

# ----------------------------
# STFT using rFFT
# ----------------------------
fft_size = frame_length
stft = np.fft.rfft(windowed_frames, n=fft_size)

# Magnitude spectrum
magnitude = np.abs(stft)

# Convert to dB scale
eps = 1e-10  # avoid log(0)
magnitude_db = 20 * np.log10(magnitude + eps)

# ----------------------------
# Plot Spectrogram
# ----------------------------
plt.figure(figsize=(10,6))

time_axis = np.arange(num_frames) * frame_step / fs
freq_axis = np.fft.rfftfreq(fft_size, d=1/fs)

plt.pcolormesh(time_axis, freq_axis, magnitude_db.T, shading='gouraud')
plt.ylabel("Frequency (Hz)")
plt.xlabel("Time (s)")
plt.title("Spectrogram (STFT)")
plt.colorbar(label="Magnitude (dB)")
plt.tight_layout()
plt.show()
