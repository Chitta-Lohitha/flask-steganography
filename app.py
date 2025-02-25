from flask import Flask, render_template, request, send_file
from PIL import Image
import io
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
OUTPUT_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Ensure upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def encode_message(image, message):
    binary_message = ''.join(format(ord(i), '08b') for i in message)
    binary_message += '1111111111111110'  # Message delimiter
    
    img = image.convert('RGB')
    pixels = img.load()
    message_index = 0
    
    for y in range(img.height):
        for x in range(img.width):
            pixel = list(pixels[x, y])
            for i in range(3):  # RGB channels
                if message_index < len(binary_message):
                    pixel[i] = (pixel[i] & 0xFE) | int(binary_message[message_index])
                    message_index += 1
            pixels[x, y] = tuple(pixel)
            if message_index >= len(binary_message):
                break
        if message_index >= len(binary_message):
            break
    
    return img

def decode_message(image):
    img = image.convert('RGB')
    pixels = img.load()
    
    binary_message = ''
    
    for y in range(img.height):
        for x in range(img.width):
            pixel = pixels[x, y]
            for i in range(3):  # RGB channels
                binary_message += str(pixel[i] & 1)
    
    delimiter = '1111111111111110'
    message_binary = binary_message.split(delimiter)[0]
    
    message = ''.join(chr(int(message_binary[i:i+8], 2)) for i in range(0, len(message_binary), 8))
    
    return message

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hide_message', methods=['POST'])
def hide_message():
    image_file = request.files['image']
    message = request.form['message']
    
    if image_file.filename == '':
        return "No selected file"
    
    image_path = os.path.join(app.config["UPLOAD_FOLDER"], image_file.filename)
    image_file.save(image_path)
    
    image = Image.open(image_path)
    output_image = encode_message(image, message)
    
    output_path = os.path.join(OUTPUT_FOLDER, "output.png")
    output_image.save(output_path, 'PNG')
    
    return send_file(output_path, mimetype='image/png', as_attachment=True)

@app.route('/extract_message', methods=['POST'])
def extract_message():
    image_file = request.files['image']
    
    if image_file.filename == '':
        return "No selected file"
    
    image = Image.open(image_file)
    message = decode_message(image)
    
    return message

if __name__ == '__main__':
    app.run(debug=True)
