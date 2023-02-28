from flask import Flask, render_template, request, url_for, flash, session, redirect, abort
from fldb import Database
app = Flask(__name__)

#Подключение к БД, создание таблиц
db = Database("test.db")
db.create_table('users', ['id INTEGER', 'username TEXT', 'psw TEXT'])
if not len(db.select_data('users', '*', 'username = "EvstiAl"')):
    db.insert_row('users', '(2, "EvstiAl", "123123")')

db.create_table('posts', ['title TEXT','content TEXT']) 
if not len(db.select_data('posts', '*', 'title = "WP"')):
    db.insert_row('posts', '("WP", "Дима Даня в домике")')

app.config['SECRET_KEY'] = 'qwerty1234' #секретный ключ для шифрования

@app.route('/') #Начальная вкладка
def html():
    return render_template('index.html') 

@app.route('/author') #Вкладка входа в систему
def about():
    return render_template('author.html')

@app.route('/lastsetup') #Вкладка с новостью. В дальнейшем доработать с автодобавлением
def news():
    return render_template('lastsetup.html')
@app.route('/free')
def free():
    return render_template('lastsetup.html')

@app.route('/education')
def edu():
    return render_template('lastsetup.html')

@app.route('/forum_main')
def forum():
    return render_template('main-forum.html')

@app.route('/profile/<username>')
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)
    return f'Юзверь: {username}'


@app.errorhandler(404)
def pageNotFount(error):
    return render_template('page404.html', title='Страница не найдена')

@app.route('/login', methods= ['POST', 'GET'])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    print(request.form)
    if request.method == 'POST' and len(db.select_data('users', '*', f'id = "{request.form["id"]}" AND username = "{request.form["username"]}" AND psw = "{request.form["psw"]}"')):
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged'])) 

    return render_template('login.html')
@app.route('/article/new', methods=['GET', 'POST'])
def new_article():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        db.insert_row('posts', f'("{title}","{content}")')
        return redirect(url_for('index'))
    return render_template('new_article.html')
print(db.select_data('posts', '*', 'title = 1'))
@app.route("/post/<name_post>", methods=['GET'])
def showPost(name_post):
    if request.method == 'GET':
        title, content = db.select_data('posts', '*', f'title = {name_post}')[0]
        if not title:
            abort(404)
        return render_template('post.html', title=title, content=content)

if __name__ == '__main__':
#    from waitress import serve
#    serve(app, host="0.0.0.0", port=8080)
    app.run(debug=True) #True для разработки, чтобы видеть ошибки на сайте. False - для пользователей.

#http://localhost:8080