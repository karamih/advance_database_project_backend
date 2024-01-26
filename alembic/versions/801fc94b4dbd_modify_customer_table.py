"""modify customer table

Revision ID: 801fc94b4dbd
Revises: fa6b0fe820bb
Create Date: 2024-01-24 13:03:44.831791

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '801fc94b4dbd'
down_revision: Union[str, None] = 'fa6b0fe820bb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('ET_CUSTOMER', 'A_customerID',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.Integer(),
               existing_nullable=False,
               autoincrement=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('ET_CUSTOMER', 'A_customerID',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(length=20),
               existing_nullable=False,
               autoincrement=True)
    # ### end Alembic commands ###
