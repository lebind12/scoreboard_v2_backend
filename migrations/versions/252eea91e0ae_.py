"""empty message

Revision ID: 252eea91e0ae
Revises: f92150cd52b0
Create Date: 2024-06-15 05:23:22.708457

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '252eea91e0ae'
down_revision: Union[str, None] = 'f92150cd52b0'
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
    sa.Column('starttime', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_match'))
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('match')
    # ### end Alembic commands ###
