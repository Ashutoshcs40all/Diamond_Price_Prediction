from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requiremnts(file_path:str)->List[str]:
    requiremnts=[]
    with open(file_path) as file_obj:
        requiremnts=file_obj.readlines()
        requiremnts=[req.replace("\n", "") for req in requiremnts]

        if HYPEN_E_DOT in requiremnts:
           requiremnts.remove(HYPEN_E_DOT)


        return requiremnts
    
       

setup(
    name='DiamondPricePrediction',
    version= '0.0.01',
    author='Ashutosh',
    author_email='ashutoshmaurya063@gmail.com',
    install_requires=get_requiremnts('requiremnts.txt'),
    packages=find_packages()
    
)