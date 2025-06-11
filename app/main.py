from fastapi import FastAPI, Depends, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from typing import Optional

from .database import get_db
from . import models, crud
from .init_db import init_db

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")

# Initialize database on startup
@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request, db: Session = Depends(get_db)):
    staff = crud.get_all(db, models.Staff)
    schedules = crud.get_all(db, models.Schedule)
    return templates.TemplateResponse("dashboard.html", {"request": request, "staff": staff, "schedules": schedules})


# Staff Endpoints
@app.post("/staff")
def create_staff(name: str = Form(...), db: Session = Depends(get_db)):
    crud.create(db, models.Staff, {"name": name})
    return RedirectResponse(url="/", status_code=303)


# Shifts Endpoints (simplified)
@app.post("/shifts")
def create_shift(
    staff_id: int = Form(...),
    schedule_id: int = Form(...),
    start_time: str = Form(...),
    end_time: str = Form(...),
    db: Session = Depends(get_db),
):
    crud.create(
        db,
        models.Shift,
        {
            "staff_id": staff_id,
            "schedule_id": schedule_id,
            "start_time": start_time,
            "end_time": end_time,
        },
    )
    return RedirectResponse(url="/", status_code=303)


@app.get("/staff/{staff_id}", response_class=HTMLResponse)
def view_staff(
    staff_id: int, request: Request, db: Session = Depends(get_db)
):
    staff = crud.get(db, models.Staff, staff_id)
    shifts = db.query(models.Shift).filter(models.Shift.staff_id == staff_id).all()
    return templates.TemplateResponse(
        "staff_detail.html", {"request": request, "staff": staff, "shifts": shifts}
    )
