from flask import Flask, render_template, request, redirect, url_for
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)

# Load your trained custom Xception model
model = load_model('xception_model.h5')

# Ensure the upload folder exists
UPLOAD_FOLDER = 'static/uploads/'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Define the allowed file types
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def preprocess_image(img_path):
    """
    Preprocess the uploaded image to match the input requirements of the Xception model.
    """
    img = image.load_img(img_path, target_size=(75, 100))  # Resize to match model input
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize pixel values
    return img_array

def predict_image(img_path):
    """
    Predict the class of the uploaded image using the Xception model.
    """
    preprocessed_img = preprocess_image(img_path)
    prediction = model.predict(preprocessed_img)
    class_labels = ['akiec', 'bcc', 'bkl', 'df', 'mel', 'nv', 'vasc']  # Update with your class labels
    predicted_class = class_labels[np.argmax(prediction)]
    confidence = np.max(prediction) * 100
    return predicted_class, confidence

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            predicted_class, confidence = predict_image(filepath)
            return render_template('index.html', filename=file.filename, prediction=predicted_class, confidence=confidence)
    return render_template('index.html')

@app.route('/clear', methods=['POST'])
def clear():
    return redirect(url_for('index'))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

if __name__ == "__main__":
    app.run(debug=True)