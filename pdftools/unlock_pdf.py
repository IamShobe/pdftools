import pathlib

import typer
from PyPDF2 import PdfReader, PdfWriter


def unlock(
    source_pdf: pathlib.Path,
    password: str = typer.Option(
        None, '--password', '-p', help="password to unlock the pdf with",
    ),
    output_pdf: pathlib.Path = typer.Option('out.pdf', '--output', help="output path for the pdf file"),
):
    if password is None:
        password = typer.prompt('Enter password', hide_input=True)

    writer = PdfWriter()
    reader = PdfReader(source_pdf, password=password)

    for page in reader.pages:
        writer.add_page(page)

    writer.write(output_pdf)
