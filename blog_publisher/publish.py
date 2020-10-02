import typer
from typing import Union

app = typer.Typer()


def parse_src(src: str):
    pass


@app.command()
def publish(
    src: str, dest: str, dry_run: bool = False,
):
    """
    SRC points to the Path of Markdown file

    DEST points to website where you need to publish the blog

    If you pass --dry-run flag, SRC will be parsed but will not be published
    """
    if dry_run:
        typer.echo("Running in dry_run mode")
    typer.echo(f"Publishing blog from {src} to {dest}")


if __name__ == "__main__":
    app()
