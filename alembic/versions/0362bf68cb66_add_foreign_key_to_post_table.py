"""add foreign key to post table

Revision ID: 0362bf68cb66
Revises: da5ca7a569b2
Create Date: 2024-07-11 22:58:56.596707

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0362bf68cb66'
down_revision: Union[str, None] = 'da5ca7a569b2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
