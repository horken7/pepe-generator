Pepe Generator
==============
![example workflow](https://github.com/horken7/pepe-generator/actions/workflows/main.yml/badge.svg)

This is an example project for a Python package with FastAPI web application.

This package provides a FastAPI application that serves Pepe the Frog memes from a [Kaggle dataset](https://www.kaggle.com/datasets/tornikeonoprishvili/pepe-memes-dataaset) (if Kaggle auth is provided, otherwise a [default image](https://upload.wikimedia.org/wikipedia/en/6/63/Feels_good_man.jpg).)

# Installation

To install Pepe Generator, you can use pip:

```bash
pip install .
```

# Usage
The app is expecting the following environment variables authenticate to Kaggle to get the dataset:

```
export KAGGLE_ENABLE=True
export KAGGLE_USERNAME=your_kaggle_username
export KAGGLE_KEY=your_kaggle_key
```

You can generate a token by following the instructions [here](https://www.kaggle.com/docs/api#Authentication:~:text=is%20%24PYTHON_HOME/Scripts.-,Authentication,the%20download%20of%20kaggle.json%2C%20a%20file%20containing%20your%20API%20credentials.,-If%20you%20are).

If you do not provide Kaggle authentication, a [default image](https://upload.wikimedia.org/wikipedia/en/6/63/Feels_good_man.jpg) will be used.

The application is exposed as an entry point, after installing the package you can run it by:

```bash
run-pepe-generator
```

This will start the application on http://localhost:8000. You can access the Swagger UI documentation at http://localhost:8000/docs.

# Testing

The tests run with tox, use the following commands:

```bash
pip install tox
tox
```

# Continuous Integration
This project uses GitHub Actions for Continuous Integration (CI). The CI pipeline is defined in the [.github/workflows/main.yml](.github/workflows/main.yml) file and is triggered on every push or pull request to the main branch. The pipeline runs tox to execute the tests and linting checks.

# Contributing
Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive commit messages.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository.