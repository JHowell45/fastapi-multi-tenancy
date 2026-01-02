from typing import Annotated, Generator

from fastapi import Depends
from sqlalchemy import Connection
from sqlalchemy.sql import text
from sqlmodel import Session, create_engine

from .config import Settings, get_settings

settings: Settings = get_settings()

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))


def get_session() -> Generator[Session]:
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]


def update_search_path(conn: Connection, schemas: list[str]) -> None:
    formatted_schemas: str = ", ".join(f'"{schema}"' for schema in schemas)
    conn.execute(text(f"set search_path to {formatted_schemas};"))
    conn.commit()
