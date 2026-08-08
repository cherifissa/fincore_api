import importlib
import os
from pathlib import Path
import pkgutil
from dotenv import load_dotenv
from sqlalchemy.engine import URL
from sqlmodel import SQLModel, Session, create_engine

# Import du dossier/paquet models
import models

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

db_url = URL.create(
    drivername="postgresql+psycopg",
    username=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST", "localhost"),
    port=int(os.getenv("POSTGRES_PORT", 5432)),
    database=os.getenv("POSTGRES_DB"),
)

engine = create_engine(db_url, echo=True)


def load_all_models():
    """Scanne le dossier models/ et charge automatiquement TOUS les fichiers .py."""
    for _, module_name, _ in pkgutil.iter_modules(models.__path__):
        importlib.import_module(f"models.{module_name}")


def create_db_and_tables():
    # 1. On charge automatiquement tous les modèles du dossier models/
    load_all_models()
    # 2. SQLModel crée toutes les tables découvertes
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
