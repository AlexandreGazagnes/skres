from setuptools import setup, find_packages

VERSION = "0.0.12"
DESCRIPTION = "My first Python package"
LONG_DESCRIPTION = "My first Python package with a slightly longer description"

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="skres",
    version=VERSION,
    author="Alex Gazagnes",
    author_email="<alex.gaz@email.com>",
    url="https://github.com/AlexandreGazagnes/skres",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    # packages=find_packages(),
    packages=["skres"],
    install_requires=["pandas"],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'
    keywords=["python", "first package"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
    ],
)
