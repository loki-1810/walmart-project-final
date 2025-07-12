from flask import Flask, render_template

app = Flask(__name__)

# Home Page
@app.route('/')
def index():
    return render_template('index.html')

# Login Page
@app.route('/login')
def login():
    return render_template('login.html')

# Circular Cart Page
@app.route('/circular-cart')
def circular_cart():
    return render_template('circular_cart.html')

# Recycle Form Page
@app.route('/recycle-form')
def recycle_form():
    return render_template('recycle_form.html')

# Cart Page
@app.route('/cart')
def cart():
    return render_template('cart.html')

if __name__ == '__main__':
    app.run(debug=True)
