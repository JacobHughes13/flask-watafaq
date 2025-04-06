from flask import Flask, render_template, url_for
import json
from random import choice

app = Flask(__name__)


@app.route('/')
@app.route('/index/<title>')
def index(title: str = "Добро пожаловать") -> str:
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof: str) -> str:
    return render_template('training.html', prof=prof)


@app.route('/list_prof/<list_type>')
def list_prof(list_type: str) -> str:
    professions = [
        "Инженер-механик", "Инженер-строитель", "Астроном", "Биолог",
        "Геолог", "Химик", "Программист", "Робототехник",
        "Медик", "Пилот", "Связист", "Штурман"
    ]
    return render_template('list_prof.html', title="Профессии", list_type=list_type, professions=sorted(professions))


@app.route('/answer')
@app.route('/auto_answer')
def auto_answer() -> str:
    '''data = {
        "title": input(),
        "surname": input(),
        "name": input(),
        "education": input(),
        "profession": input(),
        "sex": input(),
        "motivation": input(),
        "ready": input()
    }'''
    data = {
        "title": "Ответ на анкету",
        "surname": "Иванов",
        "name": "Иван",
        "education": "Высшее",
        "profession": "Инженер-исследователь",
        "sex": "мужской",
        "motivation": "Хочу построить новую цивилизацию",
        "ready": "Да"
    }
    return render_template("auto_answer.html", **data)


@app.route('/login', methods=['GET', 'POST'])
def login() -> str:
    return render_template('login.html', title="Аварийный доступ")


@app.route('/distribution')
def distribution() -> str:
    astronauts = [
        "Иванов Иван", "Петров Петр", "Сидоров Сидор",
        "Андреева Анна", "Кузнецов Николай", "Васильева Мария"
    ]
    return render_template("distribution.html", title="Распределение по каютам", astronauts=astronauts)


@app.route('/member')
def member() -> str:
    with open("templates/crew.json", encoding="utf-8") as f:
        crew = json.load(f)
    return render_template("member.html", title="Экипаж", member=choice(crew))


def main() -> None:
    app.run(port=8080, host='127.0.0.1', debug=True)


if __name__ == "__main__":
    main()