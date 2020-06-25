import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pepe_calc",
    version="0.0.6",
    author="Halil Bagdadi",
    author_email="halil.bagdadi@epitech.eu",
    description="This program is not a simple calculator, but a pepe calculator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your_github_page",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)