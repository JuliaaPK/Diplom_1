import pytest

import data
from praktikum.bun import Bun


class TestBun:
    @pytest.mark.parametrize("name", data.BunParameters.values_for_name)
    def test_get_bun_name(self, name):
        bun = Bun(name, data.BunParameters.static_price)
        assert bun.get_name() == name

    @pytest.mark.parametrize("price", data.BunParameters.values_for_price)
    def test_get_bun_price(self, price):
        bun = Bun(data.BunParameters.static_name, price)
        assert bun.get_price() == price
