from flask import Flask, render_template, request
from flask_caching import Cache
import os

PHOTOS_FOLDER = os.path.join('static', 'pictures')

# Setting-up Cashe
config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 50 ,
    "UPLOAD_FOLDER": PHOTOS_FOLDER # Passing photo folder direction to the Flask
} 

app = Flask(__name__)
app.config.from_mapping(config) # Inserting config defined above to the app
cache = Cache(app)


@app.route('/<photo>') # get resized photo app
@cache.cached(timeout=5) # addding 5s cache to the app

# arg: photo - string with file name including extention e.g. cute_cat.jpg
def show_photo(photo):
    
    width = request.args.get("w")
    height = request.args.get("h")
    
    # Specifying full path to the rendered image
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], photo)
    
    # Render html template from /templates/ with provided args
    return render_template("index.html", resized_photo=full_filename, width=width, height=height)

if __name__=='__main__':
    app.run(debug=True) # run app