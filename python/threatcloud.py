from http.client import REQUEST_HEADER_FIELDS_TOO_LARGE
import requests
import json

def getKey():
	keyfile = '.threatcloud.key'
	key = ''

	# potential error: FileNotFoundError: [Errno 2] No such file or directory: '.threatcloud.key'
	with open(keyfile, 'r') as f:
		key = f.read().rstrip('\n')

	f.close()

	return key


def post(address, command, payload):

	address = address + command
	print("POST: " + address)
	return None

def upload_av(address):

	# will need to be an arg
	filename = "LoaderDemo4.xlsm"

	address = address + 'upload'

	request = {"request": { "file_name": filename,
		"te": { "reports": ["pdf", "xml"]} }}

	files = { "file": (open(filename, "rb")), 'request': json.dumps(request)}
	# payload = { "request": { "features": ["te"], "te": {"reports": ["pdf"] }}}
	#payload = { "request": { "features": ["te"], "te": {"reports": ["pdf"] }} }



	key = getKey()
	# request_headers = { 'Authorization': key, 'Content-Type': 'multipart/form-data'}
	request_headers = { 'Authorization': key } 
	
	print("POST %s" % address)
#print("headers: %s " % request_headers)
	#print("Payload: %s " % payload)

	#r = requests.post(address, headers=request_headers, data=payload, files=files)
	r = requests.post(address, headers=request_headers, files=files, verify=False)
	print(r.status_code)
	print(r.text)



def quota(address):


	address = address + 'quota'
	print("POST: " + address)
	key = getKey()
	request_headers = { 'Authorization': key }
	r = requests.post(address, headers=request_headers)
	print(r.status_code)
	print(r.text)


def main():
	address = 'https://te.checkpoint.com/tecloud/api/v1/file/'
	
	quota(address)
	#post(address, 'query', None)
	#post(address, 'upload', None)
	#post(address, 'download', None)

	upload_av(address)

	print("Hello")


if __name__ == '__main__':
	main()
