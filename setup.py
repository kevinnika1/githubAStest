from setuptools import setup, find_packages

# imports __version__ variable
import os
with open(os.path.join('PROJECTNAME', 'VERSION')) as f: 
    __version__ = f.readline().strip()

setup(name='PROJECTNAME',
    version=__version__,
    description='PROJECTNAME in setup.py',
    url='',
    author='AUTHORNAME in setup.py',
    author_email='AUTHORNAME@ba.com',
    license='',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.15.1',
        'scipy>=1.1.0',
        'matplotlib>=2.2.3',
        'seaborn>=0.9.0',
        'pyCompare>=1.0.0',
        'cadspy>=1.4.0'
    ],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Visualization",
        ],
    long_description = """
            PROJECTNAME Project outline.
        """,
    documentation='',
    include_package_data=True,
    zip_safe=True
    )
