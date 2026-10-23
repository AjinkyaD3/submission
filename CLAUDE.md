# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is not a software project. It is a folder of BE IT (SCOE, Vadgaon) lab submissions for two courses. There is no build system, package manifest, test suite, linter, or git repo, and no README or Cursor/Copilot rules. Work here means editing or generating notebooks and write-ups against the lab manuals.

| Course | Manual | Submissions |
|---|---|---|
| Deep Learning (DL) | `Final_Deep Learning Lab Manual 26-27.pdf.pdf` (double `.pdf` extension is real) | Jupyter notebooks in `DL PRAC CODE/` |
| Information Storage and Retrieval (ISR) | `FINAL_ISR LAB MANUAL 2026_27.pdf` | `ISR 1.pdf` to `ISR 8.pdf` at the repo root |

The manuals define each assignment and its expected outcomes. Check the matching manual entry before changing a submission.

## Deep Learning (`DL PRAC CODE/`)

Each notebook is standalone and starts with a header cell holding the student name, roll number, class, and the practical's `Title` with lettered stages (a., b., c. ...). Keep that header and follow its stage structure when editing. 

| File | Topic | Stack |
|---|---|---|
| `DL practical 2 .ipynb` (note the space before `.ipynb`) | Feedforward NN on MNIST, SGD, loss/accuracy plots | TensorFlow/Keras |
| `DL Practical 3.ipynb` | CNN classifier on MNIST in 4 stages | Keras |
| `DL Practical 4.ipynb` | Autoencoder anomaly detection on credit-card fraud | Keras, pandas, sklearn, seaborn |
| `DL practical 5.ipynb` | CBOW word embeddings from scratch | NumPy only |
| `dl practical 6 cifar-ds.ipynb` | VGG16 transfer learning on CIFAR-10 images | Keras |

Practical 1 is not in the folder. Run notebooks with Jupyter or VS Code, executing cells top to bottom. Practical 2 has `pip install` cells (`keras`, `tensorflow`, `numpy==1.24`, `h5py`); the others assume these are installed.

### Data and environment

- Practical 4 reads `creditcard.csv` from the working directory. It is in `DL PRAC CODE/` (copy of the public TensorFlow mirror, `https://storage.googleapis.com/download.tensorflow.org/data/creditcard.csv`, same columns as Kaggle). It saves `autoencoder_fraud.h5`.
- Practicals 2, 3 and 6 download their data and weights (MNIST, CIFAR-10, ImageNet VGG16) via Keras, so nothing else is needed.
- Verified with TensorFlow 2.21 on Python 3.12. TensorFlow does not support the system Python 3.14, so use a separate 3.12 environment.

### Editing notes

- Outputs are stored inside the `.ipynb` files. Prefer NotebookEdit or JSON-aware edits over text replacement.
- The header cell (name, roll, class, title) is a markdown cell. Name, roll and class were replaced with the user's (Ajinkya Kishan Dhotre, 407I082, BEIT).
- Fixes already applied: Practical 2 duplicate `/255` removed; Practical 4 uses per-feature scaling and a 99th-percentile threshold from normal training data (recall about 0.84); Practical 6 loads CIFAR-10 and ImageNet weights through Keras instead of hardcoded local paths.
- Practical 5 trains on a tiny hardcoded paragraph and plots only the first sample's loss per epoch.

## Information Storage and Retrieval (`ISR n.pdf`)

`ISR OUTPUT PDF/ISR 1.pdf` to `ISR 8.pdf` are teacher-provided outputs relabeled for the user (BEIT, 407I082); `sam ise output pdf/` holds copies for Samruddhi Atul Bhandari (407I002). Extracted code is in `ISR code/` (assignments 5 and 6 are C++, the rest Python). Each has an "Assignment N / Code and Output" header followed by what appear to be screenshots. They have no extractable text, and there is no source code in the repo. They map to the manual's experiments:

1. Conflation algorithm for a document representative of a text file
2. Single-pass clustering of 4 to 5 files
3. Document retrieval using inverted files
4. Precision and recall for sample input
5. Harmonic mean (F-measure) and E-measure for the same example
6. Feature extraction from 2D colour images, with histogram plots
7. Web crawler pulling product info and links from an e-commerce site (Python)
8. Live weather report for a city (Python)

The manual also lists experiment 9 (a recommender-system case study), which has no `ISR 9.pdf` here. It also asks for at least one "lab innovation".

PDF tooling on this machine: `pdftotext` works from Bash, but the Read tool's PDF mode fails because `pdftoppm` (poppler) is not installed.
