# PDF Manipulation with PyPDF

This Python script demonstrates how to perform various operations on PDF files using the PyPDF library.

## Features

1. **Merging PDF Files**: Merges multiple PDF files into a single PDF file.

2. **Reading Text from PDF**: Extracts text from a PDF file.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/pypdf-demo.git
    ```

2. Install the required library:

    ```bash
    pip install PyPDF2
    ```

## Usage

### Merging PDF Files

To merge PDF files, update the file names in the list `file_list` with the names of the PDF files you want to merge. Then run the script:

```python
python merge_pdfs.py
```

The merged PDF file will be created as `resumefile.pdf`.

### Reading Text from PDF

To read text from a PDF file, specify the file name in the `PdfReader` constructor and run the script:

```python
python read_pdf.py
```

The text content of the PDF file will be printed to the console.

## Example

Suppose you have three PDF files named "pdfkk.pdf", "RTU (1).pdf", and "RTV.pdf" that you want to merge. After running the script, the merged PDF file will be created as `rLL.pdf`.

Additionally, if you want to extract text from the "pdfkk.pdf" file, the script will print the text content to the console.

## Note

Make sure to update the file names and paths as per your directory structure.

---

### Code Output:

```plaintext
# Output of reading text from "pdfkk.pdf" file
Text content of pdfkk.pdf
...

```

