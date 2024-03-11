import os

from pypdf import PdfWriter

merger = PdfWriter()

for pdf in sorted(os.listdir('source')):
    pdf_path = f"source/{pdf}"
    print(f"Merging: {pdf_path}")
    merger.append(pdf_path)

merger.write('output/merged.pdf')
merger.close()
