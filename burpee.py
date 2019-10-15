import requests

def parse_request(file_object):
	line = ""
	headers = {}
	post_data = ""
	header_collection_done = False
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
