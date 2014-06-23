from listurls import list_urls
import sys,os

def details(url):
	req_type = 'Request Type : ' + raw_input('Enter Type of Request - ')
	params = 'params : ' + raw_input('Enter parameters {key1:value,key2:value} - ')
	response_type = 'Response Type : ' + raw_input('Enter Type of Response - ')
	response = 'Response : ' + raw_input('Enter Response - ')
	return '\n'.join(['URL : '+url,req_type,params,response_type,response])

project_name = sys.argv[1]
urls = list_urls(project_name)
for url in urls:
	print 'Enter details for '+url
	det = details(url)
	with open(os.path.join(project_name,'documentation'),'a') as doc:
		doc.write(det + '\n\n')
