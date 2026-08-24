# Open AI Portfolio

[![Portfolio CI](https://github.com/Goktug-Dusunen/open-ai-portfolio/actions/workflows/ci.yml/badge.svg)](https://github.com/Goktug-Dusunen/open-ai-portfolio/actions/workflows/ci.yml)
[![Hugging Face Sync](https://github.com/Goktug-Dusunen/open-ai-portfolio/actions/workflows/sync.yml/badge.svg)](https://github.com/Goktug-Dusunen/open-ai-portfolio/actions/workflows/sync.yml)
[![Live Portfolio](https://img.shields.io/badge/live-portfolio-8df7c5)](https://goktug-dusunen.github.io/open-ai-portfolio/)
[![License: MIT](https://img.shields.io/badge/license-MIT-7aa2ff.svg)](LICENSE)

An automatically maintained index of the public models, datasets, and interactive demos published by [Göktuğ Düşünen](https://huggingface.co/GoktugD) and [Werea](https://huggingface.co/Werea-co).

This repository makes the Hugging Face portfolio discoverable from GitHub while keeping Hugging Face as the source of truth for model weights, dataset files, licenses, and model cards.

**[Explore the live portfolio →](https://goktug-dusunen.github.io/open-ai-portfolio/)**

## What is included

- Turkish NLP, retrieval, speech, OCR, document AI, and security models
- Public datasets and evaluation resources
- Hugging Face Spaces and product demos
- A machine-readable [`data/portfolio.json`](data/portfolio.json) catalog
- A responsive, searchable [GitHub Pages portfolio](https://goktug-dusunen.github.io/open-ai-portfolio/)
- A dependency-free synchronization script and scheduled GitHub Action

<!-- portfolio:start -->

## Current snapshot

Last synchronized: `2026-08-24T13:38:45+00:00`

| Publisher | Models | Datasets | Spaces | Downloads |
|---|---:|---:|---:|---:|
| [GoktugD](https://huggingface.co/GoktugD) | 30 | 20 | 9 | 3,004 |
| [Werea-co](https://huggingface.co/Werea-co) | 17 | 4 | 5 | 1,182 |

## Most-used models

| Model | Task | Downloads | Likes |
|---|---|---:|---:|
| [GoktugD/DUSUNEN-Rota-270M-v1](https://huggingface.co/GoktugD/DUSUNEN-Rota-270M-v1) | sentence-similarity | 566 | 1 |
| [Werea-co/Werea-TR-TextRestore](https://huggingface.co/Werea-co/Werea-TR-TextRestore) | text-generation | 524 | 2 |
| [GoktugD/Werea-TR-TextRestore](https://huggingface.co/GoktugD/Werea-TR-TextRestore) | text-generation | 291 | 1 |
| [GoktugD/DUSUNEN-Oku-62M-v1](https://huggingface.co/GoktugD/DUSUNEN-Oku-62M-v1) | image-to-text | 73 | 1 |
| [GoktugD/DUSUNEN-Dinle-244M-v1](https://huggingface.co/GoktugD/DUSUNEN-Dinle-244M-v1) | automatic-speech-recognition | 49 | 0 |
| [GoktugD/DUSUNEN-Rota-270M-v2](https://huggingface.co/GoktugD/DUSUNEN-Rota-270M-v2) | sentence-similarity | 47 | 0 |
| [Werea-co/Werea-TSS](https://huggingface.co/Werea-co/Werea-TSS) | text-to-speech | 45 | 1 |
| [GoktugD/DUSUNEN-Atlas-278M-v1](https://huggingface.co/GoktugD/DUSUNEN-Atlas-278M-v1) | sentence-similarity | 42 | 3 |
| [GoktugD/DUSUNEN-Pusula-118M-v1](https://huggingface.co/GoktugD/DUSUNEN-Pusula-118M-v1) | sentence-similarity | 42 | 0 |
| [GoktugD/DUSUNEN-Pusula-118M-v0](https://huggingface.co/GoktugD/DUSUNEN-Pusula-118M-v0) | sentence-similarity | 38 | 0 |

<!-- portfolio:end -->

## Update locally

```bash
python scripts/sync_huggingface.py
```

The script uses only Python's standard library. The scheduled workflow checks for public Hugging Face updates every Monday and commits only when the catalog changes.

## Quality and maintenance

- `python -m unittest discover -s tests` runs the offline test suite.
- `python scripts/validate_portfolio.py` validates catalog structure and website data parity.
- [`CONTRIBUTING.md`](CONTRIBUTING.md) documents the contribution workflow.
- [`SECURITY.md`](SECURITY.md) explains responsible vulnerability reporting.

## License

The catalog code is available under the [MIT License](LICENSE). Models and datasets retain the licenses declared on their individual Hugging Face pages.
