from setuptools import setup

setup(
    name='experts',
    version='0.1.0',
    py_modules=['experts'],
    install_requires=['Click', ],
    entry_points={
        'console_scripts': ['experts = experts:main', ]
    }
)
