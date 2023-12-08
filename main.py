from typing import Union
import uvicorn
from datetime import datetime
from tortoise import fields
from tortoise.models import Model
from fastapi import FastAPI
from pydantic import BaseModel
from tortoise.contrib.fastapi import register_tortoise

api = FastAPI()

class Item(Model):
    id = fields.IntField(pk=True)
    plant_name = fields.CharField(50, null=False) # plant name
    temperature = fields.FloatField(null=False)
    air_humidity = fields.IntField() # w procentach
    dirt_humidity = fields.IntField()
    water_level = fields.IntField() # w procentach/litrach (tak myślę)

register_tortoise(
    api,
    db_url='sqlite://doniczka.sqlite3',
    modules={'models': ['main']},
    add_exception_handlers=True,
    generate_schemas=True
)


# if __name__ == "__name__":
#     uvicorn.run('main:api', host='127.0.0.1', reload=True)

