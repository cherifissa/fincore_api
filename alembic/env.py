import importlib
from logging.config import fileConfig
import pkgutil
from alembic import context
from sqlalchemy import engine_from_config, pool
from sqlmodel import SQLModel

# 1. Import de l'engine et du dossier models
from config.database import engine
import models

# 2. Scanner automatiquement tous les modèles du dossier models/
for _, module_name, _ in pkgutil.iter_modules(models.__path__):
    importlib.import_module(f"models.{module_name}")

config = context.config

# 3. Récupération dynamique de l'URL avec évasion des caractères spéciaux (%)
url_str = engine.url.render_as_string(hide_password=False).replace("%", "%%")
config.set_main_option("sqlalchemy.url", url_str)

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# 4. Métadonnées SQLModel
target_metadata = SQLModel.metadata


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
