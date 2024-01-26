from flask import Blueprint
from flask import render_template, redirect, url_for, request, session, jsonify
from flask_login import login_user, logout_user, current_user
from app.master import bp
from app.master.model import City , CitySchema
from app import db, ma


# Emp. Cat Master Routes


@bp.route('/get/city', methods=['GET'])
def get_city():
    print("Inside get_city route")
    try:
        if request.method == 'GET':
            data_schema = CitySchema(many=True)
            data = City.query.all()
            json_data = data_schema.dump(data)
            print("JSON data:", json_data)
            return jsonify(json_data)
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": "An error occurred"}), 500

# def get_city():
#     if request.method == 'GET':
#         print("hello")
#         data_schema = CitySchema(many=True)
#         print("hello1")
#         data = City.query.all()
#         print("hello2")
#         json_data = data_schema.dump(data)
#         print("hello3")
#         return jsonify(json_data)

# @bp.route('/get/city', methods=['GET'])
# def get_city():
#     print("Inside get_city route")
#     try:
#         if request.method == 'GET':
#             data = City.query.all()
#             data_list = [{'id': city.id, 'name': city.name} for city in data]
#             json_data = jsonify(data_list)
#             print("JSON data:", json_data)
#             return json_data
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return jsonify({"error": "An error occurred"}), 500
# def get_city():
#     print("Inside get_city route")
#     try:
#         if request.method == 'GET':
#             data_schema = CitySchema(many=True)
#             data = City.query.all()
#             print("Data from the database:", data)
#             data_list = [{'id': city.id, 'name': city.name} for city in data]
#             json_data = jsonify(data_list)
#             print("heyy",json_data )
#             json_data = data_schema.dump(data)
#             print("JSON data:", json_data)
#             return jsonify(json_data)
        
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return jsonify({"error": "An error occurred"}), 500


@bp.route('/add/city', methods=['POST'])
def add_city():
    if request.method == 'POST':
        payload = request.json
        if payload['name'] is not None:

            check_data = City.query.filter_by(name=payload['name'])
            if check_data.first():
                return jsonify({'message': 'City - '+check_data.first().name+' already exists.'})
            else:
                try:
                    new_data = City(payload['name'])
                    db.session.add(new_data)
                    db.session.commit()
                    return jsonify({'success': 'Data Added'})

                except Exception as e:
                    db.session.rollback()
                    db.session.close()
                    return jsonify({'message': 'Something unexpected happened. Check logs', 'log': str(e)})
        else:
            return jsonify({'message': 'Empty Data.'})

    else:
        return jsonify({'message': 'Invalid HTTP method . Use POST instead.'})


@bp.route('/edit/city', methods=['POST'])
def edit_city():
    if request.method == 'POST':
        payload = request.json
        if payload['name'] is not None:

            check_data = City.query.filter_by(name=payload['name'])
            if check_data.first():
                return jsonify({'message': 'City - '+check_data.first().name+' already exists.'})
            else:
                try:
                    new_data = City.query.filter_by(
                        id=payload['id']).first()
                    new_data.name = payload['name']
                    db.session.commit()
                    return jsonify({'success': 'Data Updated'})

                except Exception as e:
                    db.session.rollback()
                    db.session.close()
                    return jsonify({'message': 'Something unexpected happened. Check logs', 'log': str(e)})
        else:
            return jsonify({'message': 'Empty Data.'})

    else:
        return jsonify({'message': 'Invalid HTTP method . Use POST instead.'})


@bp.route('/delete/city', methods=['POST'])
def delete_city():
    if request.method == 'POST':
        payload = request.json
        check_data = City.query.filter_by(id=payload['id'])
        if check_data.first():
            # if(len(check_data.first().emp_post) != 0):
            #     return jsonify({'message': 'Cannot delete , data being used. '})
            # else:
                try:
                    check_data.delete()
                    db.session.commit()
                    return jsonify({'success': 'Data deleted'})
                except Exception as e:
                    db.session.rollback()
                    db.session.close()
                    return jsonify({'message': 'Something unexpected happened. Check logs', 'log': str(e)})
        else:
            return jsonify({'message': 'Data does not exist.'})

    else:
        return jsonify({'message': 'Invalid HTTP method . Use POST instead.'})
