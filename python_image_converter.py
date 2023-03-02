import os
import shutil
from PIL import Image
import pillow_avif


# Ask the user for the source directory
source_dir = input("Enter the path to the source directory: ")
if not os.path.isdir(source_dir):
    print(f"Error: {source_dir} is not a valid directory.")
    exit()

# Ask the user for the output directory
output_dir = input("Enter the path to the output directory: ")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"Created directory {output_dir}")
elif not os.path.isdir(output_dir):
    print(f"Error: {output_dir} is not a valid directory.")
    exit()

# Ask the user for the quality output
quality = int(input("Enter the quality level for the saved images (1-100): "))

# Ask the user for the max width size resolution (the height adapts to the width)
max_output_size = input("Do you want to set a maximum output size resolution ? (y/n)").lower() == "y"
if max_output_size:
    max_size = int(input("Enter the maximum Width resolution of the output file: "))
else:
    max_size = None

# standart Pillow lib is not compatible with converting directly .avif to .webp so the script convert to png first.
def convert_avif_to_png(input_file):
    filename, extension = os.path.splitext(input_file)
    output_file = filename + ".png"
    with Image.open(input_file) as img:
        img.save(output_file)
    return output_file


#function to iterate through directories and convert images to WebP
def convert_all(source_dir, output_dir, quality_set, max_resolution):
    successful = 0
    unsuccessful_paths = []
    for root, dirs, files in os.walk(source_dir):
        for filename in files:
            extension = os.path.splitext(filename)[1].lower()
            if extension in (".jpg", ".jpeg", ".png", ".gif", ".tiff", ".jfif"):
                # Convert the image to WebP
                filepath = os.path.join(root, filename)
                output_filepath = os.path.join(output_dir, os.path.relpath(filepath, source_dir))
                output_filepath = os.path.splitext(output_filepath)[0] + ".webp"
                if not os.path.exists(os.path.dirname(output_filepath)):
                    os.makedirs(os.path.dirname(output_filepath))
                try:
                    with Image.open(filepath) as img:
                        # Resize the image if it's larger than the max resolution
                        if max_resolution is not None:
                            # Get the original width and height
                            width, height = img.size

                            # Define the new width and height to be equal to the original width and height
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

                            # Resize the image using the new dimensions
                            img = img.resize((new_width, new_height), resample=Image.LANCZOS)
                        print(f"Converting {filepath} to {output_filepath}")
                        img.save(output_filepath, "webp", quality=quality_set)
                    successful += 1
                except (IOError, OSError, ValueError, TypeError):
                    print(f"Skipping {filepath}: not a valid image file")
                    unsuccessful_paths.append(filepath)
            elif extension == ".webp":
                # Open the WebP file and get its width and height
                filepath = os.path.join(root, filename)
                output_filepath = os.path.join(output_dir, os.path.relpath(filepath, source_dir)).replace("\\", "/")
                if not os.path.exists(os.path.dirname(output_filepath)):
                    os.makedirs(os.path.dirname(output_filepath))
                try:
                    with Image.open(filepath) as img:
                        width, height = img.size

                        # Define the new width and height to be equal to the original width and height
                        new_width = width
                        new_height = height

                        # Resize the image if it's larger than the max resolution
                        if max_resolution is not None and max(width, height) > max_resolution:
                            if width > height:
                                new_width = max_resolution
                                new_height = int(height * (max_resolution / width))
                            else:
                                new_height = max_resolution
                                new_width = int(width * (max_resolution / height))

                            # Resize the image using the new dimensions
                            img = img.resize((new_width, new_height), resample=Image.LANCZOS)

                        print(f"Converting {filepath} to {output_filepath}")
                        img.save(output_filepath, "webp", quality=quality_set)
                        successful += 1
                except (IOError, OSError, ValueError, TypeError):
                    print(f"Skipping {filepath}: not a valid image file")
                    unsuccessful_paths.append(filepath)
            elif extension == ".avif":
                # Convert the AVIF file to PNG first, and then convert the PNG to WebP
                filepath = os.path.join(root, filename)
                png_filepath = convert_avif_to_png(filepath)
                if png_filepath is not None:
                    output_filepath = os.path.join(output_dir, os.path.relpath(png_filepath, source_dir))
                    output_filepath = os.path.splitext(output_filepath)[0] + ".webp"
                    if not os.path.exists(os.path.dirname(output_filepath)):
                        os.makedirs(os.path.dirname(output_filepath))
                    try:
                        with Image.open(filepath) as img:
                            # Resize the image if it's larger than the max resolution
                            if max_resolution is not None:
                                # Get the original width and height
                                width, height = img.size

                                # Define the new width and height to be equal to the original width and height
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

                                # Resize the image using the new dimensions
                                img = img.resize((new_width, new_height), resample=Image.LANCZOS)
                            print(f"Converting {filepath} to {output_filepath}")
                            img.save(output_filepath, "webp", quality=quality_set)
                        successful += 1
                    except (IOError, OSError, ValueError, TypeError):
                        print(f"Skipping {png_filepath}: not a valid image file")
                        unsuccessful_paths.append(png_filepath)

    print(f"Converted {successful} out of {successful + len(unsuccessful_paths)} images successfully.")
    input("Press Enter to print all unsuccessful paths.")
    for path in unsuccessful_paths:
        print(path)

if __name__ == "__main__":
    convert_all(source_dir, output_dir, quality, max_size)