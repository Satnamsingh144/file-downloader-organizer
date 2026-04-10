# 🚀 Smart File Downloader & Organizer

A powerful Python automation tool that downloads multiple files from URLs and automatically organizes them into structured folders based on file types.

---

## ✨ Features

- 📥 Download multiple files from URLs
- ⚡ Multithreaded downloads for faster performance
- 📂 Automatic file categorization (images, videos, documents, etc.)
- 🔁 Duplicate-safe file naming (file(1), file(2), etc.)
- ✅ URL validation and error handling
- 🧹 Clean and user-friendly console output

---

## 🛠️ Technologies Used

- Python
- requests
- os
- threading
- urllib.parse

---

## ▶️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Satnamsingh144/file-downloader-organizer.git

2. Navigate to the project folder:
   cd file-downloader-organizer

3. Install dependencies:
   pip install requests

4. Run the script:
  python main.py

---

📌 Example

Enter file URL:
https://example.com/file1.png, https://example.com/file2.pdf

Output:
📥 Downloading: file1.png
✅ Saved: file1.png → images

📥 Downloading: file2.pdf
✅ Saved: file2.pdf → documents

========== SUMMARY ==========
✔ Valid URLs: 2
❌ Invalid URLs: 0

🎉 All downloads completed!

📂 Folder Structure:
downloads/
│
├── images/
├── videos/
├── documents/
├── audio/
├── compressed/
├── code/
└── others/
---

🔮 Future Improvements

-GUI interface (desktop application)
-Download progress bar
-Pause/Resume downloads
-Drag & drop supportg

---

👨‍💻 Author

Satnam Singh