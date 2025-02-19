# How to build glimpse
### Generate distribution archives

```bash
## Install build
python3 -m pip install --upgrade build

## build project
python3 -m build
```

### Upload to PyPi
Create an account in https://test.pypi.org/account/register/ 

**upload package**
```bash
## install twine
python3 -m pip install --upgrade twine

## publish package
python3 -m twine upload --repository testpypi dist/*
```

### References
Oficial documentation, based to make the package
https://packaging.python.org/en/latest/tutorials/packaging-projects/#namespace-packages

Useful secondary reference
https://spike.sh/blog/how-to-create-a-pip-package-for-python/