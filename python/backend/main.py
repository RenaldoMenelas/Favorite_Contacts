import pandas as pd

from flask import request, jsonify
from config import app, db
from models import Contact

@app.route("/contacts", methods=['GET'])
def get_contacts():
    contacts = Contact.query.all()
    json_contacts = list(map(lambda x:x.to_json(), contacts))
    return jsonify({'contacts': json_contacts})

@app.route("/create_contact", methods = ['POST'])
def create_contact():
    first_name = request.json.get('firstName')
    last_name = request.json.get('lastName')
    email = request.json.get('email')


    if not first_name or not last_name or not email:
        return(
              jsonify({"message": "include, firstname, lastname, email"}),
              400,
        ) 
    new_contact = Contact(first_name = first_name, last_name = last_name, email = email)
    try:
        db.session.add(new_contact)
        db.session.commit()

    except Exception as e:
        return  jsonify({"message":"Failed to create user due to an error: "  + str(e)}), 400

    return jsonify({'message':"user created"}),201

@app.route('/update_contact/<int:user_id>', methods = ['PATCH'])
def update_contact(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({'messsage': "user not found"})

    data = request.json
    contact.first_name = data.get('firstName', contact.first_name)
    contact.last_name = data.get('lastName', contact.last_name)
    contact.email = data.get('email', contact.email)

    db.session.commit()

    return jsonify({'message': "uesr updated"}),200


@app.route('/delete/<int:user_id>', methods =['DELETE'])
def delete_Contact(user_id):
    contact = Contact.query.get(user_id)
    if not contact:
        return jsonify({'messsage': "user not found"})

    db.session.delete(contact)
    db.session.commit()

    return jsonify({'message':'user deleted'})


if __name__ == '__main__':
   # intialze our db
    with app.app_context(): ## cresste models if dont exsist
        print("Creating tables...")
        db.create_all()
        print("Tables should be created.")
    app.run(debug=True)


#df = pd.read_csv('cereal.csv')
#print(df.info())

#df = pd.read_csv('people-10000.csv')
#print(df.info())