import flask
from flask import jsonify ,request
from werkzeug.datastructures import ImmutableMultiDict
import sys
sys.path.append(".")

from Tasks import TaskShooter

app = flask.Flask(__name__)
app.config["DEBUG"] = True
shooter=TaskShooter()


@app.route('/api/tasks',methods=['POST'])
def tasks():
    tasks=request.form
    dicttasks=tasks.to_dict()

    print("*********************************")
    print(dicttasks)
    print("*********************************")
    shooter.Fire(dicttasks)
    # for key in dicttasks:
    #     print(key, '->', dicttasks[key])
        ##########send task name as Key ,values as Value##########

    return "Done"

app.run(host='0.0.0.0',port=5000)
