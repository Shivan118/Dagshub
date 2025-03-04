from setuptools import setup,find_packages
from typing import List

HYPHAN_E_DOT = "-e ."

def get_requirements(filepath:str)->[str]:
    requirements = []

    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [i.replace("\n","") for i in requirements ]

        if HYPHAN_E_DOT in requirements:
            requirements.remove(HYPHAN_E_DOT)

    return requirements


setup(
    name="IPL_match_winning_probability_prediction",
    version="0.1",
    author="Shivan_kumar",
    author_email="demo@gmail.com",
    packages=find_packages(),
    install_required = get_requirements("requirements.txt")
)