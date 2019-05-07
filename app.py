from flask import Flask, render_template, request, make_response
app = Flask(__name__)

@app.route('/')
def index():
    search = request.args.get('search')
    video = request.args.get('video')
    # if not search:
    #     return render_template('index.html')
    # if not video:
    #     # return 'hasil search adalah ' + search
    #     return render_template('index.html', search=search)

    return render_template('index.html', search=search, video=video)
    # return 'hasil search adalah ' + search + ' video nya adalah ' + video

@app.route('/setting')
def show_setting():
    return 'ini adalah halaman setting'

@app.route('/profile/<username>')
def show_profile(username):
    return render_template('profile.html', username=username)

@app.route('/blog/<int:blog_id>')
def show_blog(blog_id):
    return 'ini adalah halaman blog %s' % blog_id

@app.route('/login', methods=['GET', 'POST'])
def show_login():
    if request.method == 'POST':
        resp = make_response('Email adalah : ' + request.form['email'])
        resp.set_cookie('email_user', request.form['email'])
        return resp

    return render_template('login.html')

@app.route('/getcookie')
def getCookie():
    email = request.cookies.get('email_user')
    return 'Email yang tersimpan di cookie adalah ' + email