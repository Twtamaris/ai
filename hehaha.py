import tensorflow as tf
from tensorflow.keras import models, layers
import matplotlib.pyplot as plt

# Specify the directory path
directory = "suduko"

# Create a list of image file paths
image_paths = tf.data.Dataset.list_files(directory + "/*")

# Function to preprocess each image
def preprocess_image(image_path):
    image = tf.io.read_file(image_path)
    image = tf.image.decode_image(image, channels=3)
    image = tf.image.resize_with_pad(image, target_height=500, target_width=500)
    image = image / 255.0  # Normalize pixel values to [0, 1]
    return image

# Preprocess the image dataset
dataset = image_paths.map(preprocess_image)

# Convert the dataset to an array
sudoku_array = tf.data.experimental.get_single_element(dataset.batch(len(image_paths)))

# Print the Sudoku array
print(sudoku_array)
