from flask import Flask,render_template,request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/price')
def price():
    return render_template('price.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
    
@app.route('/blogs')
def blogs():
    return render_template('blogs.html')


if __name__=='__main__':
    app.run(debug=True)


