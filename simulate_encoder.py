from hardware.arduino_serial import connect_serial, read_line, parse_csv_line
from processing.measurement_buffer import Measurement
from processing.balans_calculator import analyze_measurement
import time
import math

measurement = Measurement()
angle = 0

ser = connect_serial("/dev/ttyUSB0", 115200)

print("🔁 Simüle edilmiş encoder ile örnek toplama başlıyor...\n(CTRL+C ile çık)")

try:
    while angle < 360:  # 1 tam dönüşlük örnek toplayalım
        raw = read_line(ser)
        if raw:
            piezo = parse_csv_line(raw)
            if piezo:
                measurement.add_data_point(angle, piezo['A0'], piezo['A1'], piezo['A2'], piezo['A3'])
                print(f"🔹 Açı: {angle}° | A0: {piezo['A0']} A1: {piezo['A1']} A2: {piezo['A2']} A3: {piezo['A3']}")
                angle += 1
        else:
            time.sleep(0.001)

except KeyboardInterrupt:
    print("\n🛑 Simülasyon durduruldu.")

# 🔍 Ölçüm tamamlandıktan sonra ANALİZ başlasın:
print("\n🔍 ANALİZ SONUCU (Bozukluk Açısı + Şiddet):")
results = measurement.detect_peak_angles()

for piezo, info in results.items():
    r = info["amplitude"]
    theta_deg = info["angle"]
    if theta_deg is None:
        print(f"\n⚠️ {piezo}: Yeterli veri yok.")
        continue

    theta_rad = math.radians(theta_deg)

    print(f"\n⚙️ {piezo}:")
    print(f"   En büyük titreşim: {r}")
    print(f"   Bozukluk açısı: {theta_deg}°")

    ma, mb = analyze_measurement(r, theta_deg)

    print(f"   ➕ Düzeltici Ağırlık A: {ma}")
    print(f"   ➕ Düzeltici Ağırlık B: {mb}")
