"""Add new columns to Financial Statement model

Revision ID: 44f007f060bb
Revises: e4a2626a7b4d
Create Date: 2020-05-03 15:55:45.711137

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44f007f060bb'
down_revision = 'e4a2626a7b4d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_item_description', table_name='item')
    op.drop_index('ix_item_id', table_name='item')
    op.drop_index('ix_item_title', table_name='item')
    op.drop_table('item')
    op.add_column('financial_statement', sa.Column('amortization', sa.BigInteger(), nullable=True))
    op.add_column('financial_statement', sa.Column('cash_and_equivalents', sa.BigInteger(), nullable=True))
    op.add_column('financial_statement', sa.Column('cost_of_revenue', sa.BigInteger(), nullable=True))
    op.add_column('financial_statement', sa.Column('costs_of_goods_sold', sa.BigInteger(), nullable=True))
    op.add_column('financial_statement', sa.Column('depreciation', sa.BigInteger(), nullable=True))
    op.add_column('financial_statement', sa.Column('earnings_per_share', sa.Float(), nullable=True))
    op.add_column('financial_statement', sa.Column('interest_expense', sa.BigInteger(), nullable=True))
    op.add_column('financial_statement', sa.Column('long_term_debt', sa.BigInteger(), nullable=True))
    op.add_column('financial_statement', sa.Column('short_term_debt', sa.BigInteger(), nullable=True))
    op.add_column('financial_statement', sa.Column('tax_expense', sa.BigInteger(), nullable=True))
    op.add_column('financial_statement', sa.Column('total_debt', sa.BigInteger(), nullable=True))
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('user', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_column('financial_statement', 'total_debt')
    op.drop_column('financial_statement', 'tax_expense')
    op.drop_column('financial_statement', 'short_term_debt')
    op.drop_column('financial_statement', 'long_term_debt')
    op.drop_column('financial_statement', 'interest_expense')
    op.drop_column('financial_statement', 'earnings_per_share')
    op.drop_column('financial_statement', 'depreciation')
    op.drop_column('financial_statement', 'costs_of_goods_sold')
    op.drop_column('financial_statement', 'cost_of_revenue')
    op.drop_column('financial_statement', 'cash_and_equivalents')
    op.drop_column('financial_statement', 'amortization')
    op.create_table('item',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('owner_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], name='item_owner_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='item_pkey')
    )
    op.create_index('ix_item_title', 'item', ['title'], unique=False)
    op.create_index('ix_item_id', 'item', ['id'], unique=False)
    op.create_index('ix_item_description', 'item', ['description'], unique=False)
    # ### end Alembic commands ###
