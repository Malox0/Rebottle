
from flask import Flask, request, jsonify
import base64
from PIL import Image
import io
import sys
import os
import threading
import traceback

name = "tests"

app = Flask(name)

def image_processor(base64_image, image_size=(224, 224)):
    try:
        # Decode the base64 image
        img_data = base64.b64decode(str(base64_image))

        
        b_img = io.BytesIO(img_data)
        b_img = b_img
        img = Image.open(b_img)
        
        img_resized = img.resize(image_size)
        img_resized = img_resized.convert('RGB')
        img_buffer = io.BytesIO()
        img_resized.save(img_buffer, format='JPEG')

        img_base64 = base64.b64encode(img_buffer.getvalue()).decode()

        return img_base64
        
        
    except Exception as e:
       return str( traceback.format_exc()) + "   FLKAG " + str(img_data)



@app.route('/process_image', methods=['POST'])
def process_image():
    try:
        # Get the base64 image from the request body
        base64_image = request.get_json()['img']
        
        # Process the image
        result = image_processor(base64_image)

        # Return the processed image
        return jsonify({'status': 'success', 'result': result})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

def run_flask_app():
    app.run(port = 5005, debug=True, use_reloader=False, threaded=True)

# Run the Flask app in a separate thread
thread = threading.Thread(target=run_flask_app)
thread.start() 
	 
