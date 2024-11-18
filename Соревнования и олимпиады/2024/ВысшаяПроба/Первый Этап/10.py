from flask import Flask, request

file = open("input.txt")
app = Flask(__name__)


feromons = file.readline().split()
file.close()
feromon_data = {feromons[i]: i + 1 for i in range(len(feromons))}


def get_feromon(characters: str) -> dict:
    data = {}
    for f in set(characters):
        data[f] = feromon_data.get(f, 0) * characters.count(f)
    return max(data, key=data.get)


@app.route('/feromon', methods=["GET"])
def handle_feromon(*args, **kwargs):
    line = request.args.get("line")
    return get_feromon(line)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')