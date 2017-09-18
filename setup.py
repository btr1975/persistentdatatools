from setuptools import setup
from persistentdatatools.persistentdatatools import __version__

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
    keywords='persistence data manipulation save easy shortcuts',
    url='https://github.com/btr1975/persistentdatatools',
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