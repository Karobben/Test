#!/usr/bin/env python3

import urwid, time, sys, ast, requests, json, os
from urllib.request import urlopen

###################
# Bilive is Start #
###################

Logo = '                     //\n         \\\\         //\n          \\\\       //\n    ##DDDDDDDDDDDDDDDDDDDDDD##\n    ## DDDDDDDDDDDDDDDDDDDD ##\n    ## hh                hh ##\n    ## hh    //    \\\\    hh ##\n    ## hh   //      \\\\   hh ##\n    ## hh                hh ##\n    ## hh      wwww      hh ##\n    ## hh                hh ##\n    ## MMMMMMMMMMMMMMMMMMMM ##\n    ##MMMMMMMMMMMMMMMMMMMMMM##\n         \\/            \\/\n'
print(Logo)

class BiliSpider:
    def __init__(self):
        self.online_api = "https://api.bilibili.com/x/web-interface/online"  # 在线人数
        self.video_api = "https://api.bilibili.com/x/web-interface/archive/stat?&aid=%s"    # 视频信息
        self.newlist_api = "https://api.bilibili.com/x/web-interface/newlist?&rid=%s&pn=%s&ps=%s"     # 最新视频信息
        self.region_api = "https://api.bilibili.com/x/web-interface/dynamic/region?&rid=%s&pn=%s&ps=%s"  # 最新动态信息
        self.member_api = "http://space.bilibili.com/ajax/member/GetInfo"  # 用户信息
        self.stat_api = "https://api.bilibili.com/x/relation/stat?vmid=%s"  # 用户关注数和粉丝总数
        self.upstat_api = "https://api.bilibili.com/x/space/upstat?mid=%s"     # 用户总播放量和总阅读量
        self.follower_api = "https://api.bilibili.com/x/relation/followings?vmid=%s&pn=%s&ps=%s"    # 用户关注信息
        self.fans_api = "https://api.bilibili.com/x/relation/followers?vmid=%s&pn=%s&ps=%s"    # 用户粉丝信息
    #
    def get_api(api_url):
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Host": "api.bilibili.com",
            "Referer": "https://www.bilibili.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
        }
        res = requests.get(api_url, headers=headers)
        res_dict = res.json()
        return res_dict
    #
    def get_online(self):
        """
        获取在线信息
        all_count: 最新投稿
        web_online: 在线人数
        :return:
        """
        online_dic = BiliSpider.get_api(self.online_api)
        return online_dic
    #
    def get_video_info(self, aid):
        """
        获取视频信息
        :param aid: 视频id
        :return:
        """
        res = BiliSpider.get_api(self.video_api %aid)
        # print(res)
        return res
    #
    def get_newlist_info(self, rid, pn, ps):
        """
        获取最新视频信息
        :param rid: 二级标题的id (详见tid_info.txt)
        :param pn:  页数
        :param ps:  每页条目数 1-50
        :return:
        """
        res = BiliSpider.get_api(self.newlist_api %(rid, pn, ps))
        return res
    #
    def get_region_info(self, rid, pn, ps):
        """
        获取最新视频信息
        :param rid: 二级标题的id (详见tid_info.txt)
        :param pn:  页数
        :param ps:  每页条目数 1-50
        :return:
        """
        res = BiliSpider.get_api(self.region_api %(rid, pn, ps))
        return res
    #
    def get_member_info(self, mid):
        """
        获取用户信息
        :param mid:用户id
        :return:
        """
        post_data = {
            "crsf": "",
            "mid": mid,
        }
        header = {
            "Host": "space.bilibili.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0",
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Referer": "https://www.bilibili.com/",
        }
        res = requests.post(self.member_api, data=post_data, headers=header)
        member_dic = json.dumps(res.json(), ensure_ascii=False)
        return member_dic
    #
    def get_stat_info(self, vmid):
        """
        获取某用户的关注数和粉丝总数
        :param vmid: 用户id
        :return:
        """
        res = BiliSpider.get_api(self.stat_api % vmid)
        return res
    #
    def get_upstat_info(self, mid):
        """
        获取某用户的总播放量和总阅读量
        :param mid: 用户id
        :return:
        """
        res = BiliSpider.get_api(self.upstat_api % mid)
        return res
    #
    def get_follower_info(self, vmid, pn, ps):
        """
        获取某用户关注者信息
        :param vmid:用户id
        :param pn:  页数 最多5页
        :param ps:  每页条目数 1-50
        :return:
        """
        res = BiliSpider.get_api(self.follower_api %(vmid, pn, ps))
        return res
    #
    def get_fans_info(self, vmid, pn, ps):
        """
        获取某用户粉丝信息
        :param vmid:用户id
        :param pn:  页数 最多5页
        :param ps:  每页条目数 1-50
        :return:
        """
        res = BiliSpider.get_api(self.fans_api %(vmid, pn, ps))
        return res

