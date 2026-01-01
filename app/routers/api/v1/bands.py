from typing import Annotated, Sequence

from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlmodel import select

from app.deps.db import SessionDep
from app.models.bands import Band, BandPublic
from app.routers.parameters import GeneralParameters

router = APIRouter(prefix="/bands")


@router.get("/", response_model=list[BandPublic])
def read_bands(
    session: SessionDep,
    params: Annotated[GeneralParameters, Depends(GeneralParameters)],
) -> Sequence[Band]:
    return session.exec(select(Band).offset(params.offset).limit(params.limit)).all()


@router.get("/{band_id}", response_model=BandPublic)
def get_band_by_id(band_id: int, session: SessionDep) -> Band:
    if band := session.get(Band, band_id):
        return band
    raise HTTPException(
        status_code=404, detail=f"Unable to find band with ID {band_id}"
    )


@router.get("/{band_name}", response_model=BandPublic)
def get_band_by_name(band_name: str, session: SessionDep) -> Band:
    if band := session.exec(select(Band).where(Band.name == band_name)).first():
        return band
    raise HTTPException(
        status_code=404, detail=f"Unable to find band with name {band_name}"
    )
