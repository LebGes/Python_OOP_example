from Car import (
    Car,
)
from Menu import (
    Menu,
)


menu = Menu()
car_1 = Car()
car_2 = Car("BMW", "M5", "Marine blue", 2022)


def run() -> None:
    """Метод запуска работы."""

    is_running = True

    while (is_running):
        menu.print_main_menu()

        choise = int(input('Введите выбор: '))
        choise_car = int(input('Введите порядковый номер авто: '))
        car = car_1 if choise_car == 1 else car_2

        is_running = menu.main_menu(choise, car)


run()