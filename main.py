import argparse
from time import sleep


def get_color():
    parser = argparse.ArgumentParser(
        description='Программа выведет в консоль планету и раскрутит её'
    )
    parser.add_argument(
        'color',
        help='''Вы можете выбрать цвет планеты из предложенных:
        Чёрный, Красный, Зелёный, Жёлтый, Синий, Пурпурный, Голубой, Белый.
        По умолчанию задан зелёный''',
        nargs='?',
        default="Зелёный",
    )
    args = parser.parse_args()
    color = args.color
    return color.capitalize()


def main():
    delay_time = 1
    colors = {
        "Чёрный": "\u001b[30m",
        "Красный": "\u001b[31m",
        "Зелёный": "\u001b[32m",
        "Жёлтый": "\u001b[33m",
        "Синий": "\u001b[34m",
        "Пурпурный": "\u001b[35m",
        "Голубой": "\u001b[36m",
        "Белый": "\u001b[37m",
    }
    color = colors[get_color()]
    with open("planets.txt", "r", encoding="UTF-8") as file:
        content = file.read()
    images = content.split("Кадр")
    print(color)
    for planet in images:
        print(planet)
        sleep(delay_time)
        print('\033[2J', end="")
        print("\u001b[100A", end="")
    print("\u001b[0m \u001b[37;1m The End")


if __name__ == "__main__":
    main()
