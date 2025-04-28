# Image Recognition AI Project (TensorFlow)

This project provides a simple deep learning pipeline for image recognition using TensorFlow and Keras.

## Project Structure

- `data/` — Place your image datasets here (e.g., train, val, test folders)
- `src/`
  - `train.py` — Main script to train and evaluate the model
  - `model.py` — CNN model definition
  - `dataset.py` — Utilities for loading image data
- `requirements.txt` — Python dependencies

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Prepare your dataset under the `data/` directory. For example:

```
data/
  train/
    class1/
    class2/
  val/
    class1/
    class2/
```

3. Run training:

```bash
python src/train.py
```

## Customization
- Edit `src/model.py` to change the model architecture.
- Edit `src/dataset.py` for custom data loading or augmentation.

## Requirements
- Python 3.8+
- TensorFlow 2.x

---
