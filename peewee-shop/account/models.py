from abstract.models import BaseModel
import peewee

class MyUser(BaseModel):
    username = peewee.CharField(max_length = 20, unique = True)
    password = peewee.CharField(max_length = 100)
    