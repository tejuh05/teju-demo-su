import joblib
from flask import Flask, request, render_template
from sklearn.neighbors import KNeighborsClassifier

app = Flask(__name__)

X = [[20], [30], [40], [50], [65], [70]]
Y = ["yes", "no", "yes", "no", "yes", "no"]

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, Y)
joblib.dump(knn, "knn_model.pkl")
@app.route("/", methods=["GET", "POST"])
def homepage():
    prediction = None
    name = "Sonali"

    if request.method == "POST":
        num = request.form.get("number")
        t1 = request.form.get("t1")

        if t1:
            name = t1

        if num:
            try:
                num = float(num)
                prediction = knn.predict([[num]])[0]
            except:
                prediction = "Only numbers allowed!"

    return render_template("index.html", fname=name, prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
