# Example Package

This is a simple example package. 


## Usage
- add stuff in `example_pkg`. This is where the actual functions live. 
- in `__about__.py` change the version number if you want to deploy a new version
- open anaconda prompt, navigate to the folder where `setup.py` lives and run `python setup.py sdist bdist_wheel`
- Upload to PyPi using `python -m twine upload --repository testpypi dist/*`
- Use username and password to upload
- Install the package from anywhere using `pip install -i https://test.pypi.org/simple/ example-pkg-roblocks==0.0.2`. Change version number appropriately
- In any python script you can then use `from example_pkg.useful_functions import adding_up` and run `adding_up(2,3)`





## Authors
Jannic Cutura