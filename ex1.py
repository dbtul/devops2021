from jenkinsapi.jenkins import Jenkins

def get_server_instance():
    jenkins_url = 'http://dbtul.com:8080'
    server = Jenkins(jenkins_url, username='admin', password='Rock2Roll')
    return server

if __name__ == '__main__':
    print (get_server_instance().version)