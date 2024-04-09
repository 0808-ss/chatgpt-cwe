from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb
import base64

app = Flask(__name__)

#save uploaded images to the database base64 encoded
#ensure they are jpg images less than 1024kb in size
@app.route('/img/upload')
# def upload_image():
#     img_file = request.files['img']
#     img_name = img_file.filename
#     img_data = img_file.read()
#     img_file.close()
#-copilot next line-
def upload_image():
    img_file = request.files['img']
    img_name = img_file.filename
    img_data = img_file.read()
    img_file.close()

    if img_name.endswith('.jpg') and len(img_data) < 1048576:
        # Encode image data to base64
        img_base64 = base64.b64encode(img_data).decode('utf-8')

        # Save base64 encoded image to database
        connection = MySQLdb.connect(host='localhost', user='root', password='password', database='images_db')
        cursor = connection.cursor()
        cursor.execute("INSERT INTO images (name, data) VALUES (%s, %s)", (img_name, img_base64))
        connection.commit()
        cursor.close()
        connection.close()
        
        return 'Image uploaded successfully!'
    else:
        return 'Invalid image format or size exceeds 1024kb'


