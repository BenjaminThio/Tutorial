import requests

response = requests.get("https://d1yjjnpx0p53s8.cloudfront.net/styles/logo-thumbnail/s3/042018/untitled-2_285.png?.o.pn7QJeX15laHMgU2zT30uWoj2Jmsx&itok=cHBhvP5s")
with open("Image.jpg", "wb") as file:
    file.write(response.content)