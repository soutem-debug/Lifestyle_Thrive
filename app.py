from flask import Flask, render_template, request, flash, redirect
from sqlalchemy.orm import Session
from dbsetup import Comment
from dbsetup import engine
with Session(engine) as session:


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


@app.route('/article')
def article():
    return render_template('blog_post2.html')


@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post(post_id):
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        comment = Comment(name=name, email=email, message=message, post_id=post_id)
        session.add(comment)
        flash('Comment submitted')
        session.commit()
        return redirect(request.url)


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

