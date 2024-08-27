# Домашнее задание по теме "Методы Юнит-тестирования"
# Цель: освоить методы, которые содержит класс TestCase.

from unittest import TestCase


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(TestCase):
    all_results = {} # для хранения результатов всех тестов создаем пустой словарь

    def setUp(self): # создаем три объекта класса Runner
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values(): # перебираем все значения словаря all_results
            result_str = ', '.join([f"{k}: {v}" for k, v in result.items()]) # преобразуем каждый результат в строку
            # используем метод join() для объединения всех строк в одну строку, разделенную запятыми
            print(f"{{{result_str}}}") # внешние двойные фигурные скобки {{ и }} для вывода фигурных скобок.

    def test_run_1(self):
        tour_1 = Tournament(90, self.runner_1, self.runner_3)
        result = tour_1.start() # запускаем турнир
        self.all_results['test_run_1'] = result
        self.assertTrue(result[max(result)] == "Ник") # запускаем тест и проверяем что Ник занял последнее место



    def test_run_2(self):
        tour_2 = Tournament(90, self.runner_2, self.runner_3)
        result = tour_2.start() # запускаем турнир
        self.all_results['test_run_2'] = result
        self.assertTrue(result[max(result)] == "Ник") # запускаем тест и проверяем что Ник занял последнее место


    def test_run_3(self):
        tour_3 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        result = tour_3.start() # запускаем турнир
        self.all_results['test_run_3'] = result
        self.assertTrue(result[max(result)] == "Ник") # запускаем тест и проверяем что Ник занял последнее место







