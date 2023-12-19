import sqlalchemy
from sqlalchemy import DateTime
from main.database_set import metadata

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("full_name", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("chat_id", sqlalchemy.BigInteger),
    sqlalchemy.Column("phone_number", sqlalchemy.String),
    sqlalchemy.Column('created_at', DateTime(timezone=True), nullable=True)
)




items = sqlalchemy.Table(
    "items",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("item_name", sqlalchemy.String),
    sqlalchemy.Column("item_photo", sqlalchemy.String),
    sqlalchemy.Column('chat_id', sqlalchemy.BigInteger)
)


