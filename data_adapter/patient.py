from sqlalchemy import Column, String

from sqlalchemy.orm import Session
from data_adapter.db import DBBase, ModelDBBase
from models.patient import PatientModel


class Patient(DBBase, ModelDBBase):
    __tablename__ = 'patient'

    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    address = Column(String(200), nullable=False)
    phone_number = Column(String(20), nullable=False)
    photo_url = Column(String(200), nullable=False)

    def __to_model(self) -> PatientModel:
        """converts db orm object ot pydantic model"""
        return PatientModel.from_orm(self)
    
    @classmethod
    def create_patient(cls, patient) -> PatientModel:
        from controller.context_manager import get_db_session
        db: Session = get_db_session()
        db.add(patient)
        db.flush()
        return patient.__to_model()
    
    