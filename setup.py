from setuptools import setup, find_packages

setup(
    name="rootdescent",
    version="0.0.2",
    author="Tshepo Moagi",
    author_email="youremail@example.com",
    description="A numerical analysis package for solving roots using bisection, secant, and Newton-Raphson methods.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/TshepoMK/rootdescent",
    project_urls={
        "PyPI": "https://pypi.org/project/rootdescent/",
        "Source": "https://github.com/TshepoMK/rootdescent",
    },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    python_requires='>=3.6',
)
