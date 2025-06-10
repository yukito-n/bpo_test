from sqlalchemy import Column, Integer, String, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base

class Staff(Base):
    __tablename__ = 'staff'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

class Schedule(Base):
    __tablename__ = 'schedules'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)

class Shift(Base):
    __tablename__ = 'shifts'

    id = Column(Integer, primary_key=True, index=True)
    staff_id = Column(Integer, ForeignKey('staff.id'))
    schedule_id = Column(Integer, ForeignKey('schedules.id'))
    start_time = Column(DateTime)
    end_time = Column(DateTime)

    staff = relationship('Staff', backref='shifts')
    schedule = relationship('Schedule', backref='shifts')

class WorkAnalytics(Base):
    __tablename__ = 'work_analytics'

    id = Column(Integer, primary_key=True, index=True)
    staff_id = Column(Integer, ForeignKey('staff.id'))
    date = Column(Date)
    punch_count = Column(Integer)

    staff = relationship('Staff', backref='work_analytics')
