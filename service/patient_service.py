import http

from controller.context_manager import context_log_meta
from data_adapter.patient import Patient
from logger import logger
from models.base import GenericResponseModel
from models.patient import PatientInsertModel


class PatientService:
    MSG_PATIENT_CREATED_SUCCESS = "Patient created successfully"

    @staticmethod
    def add_patient(patient: PatientInsertModel) -> GenericResponseModel:
        """
        Add patient
        :param patient: patient details to add
        :return: GenericResponseModel
        """
        print(patient, " this is add patient 1")
        patient_to_create = patient.create_db_entity()
        print(patient_to_create, " this is add patient 2")
        patient_data = Patient.create_patient(patient_to_create)
        print(patient_data, " this is add patient 3")
        print(patient_data.build_response_model(), " this is a add patient 4")
        logger.info(extra=context_log_meta.get(),
                    msg="Patient created successfully with uuid {}".format(patient_to_create.uuid))
        return GenericResponseModel(status_code=http.HTTPStatus.CREATED, message=PatientService.MSG_PATIENT_CREATED_SUCCESS,
                                    data=patient_data.build_response_model())