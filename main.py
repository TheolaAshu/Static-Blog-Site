from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

#main links
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/blogs/')
def blogs():
    return render_template('blogs.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

@app.route('/related_posts/')
def related_posts():
    return render_template('related_posts.html')


#redirect links

# @app.route('/redirect_me0')
# def redirect_me0():
#     return redirect(url_for('home'))
#
# @app.route('/redirect_me1')
# def redirect_me1():
#     return redirect(url_for('about'))
#
# @app.route('/redirect_me2')
# def redirect_me2():
#     return redirect(url_for('blogs'))
#
# @app.route('/redirect_me3')
# def redirect_me3():
#     return redirect(url_for('contact'))
#
# @app.route('/redirect_me4')
# def redirect_me3():
#     return redirect(url_for('related_posts'))

if __name__ == '__main__':
    app.run(debug=True)