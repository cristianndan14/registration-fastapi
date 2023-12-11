import http

from fastapi import APIRouter, Depends

from controller.context_manager import build_request_context
from models.base import GenericResponseModel
from models.patient import PatientInsertModel
from service.patient_service import PatientService
from utils.helper import build_api_response

patient_router = APIRouter(prefix="/v1/patient", tags=["patient"])


@patient_router.post("/add-new-patient", status_code=http.HTTPStatus.CREATED, response_model=GenericResponseModel)
async def new_patient(patient: PatientInsertModel, _=Depends(build_request_context)):
    """
    New patient
    :param _: build_request_context dependency injection handles the request context
    :param patient: patient details to add
    :return:
    """
    response: GenericResponseModel = PatientService.add_patient(patient=patient)
    return build_api_response(response)

