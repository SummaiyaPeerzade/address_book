from sqlalchemy import Column, Integer, String
from database import Base

#SQLAlchemy model
class AddBook(Base): #Import Base from database (the file database.py from above).Creating class that inherit from it.
    __tablename__ = "address_book" #name of the table

    # creating model attributes.These attributes represents a column in its corresponding database table.
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    address = Column(String)
    pincode = Column(Integer)
    city = Column(String)
    state = Column(String)
    country = Column(String)
