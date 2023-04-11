from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="rootdescent",
    version="0.1.0",
    author="Tshepo Moagi",
    author_email="tshepo.k.moagi@gmail.com",
    description="A package for approximating roots using various methods.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tshepomk/rootdescent",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    python_requires=">=3.6",
)
