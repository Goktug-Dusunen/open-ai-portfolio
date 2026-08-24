# Contributing

Thanks for helping improve the open AI portfolio.

## Development workflow

1. Create a focused branch from `main`.
2. Make the smallest change that solves the problem.
3. Run the offline checks:

   ```bash
   python -m compileall -q scripts tests
   python -m unittest discover -s tests -v
   python scripts/validate_portfolio.py
   ```

4. Open a pull request describing the behavior change and verification performed.

## Catalog updates

Do not edit generated catalog rows manually. Run `python scripts/sync_huggingface.py`; Hugging Face remains the source of truth for public artifacts and metadata.

## Scope

Contributions should improve catalog accuracy, accessibility, maintainability, or presentation. Model and dataset issues belong in the relevant Hugging Face repository.
