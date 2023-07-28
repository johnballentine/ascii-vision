import os
import argparse
import cv2
import numpy as np
import requests
from io import BytesIO

def get_canny(image):
    # Invert brightness for higher contrast
    inverted_image = invert_brightness(image)

    # Perform Canny edge detection
    edges = cv2.Canny(inverted_image, 100, 200)

    return edges

def invert_brightness(image):
    # Invert the brightness of the image
    inverted_image = 255 - image
    return inverted_image

def image_to_ascii(image, width: int, height: int, from_canny: bool = False):
    # List of characters to represent various shades in ASCII
    ascii_chars = "@%#*+=-:. "

    # Resize the image
    image = cv2.resize(image, (width, height))

    # Normalize the pixel values to range 0-255
    image = cv2.normalize(image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

    # Invert the brightness for higher contrast if input is from Canny
    if from_canny:
        image = invert_brightness(image)

    # Scale down the pixel values to the range 0-9 (corresponding to the ascii characters)
    image = image // 28

    ascii_str = ""
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            ascii_str += ascii_chars[image[y, x]]
        ascii_str += "\n"
    
    return ascii_str

def convert_to_ascii(image_bytes, width=80, canny=True):
    # Load image if BytesIO object is provided
    if isinstance(image_bytes, BytesIO):
        image = cv2.imdecode(np.frombuffer(image_bytes.read(), np.uint8), cv2.IMREAD_GRAYSCALE)

        # Calculate height to maintain aspect ratio, divide by 2 for monospace font aspect ratio
        aspect_ratio = image.shape[0] / image.shape[1]
        height = int(width * aspect_ratio / 2)

        # Save the original image
        orig_filename = make_filename("output", "image_out-orig-", "png")
        cv2.imwrite(orig_filename, image)

        if canny:
            # Get Canny edges
            edges = get_canny(image)

            # Save the Canny edge detection output
            canny_filename = make_filename("output", "image_out-canny-", "png")
            cv2.imwrite(canny_filename, edges)

            # Use Canny edges for ASCII conversion
            image = edges

        # Convert to ASCII art
        ascii_art = image_to_ascii(image, width, height, from_canny=canny)

        # Save the ASCII art as a text file
        ascii_filename = make_filename("output", "image_out-ascii-", "txt")
        with open(ascii_filename, "w") as file:
            file.write(ascii_art)

        print(f"Conversion and saving completed.")

    return ascii_art


def url_to_ascii(image_url, width=80, canny=True):
    # Get BytesIO object of the image from the URL
    image_bytes = url_to_image(image_url)
    
    # Convert to ASCII art using convert_to_ascii with the canny argument
    ascii_art = convert_to_ascii(image_bytes, width=width, canny=canny)
    
    return ascii_art


def url_to_image(image_url):
    # Download the image from the URL and return as BytesIO
    response = requests.get(image_url)
    return BytesIO(response.content)

def save_bytesio_to_png(image_bytes, base_filename="image_out-"):
    # Get the folder path to save the image
    folder_path = os.getcwd()  # You can change this to the desired folder path

    # Generate a unique filename using the make_filename function
    filename = make_filename(folder_path, base_filename, "png")

    # Save the BytesIO image to the PNG file
    with open(filename, "wb") as file:
        file.write(image_bytes.getvalue())

    print(f"Image saved as {filename}")

import os

def make_filename(folder_path, base_filename, extension):
    # Create the 'output' directory if it doesn't exist
    output_folder = os.path.join(folder_path, "output")
    os.makedirs(output_folder, exist_ok=True)

    i = 1
    while True:
        filename = f"{base_filename}{str(i).zfill(5)}.{extension}"
        filepath = os.path.join(output_folder, filename)
        if not os.path.exists(filepath):
            return filepath
        i += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert an image to ASCII art.")
    parser.add_argument("--url", type=str, help="URL of the image to convert to ASCII art")
    parser.add_argument("--canny", action="store_true", help="Enable Canny edge detection")
    parser.add_argument("--width", type=int, default=80, help="Width of the ASCII art (default is 80 characters)")
    args = parser.parse_args()

    if args.url:
        ascii_art_url = url_to_ascii(args.url, width=args.width, canny=args.canny)  # Pass the width argument here
        print("Image URL to ASCII Art:")
        print(ascii_art_url)
    else:
        print("Please provide a valid URL using --url argument.")

