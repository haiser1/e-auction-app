import logging
from cloudinary.uploader import upload


def upload_to_cloudinary(image):
    try:
        response = upload(image)
        return response['secure_url']
    except Exception as e:
        logging.error("Error uploading to Cloudinary", exc_info=True)
        print(e)
        return None
