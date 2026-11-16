# Contributing to greet-community

## Set up for development

Activate a Python 3.11+ virtual environment, then install in editable mode:

```bash
python -m pip install -e .
```

## Run the tests

```bash
python -c "from greet_community import greet; print(greet('Hee'))"
```

Expected output: `Hello, Hee!`

## Send a change

1. Create a branch from `main`: `git switch -c <branch> main`, then commit.
2. Push the branch: `git push -u origin <branch>`.
3. Open a pull request from `<branch>` into `main` on GitHub.
