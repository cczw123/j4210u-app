import requests

url = 'https://www.songshujuran.com/record'
form_data = {'key': 'p_mnMjRY9cgzNIJsLEWZyjdrKOSDtXsb1raHXU','id':'a'}
server = requests.post(url, data=form_data)
output = server.text
print(output)