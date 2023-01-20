'''Testing Person class'''

from pytest import raises
from scrape.wiki import Person

person = Person('mariusz', 'pudzianowski')


def test_person_init_value() -> None:
    with raises(TypeError):
        assert person.__init__(123, 'pudzianowski') == TypeError


def test_get_person_name() -> None:
    assert person.get_name() == 'Mariusz Pudzianowski'


def test_get_date_of_birth() -> None:
    assert person.get_date_of_birth() == '7 lutego 1977'


def test_get_image() -> None:
    assert person.get_image() == '''//upload.wikimedia.org/wikipedia/commons/thumb/0/00/Mariusz_Pudzianowski_5.JPG/221px-Mariusz_Pudzianowski_5.JPG'''
