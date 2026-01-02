from enum import StrEnum, auto
from pathlib import Path
from typing import Annotated

import typer
from alembic import command
from alembic.config import Config

cli = typer.Typer(no_args_is_help=True)


class SchemaType(StrEnum):
    CORE = auto()
    TENANTS = auto()


def get_alembic_config(schema: SchemaType, cmd_opts: list[str] | None = None) -> Config:
    file: Path = Path("../../../alembic.ini")
    return Config(file.resolve(), ini_section=schema.value, cmd_opts=cmd_opts)


@cli.command(help="Create a new migration for the called schema.")
def revision(
    schema: Annotated[
        SchemaType,
        typer.Argument(help="which schema type to create a migration revision for."),
    ],
    msg: Annotated[
        str, typer.Argument(help="The message to give to the new migration revision.")
    ],
) -> None:
    command.revision(get_alembic_config(schema), msg, autogenerate=True)


@cli.command(help="runs all of the newest migrations for the given schema type.")
def upgrade(
    schema: Annotated[SchemaType, typer.Argument()],
    rev: Annotated[str, typer.Option(help="Revision version to upgrade to.")] = "heads",
) -> None:
    command.upgrade(get_alembic_config(schema), revision=rev)


@cli.command(
    help="Lets you downgrade to an earlier migration version for the given schema type."
)
def downgrade(
    schema: Annotated[SchemaType, typer.Argument()],
    rev: Annotated[str, typer.Argument(help="Revision version to downgrade to.")],
) -> None:
    command.downgrade(get_alembic_config(schema), revision=rev)
