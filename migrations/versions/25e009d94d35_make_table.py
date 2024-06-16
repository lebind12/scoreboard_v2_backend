"""make Table

Revision ID: 25e009d94d35
Revises: 33f3216ee451
Create Date: 2024-06-12 16:00:03.492189

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '25e009d94d35'
down_revision: Union[str, None] = '33f3216ee451'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
