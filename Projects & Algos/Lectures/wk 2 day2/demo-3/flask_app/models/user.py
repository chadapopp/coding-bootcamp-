from flask_app.config.mysqlconnection import connectToMySQL

class User:
    DB = "gallery"
    def __init__(self, user_dict):
        self.id = user_dict["id"]
        self.email = user_dict["email"]
        self.user_name = user_dict["user_name"]
        self.password = user_dict["password"]
        self.created_at = user_dict["created_at"]
        self.updated_at = user_dict["updated_at"]

        self.files = []

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email=%(email)s"
        result = connectToMySQL(cls.DB).query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users"
        result = connectToMySQL(cls.DB).query_db(query)
        users = []
        for user_dict in result:
            users.append(cls(user_dict))

        return users
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (email, user_name, password) VALUES (%(email)s, %(user_name)s, %(password)s)"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result
        