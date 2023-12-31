# کتابخانه های مورد نیاز را وارد می کنیم
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
import scipy.fftpack
import pywt

"""
این کد یک فایل صوتی را می خواند، تبدیل فوریه سریع و
تبدیل موجک آن را انجام می دهد، و سپس نتایج را نمایش می دهد.
"""

# تابعی برای رسم سیگنال
def namayesh_signal(ax, x, y, title):
    ax.plot(x, y)  # رسم سیگنال
    ax.set_title(title)  # تنظیم عنوان نمودار
    ax.set_xlabel('Time (seconds)')  # تنظیم برچسب محور x
    ax.set_ylabel('Amplitude')  # تنظیم برچسب محور y

# فایل صوتی را می خوانیم
sample_rate, audio_data = read('salam.wav')

# نمایش سیگنال صوتی
time_array = np.arange(0, len(audio_data)/sample_rate, 1/sample_rate)

# تبدیل فوریه سریع
fft_result = scipy.fftpack.fft(audio_data)
frequencies = scipy.fftpack.fftfreq(len(fft_result), 1/sample_rate)

# تبدیل موجک
wavelet_type = pywt.Wavelet('db8')
wavelet_coeffs = pywt.wavedec(audio_data, wavelet_type, level=6)

# ایجاد یک شکل برای نمایش تصاویر
fig, axs = plt.subplots(3, 1, figsize=(20, 18))

# نمایش سیگنال صوتی اصلی
namayesh_signal(axs[0], time_array, audio_data, 'Audio Signal')

# نمایش تبدیل فوریه
namayesh_signal(axs[1], np.abs(frequencies), np.abs(fft_result), 'Signal Spectrum')

# نمایش جزئیات تبدیل موجک
namayesh_signal(axs[2], range(len(wavelet_coeffs[0])), wavelet_coeffs[0], 'Wavelet Transform')

fig.tight_layout()
plt.show()
