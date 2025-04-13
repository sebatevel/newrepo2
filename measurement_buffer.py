# processing/measurement_buffer.py

# processing/measurement_buffer.py

class Measurement:
    def __init__(self):
        self.encoder_angles = []
        self.piezo_signals = { "A0": [], "A1": [], "A2": [], "A3": [] }

    def add_data_point(self, angle, a0, a1, a2, a3):
        self.encoder_angles.append(angle)
        self.piezo_signals["A0"].append(a0)
        self.piezo_signals["A1"].append(a1)
        self.piezo_signals["A2"].append(a2)
        self.piezo_signals["A3"].append(a3)

    def detect_peak_angles(self):
        results = {}
        for channel, data in self.piezo_signals.items():
            if not data:
                results[channel] = {"angle": None, "amplitude": None}
                continue

            peak_idx = data.index(max(data))
            angle_at_peak = self.encoder_angles[peak_idx]
            amplitude = data[peak_idx]

            results[channel] = {
                "angle": angle_at_peak,
                "amplitude": amplitude
            }

        return results
