# Image to ASCII Art Converter for Text-Only Language Models

This tool converts an image, accessed via a URL, into ASCII art. It's specifically designed to enable language models to interpret image data by transposing it into a textual format. 

## Overview

Our conversion process includes:

1. **Canny Edge Detection**: We leverage this computer vision algorithm to extract critical structural information from images. This technique focuses on areas with significant changes in pixel intensity (edges), distilling the image into its essential elements.

2. **Pixel-to-ASCII Conversion**: Each pixel from the processed image gets mapped to a corresponding ASCII character. The conversion hinges on pixel brightness, with denser ASCII characters (e.g., '@', '%') representing darker pixels and sparser characters (e.g., '.', ' ') denoting lighter ones.

By generating ASCII art, we enable environments primarily supporting text output to "visualize" images. This makes the tool particularly beneficial for text-based AI models like GPT-4.

## Usage

1. Make sure Python is set up on your machine.

2. Install the required Python libraries. You can do this using the provided `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

3. Clone this repository or download the `ascii_converter.py` script.

4. Run the `main.py` script with this command:

   ```bash
   python main.py <url_to_image> <output_width>
   ```
   Replace `<url_to_image>` with the URL of your image and `<output_width>` with the desired ASCII output width (in characters).

ASCII outputs are also stored for future reference.

Note: The Canny edge detection parameters (threshold values) default to 100 and 200, but you can adjust these based on the image and edge detection requirements.

## Example

Here's a script usage example:

```bash
python main.py https://example.com/path/to/image.jpg 80
```
This command converts the image at the provided URL into ASCII art with an 80-character width and displays the result in the console.
