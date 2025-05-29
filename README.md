# Marimo Reactive Notebook Prompt Library

## Instalation

- Install UV [UV Python Package and Project](https://docs.astral.sh/uv/getting-started/installation/)
- Install dependencies `uv sync`
- Install marimo `uv pip install marimo` if necessary

## Prompt Library

### Setup

- Add `.env` and set `PROMPT_LIBRARY_DIR` if you want to use directory different from `prompt_library` for storing your prompts.

### View the library

- `uv run marimo run prompt_library.py`

### Add new prompts

- Open project in the ide
- Open `prompt_library` directory and add/edit prompts here

### Edit the library (for updating the Notebook, not the prompts)

- `uv run marimo edit prompt_library.py`

## Marimo docs

> See the [Marimo Docs](https://docs.marimo.io/index.html) for general usage details
> Copied from https://github.com/disler/marimo-prompt-library