"""empty message

Revision ID: 52349eeb2495
Revises: 20f248a74d5d
Create Date: 2022-09-19 18:10:45.172167

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52349eeb2495'
down_revision = '20f248a74d5d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('review', 'rating',
               existing_type=sa.VARCHAR(length=2),
               type_=sa.Integer(),
               existing_nullable=True,
               postgresql_using="rating::integer")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('review', 'rating',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(length=2),
               existing_nullable=True)
    # ### end Alembic commands ###
