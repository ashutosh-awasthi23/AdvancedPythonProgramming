from flask import Flask, render_template, request, redirect, url_for,session

app_p = Flask(__name__)
app_p.secret_key="secret"

@app_p.route('/')
def home():
    return render_template("product.html")

@app_p.route('/home',methods=['POST'])
def home1():
    session["productname"]=request.form["productname"]
    session["quantity"]=request.form["quantity"]

    return redirect(url_for("shipping_details"))

@app_p.route('/shipping_details')
def shipping_details():
    return render_template("shipping_details.html")

@app_p.route('/shipping_details',methods=["POST"])
def shipping_details1():
    session["name"] = request.form["name"]
    session["address"] = request.form["address"]
    session["contact"] = request.form["contact"]
    return render_template("order_summary.html")

@app_p.route('/order_summary')
def order_summary():
    name= session.get("name")
    address=session.get("address")
    contact=session.get("contact")
    productname=session.get("productname")
    quantity=session.get("quantity")
    return render_template("order_summary.html", productname=productname, address=address, contact=contact, name=name, quantity=quantity)


if __name__ == "__main__":
    app_p.run(port=5001)

