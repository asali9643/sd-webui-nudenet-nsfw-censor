from tensorflow.keras.models import load_model
from concurrent.futures import ThreadPoolExecutor
from PIL import Image, ImageFilter
import numpy as np

# モデルを読み込む
model = load_model('my_trained_model.h5')

def combine_results(input_image, input_mask, processed):
    canvas = input_image.copy()
    canvas.paste(processed, input_mask)
    return canvas

def variable_blur(input_image: Image, control_mask: Image, blur_radius: float = 10, blur_strength_curve: float = 3, *args, **kwargs):
    """
    Apply gaussian blur of varying strength to the image based on the value of the mask
    Args:
        input_image: PIL image to be filtered
        control_mask: PIL in L mode (8-bit pixels, grayscale)
        blur_radius: A float max blur radius
        blur_strength_curve: A float [0, 6]
            0 no blur (just return a copy of the input image with no change)
            3 linear blur strength (Default)
            4 linear blur radius
            6 Applies uniform blur_radius to the entire image, same as ImageFilter.GaussianBlur(blur_radius)
    Returns: filtered PIL image
    """
    # The rest of the code remains unchanged...

# Ensure the rest of your code remains below this line
