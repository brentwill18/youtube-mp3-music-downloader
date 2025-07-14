# Game Music Analyzer

A Python-based tool that analyzes game music tracks to classify their **mood**, **tempo**, and **instrumentation** using machine learning and deep learning models. The project leverages full game OSTs downloaded from KHInsider and employs audio feature extraction with `librosa`, along with PyTorch for model training.

---

## Project Overview

This project aims to explore the emotional and musical characteristics of game soundtracks. By analyzing audio features from full-length tracks, it classifies the mood (e.g., calm, intense), tempo (BPM), and instrumentation (e.g., orchestral, electronic) of game music.

---

## Features

- Download full game OSTs from KHInsider using a downloader script
- Extract detailed audio features using `librosa`
- Train machine learning and deep learning models to classify mood, tempo, and instrumentation
- Visualize music features and model predictions with `matplotlib` and `seaborn`
- Optional integration with Spotify API metadata for enhanced labeling and comparisons

---

## Requirements

- Python 3.8+
- Libraries:
  - `khinsider.py` (or manual downloads) for game OST acquisition
  - `librosa` for audio processing
  - `pydub` and `ffmpeg` for audio file handling
  - `PyTorch` for deep learning modeling
  - `scikit-learn` for traditional machine learning models
  - `numpy`, `pandas` for data manipulation
  - `matplotlib`, `seaborn` for visualization

---

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/brentwill18/vgm-analyzer.git
   cd "Game Music Analyzer"
