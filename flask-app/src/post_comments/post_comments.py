from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

post_comments = Blueprint('Post_Comments', __name__)

# post comments on posts 
@post_comments.route('/Post_Comments', methods=['POST'])
def add_new_comments():
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    commentID = the_data['commentID']
    comment = the_data['comment']
    commenterID = the_data['commenterID']
    postID = the_data['postID']

    # Constructing the query
    query = 'insert into Post_Comments (commentID, comment, commenterID, postID) values ('
    query += str(commentID) + ', "'
    query += comment + '", '
    query += str(commenterID) + ', '
    query += str(postID)  + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'


### Get all post comments of a post 
@post_comments.route('/Post_Comments/<postID>', methods = ['GET'])
def get_post_comment_detail(postID):

    query = 'SELECT * FROM Post_Comments WHERE postID = ' + str(postID)
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    the_data = cursor.fetchall()
    for row in the_data:
        json_data.append(dict(zip(column_headers, row)))
    return jsonify(json_data)
    
@post_comments.route('/Post_Comments', methods=['PUT'])
def update_comment():
    the_data = request.json
    
    commentID = the_data['commentID']
    comment = the_data['comment']
    replyingTo = the_data['replyingTo']
   
    query = 'UPDATE Post_Comments SET comment = %s, replyingTo = %s WHERE commentID = %s'
    
    current_app.logger.info(f'Preparing to update comment with ID {commentID}')
    
    cursor = db.get_db().cursor()
    cursor.execute(query, (comment, replyingTo, commentID))
    db.get_db().commit()
    return 'Success!'


# Delete post comments for a particular comment ID
@post_comments.route('/Post_Comments/', methods=['DELETE'])
def delete_comment ():
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    commentID = the_data['commentID']

    cursor = db.get_db().cursor()
    cursor.execute('DELETE from Post_Comments where commentID = ' + str(commentID))
    db.get_db().commit()
    return 'Post comment has been deleted!'