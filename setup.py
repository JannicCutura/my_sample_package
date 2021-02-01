import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

about ={}
with open("example_pkg/__about__.py") as f:
    exec(f.read(),about)

setuptools.setup(
    name="example-pkg-roblocks", # Replace with your own username
    version=about["__version__"],
    author=about["__author__"],
    author_email=about["__email__"],
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=about["__url__"],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)