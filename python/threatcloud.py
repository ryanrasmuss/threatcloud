import requests

def getKey():
	keyfile = '.threatcloud.key'
	key = ''

	# potential error: FileNotFoundError: [Errno 2] No such file or directory: '.threatcloud.key'
	with open(keyfile, 'r') as f:
		key = f.read()

	f.close()

	return key


def post(address, command, payload):

	address = address + command
	print("POST: " + address)
	return None

def upload_av(address):

	# will need to be an arg
	filename = "file-sample_100kB.doc"

	address = address + 'upload'
	payload = { 'request': { "features": ["av"] } }
	file = { 'request': { "features": ["av"] }, 'file': open(filename, "rb") }

	key = getKey()
	request_headers = { 'Authorization': key, 'Content-Type': 'multipart/form-data'}

	r = requests.post(address, headers=request_headers, data=payload)
	print(r.status_code)
	print(r.text)



def quota(address):


	address = address + 'quota'
	print("GET: " + address)
	key = getKey()
	request_headers = { 'Authorization': key }
	r = requests.get(address, headers=request_headers)
	print(r.status_code)
	print(r.text)


def main():
	address = 'https://te.checkpoint.com/tecloud/api/v1/file/'
	
	#quota(address)
	#post(address, 'query', None)
	#post(address, 'upload', None)
	#post(address, 'download', None)

	upload_av(address)

	print("Hello")


if __name__ == '__main__':
	main()
