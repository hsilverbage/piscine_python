# ft_package

A minimal Python package created as part of a packaging exercise at 42.

This project demonstrates how to create, build, install, and use a simple Python package configured with `pyproject.toml`.

## About the project

The goal of this exercise is to learn how to:

* create a real Python package
* organize package files correctly
* declare project metadata in `pyproject.toml`
* build distributable files
* install the package with `pip`
* import and use the package from another script

## Features

This package currently provides one function:

### `count_in_list(lst, value)`

Returns the number of times `value` appears in the given list.

Example:

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))  # 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # 0
```

## Project structure

```text
.
├── ft_package/
│   ├── __init__.py
│   └── count_in_list.py
├── pyproject.toml
├── setup.py
├── README.md
└── LICENSE
```

## Build

First install the build module:

```bash
python3 -m pip install build
```

Then build the package from the root of the project:

```bash
python3 -m build
```

This command will generate a `dist/` directory containing:

```text
dist/
├── ft_package-0.0.1.tar.gz
└── ft_package-0.0.1-py3-none-any.whl
```

#### Usage

Install the package from the generated source archive:

```bash
python3 -m pip install ./dist/ft_package-0.0.1.tar.gz
```

Or install it from the wheel:

```bash
python3 -m pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

Once installed, you can use it in any Python script:

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))
print(count_in_list(["toto", "tata", "toto"], "tutu"))
```

Expected output:

```text
2
0
```

You can also verify that the package is correctly installed:

```bash
python3 -m pip show -v ft_package
```

Or list every installed package:

```bash
python3 -m pip list
```

##### Source

Documentation used while creating this package:

* https://packaging.python.org/en/latest/guides/writing-pyproject-toml/

## License

This project is distributed under the MIT License.
