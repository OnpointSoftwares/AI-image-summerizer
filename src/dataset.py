import tensorflow as tf
import os

def get_datasets(data_dir, img_size=(128, 128), batch_size=32):
    train_ds = tf.keras.utils.image_dataset_from_directory(
        os.path.join(data_dir, 'train'),
        image_size=img_size,
        batch_size=batch_size,
        shuffle=True
    )
    val_ds = tf.keras.utils.image_dataset_from_directory(
        os.path.join(data_dir, 'val'),
        image_size=img_size,
        batch_size=batch_size,
        shuffle=False
    )
    return train_ds, val_ds
