import typer

from .unlock_pdf import unlock
from .extract_page import extract_page
from .merge import merge


app = typer.Typer()
app.command()(unlock)
app.command()(extract_page)
app.command()(merge)


def main():
    app()


if __name__ == "__main__":
    main()
