from flask import Flask, render_template, request
import requests
#import io
#from PIL import Image

app = Flask(__name__)

# Define route for the main page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        category = request.form['category']
        img_url = get_image_url(category)
        return render_template('index.html', img_url=img_url)
    return render_template('index.html', img_url=None)

# Function to retrieve image URL based on category
def get_image_url(category):
    # Make a request to the Unsplash API to get a random image
    url = f"https://api.unsplash.com/photos/random?query={category}&orientation=landscape&client_id=1n7sSMtCh8Hs_MrBOjhQ1SygTDA-BJ550UdX3rwLYZQ"
    data = requests.get(url).json()
    return data["urls"]["regular"]

if __name__ == '__main__':
    app.run(debug=True,port=5001)