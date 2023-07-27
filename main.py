import cv2
import numpy as np

def get_canny(image_path):
    # Load the image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # Perform Canny edge detection
    edges = cv2.Canny(img, 100, 200)
    return edges

def image_to_ascii(image, width: int, height: int):
    # List of characters to represent various shades in ASCII
    ascii_chars = "@%#*+=-:. "

    # Resize the image
    image = cv2.resize(image, (width, height))

    # Normalize the pixel values to range 0-255
    image = cv2.normalize(image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

    # Scale down the pixel values to the range 0-9 (corresponding to the ascii characters)
    image = image // 28

    ascii_str = ""
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            ascii_str += ascii_chars[image[y, x]]
        ascii_str += "\n"
    
    return ascii_str

if __name__ == "__main__":
    image_path = "your_image_path_here"
    edges = get_canny(image_path)
    ascii_art = image_to_ascii(edges, 80, 30)
    print(ascii_art)
