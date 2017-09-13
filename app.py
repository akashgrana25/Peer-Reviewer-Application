from flask import Flask, request, render_template,Response
import json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/compute", methods=['POST'])
def compute():
    elementList = []
    m = int(request.form['m'])
    n = int(request.form['n'])
    for i in range(0, m):
        elementList.append(i)

    graph = {}
    for i in range(0, m):
        elementList = elementList[1:] + elementList[:1]
        temp = []
        for x in range(1, n + 1):
            temp.append(elementList[x])
        graph[str(elementList[0])] = temp

    result = json.dumps(graph)
    # print(result)
    return result


if __name__ == "__main__":
    app.run()
