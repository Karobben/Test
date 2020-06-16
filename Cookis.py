# -*- coding:utf-8 -*-

import requests, time
from bs4 import BeautifulSoup



Git_commit_header = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'en-US,en;q=0.9',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie': '_octo=GH1.1.1014544621.1577848239; _ga=GA1.2.827504913.1577848244; _device_id=ed11c4f75773d5fc016e406e9c214086; user_session=CM8ddn4Nrj0NYAH4n4b5_F_8qN80PPjwgo_YQkd6rMaIOXCb; __Host-user_session_same_site=CM8ddn4Nrj0NYAH4n4b5_F_8qN80PPjwgo_YQkd6rMaIOXCb; logged_in=yes; dotcom_user=Karobben; tz=Asia%2FShanghai; has_recent_activity=1; _gh_sess=ysu447QP0IJQBp1JudaQxWYRtIWOH5KrXjJaDfCIPK0NmWdPb%2B1TqxmNp6iy7HykKiGHeg4QrgM2YVyu4gwxkobgbE063FN6W97%2BzLBfYpxkIOgej0WiloqCMI8wxxZW6YNErpfdR49rY19%2Bq4gvsjncYV5dRViPNOtzqqqtqkzPNeY4o9O49%2F%2FoyUrEAb4lOHFTYcVf5f6Vj4NU4Z88HrqS7yQcNkKXDsfier0P4RvKMSDAj3KJPGvscyob4sAzBq0P%2BP30dKy3KRNunmzf2VQISlZ1pU2wlSL1jvQ%2BcWNz%2BUYBDKqzSVtglKY2TiqrdtgjIaT8JU%2F4sRiBscEbbnLw2aYqS3FZRiLn6zMLUnfFxT5BtiRVtJTfjj9ygWVtlhZ5gQHLQa8oy9LzrIGQw3jwFXW7KUiq%2FWJSH25bDaSYKjxNpjGc54bxsBZXrFmpyRI6I%2FpZgGvwsFpgXz1ogoitU0F5C5baUg468uZjHKik1DBHWoMd5V9Wu73PsKDH66vajQONohlrmvQBijVa8nuSskiKZb79Ir5mLD1rVfl0V4LCg2ddASQfzx0anfO%2FjrELQKVDcDL9k1BsvicLB9nVkI9fCUuxYHq4zJrZ98SwbK725PL5vByxurMOzPahTw6%2FUZ3io1XUREjraJJ2Ey8XmuuowpAFAEgWGSGm2zaNnJSPlL1EPUh6BYTKEeOq3YrEKNg9znmr5PQSegxOBr4cV02JmumlKF6RSEhJtR2Zh9fhfkk4S47HacunhKDdn0FH1IHmKWR2fKz9wkFpU0%2FqG%2BDNVfQZS96brVQfBBmn2G4wkwl7MDemCQxuU3Mtte25qBasaLo%2B%2F2Kk0qm9ALNsbN1atSZTX3gGEG6eUiHTzndGVXQHOhrvzkSkcf1OhM31q%2BIzs6ej8zKCvyEJDgYWKe3kvQW8yaEC6q7H64cdY8lzsQ1OJCxa%2B8qYBmBa0bmnsZaOqoevVD3jasWBdrkI6pdYPiA82utdI1FsLLGN3jE74tdvlyCFGkWl%2Bbw7X6IIFdmuw5pfKCtwierC1MwUCr2EyywR9PhixbFUbKwDWh86KJkplgH4VYMJoQnqKhH6HG1ikLxTtNT4KCy3kZTZXoJli6GVEg1mIYCXWB%2BFq9pL9uUnxcp980TCErKp1x0XsMtYIA%2BALwf%2Bra0jRcxXzCVVPEPfHJvzzXIgCrnbmo0yg0gu8XPrpqToLYi6KWikogPZ47%2FjRFVcKHdkqATbZxobJwY2yiSMDX8Gv2IvjL2UVsqSG7y44JSR%2F5%2FNR43xVTv1Dgx14BIhyGCqyaxgGKhQlrBdeKk7V9nBaf3O%2BXxY6cFX8Vx%2BNW3VaAsA7Kmb4oWBq2kVPYiaZbaHAbkVCeE%2FWVvtNUmkwY9gz4U6meubyJH%2B36PFcGeEmGWMaNFiJ%2BxzvXnzx99Y05DR3RZRopf3SjTLYftcv0U92%2FOBPpbJpUz59MTaVnVUk7g5ILcSGEg5JNUNT0ZV%2BWRmHGN2FMfXo5CbGq45PqxvkpEmAoUxZM3FYQwh6XYXlek7FFUg029%2F%2BYg5N9a7bNVRUP1OKM2Ncj%2FM9jcB1taU9W82flem9CIR4HtP4A2YeZSBbv8uTE5zb3DpHq07Xg%2BvnTRggwc%3D--F1qm7bMAYtroIkxW--NBDYLYbjSYvxKmDG1976%2Bg%3D%3D',
'Host': 'github.com',
'If-None-Match': 'W/"76b0bacd37337f144b35268e2d3d3d64"',
'Referer': 'https://github.com/Karobben/Karobben.github.io',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
}

