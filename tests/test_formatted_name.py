'''Testing utils functions'''

from pytest import raises
from utils.functions import formatted_name


def test_formatted_name_correct() -> None:
    assert formatted_name('mariusz', 'pudzianowski') == 'Mariusz_Pudzianowski'
    assert formatted_name('marIusZ', 'PuDziaNowsKi') == 'Mariusz_Pudzianowski'
    assert formatted_name('MARIUSZ', 'PUDZIANOWSKI') == 'Mariusz_Pudzianowski'


def test_formatted_name_incorrect() -> None:
    with raises(TypeError):
        assert formatted_name(123, 'pudzianowski') == TypeError
        assert formatted_name('mariusz', 321) == TypeError
