import typer

from app.commands import db

cli = typer.Typer(no_args_is_help=True)
cli.add_typer(db.cli, name="db", help="commands for interacting with the db")

if __name__ == "__main__":
    cli()
