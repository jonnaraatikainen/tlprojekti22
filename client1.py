import requests


r = requests.get('http://172.20.241.9/luedataa_kannasta_groupid_csv.php?groupid=55')
 
with open('jonnandata.csv', 'w') as f:
    f.write(r.text) 
