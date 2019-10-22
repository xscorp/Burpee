import requests

def parse_request(file_name):
	line = ""
	headers = {}
	post_data = ""
	header_collection_done = False
	file_object = open(file_name , "r")
	file_object.seek(0)
	file_object.readline()
	for line in file_object.readlines():
		if header_collection_done is False:
			if line.startswith("\n"):
				header_collection_done = True
			else:
				headers.update({
					line.split(":")[0].strip() : line.split(":")[1].strip()
				})
		else:
			post_data = post_data + line
	file_object.close()
	return (headers , post_data)

def dump_headers(file_name):
	headers , post_data = parse_request(file_name)
	for header , value in headers.items():
		print(header , ": " , value , sep = "")

def dump_data(file_name):
	headers , post_data = parse_request(file_name)
	print(post_data)

def get_method_and_resource(file_name):
    file_object = open(file_name , "r")
    request_line = file_object.readline()
    file_object.close()
    request_line = request_line.split(" ")
    method_name = request_line[0]
    if request_line[1].startswith("/"):
	    resource_name = request_line[1]
    else:
	    resource_name = request_line[1][request_line[1].find("/"):]
    return method_name , resource_name

def request(file_name , https = False , proxies = None):
	headers , post_data = parse_request(file_name)
	method_name , resource_name = get_method_and_resource(file_name)
	protocol = "https" if (https is True) else "http"
	url = protocol + "://" + headers["Host"] + resource_name
	if method_name.lower() == "get":
		response = requests.get(url = url , headers = headers , proxies = proxies , verify = False)
	elif method_name.lower() == "post":
		response = requests.post(url = url , headers = headers , data = data , proxies = proxies , verify = False)
	return response

