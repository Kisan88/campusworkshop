"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgpqqr8u9tun42u4i8c0-a",
        database="betsol_todo",
        user="betsol_todo_user",
        password="2rfW8xu6CGIx6u4p2hhx8sMMw0p8i8I1")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
