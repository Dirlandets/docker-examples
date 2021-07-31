import sqlalchemy as sa
from database import Base

class Product(Base):
    __tablename__ = 'products'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, nullable=False)

    def __repr__(self):
        return f'<Item {self.name} {self.id}>'
