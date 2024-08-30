import unittest
import logging
from runner import Runner  # Импортируем класс Runner из runner.py

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(levelname)s: %(message)s'
)

class RunnerTest(unittest.TestCase):
    is_frozen = False  # Атрибут для управления заморозкой тестов

    def skip_if_frozen(func):
        def wrapper(self, *args, **kwargs):
            if self.is_frozen:
                self.skipTest('Тесты в этом кейсе заморожены')
            return func(self, *args, **kwargs)
        return wrapper

    @skip_if_frozen
    def test_walk(self):
        try:
            runner = Runner("Test Runner", speed=-5)  # Проверяем отрицательную скорость
            runner.walk()  # Этот вызов не должен дойти до этого места
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            # Если возникает исключение, логируем его
            logging.warning("Неверная скорость для Runner")

    @skip_if_frozen
    def test_run(self):
        try:
            runner = Runner(name=123)  # Проверяем неверный тип для имени
            runner.run()  # Этот вызов не должен дойти до этого места
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            # Если возникает исключение, логируем его
            logging.warning("Неверный тип данных для объекта Runner")

    @skip_if_frozen
    def test_challenge(self):
        runner1 = Runner("Runner 1")
        runner2 = Runner("Runner 2")

        for _ in range(10):
            runner1.run()
            runner2.walk()

        self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == '__main__':
    unittest.main()