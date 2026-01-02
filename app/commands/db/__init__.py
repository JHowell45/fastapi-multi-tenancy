import typer

from . import schema

cli = typer.Typer(no_args_is_help=True)
cli.add_typer(schema.cli, name="schema")
