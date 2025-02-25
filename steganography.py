from flask import Flask, render_template, request, send_file
from PIL import Image
import io

app = Flask(__name__)

def encode_message(image, message):
    binary_message = ''.join(format(ord(i), '08b') for i in message)
    binary_message += '1111111111111110'  # Message delimiter
    
    img = image.convert('RGB')
    pixels = img.load()
    data_index = 0
    message_index = 0
    
    # Loop over each pixel and replace LSB with message bits
    for y in range(img.height):
        for x in range(img.width):
            pixel = list(pixels[x, y])
            for i in range(3):  # Red, Green, Blue channels
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
            for i in range(3):  # Red, Green, Blue channels
                binary_message += str(pixel[i] & 1)
    
    # Find the delimiter (1111111111111110)
    delimiter = '1111111111111110'
    message_binary = binary_message.split(delimiter)[0]
    
    message = ''
    for i in range(0, len(message_binary), 8):
        byte = message_binary[i:i+8]
        message += chr(int(byte, 2))
    
    return message

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hide_message', methods=['POST'])
def hide_message():
    image_file = request.files['image']
    message = request.form['message']
    
    image = Image.open(image_file)
    output_image = encode_message(image, message)
    
    img_io = io.BytesIO()
    output_image.save(img_io, 'PNG')
    img_io.seek(0)
    
    return send_file(img_io, mimetype='image/png')

@app.route('/extract_message', methods=['POST'])
def extract_message():
    image_file = request.files['image']
    
    image = Image.open(image_file)
    message = decode_message(image)
    
    return message

if __name__ == '__main__':
    app.run(debug=True)