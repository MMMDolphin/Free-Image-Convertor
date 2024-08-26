from PIL import Image
import os


def detect_and_convert_images(input_directory, output_directory, output_format):
    """
    Detects the format of images in a directory and converts them to the specified format.

    Args:
    - input_directory (str): Path to the directory containing images.
    - output_directory (str): Path to the directory where converted images will be saved.
    - output_format (str): Desired image format to convert to.
    """

    # Supported formats by Pillow
    supported_formats = ['JPEG', 'PNG', 'BMP', 'GIF', 'TIFF', 'ICO', 'WEBP']

    # Convert the output format to uppercase for consistency
    output_format = output_format.upper()

    if output_format not in supported_formats:
        print(f"Error: '{output_format}' is not a supported format.")
        return

    if not os.path.isdir(input_directory):
        print(f"Error: '{input_directory}' is not a valid directory.")
        return

    # Check if the output directory exists, if not, create it
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Process each file in the input directory
    for filename in os.listdir(input_directory):
        filepath = os.path.join(input_directory, filename)

        # Check if it's a file (not a subdirectory)
        if os.path.isfile(filepath):
            try:
                # Open the image file
                with Image.open(filepath) as img:
                    # Get the current image format
                    original_format = img.format

                    print(f"Detected {original_format} format for image: {filename}")

                    # Create a new filename with the desired format
                    base, _ = os.path.splitext(filename)
                    new_filename = f"{base}.{output_format.lower()}"
                    new_filepath = os.path.join(output_directory, new_filename)

                    # Save the image in the new format
                    img.save(new_filepath, output_format)

                    print(f"Converted and saved to: {new_filepath}")

            except Exception as e:
                print(f"Error processing file {filename}: {e}")


if __name__ == "__main__":
    # Supported formats for display
    supported_formats = ['JPEG', 'PNG', 'BMP', 'GIF', 'TIFF', 'ICO', 'WEBP']

    # Get user input for input directory path, output directory path, and desired output format
    input_directory = input("Enter the path to the directory containing images: ")
    output_directory = input("Enter the path to the directory where converted images will be saved: ")
    output_format = input(f"Enter the desired output image format ({', '.join(supported_formats)}): ")

    detect_and_convert_images(input_directory, output_directory, output_format)
