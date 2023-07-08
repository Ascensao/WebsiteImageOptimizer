import os
from PIL import Image


# ------------------------------------------------
# Section 1: User Inputs
# ------------------------------------------------

# Ask the user for the source directory or use a default
source_dir = input("Enter the path to the source directory: ") or "./images_sample"
if not os.path.isdir(source_dir):
    print(f"Error: {source_dir} is not a valid directory.")
    exit()

# Ask the user for the output directory or use a default
output_dir = input("Enter the path to the output directory: ") or "./images_sample_cleaned"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"Created directory {output_dir}")
elif not os.path.isdir(output_dir):
    print(f"Error: {output_dir} is not a valid directory.")
    exit()

# Ask the user for the quality output or use a default
quality = int(input("Enter the quality level for the saved images (1-100): ") or 85)

# Ask the user for the max width size resolution (the height adapts to the width) or use a default
max_output_size = (input("Do you want to set a maximum output size resolution ? (y/n): ") or "n").lower() == "y"
if max_output_size:
    max_size = int(input("Enter the maximum Width resolution of the output file: ") or 1000)
else:
    max_size = None


# ------------------------------------------------
# Section 2: Function Definitions
# ------------------------------------------------

def validate_directory(path, create=False):
    if not os.path.exists(path) and create:
        os.makedirs(path)
        print(f"Created directory {path}")
    elif not os.path.isdir(path):
        print(f"Error: {path} is not a valid directory.")
        exit()
        
def convert_avif_to_png(input_file):
    filename, extension = os.path.splitext(input_file)
    output_file = filename + ".png"
    with Image.open(input_file) as img:
        img.save(output_file)
    return output_file

def resize_image(img, max_resolution):
    # Get the original width and height
    width, height = img.size
    new_width = width
    new_height = height

    # Find the largest dimension and scale down if necessary
    if max(width, height) > max_resolution:
        if width > height:
            new_width = max_resolution
            new_height = int(height * (max_resolution / width))
        else:
            new_height = max_resolution
            new_width = int(width * (max_resolution / height))
    return img.resize((new_width, new_height), resample=Image.LANCZOS)

def convert_image(filepath, output_filepath, quality_set, max_resolution):
    with Image.open(filepath) as img:
        if max_resolution is not None:
            img = resize_image(img, max_resolution)
        print(f"Converting {filepath} to {output_filepath}")
        img.save(output_filepath, "webp", quality=quality_set)

def convert_all(source_dir, output_dir, quality_set, max_resolution):
    successful = 0
    unsuccessful_paths = []
    for root, dirs, files in os.walk(source_dir):
        for filename in files:
            extension = os.path.splitext(filename)[1].lower()
            if extension in (".jpg", ".jpeg", ".png", ".gif", ".tiff", ".jfif", ".webp", ".avif"):
                filepath = os.path.join(root, filename)
                output_filepath = os.path.join(output_dir, os.path.relpath(filepath, source_dir))
                output_filepath = os.path.splitext(output_filepath)[0] + ".webp"
                os.makedirs(os.path.dirname(output_filepath), exist_ok=True)
                try:
                    if extension == ".avif":
                        filepath = convert_avif_to_png(filepath)
                    convert_image(filepath, output_filepath, quality_set, max_resolution)
                    successful += 1
                except (IOError, OSError, ValueError, TypeError) as e:
                    print(f"Skipping {filepath}: not a valid image file. Error: {str(e)}")
                    unsuccessful_paths.append(filepath)

    print(f"Converted {successful} out of {successful + len(unsuccessful_paths)} images successfully.")
    print("Unsuccessful paths:")
    for path in unsuccessful_paths:
        print(path)

if __name__ == "__main__":
    validate_directory(source_dir)
    validate_directory(output_dir, create=True)
    convert_all(source_dir, output_dir, quality, max_size if max_output_size else None)