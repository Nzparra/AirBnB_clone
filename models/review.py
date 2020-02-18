#!/usr/bin/python3
""" Review class of AirBnB clone project """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class """

    place_id = ""
    user_id = ""
    text = ""
