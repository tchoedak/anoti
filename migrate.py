from alembic.config import Config
from alembic import command
from anoti.db import _engine

migrations_cfg = Config()
migrations_cfg.set_main_option("script_location", "migrations")
engine = _engine()
connection = engine.begin()

command.upgrade(
    migrations_cfg,
    'head'
)
