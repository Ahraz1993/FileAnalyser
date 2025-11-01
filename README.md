# 🧮 File Analyzer

A Python tool that analyzes text files and provides detailed statistics like:

- Total lines, words, and characters  
- The longest and shortest lines (with index and length)  
- Top N most frequent words  
- Automatic file backup in a `backupDir` folder  

---

## ⚙️ How to Run

You can run the File Analyzer in two ways — either directly as a Python script or through Jupyter Notebook.

▶️ Option 1 — Run as a Python Script

Open a terminal or command prompt in your project folder.

Run:

python AnalyserProject.py

When prompted, enter:
• Either the full path to your text file
(e.g. C:\Users\Ahraz Athar\FileAnalyserProject\Ahraz.txt)
• Or just the file name if it’s in the same folder.

▶️ Option 2 — Run in Jupyter Notebook

Open Jupyter Notebook or Jupyter Lab.

Navigate to your project folder.

Open AnalyserProject.ipynb.

Run the notebook cells in order to see results interactively — perfect for demos, debugging, or classroom use.

---

## 💡 Features

✅ Counts total lines, words, and characters  
✅ Finds longest and shortest lines  
✅ Detects most frequent words (user-controlled number)  
✅ Creates a backup automatically  
✅ Handles missing files and bad inputs gracefully  

---

## 📊 Example Output

📊 File Analysis Summary:
Total Lines : 102
Total Words : 405
Total Characters : 1752

✅ A copy of your file has been saved at C:\Users\Ahraz Athar\backupDir\Ahraz.txt

📏 The longest line is at index 101 with length 44:
dchdsjndsjnvsdjvndsjvnjdsndjvnsdjnwewiequhhh

📏 The shortest line is at index 0 with length 16:
This is 0 line

🔤 Top 3 most frequent words:

'this' appears 101 times

'is' appears 101 times

'line' appears 101 times

---

## 🛠️ Requirements

No external dependencies — only standard Python libraries:

- `pathlib`  
- `shutil`  
- `string`  
- `collections.Counter`

✅ Tested on **Python 3.10+**

---

## 🧱 Project Structure

FileAnalyserProject/
│
├── AnalyserProject.py  # Main Python script
├── AnalyserProject.ipynb # Notebook version (interactive)
├── sample_data/
│  └── Ahraz.txt  # Sample test file
├── README.md    # Documentation
├── .gitignore   # Ignores cache + backupDir
└── backupDir/   # Created automatically

---

## 👨‍💻 Author

**Ahraz Athar**
