"""link_user_medicine

Revision ID: e2397b1179d0
Revises: 9f3d5f903add
Create Date: 2021-10-05 23:38:37.842666

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "e2397b1179d0"
down_revision = "9f3d5f903add"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user_medicine",
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("medicine_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["medicine_id"],
            ["medicine.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
    )
    op.add_column("medicine", sa.Column("dosage", sa.JSON(), nullable=True))
    op.drop_column("medicine", "frequency")
    op.alter_column("user", "chat_id", existing_type=sa.INTEGER(), nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("user", "chat_id", existing_type=sa.INTEGER(), nullable=False)
    op.add_column(
        "medicine",
        sa.Column(
            "frequency",
            postgresql.JSON(astext_type=sa.Text()),
            autoincrement=False,
            nullable=True,
        ),
    )
    op.drop_column("medicine", "dosage")
    op.drop_table("user_medicine")
    # ### end Alembic commands ###
