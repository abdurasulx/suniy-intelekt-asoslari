import numpy as np
from scipy.io.wavfile import read, write
import os

def moving_average(signal, window_size=10):
    filtered = np.copy(signal)
    for i in range(window_size, len(signal)):
        filtered[i] = np.mean(signal[i - window_size:i])
    return filtered

def normalize(signal):
    return np.int16(signal / np.max(np.abs(signal)) * 32767)

# --- 1. WAV faylni yuklaymiz ---
input_file = "original.wav"

if not os.path.exists(input_file):
    print("❌ Xatolik: 'noisy.wav' fayli mavjud emas.", os.path.exists(input_file) )
    print("Iltimos, shu nomli .wav faylni dasturni yoniga joylashtiring.")
    exit()

samplerate, data = read(input_file)

# Mono yoki stereo tekshiramiz
if len(data.shape) == 2:
    print("🎧 Stereo fayl aniqlandi — faqat 1-kanal (chap kanal) ustida ishlanadi.")
    data = data[:, 0]  # faqat chap kanal

# --- 2. Signalni float formatga o‘tkazamiz ---
data = data.astype(np.float32)

# --- 3. Filtrlash ---
cleaned = moving_average(data, window_size=10)

# --- 4. Tozalangan signalni saqlash ---
write("cleaned_output.wav", samplerate, normalize(cleaned))

print("✅ Tozalash yakunlandi!")
print("👉 Yangi fayl: cleaned_output.wav")
