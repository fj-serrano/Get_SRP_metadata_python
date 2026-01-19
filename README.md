# 📄 SRA Metadata Table Generator (Python)

This Python script processes **SRA metadata files in `.csv` format** and automatically generates a **clean, formatted `.tsv` table**. The output is designed to be directly usable in downstream bioinformatics pipelines, ensuring consistent naming and structure.

---

## 📁 Input files

### Required input
- **Metadata `.csv` file**
  - Selected by the user through a graphical file explorer.
  - Must contain at least the following columns:
    - `Experiment`
    - `Run`
    - `SRA Study`
  - May include additional columns that the user can optionally select.

---

## ⚙️ Requirements

- **Python 3**
- Required libraries:
  - `pandas`
  - `tkinter` (included by default in most Python installations)

No additional external dependencies are required.

---

## ▶️ Script usage

Run the script from the terminal or a Python environment:

```bash
python Get_SRP_metadata_python.py
````

---

## 🔀 Execution workflow

1. A **graphical file dialog** opens, allowing the user to select the input `.csv` metadata file.
2. The script prints **all available column names** to the terminal.
3. The user can type, one by one, the names of any **additional columns** they want to include.
4. Press **Enter on an empty line** to finish the column selection.
5. The script automatically generates a formatted `.tsv` file using the study name.

---

## 🧑‍💻 User interaction

- File selection is performed via a **Tkinter graphical interface**.
- Column selection is done through **standard input (command line)**.
- Only columns that exist in the input file are included in the output.
- If an error occurs during file loading, an informative message is printed.

---

## 📤 Output

The script generates a single output file:

- **Tab-separated values file (`.tsv`)**
  - File name format:
    ```
    <SRA_Study>.tsv
    ```
  - Table contents:
    - Fixed columns:
      - `Experiment.fa.gz`
      - `Experiment`
      - `Run`
    - Additional columns selected by the user

---

### 🛠️ Data processing applied

- A new column is created automatically:
  - `Experiment.fa.gz` 
- Any text enclosed in parentheses is removed using regular expressions.
- All spaces are replaced with underscores (`_`) to ensure consistent naming.

---

## 🔍 How the script works

The script is divided into three main stages:

### 1️⃣ File selection and loading

- A file explorer is launched using `tkinter`.
- The selected `.csv` file is read into a `pandas` DataFrame.
- File paths are normalized to avoid compatibility issues.

### 2️⃣ Data preprocessing

- Creation of the `Experiment.fa.gz` column.
- Removal of parenthetical annotations.
- Replacement of spaces with underscores across all fields.

These steps ensure clean, uniform, and pipeline-friendly identifiers.

### 3️⃣ Output table generation

- The user specifies additional columns to include.
- Column widths are calculated dynamically based on the longest value of length per column.
- A left-justified text table is constructed.
- The formatted table is written to a `.tsv` file.

---

## 🧠 Implementation details

- Data access is handled using a `DataFrame`.
- Column justification adapts automatically to content length.
- The output is both **human-readable** and **machine-friendly**.
- The modular structure allows easy extension or customization.

---

## 📌 Notes

- The input `.csv` file must be correctly formatted.
- User-specified columns that do not exist are ignored.
- Compatible with **Windows, Linux, and macOS**.
