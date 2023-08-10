from models import Dog
from sqlalchemy import (Column,String,Integer,create_engine,)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
Base = declarative_base()
def create_table(base,engine):
    if __name__ == "__main__":
        create_engine("sqlite:///:memory:")
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        

def save(session, dog):
    session.add(dog)
    session.commit()

    pass

def get_all(session):
    x = session.query(Dog).all()
    return x
    pass

def find_by_name(session, name):
     y = session.query(Dog).filter(Dog.name.like(name)).all()
     for i in y: 
         return i

def find_by_id(session, id):
    z = session.query(Dog).filter(Dog.id.like(id)).all()
    for i in z:
        return i
    pass

def find_by_name_and_breed(session, name, breed):
    A = session.query(Dog).filter(Dog.name.like(name),Dog.breed.like(breed)).all()
    for i in A:
        return i 
    pass

def update_breed(session, dog, breed):
    session.query(Dog).update({Dog.breed: breed})
    session.commit()
    pass