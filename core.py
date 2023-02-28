from flask import Flask, render_template
app = Flask(__name__)

class Sites():
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


if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
    app.run(debug=True) #True для разработки, чтобы видеть ошибки на сайте. False - для пользователей.

#http://localhost:8080