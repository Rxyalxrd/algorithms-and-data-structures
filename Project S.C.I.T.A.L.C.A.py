import sys


def reckoning(contenders: int, counting_beat: int) -> int:
    """
    Полёты на Марс с участием человека уже не за горами. Команда для полёта
    почти сформирована. Осталось одно свободное место и масса претендентов
    на него.
    Для решения этой задачи создан проект С.Ч.И.Т.А.Л.К.А. —
    Стандартный Числовой Иррационально-Точный АЛгоритм Кастинга Астронавтов.
    На практике алгоритм реализуется так:
    Группа претендентов выстраивается в круг. Число претендентов обозначим
    через N, претенденты получают номера от 1 до N.
    Претенденты получают лист бумаги, на котором написана считалка. Считалка
    состоит из определённого количества «ритмических частей», тактов.
    Число тактов обозначим через K.
    Претендент под номером 1 произносит вслух считалку и, начиная с себя,
    на каждый такт указывает на каждого из претендентов.
    Тот, на ком считалка закончилась, выбывает из числа претендентов.
    Участник, следующий за выбывшим, вновь начинает произносить считалку,
    начав с себя и указывая последовательно на оставшихся претендентов.
    Отсев продолжается до тех пор, пока не останется только один претендент —
    именно он и войдёт в команду.
    Посмотрим, как это сработает на примере считалки из 16 тактов для группы
    из 5 человек. Считалка разбита на такты символом |, а над каждым такто
    стоит цифра от 1 до 5: она обозначает, на кого именно показывает ведущий
    в процессе счёта.
    1          2          3      4
    Десять, | девять, | восемь, | семь
    5      1         2       3
    В кора|бле | нет места | всем
    4        5          1     2
    Тот, | кто плохо | кашу | ел
    3     4      5     1
    Нику|да | не поле|тел!

    # Претендент под номером 1 выбывает.
    # Считать начинает претендент, следующий за выбывшим, его
    номер - 2, он начинает с себя:

    2          3          4         5
    Десять, | девять, | восемь, | семь
    2       3       4         5
    В кора|бле | нет места | всем
    2        3          4      5
    Тот, | кто плохо | кашу | ел
    2     3     4      5
    Нику|да | не поле|тел!

    # Претендент под номером 5 выбывает.
    # Считать начинает претендент, следующий за выбывшим.
    # И так до последнего претендента.
    В считалке может быть от 1 до 500 ритмических шагов.

    Эни | бени | аппер | боттом
    Не | бывать | тебе | пилотом!
    В кастинге может принимать участие от 1 до 500 претендентов.
    """

    candidates = list(range(1, contenders + 1))
    index = 0

    while len(candidates) > 1:
        index = (index + counting_beat - 1) % len(candidates)
        candidates.pop(index)

    return candidates[0]


if __name__ == '__main__':
    test_case_contenders: int = int(sys.stdin.readline().rstrip())
    test_case_counting_beat: int = int(sys.stdin.readline().rstrip())
    print(reckoning(test_case_contenders, test_case_counting_beat))
