from setuptools import setup, find_namespace_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    requirements = fh.readlines()

setup(
    name='eu',
    version='0.0.1',
    author='Jaroslav Beran',
    author_email='jaroslav.beran@gmail.com',
    description='Textová hra Evropská Unie',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/berk76/eu',
    project_urls={
        "Bug Tracker": "https://github.com/berk76/eu/issues"
    },
    entry_points={
        'console_scripts': [
            'eu = eu.app:main',
        ],
    },
    license='GPL-3.0',
    packages=find_namespace_packages(include=['eu', 'eu.*']),
    install_requires=requirements,
)
