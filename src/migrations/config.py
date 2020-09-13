from alembic.config import Config

from src.settings import DB_URI, BASE_DIR

alembic_cfg = Config()
alembic_cfg.set_main_option('script_location', f"{BASE_DIR}/src/migrations")
alembic_cfg.set_main_option('sqlalchemy.url', DB_URI)
