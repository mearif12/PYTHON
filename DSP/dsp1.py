import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import os

# =========================================================
# Q1. Audio Loading and Signal Analysis
# =========================================================

# -----------------------------
# 1. Load WAV File
# -----------------------------
file_path = "anger.wav"   # Change to your file path

if not os.path.exists(file_path):
    print("Error: File not found.")
    exit()

sampling_rate, signal = wavfile.read(file_path)

# Convert stereo → mono if needed
if len(signal.shape) == 2:
    signal = signal.mean(axis=1)

# Normalize signal (recommended for analysis)
signal = signal / np.max(np.abs(signal))


# -----------------------------
# 2. Basic Signal Information
# -----------------------------
num_samples = len(signal)
duration = num_samples / sampling_rate
max_amp = np.max(signal)
min_amp = np.min(signal)

print("===== Signal Information =====")
print("Sampling Rate      :", sampling_rate, "Hz")
print("Number of Samples  :", num_samples)
print("Duration           :", duration, "seconds")
print("Maximum Amplitude  :", max_amp)
print("Minimum Amplitude  :", min_amp)


# -----------------------------
# 3. Plot Waveform
# -----------------------------
time_axis = np.linspace(0, duration, num_samples, endpoint=False)

plt.figure(figsize=(10,4))
plt.plot(time_axis, signal)
plt.title("Waveform of Speech Signal")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.show()

# -----------------------------
# 4. FFT and Magnitude Spectrum
# -----------------------------
fft_values = np.fft.rfft(signal)
fft_magnitude = np.abs(fft_values)

freq_axis = np.fft.rfftfreq(num_samples, d=1/sampling_rate)


# -----------------------------
# 5. Plot Magnitude Spectrum
# -----------------------------
plt.figure(figsize=(10,4))
plt.plot(freq_axis, fft_magnitude)
plt.title("Magnitude Spectrum of Speech Signal")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid(True)
plt.tight_layout()
plt.show()

# -----------------------------
# 5. Plot Magnitude Spectrum dB
# -----------------------------
plt.figure(figsize=(10,4))
plt.plot(freq_axis, 20*np.log10(fft_magnitude + 1e-8))
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")
plt.title("Magnitude Spectrum (Log Scale)")
plt.grid()
plt.show()
