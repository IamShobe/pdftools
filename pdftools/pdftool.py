import typer

from .unlock_pdf import unlock
from .extract_page import extract_page


app = typer.Typer()
app.command()(unlock)
app.command()(extract_page)


def main():
    app()


if __name__ == "__main__":
    main()
