class Car:
    """Класс для описания авто."""

    __year_of_manufacturing_first_vehicle = 1885
    __engine_status = False

    def __init__(self, manufacturer: str="NA", model: str="NA", color: str="NA", year: int=None) -> None:
        """Инициализация/конструктор класса.

        Args:
            manufacturer: Марка авто.
            model: Модель авто.
            color: Цвет авто.
            year: Год производства.
        """

        self.__manufacturer = manufacturer
        self.__model = model
        self.__color = color
        self.__year = year

    def set_manufacturer(self, manufacturer: str) -> None:
        """Сеттер для марки авто.

        Args:
            manufacturer: Марка авто.
        """

        self.__manufacturer = manufacturer

    def get_manufacturer(self) -> str:
        """Геттер для марки авто.

        Returns:
            manufacturer: Марка авто
        """

        return self.__manufacturer

    def set_model(self, model: str) -> None:
        """Сеттер для модели авто.

        Args:
            model: Модель авто.
        """

        self.__model = model

    def get_model(self) -> str:
        """Геттер для модели авто.

        Returns:
            model: Модель авто.
        """

        return self.__model

    def set_color(self, color: str) -> None:
        """Сеттер для цвета авто.

        Args:
            color: Цвет авто.
        """

        self.__color = color

    def get_color(self) -> str:
        """Геттер для цвета авто.

        Returns:
            color: Цвет авто.
        """

        return self.__color

    def set_year(self, year: int) -> None:
        """Сеттер для года выпуска авто.

        Args:
            year: Год выпуска авто.
        """

        while(year < self.__year_of_manufacturing_first_vehicle):
            year = int(input('Введите корректный год производства авто (не раньше 1885): '))

        self.__year = year

    def get_year(self) -> int:
        """Геттер для года выпуска авто.

        Returns:
            year: Год выпуска авто.
        """

        return self.__year

    def print_info(self) ->None:
        """Вывод информации об авто."""

        print(
            f'\nМарка автомобиля: {self.get_manufacturer()}\n'
            f'Модель автомобиля: {self.get_model()}\n'
            f'Цвет автомобиля: {self.get_color()}\n'
            f'Год производства: {self.get_year()}\n'
            f'Состояние двигателя: {"Запущен" if self.is_engine_started() else "Остановлен"}\n'
        )

    def is_engine_started(self) -> bool:
        """Геттер для состояния двигателя авто.

        Returns:
            __engine_status: Состояние двигателя авто.
        """

        return self.__engine_status


    def start_engine(self) -> bool:
        """Метод для запуска двигателя автомобиля.

        Returns:
            __engine_status: Состояние двигателя авто.
        """

        if self.__engine_status is False:
            self.__engine_status = True

        return self.__engine_status

    def stop_engine(self) -> bool:
        """Метод для остановки двигателя автомобиля.

        Returns:
            __engine_status: Состояние двигателя авто.
        """

        if self.__engine_status is True:
            self.__engine_status = False

        return self.__engine_status


