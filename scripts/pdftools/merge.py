import pathlib

from PyPDF2 import PdfReader, PdfWriter

from .common import output_pdf_option


def merge(
        pdfs: list[pathlib.Path],
        output_pdf: pathlib.Path = output_pdf_option,
):
    writer = PdfWriter()

    for pdf_path in pdfs:
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            writer.add_page(page)

    writer.write(output_pdf)
