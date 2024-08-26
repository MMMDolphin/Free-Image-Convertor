# Image Format Detection and Conversion

As web developers, we often need to use the .webp image format for its efficient compression and fast loading times. While services like CloudConvert.com offer image conversion, they typically limit you to 10 free conversions per day. This restriction can be quite challenging when working on larger projects that require multiple images to be converted.

<img width="1470" alt="image" src="https://github.com/user-attachments/assets/1e920853-0731-4495-b06b-14f104979920">

## Requirements

- Python 3.x
- `Pillow` library (`pip install Pillow`)

## Functionality

The script performs the following actions:

1. **Detect Image Format**: Identifies the format of each image in the input directory.
2. **Convert Image Format**: Converts images to the specified format if it is supported.
3. **Save Converted Images**: Saves the converted images to an output directory.

  <img width="1283" alt="image" src="https://github.com/user-attachments/assets/c4a32d06-3332-4724-9bde-68749b8ed3fb">



## Supported Formats

The script supports the following image formats:

- JPEG
- PNG
- BMP
- GIF
- TIFF
- ICO
- WEBP

## Usage

1. Clone the repository or download the script.
2. Ensure you have the `Pillow` library installed.
3. Run the script using Python:

```bash
python script_name.py
