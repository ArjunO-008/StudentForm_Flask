from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit",methods=["POST"])
def showRespone():

    studentID = request.form["studentID"]
    username = request.form["username"]
    department = request.form["department"]
    studentClass = request.form["studentClass"]
    phoneNo = request.form["phoneNo"]

    return render_template("data.html",
                           studentID=studentID,
                           username=username,
                           studentClass=studentClass,
                           department=department,
                           phoneNo=phoneNo)
    


if __name__ == "__main__":
    app.run(debug=True)
