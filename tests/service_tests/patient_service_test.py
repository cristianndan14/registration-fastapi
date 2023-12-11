import unittest
import uuid
from unittest.mock import patch, MagicMock

import http

from models.patient import PatientInsertModel, PatientModel
from service.patient_service import PatientService


class TestPatientService(unittest.TestCase):
    def setUp(self):
        self.patient_insert_data = PatientInsertModel(
            name="John",
            email="johndoe@example.com",
            address="Cespedes 1234 dpto 4F",
            phone_number="1134490012",
            photo_url="www.unplash.com/123"
        )
        self.patient = PatientModel(
            id=1,
            uuid=uuid.uuid4(),
            created_at="2023-04-09T14:53:10.285Z",
            is_deleted=False,
            name="John",
            email="johndoe@example.com",
            address="Cespedes 1234 dpto 4F",
            phone_number="1134490012",
            photo_url="www.unplash.com/123"
        )

    @patch("data_adapter.patient.Patient.create_patient")
    def test_add_new_patient_success(self, mock_create_patient: MagicMock):
        mock_create_patient.return_value = self.patient
        response = PatientService.add_patient(self.patient_insert_data)
        self.assertEqual(response.status_code, http.HTTPStatus.CREATED)
        self.assertEqual(response.message, PatientService.MSG_PATIENT_CREATED_SUCCESS)
        self.assertEqual(response.data, self.patient.build_response_model())