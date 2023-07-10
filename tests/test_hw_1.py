from pydantic.json_schema import model_json_schema

from api.questions_api import api
from http import HTTPStatus
from utils.assertions import Assert


def test_correct_register():
    email = 'eve.holt@reqres.in'
    password = 'Grogu'
    reg = api.correct_register(email, password)

    assert reg.status_code == HTTPStatus.OK


def test_incorrect_register():
    email = 'eve.holt@reqres.in'
    reg = api.incorrect_register(email)
    assert reg.json()
    assert reg.status_code == HTTPStatus.BAD_REQUEST
