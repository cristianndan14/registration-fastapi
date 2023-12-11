from pydantic import BaseModel, EmailStr, HttpUrl
from models.base import DBBaseModel


class PatientResponseModel(BaseModel):
    """Patient model for response"""
    name: str
    email: EmailStr
    address: str
    phone_number: str
    photo_url: HttpUrl


class PatientInsertModel(PatientResponseModel):
    """Patient model for insert"""

    def create_db_entity(self):
        """
        Creates a db entity from the insert model
        """
        from data_adapter.patient import Patient
        dict_to_build_db_entity = self.dict()
        print(dict_to_build_db_entity, " print in PatientInsertModel")
        return Patient(**dict_to_build_db_entity)


class PatientModel(PatientResponseModel, DBBaseModel):
    """Patient model"""

    class Config:
        from_attributes = True

    def build_response_model(self) -> PatientResponseModel:
        return PatientResponseModel.parse_obj(self.dict())