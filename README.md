# 📄 SRA Metadata Table Generator (Python)

This Python script processes **SRA metadata files in `.csv` format** and automatically generates a **clean, formatted `.tsv` table**. The output is designed to be directly usable in downstream bioinformatics pipelines, ensuring consistent naming and structure.

---

## 📁 Input files

- **Metadata `.csv` file**
  - Selected by the user through a graphical file explorer.
  - Must contain at least the following columns:
    - `Experiment`
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
- If an error occurs during file loading or processing, an informative message is printed.

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
      - `file` (constructed as `<Experiment>.fa.gz`)  
      - `name` (renamed from the original `Experiment` column)  
    - Additional columns selected by the user

---

### 🛠️ Data processing applied

- A new column `file` is created automatically by appending `.fa.gz` to each `Experiment` value.  
- The original column `Experiment` is renamed to `name`.  
- Any text enclosed in parentheses is removed using regular expressions.  
- All spaces are replaced with underscores (`_`) to ensure consistent naming.

---

## 🔍 How the script works

The script is divided into three main stages:

### 1️⃣ File selection and loading

- A file explorer is launched using `tkinter`.  
- The selected `.csv` file is read into a `pandas DataFrame`.  
- File paths are normalized to avoid compatibility issues.

### 2️⃣ Data preprocessing

- Creation of the `file` column with `<Experiment>.fa.gz` entries.  
- Renaming of the `Experiment` column to `name`.  
- Removal of parenthetical annotations.  
- Replacement of spaces with underscores across all fields.

These steps ensure clean, uniform, and pipeline-friendly identifiers.

### 3️⃣ Output table generation

- The user specifies additional columns to include. Only existing columns are included.  
- The DataFrame is exported to a tab-separated `.tsv` file including the fixed and selected columns.  
- The output is saved with the filename based on the `SRA Study`.

---

## 🧠 Implementation details

- Data is handled using a `pandas DataFrame`.  
- The output table columns include fixed and user-selected columns.  
- The output file is a `.tsv` with no row indices.  
- The script handles potential errors by printing a user-friendly message.

---

## 📌 Notes

- The input `.csv` file must be correctly formatted.  
- User-specified columns that do not exist in the input are ignored.  
- Compatible with **Windows, Linux, and macOS**.
