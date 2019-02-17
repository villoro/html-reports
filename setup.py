import io
from setuptools import setup

setup(
    name="html-reports",
    version="0.0.0.11",
    author="Arnau Villoro",
    author_email="arnau@villoro.com",
    packages=["html_reports"],
    include_package_data=True,
    license="MIT",
    description=("Module to create static html reports"),
    long_description=io.open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/villoro/html-reports",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Manufacturing",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
    ],
    package_data={"html_reports": ["resources/*"]},
    install_requires=["beautifulsoup4", "jinja2", "markdown", "easydev"],
)
