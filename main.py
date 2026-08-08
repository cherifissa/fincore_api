from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI, HTTPException, status
from sqlmodel import Session, select

from database import create_db_and_tables, get_session
from models import User, UserCreate, UserResponse


# Lifespan : Crée automatiquement les tables manquantes dans Postgres au lancement
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(title="Fincore API (SQLModel)", lifespan=lifespan)


@app.get("/")
def home():
    return {"message": "Fincore API avec SQLModel est fonctionnelle !"}


# --- POST : Créer un utilisateur ---
@app.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user_data: UserCreate, session: Session = Depends(get_session)):
    # Vérifier si l'email existe déjà
    existing_user = session.exec(
        select(User).where(User.email == user_data.email)
    ).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Cet email est déjà utilisé.")

    # Conversion automatique du schéma Pydantic vers le modèle de table
    db_user = User.model_validate(user_data)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


# --- GET : Lister tous les utilisateurs ---
@app.get("/users", response_model=list[UserResponse])
def get_users(session: Session = Depends(get_session)):
    users = session.exec(select(User)).all()
    return users


# --- GET : Récupérer un utilisateur par son ID ---
@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Utilisateur non trouvé",
        )
    return user


# --- DELETE : Supprimer un utilisateur ---
@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Utilisateur non trouvé",
        )
    session.delete(user)
    session.commit()
    return None