bili = BiliSpider()

def Bili_v(Title,ID):
    try:
        ID = str(ID)
        url = "http://api.bilibili.com/archive_stat/stat?aid=" + ID
        html = urlopen(url).read().decode('utf-8')
        d = ast.literal_eval(html)
        Cont = d['data']
        View    = str(Cont['view'])
        Like    = str(Cont['like'])
        Reply   = str(Cont['reply'])
        Coin    = str(Cont['coin'])
        Result = "\n".join([Title,View, Like, Reply, Coin])
    except:
        Result = "\n".join([Title, '0','0','0','0'])
    return Result

def Bili_UPinf(mid):
    A= bili.get_member_info(mid)
    Name = A[A.find('name'):].split(',')[0].split(':')[1][2:-1]
    Blog = A[A.find('blog'):].split(',')[0][14:-2]
    return Name + "\n" + Blog

def Bili_difer(Bv1_N,Bv2_N):
    a = list(map(int, Bv1_N.split('\n')[1:]))
    b = list(map(int, Bv2_N.split('\n')[1:]))
    c = [b[i] - a[i] for i in range(len(a))]
    a2 = list(map(str, a))
    c = list(map(str, c))
    d = [a2[i] + "+"+ c[i] for i in range(len(c))]
    Result = Bv1_N.split('\n')[0] +"\n"+ '\n'.join(d)
    return Result

def Onl_inf():
    Bi_online = bili.get_online()
    web_online = Bi_online['data']['web_online']
    play_online = Bi_online['data']['play_online']
    Online_inf = "网页: " + str(web_online) +"; 移动: "+str(play_online)
    return Online_inf

def Bili_msg():
    Int = open(sys.path[0]+'/tmp.int').read()
    Msg = open(sys.path[0]+'/tmp.msg').read()
    return Int, Msg

def Bili_reply():
    url = "https://api.bilibili.com/x/msgfeed/reply?build=0&mobi_app=web"
    headers = {'Accept': 'application/json, text/plain, */*',
        'Origin': 'https://message.bilibili.com',
        'Referer': 'https://message.bilibili.com/',
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
        'Cookie': "LIVE_BUVID=AUTO5015807896693605; _uuid=58C69C39-C741-47C7-0E98-A379326816DE70318infoc; buvid3=3B00857F-A757-4982-9792-4B46DEC0BB12155821infoc; sid=bejf3qns; DedeUserID=393056819; DedeUserID__ckMd5=43771d91224c7285; SESSDATA=3a43b29f%2C1583381709%2C3a1b4f21; bili_jct=13c7b5c33bea5aaa2683dd24ef14f9df; CURRENT_FNVAL=16; rpdid=|(k|k)k|))Y)0J'ul)|~mYmk|; im_notify_type_393056819=0; CURRENT_QUALITY=80; _ga=GA1.2.517604625.1581950019; dy_spec_agreed=1; bp_t_offset_393056819=358015176582525173"
    }
    Result = requests.get(url,headers=headers).json()
    Msg = ["評論: "+Result['message']+"|"+str( Result['ttl'])]
    Reply = Result['data']['items']
    for i in range(5):
        Msg +=[Reply[i]['user']['nickname']+":"+Reply[i]['item']['source_content'].replace("\n"," ")]
    return "\n".join(Msg)

