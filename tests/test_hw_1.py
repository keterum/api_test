from pydantic.json_schema import model_json_schema

from api.questions_api import api
from http import HTTPStatus
from utils.assertions import Assert


def test_correct_register():
    email = 'eve.holt@reqres.in'
    password = 'Grogu'
    reg = api.correct_register(email, password)

    assert reg.status_code == HTTPStatus.OK

    # assert api.delete_user(res.json()['id']).status_code == HTTPStatus.NO_CONTENT