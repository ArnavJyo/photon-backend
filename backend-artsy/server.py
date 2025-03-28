from flask import Flask, request, jsonify
from flask_cors import CORS
from distance_metric import euclidian_distance,minkowski_distance,manhattan_distance,chebyshev_distance
from psudo_halftone import PointAdd,PointSub,halftone_add,halftone_sub,setRange
from diagonal_tracing import diagonal_trace
from circle_scatter import circle_scatter,square_scatter
from strings import strings
from segmentation import segmentation
from greyscale import grayscale
from blur import blur
from noise import add_noise
from pixalate import pixelate
from ASCII import ASCII
from removebg import removebg
app = Flask(__name__)
CORS(app)
@app.route('/process-image', methods=['POST'])
def process_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image_file = request.files['image']
    temp_image_path = 'C:/Users/arnav/Desktop/artsy/data/image-test.png'
    image_file.save(temp_image_path)
    button_text = request.form.get('buttonText')
    if button_text == "Euclidean":
        processed_image_path = euclidian_distance(temp_image_path)
    elif button_text == "Minkowski":
        processed_image_path = minkowski_distance(temp_image_path)
    elif button_text == "Manhattan":
        processed_image_path = manhattan_distance(temp_image_path)
    elif button_text == "Chebyshev":
        processed_image_path = chebyshev_distance(temp_image_path)
    elif button_text == "Halftone Add":
        processed_image_path = halftone_add(temp_image_path)
    elif button_text == "Halftone Sub":
        processed_image_path = halftone_sub(temp_image_path)
    elif button_text == "Diagonal Tracing":
        processed_image_path = diagonal_trace(temp_image_path)
    elif button_text == "Circle Scatter":
        processed_image_path = circle_scatter(temp_image_path)
    elif button_text == "Square Scatter":
        processed_image_path = square_scatter(temp_image_path)
    elif button_text == "Strings":
        processed_image_path = strings(temp_image_path)
    elif button_text == "Segment":
        processed_image_path = segmentation(temp_image_path)
    elif button_text == "Grayscale":
        processed_image_path = grayscale(temp_image_path)
    elif button_text == "Blur":
        blur_intensity = int(request.form.get('blurIntensity',1))
        processed_image_path = blur(temp_image_path,blur_intensity)
    elif button_text == "Noise":
        noise_intensity = int(request.form.get('noiseIntensity',25))
        processed_image_path = add_noise(temp_image_path,0,noise_intensity)
    elif button_text == "Pixalate":
        pixel_intensity = int(request.form.get('pixelIntensity',0))
        processed_image_path = pixelate(temp_image_path,pixel_intensity)
    elif button_text == "ASCII":
        processed_image_path = ASCII(temp_image_path)
    elif button_text == "RemoveBG":
        processed_image_path = removebg(temp_image_path)
    
    else:
        return jsonify({'error': 'Invalid button text'}), 400
    

    return jsonify({'processed_image_path': processed_image_path.tolist()})

if __name__ == '__main__':
    app.run(debug=True,port=5000)
