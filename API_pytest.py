from API_yandex import YD, TokenYandexPoligon
import pytest
from parameterized import parameterized

fixture = [
    ("test1234", 201),
    ("test12345", 201),
    ("test123456", 201)
]


@pytest.mark.parametrize("path, result", fixture)
def test_disk_file_path(path, result):
    res = YD(TokenYandexPoligon)
    yd_result = res.disk_file_path(path)
    assert yd_result == result
