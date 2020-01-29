from flask import make_response

def req_white_paper():
	binary_pdf = get_binary_pdf_data_from_database('wp')
	response = make_response(binary_pdf)
	response.headers['Content-Type'] = 'application/pdf'
	response.headers['Content-Disposition'] = 'inline; filename=whitepaper.pdf'
	return response
