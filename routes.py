from app import app, db, bcrypt, jwt
from flask import jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models import User, Note

def user_routes(app):
    @app.route('/register', methods=['POST'])
    def register():
        if request.method == 'POST':
            data = request.json

            username = data.get('username')
            email = data.get('email')
            password = data.get('password')

            if username and email and password:
                hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
                new_user = User(username=username, email=email, password=hashed_password)
                db.session.add(new_user)
                db.session.commit()

                access_token = create_access_token(identity={'id': new_user.id})

                response = jsonify({'message': 'User created successfully', 'access_token': access_token})
                response.status_code = 201
                return response
            else:
                return jsonify({'error': 'Missing data'}), 400

    @app.route('/login', methods=['POST'])
    def login():
        if request.method == 'POST':
            data = request.json
            email = data.get('email')
            password = data.get('password')

            if email and password:
                user = User.query.filter_by(email=email).first()

                if user and bcrypt.check_password_hash(user.password, password):
                    access_token = create_access_token(identity={'id': user.id})

                    response = jsonify({'message': 'Login successful', 'access_token': access_token})
                    response.status_code = 200
                    return response
                else:
                    return jsonify({'error': 'Invalid username or password'}), 401
            else:
                return jsonify({'error': 'Missing data'}), 400
            
    @app.route('/user', methods=['DELETE'])
    @jwt_required()  # L'utilisateur doit être authentifié pour supprimer son propre compte
    def delete_user():
        current_user = get_jwt_identity()
        user = User.query.filter_by(id=current_user['id']).first()

        if user:
            Note.query.filter_by(user_id=current_user['id']).delete()

            db.session.delete(user)
            db.session.commit()

            response = jsonify({'message': 'User deleted successfully'})
            response.status_code = 200
            return response
        else:
            return jsonify({'error': 'User not found'}), 404

def note_routes(app):
    @app.route('/note', methods=['POST'])
    @jwt_required()
    def create_note():
        current_user = get_jwt_identity()
        data = request.json

        title = data.get('title')
        content = data.get('content')

        if title and content:
            new_note = Note(title=title, content=content, user_id=current_user['id'])

            db.session.add(new_note)
            db.session.commit()

            response = jsonify({'message': 'Note created successfully'})
            response.status_code = 201
            return response
        else:
            return jsonify({'error': 'Missing data'}), 400

    @app.route('/note', methods=['GET'])
    @jwt_required()
    def get_notes():
        current_user = get_jwt_identity()
        user_notes = Note.query.filter_by(user_id=current_user['id']).all()

        notes_list = []
        for note in user_notes:
            notes_list.append({
                'id': note.id,
                'title': note.title,
                'content': note.content,
                'created_at': note.created_at,
                'modified_at': note.modified_at
            })

        return jsonify({'notes': notes_list})

    @app.route('/note', methods=['PUT'])
    @jwt_required() 
    def update_note():
        current_user = get_jwt_identity()
        data = request.json

        note_id = data.get('note_id')
        title = data.get('title')
        content = data.get('content')

        note = Note.query.filter_by(id=note_id, user_id=current_user['id']).first()

        if note: 
            if title is not None:
                note.title = title
            if content is not None:
                note.content = content

            note.modified_at = db.func.current_timestamp()

            db.session.commit()

            response = jsonify({'message': 'Note updated successfully'})
            response.status_code = 200
            return response
        else:
            return jsonify({'error': 'Note not found or does not belong to the current user'}), 404

    @app.route('/note', methods=['DELETE'])
    @jwt_required()  # L'utilisateur doit être authentifié pour supprimer une note
    def delete_note():
        current_user = get_jwt_identity()

        data = request.json
        note_id = data.get('note_id')

        note = Note.query.filter_by(id=note_id, user_id=current_user['id']).first()

        if note:
            db.session.delete(note)
            db.session.commit()

            response = jsonify({'message': 'Note deleted successfully'})
            response.status_code = 200
            return response
        else:
            return jsonify({'error': 'Note not found or does not belong to the current user'}), 404
