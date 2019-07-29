import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pysiconfi",
    version="0.0.1",
    author="Bruno Simoes",
    author_email="b.ssimoes@hotmail.com",
    description="Uma biblioteca para consumo da API do Siconfi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/stn-science/pysiconfi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)