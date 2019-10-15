def parse_request(file_name):
	line = ""
	headers = {}
	post_data = ""
	header_collection_done = False
	file_object = open(file_name , "r")
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
	return headers , post_data

def dump_headers(file_object):
	headers , post_data = parse_request(file_object)
	for header , value in headers.items():
		print(header , ": " , value , sep = "")

def dump_data(file_object):
	headers , post_data = parse_request(file_object)
	print(post_data)

