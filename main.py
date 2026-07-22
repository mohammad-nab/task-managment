from fastapi import FastAPI
from fastapi import Depends
import models
from database import get_db
from sqlalchemy import select
from sqlalchemy.orm import Session

app = FastAPI()

@app.get("/task")
def get_task(db: Session = Depends(get_db)):
    result = db.scalars(select(models.Task)).all()
    return result