from flask import Flask, render_template, request
app = Flask(__name__)#Экземпляр приложения flask


@app.route('/')#Обозначение, что функция будет отвечать на веб запросы
@app.route('/index')
def index():
    return render_template("index.html")#Импорт html файла


@app.route('/', methods=['post', 'get'])
def form():
    if request.method == 'POST':
        sum = int(request.form.get('num_1'))
        type = request.form['options']
    if type == '1':#Доллар
        answer=sum*80.06
        return render_template('index.html', ans= str(str(sum)+" Рублей - " + str(answer) +" Доллар"))
    if type == '2':#Евро
        answer = sum * 85.9
        return render_template('index.html', ans=str(str(sum) + " Рублей - " + str(answer) + " Евро"))
    if type == '3':  # Доллар
        answer = sum / 80.06
        return render_template('index.html', ans=str(str(sum) + " Доллар - " + str(answer) + " Рублей"))
    if type == '4':  # Евро
        answer = sum / 85.9
        return render_template('index.html', ans=str(str(sum) + " Евро - " + str(answer) + " Рублей"))
    elif type != '1':
        return render_template('index.html', ans='Выберите валюту!')

if __name__ == '__main__':
    app.run()