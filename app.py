from flask import Flask, render_template_string

app = Flask(__name__)

# Örnek analiz verisi (gerçekten alınabilir hale gelecek)
results = {
    "A0": {"angle": 16, "amplitude": 164, "ma": {"angle": 16, "r": 54.25}, "mb": {"angle": 106, "r": 41.07}},
    "A1": {"angle": 16, "amplitude": 172, "ma": {"angle": 16, "r": 56.25}, "mb": {"angle": 106, "r": 41.07}},
    "A2": {"angle": 173, "amplitude": 181, "ma": {"angle": 173, "r": 39.20}, "mb": {"angle": 263, "r": 43.78}},
    "A3": {"angle": 267, "amplitude": 197, "ma": {"angle": 267, "r": 51.86}, "mb": {"angle": 357, "r": 0.12}},
}

html_template = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>Balans Web Paneli</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        table { border-collapse: collapse; width: 70%; margin: auto; }
        th, td { border: 1px solid #ccc; padding: 8px; text-align: center; }
        th { background-color: #f2f2f2; }
        h1 { text-align: center; }
    </style>
</head>
<body>
    <h1>Balans Tespit Sonuçları</h1>
    <table>
        <tr>
            <th>Sensör</th><th>Bozukluk Açısı (°)</th><th>Titreşim</th><th>ma (g @ °)</th><th>mb (g @ °)</th>
        </tr>
        {% for key, data in results.items() %}
        <tr>
            <td>{{ key }}</td>
            <td>{{ data.angle }}</td>
            <td>{{ data.amplitude }}</td>
            <td>{{ data.ma.r }}g @ {{ data.ma.angle }}°</td>
            <td>{{ data.mb.r }}g @ {{ data.mb.angle }}°</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(html_template, results=results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
