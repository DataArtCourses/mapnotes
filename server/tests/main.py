from unittest import TestLoader, TextTestRunner
from os import path


def main():
    suite = TestLoader().discover(start_dir=path.join(path.dirname(__file__), 'test_cases'))
    runner = TextTestRunner(verbosity=2)
    runner.run(suite)


if __name__ == '__main__':
    main()
