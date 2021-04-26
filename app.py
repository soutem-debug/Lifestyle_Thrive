from flask import Flask, render_template, request, flash, redirect, url_for
from sqlalchemy import create_engine, orm
from forms import LoginForm, RegistrationForm, BlogPost
import initial
from dbsetup import Base, Users, BlogPosts
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
from flask_login import LoginManager
from flask_login import login_user, login_required, logout_user, current_user

today = datetime.datetime.today()

engine = create_engine("mysql+mysqlconnector://admin2:@GitPa$$w0rd#@54.74.234.11/thefantasticfour?charset=utf8mb4")
DBSession = orm.sessionmaker(bind=engine)
session = DBSession()
session.rollback()

app = initial.create_app()

login_manager = LoginManager()
login_manager.login_view = 'app.login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(id):
    return engine.execute(f"SELECT user_id FROM users WHERE user_id = '{id()}';")


@app.route('/home')
@app.route('/')
def home():
    blogs = session.query(BlogPosts).all()
    return render_template('index.html', blogs=blogs)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/blogs')
@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/post', methods=['GET'])
def post():
    return render_template('swim.html')


@app.route('/walk', methods=['GET'])
def swim():
    return render_template('walk.html')


@app.route('/garden', methods=['GET'])
def garden():
    return render_template('garden.html')


@app.route('/mother', methods=['GET'])
def mother():
    return render_template('mother.html')


@app.route('/paddle', methods=['GET'])
def paddle():
    return render_template('paddle.html')

# @app.route('/subscribe',methods=['GET', 'POST'])
# def subscribe():
#     if request.method == 'POST':
#         new_signup = Users(user_name=request.form['firstName'], user_email=request.form['email'],
#                        user_pw=generate_password_hash(request.form['password1']))
#         session.add(new_signup)
#         session.commit()
#         return render_template("subscribe.html")
#     else:
#         return render_template("subscribe.html")


@app.route('/subscribe', methods=['GET', 'POST'])
def subscribe():
    # flash('It worked', category='success')
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = engine.execute(f"SELECT user_email FROM users WHERE user_email = '{email}';").first()
        if user:
            flash('Email already exists.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        else:
            new_user = Users(user_name=request.form['firstName'], user_email=request.form['email'],
                             user_pw=generate_password_hash(request.form['password1']))
            session.add(new_user)
            session.commit()
            # login_user(new_user, remember=True)
            flash('Account created!', category='success')
    return render_template("subscribe.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = engine.execute(f"SELECT user_email FROM users WHERE user_email = '{email}';").first()
        pwdata = engine.execute(f"SELECT user_pw FROM users WHERE user_email = '{email}';").first()
        if user:
            for pw in pwdata:
                if check_password_hash(pw, password):
                    flash('Logged in successfully!', category='success')
                    user = login_user(remember=True)
                return render_template("index.html")
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login2.html", user=current_user)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have successfully logged out!', category='success')
    return render_template("index.html")


@app.route('/add_blog', methods=['GET', 'POST'])
def newBlog():
    if request.method == 'POST':
        new_blog = BlogPosts(post_title=request.form['title'], post_content=request.form['page-content'],
                             post_date=today)
        session.add(new_blog)
        session.commit()
        flash('You have submitted a new blog!', category='success')
        return render_template('index.html')
    else:
        return render_template('add_blog.html')

        # @login_required
        # def newpost():
        #         form = BlogPost()
        #         if request.method == 'POST':
        #             newpost = request.form.get('blog_post')
        #             # if len(newpost) < 1:
        #             #     flash('Blog post is too short!', category='error')
        #             #     return render_template('add_blog.html')
        #             if form.validate_on_submit():
        #                 title = form.title.data
        #                 content = form.content.data
        #                 new_blog = BlogPosts(post_title=title, post_content=content, post_date=today)
        #                 session.add(new_blog)
        #                 session.commit()
        #                 flash("Blog post added")
        #             return render_template('index.html')

        return render_template("add_blog.html", form=form, user=current_user)
    # form = BlogPost()
    #
    # if form.validate_on_submit():
    #     title = form.title.data
    #     content = form.content.data
    #     new_blog = BlogPosts(post_title=title, post_content=content, post_date=today)
    #     session.add(new_blog)
    #     session.commit()
    #     flash("Blog post added")
    #     return render_template('index.html')
    # return render_template('add_blog.html', form=form)


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)
