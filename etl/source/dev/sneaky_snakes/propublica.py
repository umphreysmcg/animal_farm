import requests
from .util import write_json



def senators():
    headers = {'X-API-Key': 'pD2tLve7Gd8KDdfPVE6eO7mveJyNxLip6ZGwdK0j'}
    urls = ['https://api.propublica.org/congress/v1/'+str(num)+'/senate/members.json' for num in range(1,116)]

    for url in urls:
        r = requests.get(url=url, headers=headers)
        write_json(r.text, '/var/tmp/propublica/senators'+str(urls.index(url)+1)+'.json')
