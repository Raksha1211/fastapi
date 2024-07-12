"""add last few columns to posts  table

Revision ID: 1bb841f90726
Revises: 0362bf68cb66
Create Date: 2024-07-11 23:44:47.344072

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1bb841f90726'
down_revision: Union[str, None] = '0362bf68cb66'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column(
        'published', sa.Boolean(), nullable=False,server_default='True'),)
    op.add_column('posts',sa.Column(
        'created_at',sa.TIMESTAMP(timezone=True),nullable = False, server_defaut=sa.text('NOW()')),)   

    pass


def downgrade() -> None:
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
