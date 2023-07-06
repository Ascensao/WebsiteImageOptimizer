# Website Image Optimizer - Convert bulk images to webp formatt

Website Image Optimizer is a python script that converts images to WebP format. It supports JPG, JPEG, PNG, GIF, TIFF, JFIF, and AVIF image formats. You can use it to quickly and easily convert your website's images to the WebP format. 

This conversion can result in significant file size reductions without sacrificing image quality, allowing your website to load faster and use less bandwidth.

**Note:** In our tests, we were able to reduce the file size of a folder of 714 images from 181 MB to 23.3 MB, resulting in an average **reduction of 87%**. The conversion process took approximately 40 seconds to complete.

## Buy me a coffee
Whether you use this project, have learned something from it, or just like it, please consider supporting it by buying me a coffee, so I can dedicate more time on open-source projects like this :)

<a href="https://www.buymeacoffee.com/ascensao1" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-yellow.png" alt="Buy Me A Coffee" height="41" width="174"></a>

## Prerequisites

- Python 3.x
- Pillow library

## Installation

1. Clone the repository or download the ZIP file and extract its contents.
2. Install the required Pillow library by running the following command: 
 ```
 pip install Pillow
 ```


## Usage

1. Open a command prompt or terminal window and navigate to the directory where the script is located.
2. Run the script by entering the following command:
```
python convert.py <source_dir> <output_dir> [--quality <quality>] [--max_resolution <max_resolution>]
 ```
* source_dir: The directory containing the images to be converted.
* output_dir: The directory where the converted images will be saved.
* --quality <quality> (optional): The quality setting for the WebP files (default is 80).
* --max_resolution <max_resolution> (optional): The maximum resolution of the output files. Images larger than this size will be scaled down (maintaining aspect ratio) to fit within this limit.
For example, to convert all images in the input directory to WebP format, with a maximum resolution of 1000 pixels and quality setting of 90, run the following command:
```
 python convert.py C:/Users/Ascensao/Desktop/Imgs C:/Users/Ascensao/Desktop/Imgs_converted --quality 90 --max_resolution 1000
```
3. Follow the on-screen prompts to enter the source directory, output directory, maximum resolution (optional), and quality (optional).
4. The script will convert all images in the source directory to WebP format and save them in the output directory.

## Performance
 If you're managing a website with a large number of images, optimizing them for web performance can make a huge difference in page load times and overall user experience
### Example
* > Initial folder: 714 images, **181 MB**
* > Converted Folder: 714 images, **23.3 MB** (All images converted to webp and resized to max 800px width)
### Single Image Examples
* > Original Webp image: **3.22 MB** (4000x2667) **-->** Converted Webp image: **32.41 KB** (800x533)
* > Original Jpg image: **7.06 MB** (3888x2916) --> Converted to webp image: **39.71 KB** (800x600)
  
  
By using this script to convert and resize images, we were able to achieve a significant reduction in file size, resulting in faster website load times and improved performance. In the example above, we reduced the size of 714 images from 181 MB to 23.3 MB, a reduction of approximately 87%. For example, we saw a reduction of 99% in file size for a 4000x2667 WebP image, going from 3.22 MB to just 32.41 KB (800x533). Similarly, a 7.06 MB JPEG image was reduced to 39.71 KB (800x600) when converted to WebP.
  
Additionally, the processing time for the conversion and resizing of all 714 images in the above example was only 40 second. Making it an fast and efficient way to optimize your website's images with this script.
  
## Author

Bernardo Ascensao

## License

This project is licensed under the MIT License - see the LICENSE file for details.
