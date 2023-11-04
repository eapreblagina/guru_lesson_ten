import dataclasses
from datetime import datetime, date


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile_number: str
    date_of_birth: datetime.date
    subjects: str
    hobbies: str
    picture: str
    address: str
    state: str
    city: str


student = User('Kate', 'Preblagina', 'Katitoporova@bk.ru', "Female", '1234567890', date(2000, 8, 10),
               'Economics', 'Sports', 'foto.jpg', 'Пушкина 15', 'Haryana', 'Karnal')
