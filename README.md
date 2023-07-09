# Website Image Optimizer - SEO

###  Convert bulk images to WebP Format

## About the Project

<p>Website Image Optimizer is a powerful Python script designed to convert images to the WebP format. It supports various image formats, including JPG, JPEG, PNG, GIF, TIFF, JFIF, and AVIF. The script can be used to convert your website's images to WebP format efficiently. </p>

<p>The conversion process significantly reduces the file size without compromising the image quality, improving the SEO of your website making  quicker load times and less bandwidth consumption.</p>

<p>This repository comes with a sample of images in the 'images_sample' folder. The original size of the images was 12.8 MB. After running the script and converting the images, the total size was reduced to 1.02MB, representing a significant reduction of **92%**.</p>

## Prerequisites
To run the script, you need:

- [Python 3.x](https://www.python.org/downloads/)
- [Pillow library](https://pillow.readthedocs.io/en/stable/installation.html)

## Installation
1. Clone the repository or download the ZIP file and extract its contents.
2. Open a terminal or command prompt and run the following command to install the Pillow library:


## Usage
1. Navigate to the directory where the script is located using a command prompt or terminal window.
2. Execute the script with the following command:
 ```
 cd WebsiteImageOptimizer

 python main.py
 ```
3. Follow the on-screen prompts to enter the source directory, output directory, maximum resolution (optional), and quality (optional).
4. The script will automatically convert all images in the source directory to WebP format and save them in the output directory.

If you leave all console prompt questions in blank, the default settings will be:
- Initial Folder:  `/images_sample`
- Converted Images Folder: `/images_sample_cleaned`
- Image Quality: `85`
- Images Size: `Original (No resizing)`


## Performance

 If you're managing a website with a large number of images, optimizing them for web performance can make a huge difference in page load times and overall user experience

### Example 1
* > Initial Folder ./images_sample: 25 images, **12.8 MB**
* > Converted Folder ./images_sample_cleaned: 25 images, **1.02 MB**

### Example 2
* > Initial Folder: 714 images, **181 MB**
* > Converted Folder: 714 images, **23.3 MB** (All images converted to webp and resized to max 800px width)

### Single Image Examples
* > Original Webp image: **3.22 MB** (4000x2667) **-->** Converted Webp image: **32.41 KB** (800x533)
* > Original Jpg image: **7.06 MB** (3888x2916) --> Converted to webp image: **39.71 KB** (800x600)
  

<p>By using this script to convert and resize images, I was able to achieve a significant reduction in file size, resulting in faster website load times and improved performance. In my test, this script reduced the size of 714 images from 181 MB to 23.3 MB, a reduction of approximately 87%.</p>

<p>For example, I saw a reduction of 99% in file size for a 4000x2667 WebP image, going from 3.22 MB to just 32.41 KB (800x533). Similarly, a 7.06 MB JPEG image was reduced to 39.71 KB (800x600) when converted to WebP.</p>
  
<p>Additionally, the processing time for the conversion and resizing of all 714 images in the above example was only 40 second. Making it an fast and efficient way to optimize your website's images with this script.</p>
  

## License

This project is licensed under the Apache License - see the [LICENSE](LICENSE) file for details.

<a href="https://www.buymeacoffee.com/ascensao1" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-yellow.png" alt="Buy Me A Coffee" height="41" width="174"></a>