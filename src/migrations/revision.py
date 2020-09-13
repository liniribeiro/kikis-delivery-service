
from alembic import command

from src.migrations import revision
from src.migrations.config import alembic_cfg


if __name__ == "__main__":
    revision()
