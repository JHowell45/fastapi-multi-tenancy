from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship

from .relationship_linkers import BandSupportGigLink
from .traits.tenants import TenantMixin

if TYPE_CHECKING:
    from .bands import Band


class Gig(TenantMixin, table=True):
    __tablename__ = "gigs"

    id: int | None = Field(default=None, primary_key=True)

    primary_band_id: int = Field(foreign_key="bands.id")
    primary_band: Band = Relationship(back_populates="headline_gigs")

    support_bands: list[Band] = Relationship(
        back_populates="support_gigs", link_model=BandSupportGigLink
    )
    support_bands: list[Band] = Relationship(
        back_populates="support_gigs", link_model=BandSupportGigLink
    )
