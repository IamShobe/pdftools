import pathlib

import typer
from PyPDF2 import PdfReader, PdfWriter


def extract_page(
        source_pdf: pathlib.Path,
        output_pdf: pathlib.Path,
        page: int,
        password: str = typer.Option(
            None, '--password', '-p', help="password to unlock the pdf with",
        ),
):
    writer = PdfWriter()
    reader = PdfReader(source_pdf, password=password)

    writer.add_page(reader.pages[page])

    with open(output_pdf, 'wb') as fp:
        writer.write(fp)
