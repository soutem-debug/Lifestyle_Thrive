from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
  return render_template('about.html')


@app.route('/em')
def em():
  return render_template('em.html')


@app.route('/raj')
def raj():
  return render_template('raj.html')


@app.route('/saf')
def saf():
  return  render_template('saf.html')


@app.route('/sonia')
def sonia():
  return  render_template('sonia.html')


@app.route('/subscribe')
def subscribe():
  return  render_template('subscribe.html')

@app.route('/contact')
def contact():
  return  render_template('contact.html')


@app.route('/sign-in')
def sign():
  return  render_template('sign-in.html')



if __name__ == "__main__":
    app.run(debug= True)