'''
Yuque
'''

Yuque_X_Auth_Token = {
"X-Auth-Token":"SboLOMTuWC8yvdryxbzj0xvDPjFwOKZhNGYSfxZZ"
}

def Get_ID(Slam):
    url = "https://www.yuque.com/api/v2/repos/liuwenkan/" + Slam
    headers= {"X-Auth-Token":"SboLOMTuWC8yvdryxbzj0xvDPjFwOKZhNGYSfxZZ"}
    res = requests.get(url, headers=headers)
    ID = str(res.json()['data']['id'])
    Name = res.json()['data']['name']
    Creat = res.json()['data']['created_at'].split("T")[0]
    Update = res.json()['data']['updated_at'].split('T')[0]
    return Name, ID, Creat,Update

def Get_Stat(Slam,Name = "NA"):
    Name_t,ID,Creat,Update = Get_ID(Slam)
    if Name == "NA":
        Name = Name_t
    url = "https://www.yuque.com/api/books/"+ID+"/statistics?"
    headers = {
        "authority":"www.yuque.com",
        "method": "GET",
        "path": "/api/books/"+ID+"/statistics?",
        "scheme": "https",
        "accept":"application/json",
        'accept-encoding':"gzip, deflate, br",
        "accept-language":"en-US,en;q=0.9",
        "cache-type":"application/json",
        "cookie": "lang=en-us; _yuque_session=0IcG7IcOmXq74z2jfuT3yJmjTSlrgLToswhBiI4ohDBqBts5-8WJfteRjqw88wpJQ3XStA38MULdxsFTr1ppbg==; UM_distinctid=17049c8f43fc40-0ad8aa98fd5065-1a201708-1fa400-17049c8f440c9a; __wpkreporterwid_=7c863911-550a-4b1b-933c-bee21834b911; ctoken=-WMVHRBmIhF4MxjTVZJiGEGp; CNZZDATA1272061571=561998253-1581783353-https%253A%252F%252Fwww.yuque.com%252F%7C1582205025; _TRACERT_COOKIE__SESSION=15e83d89-8aaa-4226-b69c-e5da5765906a; tree=a385%016bcaa0d8-c8e0-4d59-a3b1-dc2d6f69d87b%0114",
        #"referer":"https://www.yuque.com/r/liuwenkan/rr/statistics",
        "user-agent":"Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1",
        #"x-csrf-token": "-WMVHRBmIhF4MxjTVZJiGEGp",
        "X-Auth-Token":"SboLOMTuWC8yvdryxbzj0xvDPjFwOKZhNGYSfxZZ",
        "x-requested-with": "XMLHttpRequest"
        }
    #
    res     = requests.get(url, headers=headers, timeout=30)
    Data    = res.json()
    #
    Read    = str(Data['data'][0]['read_count'])
    Read_D  = str(Data['data'][0]['day_read_count'])
    Comment = str(Data['data'][0]['comment_count'])
    Like    = str(Data['data'][0]['like_count'])
    Like_D  = str(Data['data'][0]['day_like_count'])
    Watch   = str(Data['data'][0]['watch_count'])
    Doc     = str(Data['data'][0]['doc_count'])
    Result = "\n".join([Name,Read+"("+Read_D+")", Like+"("+Like_D+")", Comment, Watch, Doc,Creat,Update])
    return Read,Doc

