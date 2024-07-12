"""add content column to post table

Revision ID: d7b5d6eadd9c
Revises: 060808762351
Create Date: 2024-07-11 22:33:16.106117

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd7b5d6eadd9c'
down_revision: Union[str, None] = '060808762351'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
