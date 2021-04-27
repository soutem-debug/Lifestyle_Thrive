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


#@app.route('/post', methods=['GET'])
#def post():
#    return render_template('blog_post2.html')


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
                    #user = login_user(remember=True)
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


@app.route( "/blog/<int:post_id>/edit/", methods=['GET', 'POST'] )
def editBlog(post_id):
    editedBlog = session.query( BlogPosts ).filter_by( post_id=post_id ).one()
    if request.method == 'POST':
        if request.form['name']:
            editedBlog.title = request.form['name']
            return redirect( url_for( 'Blogposts' ) )
    else:
        return render_template( 'editBlog.html', blog=editedBlog )


@app.route( '/blog/<int:post_id>/delete/', methods=['GET', 'POST'] )
def deleteBlog(post_id):
    blog_to_delete = session.query( BlogPosts ).filter_by( post_id=post_id ).one()
    if request.method == 'POST':
        session.delete( blog_to_delete )
        session.commit()
        return redirect( url_for( 'BlogPosts', blog=post_id ) )
    else:
        return render_template( 'deleteblog.html', blog=blog_to_delete )


@app.route('/blog/<int:post_id>')
def post(post_id):
    post_content = engine.execute(f"SELECT post_content FROM blog_posts WHERE post_id = '{post_id}';").first()
    post_title = engine.execute(f"SELECT post_title FROM blog_posts WHERE post_id = '{post_id}';").first()
    return render_template('blog.html', blog_title=post_title[0], blog_content=post_content[0])


@app.route('/blog_index')
def blog_index():
    blogs = session.query(BlogPosts).all()
    return render_template('blog_index.html', blogs=blogs)



@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)
