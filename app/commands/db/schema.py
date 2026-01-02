from typing import Annotated

import typer
from rich import print
from sqlalchemy import inspect
from sqlalchemy.schema import CreateSchema

from app.deps.db import engine

cli = typer.Typer(no_args_is_help=True)


@cli.command(help="Creates a new postgres db schema for a tenant.")
def create(schema_name: Annotated[str, typer.Argument()]) -> None:
    with engine.connect() as connection:
        if not inspect(connection).has_schema(schema_name):
            connection.execute(CreateSchema(schema_name))
            connection.commit()
            print(f"[green] Schema '{schema_name}' successfully created!")
        else:
            print(f"[yellow] Schema '{schema_name}' already exists!")
