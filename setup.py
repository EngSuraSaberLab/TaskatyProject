from setuptools import find_packages, setup

setup(
    name='Taskaty',
    version='0.0.1',
    description='Simple CLI app to manage daily tasks',
    author='Sura Saber',
    packages=find_packages(),
    include_package_data=False,
    python_requires='>=3.9',
    install_requires=['tabulate'],
    entry_points={
        'console_scripts':[
            'taskaty=taskaty:main',
        ],
    },
)
