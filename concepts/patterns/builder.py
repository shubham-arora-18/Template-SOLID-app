from typing import Self


class House:
    def __init__(self, builder_token):
        if builder_token != HouseBuilder._BUILDER_TOKEN_:
            raise Exception("Direct instantiation of the house not allowed, please use HouseBuilder class")
        self.country = None
        self.city = None


class HouseBuilder:
    _BUILDER_TOKEN_ = object()

    def __init__(self):
        self.house = House(HouseBuilder._BUILDER_TOKEN_)

    def set_country(self, country_name: str) -> Self:
        self.house.country = country_name
        return self

    def set_city(self, city_name: str) -> Self:
        self.house.city = city_name
        return self

    def build(self) -> House:
        return self.house


house = HouseBuilder().set_country("Inida").set_city("Haldwani").build()
