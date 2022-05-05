from http.client import REQUEST_HEADER_FIELDS_TOO_LARGE
import requests
import hashlib
import json
import sys

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

def upload(address, filename):

    # will need to be an arg
    #filename = "LoaderDemo4.xlsm"

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
    r = requests.post(address, headers=request_headers, files=files)
    print(r.status_code)
    print(r.text)


def download(address, fileid):

    address = address + 'download?id=' + fileid

    print("Sending download request to: %s" % address)

    params = { "id": fileid }
    r = requests.get(address, params=params)

    print(r.status_code)
    filename = fileid + ".pdf"

    with open(filename, "wb") as report:
        report.write(r.content)


def query(address, filename):

    address = address + 'query'
    filehash = hashlib.md5(open(filename, 'rb').read()).hexdigest()
    print("%s hash %s" % (filename, filehash))

    key = getKey()
    request_headers = { 'Authorization': key }
    requestnot = { "file_name": filename, "md5": filehash, "features": ["av", "te"] }
    request = { "request": [ requestnot ]}

    r = requests.post(address, data=json.dumps(request), headers=request_headers)
    print(r.status_code)
    #print(r.text)
    pretty = json.dumps(r.json(), indent=2)
    print(pretty)


    # Turn response into dictionary
    response = json.loads(r.text)
    # bad response formatting from service... fixing it
    response = response["response"]
    # most likely because you can query multiple file_names at once? Deserialize ...
    response = response[0]
    #print(type(response))
    #print(response)
    #print (type(response))

    #print (response.keys())

#   av_response = response["av"]["status"]["label"]
#   print("AV verdict: %s" % av_response)
#   combined_verdict = response["te"]["combined_verdict"]
#   print("Emulation verdict: %s" % combined_verdict)


    

def quota(address):


    address = address + 'quota'
    print("POST: " + address)
    key = getKey()
    request_headers = { 'Authorization': key }
    r = requests.post(address, headers=request_headers)
    print(r.status_code)
    print(r.text)


def main():

    args = len(sys.argv)

    if args > 3 or args < 2:
        print("Usage: python3 threatcloud.py query|upload|quota file")
        return None

    address = 'https://te.checkpoint.com/tecloud/api/v1/file/'
    
    #quota(address)
    #post(address, 'query', None)
    #post(address, 'upload', None)
    #post(address, 'download', None)

    #upload_av(address)

    if args == 2 and sys.argv[1] == 'quota':
        quota(address)
        return None

    command, filename = sys.argv[1], sys.argv[2]

    if command == 'query':
        query(address, filename)
    if command == 'upload':
        upload(address, filename)

    if command == 'download':

        download(address, filename)
        # filename is actually the ID Lol
    


if __name__ == '__main__':

    main()
