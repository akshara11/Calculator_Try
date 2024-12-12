from flask import Flask, render_template, redirect, request

from pymongo import MongoClient
my_client = MongoClient("localhost",port=27017)
my_db = my_client["Cal_Res"]
my_coll = my_db["Results"]

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def frontend():
    if request.method == "POST":
        n1 = int(request.form["num1"])
        op = request.form["operator"]
        n2 = int(request.form["num2"])
        if op == "add":
            res = f"{n1} + {n2} = {n1+n2}"
            my_coll.insert_one({"Number1":n1,"Number2":n2,"operator":op,"ouput":res})
            return render_template("index.html", output = res)
        elif op == "sub":
            res = f"{n1} - {n2} = {n1-n2}"
            my_coll.insert_one({"Number1":n1,"Number2":n2,"operator":op,"ouput":res})
            return render_template("index.html", output = res)
        elif op == "mul":
            res = f"{n1} x {n2} = {n1*n2}"
            my_coll.insert_one({"Number1":n1,"Number2":n2,"operator":op,"ouput":res})
            return render_template("index.html", output = res)
        elif op == "div":
            try:
                res = f"{n1} / {n2} = {n1/n2}"
                my_coll.insert_one({"Number1":n1,"Number2":n2,"operator":op,"ouput":res})
                return render_template("index.html", output = res)
            except Exception as e:
                error = "Please type Valid Number"
                return render_template("index.html", output = error)
        elif op == "modu":
            res = f"{n1} % {n2} = {n1%n2}"
            my_coll.insert_one({"Number1":n1,"Number2":n2,"operator":op,"ouput":res})
            return render_template("index.html", output = res)
    else:
        return render_template("index.html")

app.run(debug=True)