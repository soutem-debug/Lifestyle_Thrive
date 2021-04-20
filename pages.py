from flask import Blueprint, render_template

pages = Blueprint('pages', __name__)

@pages.route('/')
def home():
    return render_template('Index.html')

@pages.route('/about')
def about():
  return render_template('about.html')

@pages.route('/em')
def em():
  return render_template('em.html')

@pages.route('/raj')
def raj():
  return render_template('raj.html')

@pages.route('/saf')
def saf():
  return  render_template('saf.html')

@pages.route('/sonia')
def sonia():
  return  render_template('sonia.html')

@pages.route('/subscribe')
def subscribe():
  return  render_template('subscribe.html')

@pages.route('/contact')
def contact():
  return  render_template('contact.html')

@pages.route('/sign-in')
def sign():
  return  render_template('sign-in.html')
