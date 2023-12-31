import cv2  # کتابخانه‌ای برای کار با تصاویر
import numpy as np  # کتابخانه‌ای برای کار با آرایه‌ها
import matplotlib.pyplot as plt  # کتابخانه‌ای برای رسم نمودار
import pywt  # کتابخانه‌ای برای تبدیل ویولت

"""
این کد پایتون برای تجزیه و تحلیل تصویر استفاده می‌شود. در اینجا، تصویری به صورت سیاه و سفید خوانده می‌شود
و سپس دو نوع تبدیل روی آن اعمال می‌شود: تبدیل فوریه و تبدیل ویولت.
هر دوی این تبدیل‌ها روش‌هایی برای تجزیه و تحلیل فرکانس یا جزئیات تصویر هستند.
در نهایت، تصویر اصلی، تبدیل فوریه، و جزئیات تبدیل ویولت نمایش داده می‌شوند.
"""

# گرفتن تصویر
original = cv2.imread('hame_ba_ham.jpg', cv2.IMREAD_GRAYSCALE)  # خواندن تصویر به صورت سیاه و سفید

# تبدیل فوریه
dft = cv2.dft(np.float32(original), flags=cv2.DFT_COMPLEX_OUTPUT)  # انجام تبدیل فوریه بر روی تصویر
dft_shift = np.fft.fftshift(dft)  # انتقال نقطه صفر فرکانس به مرکز تصویر
magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))  # محاسبه طیف فرکانس
# نرمال سازی تصویر تبدیل فوریه
magnitude_spectrum = cv2.normalize(magnitude_spectrum, None, 0, 255, cv2.NORM_MINMAX)  # نرمال سازی تصویر تبدیل فوریه

# تبدیل ویولت
coeffs2 = pywt.dwt2(original, 'bior1.3')  # انجام تبدیل ویولت بر روی تصویر
LL, (LH, HL, HH) = coeffs2  # استخراج جزئیات افقی، عمودی و مورب از تبدیل ویولت

# نمایش تصاویر
fig, axs = plt.subplots(2, 3, figsize=(12, 6))  # ایجاد یک شیء نمودار با دو ردیف و سه ستون

# نمایش تصویر اصلی
axs[0, 0].imshow(original, cmap=plt.cm.gray)  # نمایش تصویر اصلی
axs[0, 0].set_title('Original Image')  # تنظیم عنوان برای تصویر اصلی
axs[0, 0].set_xticks([])  # حذف مقادیر محور x برای تصویر اصلی
axs[0, 0].set_yticks([])  # حذف مقادیر محور y برای تصویر اصلی

# نمایش تبدیل فوریه
axs[0, 1].imshow(magnitude_spectrum, cmap=plt.cm.gray)  # نمایش تبدیل فوریه
axs[0, 1].set_title('Fourier Transform')  # تنظیم عنوان برای تبدیل فوریه
axs[0, 1].set_xticks([])  # حذف مقادیر محور x برای تبدیل فوریه
axs[0, 1].set_yticks([])  # حذف مقادیر محور y برای تبدیل فوریه

# نمایش تبدیل ویولت
titles = [' Horizontal detail', 'Vertical detail', 'Diagonal detail']  # عناوین برای جزئیات تبدیل ویولت
for i, a in enumerate([LH, HL, HH]):  # برای هر یک از جزئیات تبدیل ویولت
    axs[1, i].imshow(a, interpolation="nearest", cmap=plt.cm.gray)  # نمایش جزئیات تبدیل ویولت
    axs[1, i].set_title(titles[i])  # تنظیم عنوان برای جزئیات تبدیل ویولت
    axs[1, i].set_xticks([])  # حذف مقادیر محور x برای جزئیات تبدیل ویولت
    axs[1, i].set_yticks([])  # حذف مقادیر محور y برای جزئیات تبدیل ویولت

fig.tight_layout()  # تنظیم فاصله بین نمودارها
plt.show()  # نمایش نمودار
