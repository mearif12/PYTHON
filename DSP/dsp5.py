import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import find_peaks

# -----------------------------
# 1. Load audio and convert to mono
# -----------------------------
fs, signal = wavfile.read("anger.wav")
if signal.ndim > 1:              # if stereo, average channels
    signal = signal.mean(axis=1)
signal = signal.astype(float)
signal = signal / np.max(np.abs(signal))  # normalize

# -----------------------------
# 2. Frame parameters
# -----------------------------
frame_size, frame_shift = 0.03, 0.01  # seconds
N, H = int(frame_size*fs), int(frame_shift*fs)
num_frames = int((len(signal)-N)/H)

# Pitch search range (Hz)
f_min, f_max = 50, 400
lag_min, lag_max = int(fs/f_max), int(fs/f_min)

energy_threshold = 0.01

# -----------------------------
# 3. Process each frame
# -----------------------------
pitch_contour, time_axis = [], []

for i in range(num_frames):
    start = i*H
    frame = signal[start:start+N] * np.hamming(N)  # Hamming window

    # Energy-based voiced/unvoiced detection
    if np.sum(frame**2) < energy_threshold:
        pitch_contour.append(0)
    else:
        # Autocorrelation
        autocorr = np.correlate(frame, frame, mode='full')[N-1:]
        r = autocorr[lag_min:lag_max]

        peaks, _ = find_peaks(r)
        if len(peaks) > 0:
            peak = peaks[np.argmax(r[peaks])]
            pitch_contour.append(fs/(peak+lag_min))
        else:
            pitch_contour.append(0)

    time_axis.append(start/fs)

# -----------------------------
# 4. Plot pitch contour
# -----------------------------
# pitch_voiced = [f0 for f0 in pitch_contour if f0 > 0]
# time_voiced = [t for t, f0 in zip(time_axis, pitch_contour) if f0 > 0]
                                                                              #-- for voiced only
# plt.figure(figsize=(10,4))
# plt.plot(time_voiced, pitch_voiced, marker='o', linestyle='-') 
       
plt.figure(figsize=(10,4))
plt.plot(time_axis, pitch_contour)
plt.xlabel("Time (s)")
plt.ylabel("F0 (Hz)")
plt.title("Pitch Contour (Autocorrelation Method)")
plt.grid(True)
plt.show()
