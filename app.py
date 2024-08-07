from flask import Flask, request, redirect, render_template
import random
import string

app = Flask(__name__)

url_mapping = {}

def generate_short_url(length=6):             
    characters = string.ascii_letters + string.digits         # Generate a random string of fixed length
    return ''.join(random.choice(characters) for _ in range(length))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['original_url'] #return the original url
        short_url = generate_short_url()            #generates a short url
        url_mapping[short_url] = original_url
        return render_template('result.html', short_url=short_url) 
    
    return render_template('index.html')

@app.route('/<short_url>')
def redirect_to_original(short_url):
    original_url = url_mapping.get(short_url)
    if original_url:
        return redirect(original_url)
    return 'URL not found', 404

if __name__ == '__main__':
    app.run(debug=True)
