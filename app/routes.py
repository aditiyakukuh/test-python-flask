from app import app
from flask import Flask, jsonify, request
from app.models.user import User
from app.controllers.userController import getAllUser, getUserById, addUser, deleteUser, updateUserById

@app.route('/')
@app.route('/index')

def index():
    return "Hello, World! wahawwha"


@app.route('/api/pertama', methods=['GET'])
def get_data():
    data = {
        "nama": "pop mie",
        "harga": 2000
    }
    return jsonify(data)

@app.route('/api/pertama', methods=['POST'])
def add_item():
    # Menerima data JSON dari request
    data = request.json
    
    # Menyimpan data ke dalam variabel
    nama = data['nama']
    harga = data['harga']

    # Membuat dictionary dari data yang diterima
    item = {'nama': nama, 'harga': harga}

    # Mengembalikan data dalam format JSON
    return jsonify(item)

# Mengambil semua data users dari database dan mereturn sebagai JSON
@app.route('/users')
def get_users():
    return getAllUser()

# Mengambil data user dengan id tertentu dari database dan mereturn sebagai JSON
@app.route('/users/<int:id>')
def get_user_by_id(id):
    return getUserById(id)

@app.route('/users', methods=['POST'])
def create_user():
    return addUser()

@app.route('/users/<int:id>', methods=['DELETE'])
def deleteUserById(id):
    return deleteUser(id)

# Route untuk update user by id
@app.route('/users/<int:id>', methods=['PUT'])
def update_user_by_id(id):
    # Mendapatkan request JSON dari client
    request_json = request.get_json()

    # Panggil fungsi dari controller
    response = updateUserById(id, request_json)

    # Mengembalikan response JSON ke client
    return jsonify(response)