import requests

url = "http://127.0.0.1:5000/image"
file_path = "cm_api/utils/testing_images/saviour.jpg"

with open(file_path, "rb") as file:
    files = {'image': file}
    data = {'n_colors': 4}
    response = requests.post(url, files=files, data=data)

print(file)
print(response.text)