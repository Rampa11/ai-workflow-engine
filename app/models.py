from sqlalchemy import Column, Integer, String
from app.database import Base

class Workflow(Base):
    __tablename__ = "workflows"

    id = Column(Integer, primary_key=True, index=True)
    trigger = Column(String)
    condition = Column(String)
    actions = Column(String)  # store as comma-separated