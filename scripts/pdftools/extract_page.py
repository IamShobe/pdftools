import pathlib

import typer
from PyPDF2 import PdfReader, PdfWriter

from .common import output_pdf_option


def page_number_callback(value: int):
    if value <= 0:
        raise typer.BadParameter("Value must be larger than 0")
    return value


def extract_page(
        source_pdf: pathlib.Path,
        page_number: int = typer.Argument(..., callback=page_number_callback),
        output_pdf: pathlib.Path = output_pdf_option,
        password: str = typer.Option(
            None, '--password', '-p', help="password to unlock the pdf with",
        ),
):
    writer = PdfWriter()
    reader = PdfReader(source_pdf, password=password)

    page_index = page_number - 1

    if page_index > len(reader.pages) - 1:
        print(f"no such page number! insert a page number between 1 to {len(reader.pages)}")
        raise typer.Exit(1)

    writer.add_page(reader.pages[page_index])

    writer.write(output_pdf)
