from setuptools import setup
import os
from persistentdatatools.persistentdatatools import __version__

base_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(base_dir, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

packages = [
    'persistentdatatools'
]

tests_require = [
    'pytest',
]

setup(
    name='persistentdatatools',
    version=__version__,
    python_requires='~=3.3',
    description='This is a library used to manipulate, and save data quickly.',
    long_description=long_description,
    long_description_content_type='text/restructuredtext',
    keywords='persistence data manipulation save easy shortcuts',
    url='https://persistentdatatools.readthedocs.io',
    author='Benjamin P. Trachtenberg',
    author_email='e_ben_75-python@yahoo.com',
    license='MIT',
    packages=packages,
    include_package_data=True,
    test_suite='pytest',
    tests_require=tests_require,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
