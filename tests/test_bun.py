import pytest

import data
from praktikum.bun import Bun


class TestBun:
    @pytest.mark.parametrize(data.BunNameAndPrice.parameters, data.BunNameAndPrice.values)
    def test_get_bun_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize(data.BunNameAndPrice.parameters, data.BunNameAndPrice.values)
    def test_get_bun_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
