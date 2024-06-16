"""empty message

Revision ID: 1448dac5f62b
Revises: 85f00c007ea5
Create Date: 2024-06-15 05:08:57.096801

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1448dac5f62b'
down_revision: Union[str, None] = '85f00c007ea5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('match',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('naverid', sa.Integer(), nullable=False),
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
