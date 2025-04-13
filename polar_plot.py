import matplotlib.pyplot as plt
import numpy as np

# Örnek analiz verisi (simulate_encoder.py sonucundan alınmış gibi düşün)
results = {
    "A0": {"angle": 16, "amplitude": 164, "ma": {"angle": 16, "r": 54.25}, "mb": {"angle": 106, "r": 41.07}},
    "A1": {"angle": 16, "amplitude": 172, "ma": {"angle": 16, "r": 56.25}, "mb": {"angle": 106, "r": 41.07}},
    "A2": {"angle": 173, "amplitude": 181, "ma": {"angle": 173, "r": 39.20}, "mb": {"angle": 263, "r": 43.78}},
    "A3": {"angle": 267, "amplitude": 197, "ma": {"angle": 267, "r": 51.86}, "mb": {"angle": 357, "r": 0.12}},
}

fig = plt.figure(figsize=(9, 9))
ax = fig.add_subplot(111, polar=True)
ax.set_theta_zero_location('N')  # 0 derece yukarı baksın
ax.set_theta_direction(-1)       # Saat yönü tersine

# Titreşim noktalarını çiz
for piezo, info in results.items():
    angle_rad = np.radians(info['angle'])
    r = info['amplitude']
    ax.plot([angle_rad], [r], marker='o', label=f"{piezo} ({info['angle']}°, {r})")

    # Düzeltici A ağırlık oku
    ma = info['ma']
    ma_angle = np.radians(ma['angle'])
    ma_r = ma['r']
    ax.annotate(f"ma: {ma_r:.1f}g", xy=(ma_angle, ma_r), xytext=(ma_angle, ma_r + 20),
                arrowprops=dict(arrowstyle="->", color='red'), color='red', fontsize=8)

    # Düzeltici B ağırlık oku
    mb = info['mb']
    mb_angle = np.radians(mb['angle'])
    mb_r = mb['r']
    ax.annotate(f"mb: {mb_r:.1f}g", xy=(mb_angle, mb_r), xytext=(mb_angle, mb_r + 20),
                arrowprops=dict(arrowstyle="->", color='blue'), color='blue', fontsize=8)

ax.set_title("Balans Bozukluğu ve Düzeltici Ağırlık Önerileri", va='bottom')
ax.set_rlim(0, max(info['amplitude'] for info in results.values()) + 60)
ax.legend(loc='upper right')
plt.show()
