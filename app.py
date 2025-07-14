from flask import Flask, request, render_template, send_from_directory, redirect, url_for
import os
import subprocess

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

GS_PATH = "C:\\Program Files\\gs\\gs10.05.1\\bin\\gswin64c.exe"

def compress_pdf(input_path, output_path, quality="ebook"):
    command = [
        GS_PATH,
        "-sDEVICE=pdfwrite",
        "-dCompatibilityLevel=1.4",
        f"-dPDFSETTINGS=/{quality}",
        "-dNOPAUSE",
        "-dQUIET",
        "-dBATCH",
        f"-sOutputFile={output_path}",
        input_path
    ]
    subprocess.run(command, check=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("pdf")
        quality = request.form.get("quality", "ebook")

        if not file or file.filename == '':
            return "No file selected", 400

        input_path = os.path.join(UPLOAD_FOLDER, file.filename)
        compressed_name = f"compressed_{quality}_{file.filename}"
        output_path = os.path.join(UPLOAD_FOLDER, compressed_name)

        file.save(input_path)

        try:
            compress_pdf(input_path, output_path, quality=quality)
            size_kb = round(os.path.getsize(output_path) / 1024, 2)
        except Exception as e:
            return f"Compression failed: {e}", 500

        return render_template("index.html",
                               download=True,
                               filename=compressed_name,
                               filesize=size_kb)
    
    return render_template("index.html", download=False)

@app.route("/download/<filename>")
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)