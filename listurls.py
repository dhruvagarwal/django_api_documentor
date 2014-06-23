import re,os

def list_urls(project_name):
	reg = "r\'\^" + r"(?:[A-z]|[0-9]|\_|/)*"
	reg1 = "r\"\^" + r"(?:[A-z]|[0-9]|\_|/)*"
	#project_name = str(sys.argv[1])
	pro_name = project_name.split('/')
	if project_name[-1] != '/':
		pro_name = pro_name[-1]
	else:
		pro_name = pro_name[-2]
	url_file = open(os.path.join(project_name,pro_name,'urls.py'),'r').read().split('\n')
	urls = []
	for line in url_file:
		if line.strip()!='' and line.split()[0]=='#':
			continue
		l = re.findall(reg,line)
		l1 = re.findall(reg1,line)
		if l != []:
			urls.append(l[0][3:])
		elif l1 !=[]:
			urls.append(l1[0][3:])
		else:
			continue
	return urls