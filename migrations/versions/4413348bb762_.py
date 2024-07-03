"""empty message

Revision ID: 4413348bb762
Revises: a1523dad7cab
Create Date: 2024-07-03 09:08:42.605706

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4413348bb762'
down_revision: Union[str, None] = 'a1523dad7cab'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('match',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('naverid', sa.String(), nullable=False),
    sa.Column('sofascoredid', sa.Integer(), nullable=False),
    sa.Column('home', sa.String(), nullable=False),
    sa.Column('away', sa.String(), nullable=False),
    sa.Column('homeid', sa.Integer(), nullable=False),
    sa.Column('awayid', sa.Integer(), nullable=False),
    sa.Column('starttime', sa.String(), nullable=False),
    sa.Column('homenamecode', sa.String(), nullable=False),
    sa.Column('awaynamecode', sa.String(), nullable=False),
    sa.Column('matchstadium', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_match'))
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('match')
    # ### end Alembic commands ###
