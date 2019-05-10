from flask import (Flask, render_template, request, make_response, session, 
                   url_for, redirect, flash)
import database

app = Flask(__name__)
app.secret_key = '1969903800'

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
        
        # resp = make_response('Email adalah : ' + request.form['email'])
        # resp.set_cookie('email_user', request.form['email'])
        session['email'] = request.form['email']
        flash('anda berhasil login', 'sukses')
        # dataemail = request.form['email']
        # datapassword = request.form['password']
        return redirect(url_for('show_profile', username=session['email']))

    if 'email' in session:
        email = session['email']
        
        if email == "":
            kembali = render_template('login.html', text='kosong bro')
            # kosong = make_response('<script>if (window.confirm("kosong bro")) {window.location.href="http://localhost:5000/login"}</script>')
            return  kembali

        return redirect(url_for('show_profile', username=email))

    return render_template('login.html')

@app.route('/getcookie')
def getCookie():
    email = request.cookies.get('email_user')
    return 'Email yang tersimpan di cookie adalah ' + email

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('show_login'))

# @app.route('/data')
# def data():
#     connection = pymysql.connect(host='localhost', user='root', password='', db='profil')
#     with connection.cursor() as cursor:
#         cursor.execute("SELECT * FROM `posting`")
#         all = cursor.fetchall()
#         print(all)
#         return str(all[0])