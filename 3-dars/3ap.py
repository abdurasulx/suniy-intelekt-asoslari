import wave
import numpy as np
import scipy.signal
import os

# Kiruvchi fayl nomi
input_file = 'noisy.wav'
output_file = 'cleaned_full.wav'

# WAV faylni o‘qish
with wave.open(input_file, 'rb') as wav:
    params = wav.getparams()
    n_channels, sampwidth, framerate, n_frames = params[:4]
    frames = wav.readframes(n_frames)

# NumPy massivga o‘tkazish
audio = np.frombuffer(frames, dtype=np.int16)

# Har bir kanalni alohida tozalash (stereo bo‘lsa)
if n_channels == 2:
    audio = audio.reshape(-1, 2)
    cleaned = np.zeros_like(audio)
    for ch in range(2):
        b, a = scipy.signal.butter(6, 1000 / (0.5 * framerate), btype='high')
        cleaned[:, ch] = scipy.signal.filtfilt(b, a, audio[:, ch])
    cleaned_audio = cleaned.flatten()
else:
    b, a = scipy.signal.butter(6, 1000 / (0.5 * framerate), btype='high')
    cleaned_audio = scipy.signal.filtfilt(b, a, audio)

# Saqlash
with wave.open(output_file, 'wb') as out_wav:
    out_wav.setparams(params)
    out_wav.writeframes(cleaned_audio.astype(np.int16).tobytes())

print(f"✅ To‘liq tozalangan fayl saqlandi: {output_file}")
