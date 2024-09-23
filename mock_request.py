import requests

url = "http://127.0.0.1:5000/image"
file_path = "api/utils/testing_images/Untitled.jpg"

with open(file_path, "rb") as file:
    files = {'image': file}
    response = requests.post(url, files=files)

print(file)
print(response.text)