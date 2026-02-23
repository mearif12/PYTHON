import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fftpack import dct

# -----------------------------
# 1. Load audio and convert to mono
# -----------------------------
fs, signal = wavfile.read("anger.wav")
if signal.ndim > 1:
    signal = signal.mean(axis=1)
signal = signal.astype(float)

# Optional: normalize
signal = signal / np.max(np.abs(signal))

# -----------------------------
# 2. Pre-emphasis
# -----------------------------
pre_emphasis = 0.97
signal = np.append(signal[0], signal[1:] - pre_emphasis * signal[:-1])

# -----------------------------
# 3. Framing
# -----------------------------
frame_size, frame_shift = 0.025, 0.01  # seconds
N, H = int(frame_size*fs), int(frame_shift*fs)
num_frames = int(np.ceil((len(signal)-N)/H)) + 1

# Pad signal to fit frames
pad_len = num_frames*H + N
signal = np.append(signal, np.zeros(pad_len - len(signal)))

frames = np.array([signal[i*H:i*H+N] for i in range(num_frames)])
frames *= np.hamming(N)

# -----------------------------
# 4. FFT and Power Spectrum
# -----------------------------
fft_size = 512
spectrum = np.abs(np.fft.rfft(frames, fft_size))**2

# -----------------------------
# 5. Mel Filterbank
# -----------------------------
num_filters = 26

def hz_to_mel(h): return 2595*np.log10(1 + h/700)
def mel_to_hz(m): return 700*(10**(m/2595) - 1)

mel_points = np.linspace(hz_to_mel(0), hz_to_mel(fs/2), num_filters+2)
hz_points = mel_to_hz(mel_points)
bins = np.floor((fft_size+1)*hz_points/fs).astype(int)

filters = np.zeros((num_filters, fft_size//2+1))
for m in range(1, num_filters+1):
    left, center, right = bins[m-1], bins[m], bins[m+1]
    for k in range(left, center):
        filters[m-1, k] = (k-left)/(center-left)
    for k in range(center, right):
        filters[m-1, k] = (right-k)/(right-center)

mel_energy = np.dot(spectrum, filters.T)
mel_energy = np.where(mel_energy == 0, 1e-10, mel_energy)  # avoid log(0)
mel_energy = np.log(mel_energy)

# -----------------------------
# 6. DCT → MFCC
# -----------------------------
num_ceps = 13
mfcc = dct(mel_energy, type=2, axis=1, norm='ortho')[:,:num_ceps]

print("MFCC shape:", mfcc.shape)

# -----------------------------
# 7. Plot MFCC Heatmap
# -----------------------------
plt.figure(figsize=(10,5))
plt.imshow(mfcc.T, aspect='auto', origin='lower')
plt.title("MFCC Heatmap")
plt.xlabel("Frame Number")
plt.ylabel("Coefficient Number")
plt.colorbar(label="Amplitude")
plt.tight_layout()
plt.show()
