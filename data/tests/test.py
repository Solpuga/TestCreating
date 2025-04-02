from .db_session import SqlAlchemyBase
from sqlalchemy import orm
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy_serializer import SerializerMixin
import datetime
import sqlalchemy


class Test(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'tests'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)

    title = sqlalchemy.Column(sqlalchemy.String)
    theme = sqlalchemy.Column(sqlalchemy.String)
    is_visible = sqlalchemy.Column(sqlalchemy.Bool, default=True)

    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                      default=datetime.datetime.now)
    modified_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                      default=datetime.datetime.now)

    creator = orm.relationship("User")
    asks = orm.relationship("Ask", back_populates='test')

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)