def Get_Stat_From_ID(ID,path,Book_ID):
    ID = str(ID)
    url = "https://www.yuque.com/api/v2/repos/"+ str(Book_ID)+"/docs/"+ID
    headers = {
        "authority":"www.yuque.com",
        "method": "GET",
        "path": "/api/books/"+ID+"/statistics?",
        "scheme": "https",
        "accept":"application/json",
        'accept-encoding':"gzip, deflate, br",
        "accept-language":"en-US,en;q=0.9",
        "cache-type":"application/json",
        "cookie": "lang=en-us; _yuque_session=0IcG7IcOmXq74z2jfuT3yJmjTSlrgLToswhBiI4ohDBqBts5-8WJfteRjqw88wpJQ3XStA38MULdxsFTr1ppbg==; UM_distinctid=17049c8f43fc40-0ad8aa98fd5065-1a201708-1fa400-17049c8f440c9a; __wpkreporterwid_=7c863911-550a-4b1b-933c-bee21834b911; ctoken=-WMVHRBmIhF4MxjTVZJiGEGp; CNZZDATA1272061571=561998253-1581783353-https%253A%252F%252Fwww.yuque.com%252F%7C1582205025; _TRACERT_COOKIE__SESSION=15e83d89-8aaa-4226-b69c-e5da5765906a; tree=a385%016bcaa0d8-c8e0-4d59-a3b1-dc2d6f69d87b%0114",
        #"referer":"https://www.yuque.com/r/liuwenkan/rr/statistics",
        "user-agent":"Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1",
        #"x-csrf-token": "-WMVHRBmIhF4MxjTVZJiGEGp",
        "X-Auth-Token":"SboLOMTuWC8yvdryxbzj0xvDPjFwOKZhNGYSfxZZ",
        "x-requested-with": "XMLHttpRequest"
        }
    #
    res     = requests.get(url, headers=headers, timeout=30)
    Data    = res.json()
    Slug    = str(Data['data']['slug'])
    Title   = str(Data['data']['title'])
    Like    = str(Data['data']['likes_count'])
    C_des   = str(Data['data']['custom_description'])
    S_des   = str(Data['data']['description'][:20])
    Words   = str(Data['data']['word_count'])
    Creat   = str(Data['data']['created_at'].split('T')[0])
    Updat   = str(Data['data']['updated_at'].split('T')[0])
    Href = path + Slug
    if C_des == "None":
        C_des = S_des
    Result = '<p class="Docs" ><a href="'+Href+'">'+Title+'</a><count>Like:'+Like+'; creat:'+Creat+'</count></p><p class="Docs_count">'+C_des+'<data>words:'+Words+'; update:'+Updat+'</data></p>'
    return Result



'''
Baidu Tongji
'''

Baidu_TOKEN = "21.0f8ea7aa8faeb58ddefbbbfedc7becdd.2592000.1585190872.4214606488-18476103"