def Kill_bk():
    CMD = "for i in $(ps -h| grep '" +sys.path[0]+ "/Bili_output.py'| awk '{print $1}');do kill $i;done"
    os.system(CMD)

def Run_bk():
    CMD = sys.path[0]+ "/Bili_output.py &"
    os.system(CMD)

##################
# Bilive is Down #
##################


##################
# Yuque is Start #
##################

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
    return Result

def Fresh_Yuque(slef):
    print("Loading...")
    List = ['pythons',"腳本",'rr',"R語言",'python',"大蟒蛇",
    'blog',"博客",'linux','linux',
    'notes',"筆記",'bioinf','生信']
    #for i in range(1,8):
    for i in range(1,8):
        Slam = List[(i-1)*2]
        Name = List[(i-1)*2+1]
        Yuque.contents[i] = ( urwid.AttrWrap(urwid.Text(Get_Stat(Slam,Name)), 'Yellow_Text'), Yuque.options())

#################
# Yuque is Down #
#################


###################
# Tongji is Start #
###################
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
                Location_N += i[0]['name'] +'\n'
        except:
            AA = 1
        return Location,Location_N

    def New_Visitor_Get(TOKEN, TIME):
    	url1 = "https://openapi.baidu.com/rest/2.0/tongji/report/getData?access_token="
    	url2 = TOKEN + "&site_id=14350939&start_date="
    	url3 = TIME + "&end_date=" + TIME + "&metrics=new_visitor_ratio&method=source%2Fall%2Fa"
    	url = url1 + url2 +url3
    	Data = requests.get(url).json()
    	#
    	return "新訪客比例 "+str(Data['result']['sum'][0][0])+"%"

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

    return main()


def Fresh_Baidu(slef):
    TJ_Name,TJ_PV,TJ_UV,TJ_loc,TJ_loc_N,TJ_loc_C,TJ_loc_C_N,TJ_Vis = Tongji(TOKEN)
    TJ_Name = urwid.Text(TJ_Name)
    TJ_PV = urwid.Text(TJ_PV)
    TJ_UV = urwid.Text(TJ_UV)
    TJ_loc = urwid.Text(TJ_loc)
    TJ_loc_N = urwid.Text(TJ_loc_N)
    TJ_loc_C = urwid.Text(("Red_Text",TJ_loc_C))
    TJ_loc_C_N = urwid.Text(("Red_Text",TJ_loc_C_N))
    TJ_Vis = urwid.Text(TJ_Vis)

    TJ_loc = urwid.Pile([TJ_loc_C,TJ_loc])
    TJ_loc_N = urwid.Pile([TJ_loc_C_N,TJ_loc_N])

    #for i in range(1,8):
    Baidu_TJ.contents[1] = ( urwid.AttrWrap(TJ_PV,'Yellow_Text'), Baidu_TJ.options('weight',10))
    Baidu_TJ.contents[2] = ( urwid.AttrWrap(TJ_UV,'Yellow_Text'), Baidu_TJ.options('weight',10))
    Baidu_TJ.contents[3] = ( TJ_loc, Baidu_TJ.options('weight',10))
    Baidu_TJ.contents[4] = ( urwid.AttrWrap(TJ_loc_N,'Yellow_Text'), Baidu_TJ.options('weight',10))
    Baidu_TJ.contents[5] = ( urwid.AttrWrap(TJ_Vis,'Yellow_Text'), Baidu_TJ.options('weight',10))

##################
# Tongji is Down #
##################


##################
# Urwid is Start #
##################
Kill_bk()
Run_bk()
def keypress(key):
    if key in ('q', 'Q'):
        Kill_bk()
        raise urwid.ExitMainLoop()

