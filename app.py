from flask import Flask, render_template

app = Flask(__name__)


@app.route('/home')
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/blogs')
@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/post')
def post():
    return render_template('blog_post2.html')


@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/sign-in')
def sign():
    return render_template('sign-in.html')


if __name__ == "__main__":
    app.run(debug=True)

