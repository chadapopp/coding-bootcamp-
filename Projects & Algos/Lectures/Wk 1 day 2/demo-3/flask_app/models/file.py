from flask_app.config.mysqlconnection import connectToMySQL

class File:
    DB = "gallery"
    def __init__(self, file_dict):
        self.id = file_dict["id"]
        self.file_name = file_dict["file_name"]
        self.size = file_dict["size"]
        self.extension = file_dict["extension"]
        self.user_id = file_dict["user_id"]
        self.created_at = file_dict["created_at"]
        self.updated_at = file_dict["updated_at"]

    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO files (file_name, size, extension, user_id) VALUES (%(file_name)s, %(size)s, %(extension)s, %(user_id)s)"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result
        