import os

import requests
from flask import Flask, request
from flask_restful import Api, Resource

# read url from environment variable
IMAGE_API_URL = os.environ.get("CARNET_URL")

# read cookie from environment variable
CARNET_COOKIE = os.environ.get("CARNET_COOKIE")


class IdentifyVehicleEndpoint(Resource):
    def post(self):
        # read image from request
        image = request.files["image"]
        payload = {}
        image_file_object = (
            (
                image.filename,
                image.stream,
                image.content_type,
            ),
        )
        files = [("imageFile", image_file_object)]
        headers = {"Cookie": CARNET_COOKIE}

        response = requests.request(
            "POST", IMAGE_API_URL, headers=headers, data=payload, files=files
        )

        print(response.text)
        return response.json()


class MapEndpoint(Resource):
    def post(self):
        return {"message": "Map endpoint"}


# add health check endpoint
class HealthCheckEndpoint(Resource):
    def get(self):
        return {"message": "OK"}


app = Flask(__name__)
api = Api(app)

api.add_resource(IdentifyVehicleEndpoint, "/identify_vehicle")
api.add_resource(MapEndpoint, "/map")
api.add_resource(HealthCheckEndpoint, "/health")

if __name__ == "__main__":
    app.run(debug=True)
