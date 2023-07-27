# Image to ASCII Art Converter

This script converts an image to ASCII art. The process involves two main steps:

1. **Apply Canny Edge Detection**: This step helps to extract useful structural information from the image 
   and reduce the amount of data to process. It works by detecting areas of the image where the 
   intensity changes sharply, which usually indicates the edge of an object within the image. 
   By focusing on the edges, we simplify the image and keep only the most important elements.

2. **Convert to ASCII**: Each pixel of the image is replaced with a corresponding ASCII character. 
   The brightness of the pixel is used to choose the ASCII character, with darker pixels 
   represented by characters like '@' and '%', and lighter pixels represented by characters like '.' and ' '.

## Purpose

The purpose of this conversion is to create a textual representation of an image that can be used 
in environments that only support text output. This is particularly useful when working with AI models 
like GPT-4, which primarily deal with text data.

## How to Use

1. Ensure you have Python installed on your system.

2. Install the required Python libraries:
   ```bash
   pip install opencv-python
   pip install opencv-python-headless
   pip install pillow
   ```
3. Clone this repository or download the ascii_converter.py script.

4. Run the script with the following command:

```bash
python ascii_converter.py <path_to_image> <desired_width>
Replace <path_to_image> with the path to the image you want to convert and <desired_width>
with the desired width of the ASCII output in characters.
```

5. The script will display the ASCII art output in the console.

Note: The Canny edge detection parameters (threshold values) have been set to 100 and 200, but they
may be adjusted depending on the specific image and edge detection requirements.

Feel free to experiment with different images and width settings to create unique ASCII art representations!

## Example
Here's an example of how to use the script:

```bash
python ascii_converter.py /path/to/image.jpg 80
This will convert the image to ASCII art with a width of 80 characters and display the result in the console.
```
