from Car import (
    Car,
)


class Menu:
    """Класс для работы пользовательского меню."""

    def print_main_menu(self) -> None:
        """Вывод пунктов главного пользовательского меню."""

        print(
            '\n1: Печать информации об автомобиле.\n'
            '2: Изменить марку авто.\n'
            '3: Изменить модель авто.\n'
            '4: Изменить год выпуска авто.\n'
            '5: Изменить цвет авто.\n'
            '6: Получить информацию о марке авто.\n'
            '7: Получить информацию о модели авто.\n'
            '8: Получить информацию о годе выпуска авто.\n'
            '9: Получить информацию о цвете авто.\n'
            '10: Получить информацию о состоянии двигателя авто.\n'
            '11: Запустить двигатель.\n'
            '12: Остановить двигатель.\n'
            '0: ВЫХОД ИЗ ПРОГРАММЫ!\n'
        )

    def main_menu(self, choise: int, car: Car) -> bool:
        """Главное пользовательское меню.

        Args:
            choise: Выбор пользователя.

        Returns:
            is_running: Продолжается ли работа программы.

        """

        is_running = True

        match choise:
            case 0:
                is_running = False
            case 1:
                car.print_info()
            case 2:
                manufacturer = input('Введите марку авто: ')

                car.set_manufacturer(manufacturer)
            case 3:
                model = input('Введите модель авто: ')

                car.set_model(model)
            case 4:
                year = int(input('Введите год выпуска авто (не раньше 1885): '))

                car.set_year(year)
            case 5:
                color = input('Введите цвет авто: ')

                car.set_color(color)
            case 6:
                print(car.get_manufacturer())
            case 7:
                print(car.get_model())
            case 8:
                print(car.get_year())
            case 9:
                print(car.get_color())
            case 10:
                print(f'Состояние двигателя: {"Запущен" if car.is_engine_started() else "Остановлен"}')
            case 11:
                print(f'Двигатель: {"Запущен" if car.start_engine() else "Остановлен"}')
            case 12:
                print(f'Двигатель: {"Запущен" if car.stop_engine() else "Остановлен"}')

        return is_running

