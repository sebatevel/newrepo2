import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import os
import csv
import json

# Simüle edilmiş piezo verileri (örnek)
data = {
    "A0": np.abs(np.sin(np.radians(np.arange(360))) * 100 + np.random.normal(0, 5, 360)),
    "A1": np.abs(np.sin(np.radians(np.arange(360) + 90)) * 120 + np.random.normal(0, 5, 360)),
    "A2": np.abs(np.sin(np.radians(np.arange(360) + 180)) * 80 + np.random.normal(0, 5, 360)),
    "A3": np.abs(np.sin(np.radians(np.arange(360) + 270)) * 60 + np.random.normal(0, 5, 360)),
}

angles = np.arange(360)

# Zaman damgası ve klasör oluşturma
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
folder_path = f"/home/anta/BALANS2/{timestamp}"
os.makedirs(folder_path, exist_ok=True)

# Grafik çizimi
plt.figure(figsize=(12, 6))
for key, values in data.items():
    plt.plot(angles, values, label=f"{key} Piezo")

plt.title("Balans Sensörlerinden Alınan Verilerin Sinüs Dalgası Şeklinde Temsili")
plt.xlabel("Açı (°)")
plt.ylabel("Titreşim Şiddeti")
plt.legend()
plt.grid(True)
plt.tight_layout()

# PNG kaydet
png_path = os.path.join(folder_path, f"piezo_sine_plot_{timestamp}.png")
plt.savefig(png_path)

# CSV kaydet
csv_path = os.path.join(folder_path, f"piezo_data_{timestamp}.csv")
with open(csv_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    header = ["Açı"] + list(data.keys())
    writer.writerow(header)
    for i in range(360):
        row = [angles[i]] + [data[s][i] for s in data.keys()]
        writer.writerow(row)

# JSON kaydet
json_path = os.path.join(folder_path, f"piezo_data_{timestamp}.json")
with open(json_path, 'w') as f:
    json.dump({"angles": angles.tolist(), "data": {k: v.tolist() for k, v in data.items()}}, f, indent=4)

# En son grafik göster
plt.show()
