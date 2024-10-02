from flask import Flask, render_template, request, jsonify, send_file
import cv2
import pytesseract
import os

app = Flask(__name__)

# Set Tesseract executable path (modify according to your system setup)
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

# Preprocess the image and extract text
def preprocess_image(image_path):
    image = cv2.imread(image_path)
    scale_percent = 200
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    resized_image = cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, binary_image = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    binary_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)
    return binary_image

def ocr_from_image(image_path):
    processed_image = preprocess_image(image_path)
    config = r'--oem 3 --psm 6'
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    extracted_text = pytesseract.image_to_string(processed_image, config=config)
    return extracted_text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    if file:
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)
        
        # Perform OCR and extract text
        extracted_text = ocr_from_image(file_path)
        
        # Save the extracted text to a file
        text_file_path = file_path.rsplit('.', 1)[0] + '.txt'
        with open(text_file_path, 'w') as text_file:
            text_file.write(extracted_text)
        
        return jsonify({'text': extracted_text, 'text_file': text_file_path})

@app.route('/download/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
