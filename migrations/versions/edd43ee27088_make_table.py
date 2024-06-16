"""make Table

Revision ID: edd43ee27088
Revises: 25e009d94d35
Create Date: 2024-06-12 16:00:32.313863

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'edd43ee27088'
down_revision: Union[str, None] = '25e009d94d35'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
