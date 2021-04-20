from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/hobbies')
def em():
    return render_template('hobbies.html')


@app.route('/raj')
def raj():
    return render_template('raj.html')


@app.route('/fashion')
def saf():
    return  render_template('fashion.html')


@app.route('/food')
def sonia():
    return render_template('food.html')


@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')


@app.route('/contact')
def contact():
    return  render_template('contact.html')


@app.route('/sign-in')
def sign():
    return render_template('sign-in.html')


if __name__ == "__main__":
    app.run(debug=True)

