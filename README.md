Foo Bar Banana
==============
![example workflow](https://github.com/horken7/foo_bar_banana/actions/workflows/main.yml/badge.svg) ![Vercel Deploy](https://deploy-badge.vercel.app/vercel/foo-bar-banana)

This is an example project for a Python package with FastAPI web application. 

# Installation

To install foo-bar-banana, you can use pip:

```bash
pip install .
```

# Usage

The application is exposed as an entry point, after installing the package you can run it by:

```bash
run-foo-bar-banana
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

# Deploy
The app is automatically deployed to Vercel. Each push to master is deployed to production on foo-bar-banana.vercel.app. Each push to a branch is deployed to a feature environment.  

# Contributing
Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive commit messages.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository.