import pathlib

import typer
from PyPDF2 import PdfReader, PdfWriter


def unlock(
    source_pdf: pathlib.Path,
    output_pdf: pathlib.Path,
    password: str = typer.Option(
        None, '--password', '-p', help="password to unlock the pdf with",
    ),
):
    if password is None:
        password = typer.prompt('Enter password', hide_input=True)

    writer = PdfWriter()
    reader = PdfReader(source_pdf, password=password)

    for page in reader.pages:
        writer.add_page(page)

    with open(output_pdf, 'wb') as fp:
        writer.write(fp)
