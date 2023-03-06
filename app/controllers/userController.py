from app import app, db
from flask import Flask, jsonify, request
from app.models.user import User

def getAllUser():
    users = User.query.all()
    response = jsonify({'users': [{'id':user.id,'name': user.name, 'phone': user.phone} for user in users]})
    return response

def getUserById(user_id):
    user = User.query.filter_by(id=user_id).first()
    if not user:
        return jsonify({'message': 'User not found'}), 404
    response = jsonify({'user': {'name': user.name, 'phone': user.phone}})
    return response.get_json()

def addUser():
    name = request.json.get('name')
    phone = request.json.get('phone')
    
    if not name :
        return jsonify({'error': 'Please provide name'})
    if not phone :
        return jsonify({'error': 'Please provide phone'})

    user = User(name=name, phone=phone)
    db.session.add(user)
    db.session.commit()

    response = jsonify({'message': 'User added successfully', 'data': {'id': user.id, 'name': user.name, 'phone': user.phone}})
    response.status_code = 201
    return response

def deleteUser(id):
    user = User.query.filter_by(id=id).first()
    if not user:
        return jsonify({'error': 'User not found'})
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User has been deleted'})

def updateUserById(id, request_json):
    # Cari user dengan id yang sesuai
    user = User.query.filter_by(id=id).first()

    # Jika user tidak ditemukan, kirimkan response error
    if not user:
        return {'message': f'User dengan id {id} tidak ditemukan.'}, 404

    # Update data user dengan data dari request
    user.name = request_json.get('name', user.name)
    user.phone = request_json.get('phone', user.phone)

    # Commit perubahan ke database
    db.session.commit()

    # Kirimkan response sukses
    return {
        'message': f'updated user id {id} successfully.',
        'data':{
            'name' : user.name,
            'phont': user.phone
        }
    }, 200