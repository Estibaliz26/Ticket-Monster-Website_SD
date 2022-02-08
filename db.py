from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask import g, current_app

metadata = MetaData(
    naming_convention={
        "ix": 'ix_%(column_0_label)s',
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
    }
)
db = SQLAlchemy(metadata=metadata)

secret_key = "1q2s3f5g7jggujbffrhnbcdgh78jbhd"
# secret_key = current_app.secret_key
