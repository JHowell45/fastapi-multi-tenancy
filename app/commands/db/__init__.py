import typer

from . import migrate, schema

cli = typer.Typer(no_args_is_help=True)
cli.add_typer(
    schema.cli, name="schema", help="commands for interacting with postgres schemas."
)
cli.add_typer(
    migrate.cli,
    help="commands for creating and running migrations for both core and tenants.",
)
