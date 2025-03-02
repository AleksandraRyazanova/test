from typing import Union

class Iphone:
    def __init__(self, Model: Union[int], Memory: Union[int]):
        """
        Создание и подготовка к работе объекта "Iphone"
        :param Model: Модель айфона
        :param Memory: Объем памяти
        Примеры:
        >>> phone = Iphone(10, 256)  # инициализация экземпляра класса
        """
        if not isinstance(Model, (int)):
            raise TypeError("Модель айфона должна быть типа int")
        if not Model in [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]:
            raise ValueError("В линейке айфонов такая модель отсутствует")
        self.Model = Model

        if not isinstance(Memory, (int)):
            raise TypeError("Размер памяти должен быть типа int")
        if not Memory in [8, 16, 32, 64, 128, 256, 512, 1024]:
            raise ValueError("Айфона такого объема памяти не существует")
        self.Memory = Memory

    def is_model_popular(self) -> bool:
        """
        Функция, которая проверяет является ли айфон такой модели и памяти популярным у покупателей
        :return: Является ли модель и объем памяти популярным
        Примеры:
        >>> phone = Iphone(15, 512)
        >>> phone.is_model_popular()
        """

    def increase_memory(self, increase: int) -> None:
        """
        Покупка дополнительного объема памяти в облачном хранилище.
        :param increase: Добавляемая память
        :raise ValueError: Если добавляемая память меньше 0, это ошибка
        Примеры:
        >>> phone = Iphone(15, 128)
        >>> phone.increase_memory(100)
        """
        ...

        if not isinstance(increase, (int)):
            raise TypeError("Добавляемая память должна быть типа int")
        if increase < 0:
            raise ValueError("Добавляемая память должна быть положительным числом")


class Store:
    def __init__(self, Clothing_size: Union[str], Shoes_size: Union[int]):
        """
        Создание и подготовка к работе объекта "Магазин"
        :param Clothing_size: Размер рдежды
        :param Shoes_size: Размер обуви
        Примеры:
        >>> store = Store("L", 39)  # инициализация экземпляра класса
        """
        if not isinstance(Clothing_size, (str)):
            raise TypeError("Размер одежды должен быть типа str")
        if not Clothing_size in ["XXXS", "XXS", "XS", "X", "M", "L", "XL", "XXL", "XXXL"]:
            raise ValueError("Такого размера одежды нет в наличии")
        self.Clothing_size = Clothing_size

        if not isinstance(Shoes_size, (int)):
            raise TypeError("Размер обуви должен быть типа int")
        if not Shoes_size in [ 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]:
            raise ValueError("Такого размера обуви нет в наличии")
        self.Shoes_size = Shoes_size

    def is_size_popular(self) -> bool:
        """
        Функция, которая проверяет часто ли покупают обувь конкретного размера под определенный размер одежды
        :return: является ли сочетание популярным
        Примеры:
        >>> store = Store("XS", 38)
        >>> store.is_size_popular()
        """

    def height(self) -> float:
        """
        Функция, которая вычисляет рост человека по заданным параметрам
        :return: Рост человека
        Примеры:
        >>> store = Store("XL", 42)
        >>> store.height()
        """


hous = [                                      #Инициализация массива для работы с классом Apartments
            {'rooms': 1, 'area': [33.5, 38, 38.5, 46.2, 51]},
            {'rooms': 2, 'area': [50, 64.8, 51, 65, 65.7, 70]},
            {'rooms': 3, 'area': [68, 73, 89]},
            {'rooms': 4, 'area': [100, 120.8]},
            {'rooms': 5, 'area': [140, 130.5, 150, 150.6, 151.7]},
            {'rooms': 6, 'area': [180, 195, 200]},
        ]

class Apartments:
    def __init__(self, Number_of_rooms: Union[int], Area: Union[int, float]):

        """
        Создание и подготовка к работе объекта "Многоквартирный дом"
        Создание списка параметров
        :param Number_of_rooms: Колличество комнат в квартире
        :param Area: Площадь квартиры
        Примеры:
        >>> apartments = Apartments(5, 150.5)  # инициализация экземпляра класса
        """

        if not isinstance(Number_of_rooms, (int)):
            raise TypeError("Колличество комнат должно быть типа int")
        for result, dict in enumerate(hous):
            if dict.get('rooms', '') == Number_of_rooms:
                break;
        else:
            result = None
        if result == None:
            raise ValueError("Квартир с таким колличеством комнат нет")

        if not isinstance(Area, (int, float)):
            raise TypeError("Площадь должна быть типа int или float")
        if not Area in dict.get('area') and not result == None:
            raise ValueError("Такая площадь не предусмотрена для данной квартиры")

    def apartment_availability(self) -> bool:
        """
        Функция, которая проверяет наличие квартиры с конкретной площадью в доме
        :return: Наличие квартиры
        Примеры:
        >>> apartments = Apartments(1, 38)
        >>> apartments.apartment_availability()
        """

    def room_size(self) -> float:
        """
        Функция, которая считает площадь комнат
        :return: площадь комнат
        Примеры:
        >>> apartments = Apartments(1, 38)
        >>> apartments.room_size()
        """


if __name__ == "__main__":
    import doctest
    doctest.testmod() # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass