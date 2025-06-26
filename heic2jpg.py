import os
import argparse
import imageio.v3 as iio
from PIL import Image
from pillow_heif import register_heif_opener

from tqdm import tqdm

register_heif_opener()
def convert_heic_to_jpg(input_folder, output_folder):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through all files in the input folder
    # add tqdm for progress bar
    for filename in tqdm(os.listdir(input_folder), desc="Converting HEIC to JPG"):
        if filename.lower().endswith(".heic"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".jpg")

            try:
                image = Image.open(input_path)
                image.convert("RGB").save(output_path, "JPEG")  # Convert in case image is not RGB
                print(f"Converted: {input_path} -> {output_path}")
            except Exception as e:
                print(f"Failed to convert {input_path}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert HEIC images to JPG format.")
    parser.add_argument("input_folder", help="Path to the folder containing HEIC images.")
    parser.add_argument("output_folder", help="Path to the folder where JPG images will be saved.")
    args = parser.parse_args()

    convert_heic_to_jpg(args.input_folder, args.output_folder)