from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression


def model(predict):
    dataset = pd.read_csv("diabetes.csv")
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=0
    )
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)
    classifier = LogisticRegression(random_state=0)
    classifier.fit(X_train, y_train)
    return classifier.predict(sc.transform([predict]))


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/check", methods=["POST"])
def getuser():
    inp1 = request.form["inp1"]
    inp2 = request.form["inp2"]
    inp3 = request.form["inp3"]
    inp4 = request.form["inp4"]
    inp5 = request.form["inp5"]
    inp6 = request.form["inp6"]
    inp7 = request.form["inp7"]
    inp8 = request.form["inp8"]
    input = [
        float(inp1),
        float(inp2),
        float(inp3),
        float(inp4),
        float(inp5),
        float(inp6),
        float(inp7),
        float(inp8),
    ]
    prediction = model(input)
    if prediction[0] == 1:
        text = "Patient has diabetes"
    else:
        text = "Patient dont have diabetes"
    return render_template("index.html", data=text)


app.run(debug=True)
