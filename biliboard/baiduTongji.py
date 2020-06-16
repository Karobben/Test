#!/usr/bin/env python3

import requests
import time

TOKEN = "21.0f8ea7aa8faeb58ddefbbbfedc7becdd.2592000.1585190872.4214606488-18476103"
def Tongji(TOKEN):
    TIME =time.strftime("%Y%m%d", time.localtime())

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
        return Name,PV,UV

    return main()

print(Tongji(TOKEN))
