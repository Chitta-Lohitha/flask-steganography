🔐 Secure Data Hiding in Image Using Steganography
📌 Overview
This project is a Flask-based web application that implements image steganography, allowing users to securely hide and retrieve text messages inside images. The system ensures confidential communication by embedding secret data into images without noticeable changes.

Steganography is the art of concealing information within digital media. This project utilizes Least Significant Bit (LSB) Steganography to hide text messages inside images without altering their appearance, making it a secure method for data transmission.

🚀 Features
✅ Hide Secret Messages – Encode a text message inside an image.
✅ Retrieve Hidden Data – Extract the hidden message from an image.
✅ User-Friendly Interface – Simple UI for encrypting and decrypting messages.
✅ Secure Encoding – Uses LSB Steganography for data hiding.
✅ Supports Multiple Image Formats – Works with PNG, BMP images.
✅ Fast Processing – Efficient encoding and decoding of messages.
✅ No Data Loss – Maintains image quality after encoding.

🔧 Installation & Setup
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/Chitta-Lohitha/flask-steganography.git
cd flask-steganography
2️⃣ Set Up Virtual Environment
bash
Copy
Edit
python -m venv venv
For Windows
bash
Copy
Edit
venv\Scripts\activate
For macOS/Linux
bash
Copy
Edit
source venv/bin/activate
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Run the Flask Application
bash
Copy
Edit
python app.py

📸 How It Works
1️⃣ Encoding (Hiding a Message)
Upload an image 📷
Enter a secret message ✏️
Click "Encode" 🔐 (Message gets hidden in the image)
Download the stego-image 📥
2️⃣ Decoding (Revealing the Message)
Upload the stego-image 🕵️
Click "Decode" 🎭 (Secret message is revealed)
👤Author
*Chitta Lohitha
*GitHub:https://github.com/Chitta-Lohitha
📜 License
This project is licensed under the MIT License.
😊Happy Coading.
