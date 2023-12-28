# Image Segmentor

![Screenshot](https://github.com/izzat5233/image-segmentor/assets/92182269/47423b2d-898f-4e2d-8cad-541c9f4cb9c5)

## Overview

This PyQt-based application provides a GUI interface for performing various image segmentation operations,
from detection filters to thresholding. The application is built with Python and OpenCV.

## Features

- Image Loading and Saving, from and to device disk.
- Custom Filter with dynamic size.
- Predefined Filters, including:
    - Laplacian Filter: Used for edge detection.
    - Laplacian of Gaussian Filter: performs smoothing then laplacian.
    - Threshold Filter: Converts the image to a binary image with any thresh value.
    - Point Detection Filter: Highlights the points in an image.
    - Line Detection Filters: Includes horizontal, vertical, +45-degree, and -45-degree line detection.
    - Edge Detection Filters: Users can choose between Sobel and Prewitt edge detectors for horizontal, vertical,
      +45-degree, and -45-degree edges.