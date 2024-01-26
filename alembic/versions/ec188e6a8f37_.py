"""empty message

Revision ID: ec188e6a8f37
Revises: 55b19899db4a
Create Date: 2024-01-24 13:41:06.733870

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ec188e6a8f37'
down_revision: Union[str, None] = '55b19899db4a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_table('ET_CUSTOMER')


def downgrade() -> None:
    op.create_table('ET_CUSTOMER',
                    sa.Column('A_customerID', sa.Integer(), nullable=False),
                    sa.Column('A_firstName', sa.String(length=50)),
                    sa.Column('A_lastName', sa.String(length=50)),
                    sa.Column('A_age', sa.Integer()),
                    sa.Column('A_gender', sa.String(length=3)),
                    sa.Column('A_phoneNumber', sa.String(length=11)),
                    sa.PrimaryKeyConstraint('A_customerID')
                    )