def refresh(loop=None, data=None):
    loop.set_alarm_in(2.5, refresh)
    # Vedio
    Bv1_R = Bili_difer(Bv1_N,Bili_v("A",86328254))
    Bv2_R = Bili_difer(Bv2_N,Bili_v("A",89026731))
    Bv3_R = Bili_difer(Bv3_N,Bili_v("A",61040198))
    Bv4_R = Bili_difer(Bv4_N,Bili_v("A",44637823))
    Bv5_R = Bili_difer(Bv5_N,Bili_v("A",45117221))
    Vedio_inf.contents[1] = (urwid.Text(Bv1_R), Vedio_inf.options())
    Vedio_inf.contents[2] = (urwid.Text(Bv2_R), Vedio_inf.options())
    Vedio_inf.contents[3] = (urwid.Text(Bv3_R), Vedio_inf.options())
    Vedio_inf.contents[4] = (urwid.Text(Bv4_R), Vedio_inf.options())
    Vedio_inf.contents[5] = (urwid.Text(Bv5_R), Vedio_inf.options())
    Bli_reply.contents[0] = (urwid.Text(Bili_reply()), Bli_reply.options())
    # online infor
    Online_inf = Onl_inf()
    W_Tail.contents[0] = (urwid.Text(Online_inf), Vedio_inf.options())
    Ing,Msg = Bili_msg()
    Head.contents[2] = (urwid.Text("\n"*13+" "+Ing), Head.options('weight',10))
    Head.contents[3] = (urwid.AttrWrap(urwid.Text("\n"+"\n".join(Msg.split("\n")[-14:]),), 'Blue_Text'), Head.options('weight',36))

def refresh2(loop=None, data=None):
    loop.set_alarm_in(2, refresh)
    Ing,Msg = Bili_msg()
    Head.contents[3] = (urwid.Text(Ing), Head.options())
    Head.contents[2] = (urwid.Text(Msg), Head.options())

palette = [
    ('body',         'black',      'light gray', 'standout'),
    ('streak', 'black', 'dark red'),
    ('banner', 'black', 'light gray'),
    ('header',       'white',      'dark red',   'bold'),
    ('button normal','light gray', 'dark blue',  'standout'),
    ('button select','white',      'dark green'),
    ('button disabled','dark gray','dark blue'),
    ('edit',        'light gray', 'dark blue'),
    ('bigtext',     'white',      'black'),
    ('chars',       'light gray', 'black'),
    ('exit',        'white',      'dark cyan'),
    ('Red_Text',    'dark red',      '',  'bold'),
    ('Yellow_Text',    'yellow',      '',  'bold'),
    ('Blue_Text',   'dark blue',    "")
    ]

#Self infor
mid = 393056819
AA = bili.get_member_info(mid)
Up_inf = urwid.Text("\n\n\n\n\n"+Bili_UPinf(393056819))
粉丝 = urwid.Text(str(bili.get_stat_info(mid)['data']['follower']))
粉丝 = urwid.AttrWrap(粉丝, 'Red_Text')
Up_inf = urwid.Pile([Up_inf,粉丝])
Logo = urwid.Text(Logo)
Ing,Msg = Bili_msg()
Ing = urwid.Text(Ing)
Msg = urwid.Text("\n".join(Msg.split("\n")[-15:]))
Msg = urwid.AttrWrap(Msg, 'Blue_Text')
Head = urwid.Columns([('fixed',16,Up_inf),('fixed',30,Logo),('fixed',10,Ing),('fixed',36,Msg)])

#Veido Infor
Title = urwid.Text("\n".join(["","點擊:","點贊:","回覆:","投幣:" ]))
Bv1_N = Bili_v("Python色差",86328254)
Bv2_N = Bili_v("汪汪洗澡",89026731)
Bv3_N = Bili_v("生態缸",61040198)
Bv4_N = Bili_v("OneNote1",44637823)
Bv5_N = Bili_v("OneNote2",45117221)

Bv1 = urwid.Text(Bv1_N)
Bv2 = urwid.Text(Bv2_N)
Bv3 = urwid.Text(Bv3_N)
Bv4 = urwid.Text(Bv4_N)
Bv5 = urwid.Text(Bv5_N)

Vedio_inf = urwid.Columns([Title,Bv1,Bv2,Bv3,Bv4,Bv5])
# Online 信息
Online_inf = Onl_inf()
W_Tail = urwid.Columns([urwid.Text(Online_inf)])
W_Tail = urwid.AttrWrap(W_Tail, 'Red_Text')
# 弹幕
def on_ask_change(edit, new_edit_text):
    Result =  new_edit_text
