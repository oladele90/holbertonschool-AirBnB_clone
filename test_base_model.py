#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
print (my_model.id)
print(my_model.created_at)
print(my_model.updated_at)
print(my_model.__dict__)
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model.__dict__)
