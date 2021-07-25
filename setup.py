import setuptools

DEPENDENCIES = []

setuptools.setup(
    name="agro-cli",
    version="0.0.1",
    description="Search for weather worldwide from command line",
    url="https://github.com/NamamiShanker/agro-cli",
    packages=setuptools.find_packages(),
    install_requires=DEPENDENCIES,
    entry_points={"console_scripts": ['agro=main:info']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)