from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

#app variable will be an object of the class FastAPI.This will be the main point of interaction.
app = FastAPI()

#creating tables stored in metadata
models.Base.metadata.create_all(bind=engine)

#Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

#declaring data model(AddBook) as a class that inherits from BaseModel.
class AddBook(BaseModel):
    name: str = Field(min_length=1)
    address: str = Field(min_length=1, max_length=100)
    pincode: int = Field(gt=-1, lt=1000000)
    city: str = Field(min_length=1, max_length=100)
    state: str = Field(min_length=1, max_length=100)
    country: str = Field(min_length=1, max_length=100)



@app.get("/")
#reading a data
def read_api(db: Session = Depends(get_db)):
    return db.query(models.AddBook).all()

@app.get("/{address_book_id}")
#Search API
def search_address_book(address_book_id: int, db: Session = Depends(get_db)):
    add_book_model = db.query(models.AddBook).filter(models.AddBook.id == address_book_id).first()
    return add_book_model


#creating data
@app.post("/")
def create_address_book(addbook: AddBook, db: Session = Depends(get_db)):

    #Creating a SQLAlchemy model instance with data.
    add_book_model = models.AddBook()
    add_book_model.name = addbook.name
    add_book_model.address = addbook.address
    add_book_model.pincode = addbook.pincode
    add_book_model.city = addbook.city
    add_book_model.state = addbook.state
    add_book_model.country = addbook.country

    db.add(add_book_model) #add that instance object to database session.
    db.commit() #commit the changes to the database (so that they are saved).

    return addbook #return the data


@app.put("/{address_book_id}")

#Updating data
def update_address_book(address_book_id: int, addbook: AddBook, db: Session = Depends(get_db)):

    add_book_model = db.query(models.AddBook).filter(models.AddBook.id == address_book_id).first()

    if add_book_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID {address_book_id} : Does not exist"
        )

    add_book_model.name = addbook.name
    add_book_model.address = addbook.address
    add_book_model.pincode = addbook.pincode
    add_book_model.city = addbook.city
    add_book_model.state = addbook.state
    add_book_model.country = addbook.country

    db.add(add_book_model)
    db.commit()

    return addbook


@app.delete("/{address_book_id}")
#deleting data
def delete_address_book(address_book_id: int, db: Session = Depends(get_db)):

    add_book_model = db.query(models.AddBook).filter(models.AddBook.id == address_book_id).first()

    if add_book_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID {address_book_id} : Does not exist"
        )

    db.query(models.AddBook).filter(models.AddBook.id == address_book_id).delete()

    db.commit()