def Tongji(TOKEN):
    TIME =time.strftime("%Y%m%d", time.localtime())
    #
    def Get_UV(TOKEN,ID,TIME):
        A = "https://openapi.baidu.com/rest/2.0/tongji/report/getData?access_token=" + TOKEN
        B = "&site_id="+str(ID)
        C = "&start_date=20200120&end_date="+TIME
        D = "&metrics=pv_count%2Cvisitor_count&method=overview%2FgetTimeTrendRpt"
        url = A+B+C+D
        Data = requests.get(url).json()
        UVPV_list = Data['result']['items'][1]
        PV_T = UVPV_list[-1][0]
        if PV_T =="--":
            PV_T = 0
        UV_T = UVPV_list[-1][1]
        if UV_T =="--":
            UV_T = 0
        #
        PV = []
        UV = []
        for i in UVPV_list:
            if i[0] != "--":
                PV+=[i[0]]
            if i[1] != "--":
                UV+=[i[1]]
        #
        PV = str(sum(PV))+"+"+str(PV_T)
        UV = str(sum(UV))+"+"+str(UV_T)
        return PV,UV
        #
    def Location_Get(TOKEN, TIME):
        url1 = "https://openapi.baidu.com/rest/2.0/tongji/report/getData?access_token="
        url2 = TOKEN +"&site_id=14350939&start_date="
        url3 = TIME + "&end_date="+TIME+"&metrics=pv_count&method=overview%2FgetDistrictRpt"
        url = url1+url2+url3
        Data = requests.get(url).json()
        Location = ""
        Location_N = ""
        try:
            for i in Data['result']['items'][0]:
                Location += i[0] +'\n'
            for i in Data['result']['items'][1]:
                Location_N += str(i[0]) +'\n'
        except:
            AA = 1
        return Location,Location_N
        #
    def Location_Get_C(TOKEN, TIME):
        url1 = "https://openapi.baidu.com/rest/2.0/tongji/report/getData?access_token="
        url2 = TOKEN +"&site_id=14350939&start_date="
        url3 = TIME + "&end_date="+TIME+"&metrics=pv_count&method=visit%2Fworld%2Fa"
        url = url1+url2+url3
        Data = requests.get(url).json()
        Location = ""
        Location_N = ""
        try:
            for i in Data['result']['items'][0]:
                Location += i[0]['name'] +'\n'
            for i in Data['result']['items'][1]:
                Location_N += str(i[0]) +'\n'
        except:
            AA = 1
        return Location,Location_N
        #
    def New_Visitor_Get(TOKEN, TIME):
    	url1 = "https://openapi.baidu.com/rest/2.0/tongji/report/getData?access_token="
    	url2 = TOKEN + "&site_id=14350939&start_date="
    	url3 = TIME + "&end_date=" + TIME + "&metrics=new_visitor_ratio&method=source%2Fall%2Fa"
    	url = url1 + url2 +url3
    	Data = requests.get(url).json()
    	#
    	return "新訪客比例 "+str(Data['result']['sum'][0][0])+"%"
        #
    def main():
        # Aquiring Domains' Name and ID
        url1= "https://openapi.baidu.com/rest/2.0/tongji/config/getSiteList?access_token="+TOKEN
        List = requests.get(url1).json()
        Domain = List['list'][0]['domain']
        Domain_ID = List['list'][0]['site_id']
        Sub_domain = [[Domain,Domain_ID]]
        Sub_List = List['list'][0]['sub_dir_list']
        for i in Sub_List:
            Sub_domain += [[i['name'],i['sub_dir_id']]]
        Result = {}
        for i in Sub_domain:
            PV,UV = Get_UV(TOKEN,i[1],TIME)
            Result.update({i[0]:{"PV":PV,"UV":UV}})
        Name = ""
        PV   = ""
        UV   = ""
        for  i  in Result:
            Name += i + "\n"
            PV   += Result[i]['PV']+"\n"
            UV   += Result[i]['UV']+"\n"
        New_Vis_N = New_Visitor_Get(TOKEN, TIME)
        Location,Location_N = Location_Get(TOKEN, TIME)
        Location_C,Location_C_N = Location_Get_C(TOKEN, TIME)
        return Name,PV,UV,Location,Location_N,Location_C,Location_C_N,New_Vis_N
        #
    return main()

'''
Yuque_Statistic  = {
    "authority":"www.yuque.com",
    "method": "GET",
    "path": "/api/books/"+ID+"/statistics?",
    "scheme": "https",
    "accept":"application/json",
    'accept-encoding':"gzip, deflate, br",
    "accept-language":"en-US,en;q=0.9",
    "cache-type":"application/json",
    "cookie": "lang=en-us; _yuque_session=0IcG7IcOmXq74z2jfuT3yJmjTSlrgLToswhBiI4ohDBqBts5-8WJfteRjqw88wpJQ3XStA38MULdxsFTr1ppbg==; UM_distinctid=17049c8f43fc40-0ad8aa98fd5065-1a201708-1fa400-17049c8f440c9a; __wpkreporterwid_=7c863911-550a-4b1b-933c-bee21834b911; ctoken=-WMVHRBmIhF4MxjTVZJiGEGp; CNZZDATA1272061571=561998253-1581783353-https%253A%252F%252Fwww.yuque.com%252F%7C1582205025; _TRACERT_COOKIE__SESSION=15e83d89-8aaa-4226-b69c-e5da5765906a; tree=a385%016bcaa0d8-c8e0-4d59-a3b1-dc2d6f69d87b%0114",
    #"referer":"https://www.yuque.com/r/liuwenkan/rr/statistics",
    "user-agent":"Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1",
    #"x-csrf-token": "-WMVHRBmIhF4MxjTVZJiGEGp",
    "X-Auth-Token":"SboLOMTuWC8yvdryxbzj0xvDPjFwOKZhNGYSfxZZ",
    "x-requested-with": "XMLHttpRequest"
    }
'''
