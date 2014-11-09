from setuptools import setup

with open('siggy/version.py','r') as f:
    exec(f.read())
    
setup(
    name='siggy',
    version=__version__,
    packages=['siggy'],
    url='https://github.com/wiggzz/siggy',
    license='MIT',
    author='Will James',
    author_email='jameswt@gmail.com',
    description='A little module for verifying bitcoin signatures',
    install_requires=[
        'pycoin'
    ]
)
