from flask import Flask, request, send_file, jsonify
from reportlab.pdfgen import canvas
from io import BytesIO
import re

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    name = data.get('name', '')

    if not re.search(r"andrew|andy|drew|andrea", name, re.IGNORECASE):
        return jsonify({"error": "Name not allowed."}), 403

    buffer = BytesIO()
    c = canvas.Canvas(buffer)
    c.setFont("Helvetica-Bold", 24)
    c.drawString(100, 500, "This Certificate Is Presented To")
    c.setFont("Helvetica", 30)
    c.drawString(100, 450, name)
    c.setFont("Helvetica", 16)
    c.drawString(100, 400, f"In recognition of the induction of {name} into the Council of Andrews.")
    c.save()

    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name="andrew_certificate.pdf", mimetype='application/pdf')

if __name__ == '__main__':
    app.run(debug=True)
