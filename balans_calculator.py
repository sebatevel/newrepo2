import math

class Polar:
    def __init__(self, r=0.0, th=0.0):
        self.r = r
        self.th = th  # Radyan cinsinden açı

    def __repr__(self):
        return f"Polar(r={self.r:.2f}, th={math.degrees(self.th):.2f}°)"

def get_ab_equation(m1, m2, s1, s2, angle):
    D = m1 - m2
    D1 = s1 - s2
    D2 = m1 * s2 - m2 * s1

    a = Polar()
    b = Polar()
    a.r = D1 / D if D != 0 else 0
    b.r = D2 / D if D != 0 else 0
    a.th = angle
    b.th = angle
    return a, b

def polar_to_cartesian(p):
    x = p.r * math.cos(p.th)
    y = p.r * math.sin(p.th)
    return x, y

def cartesian_to_polar(x, y):
    r = math.hypot(x, y)
    th = math.atan2(y, x)
    return Polar(r, th)

def solve_balance(x: Polar, y: Polar, theta: float):
    # Açıları göreli düzeltici yönlerle ayarla
    th_a = theta
    th_b = (theta + math.radians(90)) % (2 * math.pi)

    # Kalibrasyon verileri (örnek)
    masslist = [100, 200]  # gram
    XA = [400, 800]        # x yönü tepkisi
    YA = [250, 700]        # y yönü tepkisi

    Axa, Bxa = get_ab_equation(masslist[0], masslist[1], XA[0], XA[1], th_a)
    Aya, Bya = get_ab_equation(masslist[0], masslist[1], YA[0], YA[1], th_b)

    x1, y1 = polar_to_cartesian(x)
    bx1, by1 = polar_to_cartesian(Bxa)
    bx2, by2 = polar_to_cartesian(Bya)
    ax1, ay1 = polar_to_cartesian(Axa)
    ax2, ay2 = polar_to_cartesian(Aya)

    dx = x1 - bx1
    dy = y1 - by2

    det = ax1 * ay2 - ax2 * ay1

    print(f"\n🔬 Debug: determinant = {det:.4f}")
    print(f"  x = {x}, y = {y}")
    print(f"  Axa = ({ax1:.2f}, {ay1:.2f})")
    print(f"  Aya = ({ax2:.2f}, {ay2:.2f})")
    print(f"  Bxa = ({bx1:.2f}, {by1:.2f})")
    print(f"  Bya = ({bx2:.2f}, {by2:.2f})")

    if abs(det) < 1e-6:
        return None, None

    ma_r = (dx * ay2 - dy * ax2) / det
    mb_r = (dx * ay1 - dy * ax1) / -det

    ma = Polar(ma_r, th_a)
    mb = Polar(mb_r, th_b)
    return ma, mb

# Simulate Encoder Entegrasyonu için hazır kullanım:
def analyze_measurement(amplitude, angle_deg):
    theta = math.radians(angle_deg)
    x = Polar(amplitude, theta)
    y = Polar(amplitude * 0.8, theta + math.radians(90))
    ma, mb = solve_balance(x, y, theta)
    return ma, mb

# Test örneği
if __name__ == "__main__":
    # Ölçüm vektörleri
    theta_deg = 45
    ma, mb = analyze_measurement(200, theta_deg)

    print("\n⚖️ Dengeleme Sonuçları:")
    print(f"ma: {ma}")
    print(f"mb: {mb}")
