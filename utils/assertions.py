from jsonschema import validate
from pydantic import BaseModel

class Assert:
    @staticmethod
    def validate_schema(instance: dict) -> None:
        validate(instance=instance, schema=BaseModel.schema())
        # validate(instance=instance, schema=BaseModel.model_json_schema())
        # validate(instance=instance, schema=BaseModel.schema())
        #model_json_schema
        # cls.check_schema(schema)
        #hello



