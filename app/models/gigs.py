from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .band import Band


class Gig(SQLModel, table=True):
    __tablename__ = "gigs"

    id: int | None = Field(default=None, primary_key=True)

    primary_band_id: int = Field(foreign_key="bands.id")
    primary_band: list[Band] = Relationship(back_populates="gigs")
