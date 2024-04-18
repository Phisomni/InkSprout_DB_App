
from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


writing_assistants = Blueprint('writing_assistants', __name__)

@writing_assistants.route('/writing_assistants', methods=['GET'])
def get_all_wa():
    cursor = db.get_db().cursor()
    cursor.execute('select empID, experience, asstName from Writing_Assistants')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


@writing_assistants.route('/writing_assistants', methods=['PUT'])
def update_experience():
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    empID = the_data['empID']
    experience = the_data['experience']
    # Constructing the query
    
    query = "UPDATE Writing_Assistants SET experience = %s where empID = %s"
    data = (experience,empID)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query,data)
    db.get_db().commit()
    
    return 'Success!'

@writing_assistants.route('/edits/<asstName>', methods=['GET'])
def get_post_edit_info(asstName):
    cursor = db.get_db().cursor()
    cursor.execute('select postID,editID,edit from edits where asstName = {0}'.format(asstName))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response









