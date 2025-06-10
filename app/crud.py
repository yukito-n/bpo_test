from sqlalchemy.orm import Session
from . import models

# Generic CRUD helpers

def get_all(db: Session, model):
    return db.query(model).all()


def get(db: Session, model, item_id: int):
    return db.query(model).filter(model.id == item_id).first()


def create(db: Session, model, obj_in: dict):
    obj = model(**obj_in)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def update(db: Session, obj, obj_in: dict):
    for field, value in obj_in.items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


def delete(db: Session, obj):
    db.delete(obj)
    db.commit()
