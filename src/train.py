import os
import tensorflow as tf
from model import build_cnn_model
from dataset import get_datasets

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
IMG_SIZE = (128, 128)
BATCH_SIZE = 32
EPOCHS = 10

train_ds, val_ds = get_datasets(DATA_DIR, IMG_SIZE, BATCH_SIZE)
class_names = train_ds.class_names
num_classes = len(class_names)

model = build_cnn_model(input_shape=IMG_SIZE + (3,), num_classes=num_classes)
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_ds, validation_data=val_ds, epochs=EPOCHS)

model.save(os.path.join(DATA_DIR, 'image_recognition_model.h5'))
print(f"Model saved to {os.path.join(DATA_DIR, 'image_recognition_model.h5')}")
