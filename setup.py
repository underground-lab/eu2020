from setuptools import setup, find_namespace_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("VERSION", "r") as fh:
    version = fh.read()

with open("requirements.txt", "r") as fh:
    requirements = fh.readlines()

setup(
    name='eu2020',
    version=version,
    author='Jaroslav Beran',
    author_email='jaroslav.beran@gmail.com',
    description='Textová hra Evropská Unie 2020',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/berk76/eu2020',
    project_urls={
        "Bug Tracker": "https://github.com/berk76/eu2020/issues"
    },
    entry_points={
        'console_scripts': [
            'eu2020 = eu2020.app:main',
        ],
    },
    license='GPL-3.0',
    packages=find_namespace_packages(include=['eu2020', 'eu2020.*']),
    install_requires=requirements,
)
