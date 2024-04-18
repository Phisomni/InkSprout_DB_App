
from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


moderators = Blueprint('moderators', __name__)

@moderators.route('/moderators', methods=['GET'])
def get_all_moderators():
    cursor = db.get_db().cursor()
    cursor.execute('select empID, experience, modName from Moderators')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@moderators.route('/moderators/<empID>', methods=['PUT'])
def update_experience(empID):
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    empID = the_data['empID']
    experience = the_data['experience']
    # Constructing the query
    
    query = "update Moderators set experience = %s where empID = %s"
    data = (experience,empID)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query,data)
    db.get_db().commit()
    
    return 'Success!'

@moderators.route('moderators/<empID>',methods= ['DELETE'])
def delete_moderator(empID):
    the_data = request.json
    current_app.logger.info(the_data)

    query = 'delete from moderators where empID = {0}'.format(empID)
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'
