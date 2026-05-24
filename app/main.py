from fastapi import FastAPI, Depends, HTTPException, status, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List, Optional


from .database import engine, Base, get_db
from . import models, schemas

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Gerenciamento de Voluntários")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/volunteer-list", response_model=schemas.VoluntarioPagina)
def listar_voluntarios(page: int = Query(1, ge=1),
    limit: int = Query(5, ge=1, le=100),db: Session = Depends(get_db)):
    skip = (page - 1) * limit

    query = db.query(models.VoluntarioModel)

    total = query.count()

    voluntarios = (
        query
        .offset(skip)
        .limit(limit)
        .all()
    )

    return {
        "page": page,
        "limit": limit,
        "total": total,
        "items": voluntarios
    }

@app.get("/volunteer/{id}", response_model=schemas.VoluntarioResponse)
def buscar_por_id(id: int, db: Session = Depends(get_db)):
    voluntario = db.query(models.VoluntarioModel).filter(models.VoluntarioModel.id == id).first()
    if not voluntario:
        raise HTTPException(status_code=404, detail="Voluntário não encontrado")
    return voluntario


@app.post("/volunteer-create", response_model=schemas.VoluntarioResponse, status_code=status.HTTP_201_CREATED)
def criar_voluntario(payload: schemas.VoluntarioCreate, db: Session = Depends(get_db)):
    email_existe = db.query(models.VoluntarioModel).filter(models.VoluntarioModel.email == payload.email).first()

    if email_existe:
        raise HTTPException(status_code=409, detail="Email já cadastrado!")

    dados= payload.model_dump() 
    dados["email"] = str(dados["email"])

    novo_voluntario = models.VoluntarioModel(**dados)
    
    db.add(novo_voluntario)
    db.commit()
    db.refresh(novo_voluntario)
    return novo_voluntario


@app.put("/volunteer-update/{id}", response_model=schemas.VoluntarioResponse)
def atualizar_voluntario(id: int, payload: schemas.VoluntarioUpdate, db: Session = Depends(get_db)):
    voluntario = db.query(models.VoluntarioModel).filter(models.VoluntarioModel.id == id).first()
    if not voluntario:
        raise HTTPException(status_code=404, detail="Voluntário não encontrado")

    dados_atualizacao = payload.dict(exclude_unset=True)
    for chave, valor in dados_atualizacao.items():
        setattr(voluntario, chave, valor)

    db.commit()
    db.refresh(voluntario)
    return voluntario

@app.delete("/volunteer-del/{id}", status_code=status.HTTP_200_OK)
def inativar_voluntario(id: int, db: Session = Depends(get_db)):
    voluntario = db.query(models.VoluntarioModel).filter(models.VoluntarioModel.id == id).first()
    if not voluntario:
        raise HTTPException(status_code=404, detail="Voluntário não encontrado")

    voluntario.status = False
    db.commit()
    return {"message": "Voluntário inativado com sucesso!"}