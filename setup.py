from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="CHATBOT PRODUCT RECOMMENDER",
    version="0.1",
    author="nandaryanpk",
    packages=find_packages(),
    install_requires = requirements,
)