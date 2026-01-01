from typing import Annotated, Sequence

from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlmodel import select

from app.deps.db import SessionDep
from app.models.bands import Band, BandCreate, BandPublic, BandUpdate
from app.routers.parameters import GeneralParameters

router = APIRouter(prefix="/bands")

invalid_id_exception = lambda id: HTTPException(
    status_code=404, detail=f"Unable to find band with ID {id}"
)

invalid_name_exception = lambda name: HTTPException(
    status_code=404, detail=f"Unable to find band with name {name}"
)


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
    raise invalid_id_exception(band_id)


@router.get("/{band_name}", response_model=BandPublic)
def get_band_by_name(band_name: str, session: SessionDep) -> Band:
    if band := session.exec(select(Band).where(Band.name == band_name)).first():
        return band
    raise invalid_name_exception(band_name)


@router.post("/create", response_model=BandPublic)
def create_band(session: SessionDep, band: BandCreate):
    db_model = Band.model_validate(band)
    session.add(db_model)
    session.commit()
    session.refresh(db_model)
    return db_model


@router.put("/update/{band_id}", response_model=BandPublic)
def update_band_by_id(band_id: int, session: SessionDep, band: BandUpdate):
    if db_model := session.get(Band, band_id):
        db_model.sqlmodel_update(band.model_dump(exclude_unset=True, exclude_none=True))
        session.add(db_model)
        session.commit()
        session.refresh(db_model)
        return db_model
    raise invalid_id_exception(band_id)


@router.put("/update/{band_name}", response_model=BandPublic)
def update_band_by_name(band_name: str, session: SessionDep, band: BandUpdate):
    if db_model := session.exec(select(Band).where(Band.name == band_name)).first():
        db_model.sqlmodel_update(band.model_dump(exclude_unset=True, exclude_none=True))
        session.add(db_model)
        session.commit()
        session.refresh(db_model)
        return db_model
    raise invalid_name_exception(band_name)
