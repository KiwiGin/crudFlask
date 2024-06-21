#imports
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from utils.db import db
from models.contacts import Contact
#configuraciones
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/flaskbd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db.init_app(app)

#rutas
@app.route("/")
def home():
    contactos = Contact.query.all()
    return render_template('index.html', contactos=contactos)

@app.route("/add", methods=['POST'])
def contactoNuevo():
    name=request.form['name']
    email=request.form['email']
    phone=request.form['phone']
    newContact=Contact(name,email,phone)
    print(newContact)
    db.session.add(newContact)
    db.session.commit()

    return redirect('/')

#
with app.app_context():
    db.create_all()

if __name__=="__main__":
    app.run(debug=True)