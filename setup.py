from setuptools import setup
import unittest


def test_suite():
    test_loader = unittest.TestLoader()
    return test_loader.discover("tests", pattern="test_*.py")


setup(
    name='gol',
    version='1.0',
    packages=['gol'],
    url='https://github.com/menacingChicken/game_of_life.git',
    license='MIT',
    author='Chris Evans',
    author_email='christopher.evans@gmail.com',
    description='Simple Conway Game of Life simulator',
    test_suite="setup.test_suite"
)
