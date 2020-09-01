from bs4 import BeautifulSoup
import requests
site ="https://www.instagram.com/{}/"
try:
    def parse(soup_obj):
        stats = {}
        soup_obj = soup_obj.split("-")[0]
        soup_obj = soup_obj.split(" ")
        stats['Followers'] = soup_obj[0]
        stats['Following'] = soup_obj[2]
        stats['Posts'] = soup_obj[4]
        return stats

    def scrape(un):
        req=requests.get(site.format(un))
        soup_obj = BeautifulSoup(req.text, "html.parser")
    #print (s)
        meta = soup_obj.find("meta", property="og:description" )
    #print (s)
        return parse(meta.attrs['content'])
    
    if __name__=="__main__":
        un = input("Enter un: ")
        stats=scrape(un)
        print("This acc has",stats['Followers'], "followers")
        print("this acc follows ", stats['Following'], "people")
        print ("this acc has", stats['Posts'],"posts")
except Exception as e:
    print ("Username not found")
