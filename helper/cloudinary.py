from config import cloudinary
import logging


def upload_to_cloudinary(image):
    try:
        response = cloudinary.uploader.upload(image)
        return response['secure_url']
    except Exception as e:
        logging.error(e)
        return str(e)