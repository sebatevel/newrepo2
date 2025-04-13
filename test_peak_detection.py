from processing.measurement_buffer import Measurement

# Simülasyon veya gerçek veriyle test için örnek Measurement nesnesi oluştur
m = Measurement()

# Simüle edilmiş 360 derecelik örnek veri (örnek amaçlı basitleştirilmiş)
for angle in range(360):
    m.add_data_point(
        angle,
        a0 = 100 + (50 if angle == 45 else 0),  # A0: 45 derecede pik
        a1 = 100 + (70 if angle == 120 else 0), # A1: 120 derecede pik
        a2 = 100 + (90 if angle == 270 else 0), # A2: 270 derecede pik
        a3 = 100 + (30 if angle == 200 else 0)  # A3: 200 derecede pik
    )

# Her piezo için en yüksek titreşimin olduğu açı ve şiddeti bul
results = m.detect_peak_angles()

# Sonuçları yazdır
for piezo, info in results.items():
    print(f"✩ {piezo}: Açı = {info['angle']}°, Şiddet = {info['amplitude']}")