def on_Send(new_edit_text):
    Result = str(edit)[30:-30]
    CMD = "Python-Send_blive.py " + Result
    os.system(CMD)
edit = urwid.Edit(u"发送弹幕\n")
button = urwid.Button(u'发送')
urwid.connect_signal(edit, 'change', on_ask_change)
urwid.connect_signal(button, 'click', on_Send)

# 評論
Bli_reply = urwid.Columns([urwid.Text(Bili_reply())])
Bli_reply = urwid.AttrWrap(Bli_reply, 'Blue_Text')

# Yuque Notes
YQ_HEADER = urwid.AttrMap(urwid.Text(('banner',"語雀筆記"), align='center'), 'streak')

Head_y = urwid.Text("\n".join(["","閱讀","點贊","評論","關注","文檔","初創","更新"]))
print("Aquiring python Scripts...")
PythonS = urwid.Text("123") #Get_Stat('pythons',"腳本"))
print("Aquiring python R...")
RR      = urwid.Text("123") #Get_Stat('rr',"R語言"))
print("Aquiring python Python...")
Python  = urwid.Text("123") #Get_Stat('python',"大蟒蛇"))
print("Aquiring python Blog...")
Blog    = urwid.Text( "123")#Get_Stat('blog',"博客"))
print("Aquiring python Linux...")
Linux   = urwid.Text( "123")#Get_Stat('linux'))
print("Aquiring python Notes...")
Notes   = urwid.Text( "123")#Get_Stat('notes',"筆記"))
print("Aquiring python Protocols...")
Bio     = urwid.Text( "123")#Get_Stat('bioinf','生信'))

Fresh_button = urwid.Button(u'語雀')
urwid.connect_signal(Fresh_button, 'click', Fresh_Yuque)

Yuque = urwid.Columns([("fixed",6, Head_y), PythonS, RR, Python, Blog, Notes, Bio, Linux])



# Baidu Tonhji
TJ_HEADER = urwid.AttrMap(urwid.Text(('banner',"百度統計"), align='center'), 'streak')
TJ_Name,TJ_PV,TJ_UV,TJ_loc,TJ_loc_N,TJ_loc_C,TJ_loc_C_N,TJ_Vis = Tongji(TOKEN)
TJ_Name = urwid.Text(TJ_Name)
TJ_PV = urwid.Text(TJ_PV)
TJ_UV = urwid.Text(TJ_UV)
TJ_loc = urwid.Text(TJ_loc)
TJ_loc_N = urwid.Text(TJ_loc_N)
TJ_loc_C = urwid.Text(TJ_loc_C)
TJ_loc_C_N = urwid.Text(TJ_loc_C_N)
TJ_Vis = urwid.Text(TJ_Vis)

TJ_loc = urwid.Pile([TJ_loc_C,TJ_loc])
TJ_loc_N = urwid.Pile([TJ_loc_C_N,TJ_loc_N])
Baidu_TJ = urwid.Columns([("fixed",20, TJ_Name),("fixed",10,TJ_PV),("fixed",10,TJ_UV),("fixed",10,TJ_loc),("fixed",10,TJ_loc_N),("fixed",10,TJ_Vis) ])

Baidu_Bottom = urwid.Button(u'百度統計')
urwid.connect_signal(Baidu_Bottom, 'click', Fresh_Baidu)

# 整合
Button_1 = urwid.Columns([button,Fresh_button,Baidu_Bottom])
fill = urwid.ListBox(urwid.SimpleListWalker([Head,Vedio_inf,W_Tail,edit,Button_1,Bli_reply,YQ_HEADER,Yuque,TJ_HEADER,Baidu_TJ]))

view = fill


loop = urwid.MainLoop(
    view, palette=palette,
    unhandled_input=keypress)
loop.set_alarm_in(2, refresh)
#loop.set_alarm_in(2, refresh2)
loop.run()
