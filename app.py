from flask import Flask, render_template, request, flash
from sqlalchemy import create_engine, orm
from forms import LoginForm, RegistrationForm, BlogPost
import initial
from dbsetup import Base, Users, BlogPosts
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

today = datetime.datetime.today()

engine = create_engine("mysql+mysqlconnector://admin2:@GitPa$$w0rd#@54.74.234.11/thefantasticfour?charset=utf8mb4")
DBSession = orm.sessionmaker(bind=engine)
session = DBSession()

app = initial.create_app()


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


@app.route('/post', methods=['POST'])
def post():
    return render_template('blog_post2.html')


@app.route('/subscribe',methods=['GET', 'POST'])
def subscribe():
    if request.method == 'POST':
        new_signup = Users(user_name=request.form['firstName'], user_email=request.form['email'],
                       user_pw=generate_password_hash(request.form['password1']))
        session.add(new_signup)
        session.commit()
        return render_template("subscribe.html")
    else:
        return render_template("subscribe.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()


    if form.validate_on_submit():
        email = request.form.get('email')
        password = request.form.get('password')
        user = engine.execute(f"SELECT user_email FROM users WHERE user_email = '{email}';").first()
        pwdata = engine.execute(f"SELECT user_pw FROM users WHERE user_email = '{email}';").first()
        if not user:
            flash("Invalid Credentials, Please Try Again")
        else:
            for pw in pwdata:
                if check_password_hash(pw, password):
                    print("TADA!")
                    return render_template('home.html')
                else:
                    flash("Invalid Credentials, Please Try Again")
                    return render_template("login.html", form=form)
    return render_template('login2.html', form=form)


@app.route('/blog_post', methods=['GET', 'POST'])
def newpost():
    form = BlogPost()

    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        new_blog = BlogPosts(post_title=title, post_content=content, post_date=today)
        session.add(new_blog)
        session.commit()
        flash("Blog post added")
        return render_template('home.html')
    return render_template('blog_post.html', form=form)

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)

