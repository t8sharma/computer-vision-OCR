# AI-Powered OCR

This is an AI-powered Optical Character Recognition (OCR) web application built using Flask, OpenCV, and Tesseract. The web app allows users to upload images and extract the text from those images using OCR. The extracted text is then displayed on the web page and can be downloaded as a `.txt` file.

## Features

- Upload image files and extract text using Tesseract OCR.
- Beautiful, modern AI-themed interface with glowing effects.
- Supports downloading extracted text as a `.txt` file.
- Responsive design for use on mobile devices.

## Technologies Used

- **Flask**: Python web framework used for handling server-side logic.
- **Tesseract OCR**: Open-source OCR engine for text extraction from images.
- **OpenCV**: Library used for image preprocessing to enhance OCR accuracy.
- **HTML, CSS, JavaScript**: Frontend technologies to build the AI-themed interface.

## Prerequisites

To run this application, you need to have the following installed on your machine:

- **Python 3.10**
- **pip**: Python package manager.
- **Tesseract OCR**: [Download Tesseract](https://github.com/tesseract-ocr/tesseract) and ensure it is installed and added to your system's PATH.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/ai-ocr-app.git
   cd ai-ocr-app
   ```
2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Ensure Tesseract is installed and available in your system’s PATH. If not, set the path to the Tesseract executable in app.py:

   ```bash
   pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
   ```
4. Run the Flask application:

   ```bash
   python app.py
   ```
5. Open your web browser and navigate to http://127.0.0.1:5000/

## Usage

1. Upload an Image: On the homepage, click the "Upload & Extract Text" button to select an image (JPEG, PNG, etc.) from your file system.
2. Extract Text: After the image is uploaded, the text will be extracted and displayed in the textarea below.
3. Download the Extracted Text: Click the "Download as .txt" button to download the extracted text as a .txt file.
