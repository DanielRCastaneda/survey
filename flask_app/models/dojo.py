
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_last_survey(cls):
        query = "SELECT * FROM dojos ORDER BY dojos.id  DESC LIMIT 1;"
        results = connectToMySQL('dojo_survey_schemas').query_db(query)
        return Dojo(results[0])
    
    
    @classmethod
    def save(cls,data):
        query = 'INSERT INTO dojos (name, location, language, comment) VALUES (%(name)s,%(location)s,%(language)s, %(comment)s)'
        return connectToMySQL('dojo_survey_schemas').query_db(query, data)
    
    
    @staticmethod
    def validate_info(dojo):
        is_vaild = True
        if len(dojo['name']) < 3:
            flash('Name must be greater than 3 charaters')
            is_vaild = False
        if len(dojo['location']) < 1:
            flash('Location must choosen')
            is_vaild = False
        if len(dojo['language']) < 1:
            flash('Must choose a language')
            is_vaild = False
        if len(dojo['comment']) < 5:
            flash('Comment must have more than 5 charaters')
            is_vaild = False
        return is_vaild