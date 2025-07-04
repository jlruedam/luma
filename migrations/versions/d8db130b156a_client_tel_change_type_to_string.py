"""Client - tel change type to String

Revision ID: d8db130b156a
Revises: 7c08c3c9254e
Create Date: 2025-06-24 09:33:50.350859

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8db130b156a'
down_revision = '7c08c3c9254e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('clients', schema=None) as batch_op:
        batch_op.alter_column('tel',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=200),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('clients', schema=None) as batch_op:
        batch_op.alter_column('tel',
               existing_type=sa.String(length=200),
               type_=sa.INTEGER(),
               existing_nullable=True)

    # ### end Alembic commands ###
