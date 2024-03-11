import os

from pypdf import PdfWriter

merger = PdfWriter()

for pdf in sorted(os.listdir('source/process')):
    merger.append(f"source/process/{pdf}")

merger.write('output/merged.pdf')
merger.close()
