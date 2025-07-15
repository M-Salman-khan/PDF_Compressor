# PDF Compressor Web App 📄⚡

![Flask](https://img.shields.io/badge/Flask-v2.3-blue.svg) ![Python](https://img.shields.io/badge/Python-v3.10+-yellow.svg) ![Ghostscript](https://img.shields.io/badge/Ghostscript-v10.x-red.svg) ![License](https://img.shields.io/badge/License-MIT-green.svg)

A minimal, fast, and student-friendly PDF compression web app built using **Python Flask** and **Ghostscript**. This tool allows users to upload any PDF and compress it instantly to reduce file size while retaining readable quality — all through a sleek dark-mode UI.

## 📌 Description

This application solves a common frustration among students: **large PDF assignment file sizes** that exceed upload limits on university portals or emails. Instead of using sketchy online tools or installing heavy software, this lightweight web app gives you quick, quality-controlled PDF compression right from your browser.

⚡ **Completely Offline** – Unlike most online tools that require high-speed internet, this app works entirely offline once set up. You can compress PDFs anytime, anywhere — perfect for students with limited or no internet access.

## 🚀 Features

- 📄 Upload any PDF file and compress it in seconds
- 🧠 Choose from multiple quality levels: screen, ebook, printer, prepress
- 💾 Download compressed files with size info
- 🌙 Sleek dark mode UI for late-night usage
- 📶 No internet? No problem — fully functional offline for uninterrupted productivity
- 🌀 Loading spinner and blur effect during compression
- 🔁 Auto-redirect or manual return to homepage after download

## ⚙️ Tech Stack

- **Backend**: Flask (Python)
- **Compression Engine**: Ghostscript
- **Frontend**: HTML, CSS (Dark UI), JS

## 📁 Project Structure

```
PDF_Compressor/
├── templates/
│   └── index.html          # Main frontend UI
├── static/                 # Static files (CSS & JS)
│   ├── styles.css          # Custom dark theme styles
│   └── script.js           # Frontend interactivity (spinner, blur, etc.)
├── uploads/                # Stores uploaded and compressed files
├── app.py                  # Flask app logic
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## 💡 Prerequisites

- Python 3.10 or higher
- Flask: `pip install flask`
- Ghostscript installed on system (Windows/Mac/Linux)
- Add Ghostscript to system PATH (or update the path in `app.py`)

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/M-Salman-khan/PDF_Compressor.git
   cd PDF_Compressor
   ```

2. Install Flask:
   ```bash
   pip install flask
   ```

3. Install Ghostscript:
   - [Download for Windows](https://ghostscript.com/releases/gsdnld.html)
   - [Download for Linux/Mac](https://www.ghostscript.com/download/gsdnld.html)

4. Set Ghostscript path in `app.py`:
   ```python
   GS_PATH = "C:\Program Files\gs\gs10.05.1\bin\gswin64c.exe"
   ```

5. Run the Flask app:
   ```bash
   python app.py
   ```

   Then open your browser at:  
   **http://localhost:5000**

## 📦 Output Example

After compression, the user sees:
- ✅ A download section with filename and compressed size
- 🔽 A download button
- 🔁 A button to go back and compress another file

## 🎯 Why Students Love It

This tool was built with students in mind — especially those who struggle with:
- Uploading large assignment PDFs to college portals (with size limits)
- Emailing presentations or scanned notes
- Sharing lecture notes on WhatsApp, Telegram, etc.
- Compressing files in low or no internet zones — thanks to full **offline support**
With no login, no ads, no tracking — it just gets the job done.

## 🧪 Compression Quality Options

| Option     | Description                | Compression |
|------------|----------------------------|-------------|
| `screen`   | Lowest quality (max size cut) | 🔻 Maximum |
| `ebook`    | Balanced for readability     | ✅ Recommended |
| `printer`  | Medium quality for prints    | 🖨️ Moderate |
| `prepress` | High quality for publishing  | 📚 Least |

## 🌐 Future Plans

- Drag & Drop Upload
- Real-time size preview
- Multi-file compression

## 🤝 Contributing

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to GitHub (`git push origin feature/new-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.  
See the [LICENSE](LICENSE) file for more information.

## 👨‍💻 Author

**M Salman Khan**  
[🔗 GitHub Profile](https://github.com/M-Salman-khan)

---

⭐ **Star** this repo if this project helped you compress your assignments smoothly!
