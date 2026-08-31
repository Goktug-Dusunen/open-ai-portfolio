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

Last synchronized: `2026-08-31T13:43:48+00:00`

| Publisher | Models | Datasets | Spaces | Downloads |
|---|---:|---:|---:|---:|
| [GoktugD](https://huggingface.co/GoktugD) | 30 | 20 | 9 | 4,198 |
| [Werea-co](https://huggingface.co/Werea-co) | 19 | 5 | 6 | 1,911 |

## Most-used models

| Model | Task | Downloads | Likes |
|---|---|---:|---:|
| [GoktugD/DUSUNEN-Rota-270M-v1](https://huggingface.co/GoktugD/DUSUNEN-Rota-270M-v1) | sentence-similarity | 804 | 1 |
| [Werea-co/Werea-TR-TextRestore](https://huggingface.co/Werea-co/Werea-TR-TextRestore) | text-generation | 555 | 2 |
| [GoktugD/Werea-TR-TextRestore](https://huggingface.co/GoktugD/Werea-TR-TextRestore) | text-generation | 313 | 1 |
| [GoktugD/NanoSOC-Gemstone-2B-GGUF](https://huggingface.co/GoktugD/NanoSOC-Gemstone-2B-GGUF) | text-generation | 113 | 0 |
| [GoktugD/NanoSOC-Gemstone-4B-GGUF](https://huggingface.co/GoktugD/NanoSOC-Gemstone-4B-GGUF) | text-generation | 93 | 0 |
| [GoktugD/DUSUNEN-Oku-62M-v1](https://huggingface.co/GoktugD/DUSUNEN-Oku-62M-v1) | image-to-text | 85 | 1 |
| [Werea-co/Werea-TSS](https://huggingface.co/Werea-co/Werea-TSS) | text-to-speech | 61 | 1 |
| [GoktugD/DUSUNEN-Dinle-244M-v1](https://huggingface.co/GoktugD/DUSUNEN-Dinle-244M-v1) | automatic-speech-recognition | 52 | 0 |
| [GoktugD/DUSUNEN-Rota-270M-v2](https://huggingface.co/GoktugD/DUSUNEN-Rota-270M-v2) | sentence-similarity | 51 | 0 |
| [GoktugD/DUSUNEN-Atlas-278M-v1](https://huggingface.co/GoktugD/DUSUNEN-Atlas-278M-v1) | sentence-similarity | 50 | 3 |

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
