"""Схема josn для метода create user"""
schema_create_user ={
    "data": {
    "id": 0,
    "email": "string",
    "first_name": "string",
    "last_name": "string",
    "avatar": "string"
    }
}

"""Схема josn для метода update_user"""
schema_update_user = {"updatedAt": "string"}

"""Схема josn для метода register"""
schema_register = {
  "username": "string",
  "email": "string",
  "password": "string"
}

schema_get_user_list = {
  "page": 0,
  "per_page": 0,
  "total": 0,
  "total_pages": 0,
  "data": [
    {
      "id": 0,
      "name": "string",
      "year": 0,
      "color": "string",
      "pantone_value": "string"
    }
  ]
}