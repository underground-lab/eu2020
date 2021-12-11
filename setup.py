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
    author='Jaroslav Beran, Michal Porteš',
    author_email='jaroslav.beran@gmail.com, michalportes1@gmail.com',
    description='Textová hra Evropská Unie 2020',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/underground-lab/eu2020',
    project_urls={
        "Bug Tracker": "https://github.com/underground-lab/eu2020/issues"
    },
    entry_points={
        'console_scripts': [
            'eu2020 = eu2020.app:main',
        ],
    },
    license='GPL-3.0',
    packages=find_namespace_packages(include=['eu2020', 'eu2020.*']),
    install_requires=requirements,
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
