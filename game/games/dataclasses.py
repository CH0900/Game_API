from dataclasses import dataclass
from typing import Optional, List
from datetime import date




@dataclass
class NewGame:
    title: str
    description: str
    release_date: date
    genre: str

@dataclass
class UpdateGame:
    title: str
    description: str
    release_date: date
    genre: str

@dataclass
class NewGamePlayer:
    palyer_id: int

# @dataclass
# class UpdateProduct:
#     name: str
#     price: int
