from typing import Annotated, Generator

from fastapi import Depends
from sqlmodel import Session, create_engine

from .config import Settings, get_settings

settings: Settings = get_settings()

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))


def get_session() -> Generator[Session]:
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
