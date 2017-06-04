from setuptools import setup, find_packages

setup(
    name='latviski',
    version='0.0.1',
    description='A tool to learn latviski',
    url='https://github.com/rbcasperson/src',
    author='Ryan Casperson',
    author_email='casperson.ryan@gmail.com',
    classifiers=[
        'Intended Audience :: Language Learners',
        'Topic :: Utilities',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6'
    ],
    keywords='cli',
    install_requires=['docopt'],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'lv=src.cli:main',
        ],
    }
)
