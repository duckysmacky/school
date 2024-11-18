from flask import Flask, abort

app = Flask(__name__)

days = {"Mon": 1, "Tue": 2, "Wed": 3, "Thu": 4, "Fri": 5}
schedule = {}
teachers = {}

def add_lecture(weekday: str, subject: str, name: str) -> bool:
    if len(schedule.get(weekday, [])) >= 3:
        return False
    schedule[weekday] = schedule.get(weekday, []) + [{"subject": subject, "name": name}]
    teachers[name] = teachers.get(name, []) + [[weekday, subject]]
    return True


def get_teacher(name: str) -> list:
    if name not in teachers:
        return None
    data = sorted(set(map(tuple, teachers[name])), key=lambda x: [days[x[0]], x[1]])
    return data


@app.route("/add/<weekday>/<subject>/<name>")
def handle_add(weekday, subject, name):
    if add_lecture(weekday, subject, name):
        return f"{weekday}, {subject}, {name}"
    else:
        return "FAIL"


@app.route("/get/<name>")
def handle_get(name):
    data = get_teacher(name)
    if data == None:
        return abort(404)
    else:
        return data    


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')