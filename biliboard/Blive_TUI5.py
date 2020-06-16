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
    # online infor
    Online_inf = Onl_inf()
    W_Tail.contents[0] = (urwid.Text(Online_inf), Vedio_inf.options())
    Ing,Msg = Bili_msg()
    Head.contents[2] = (urwid.Text("\n"*13+" "+Ing), Head.options('weight',10))
    Head.contents[3] = (urwid.Text("\n"+"\n".join(Msg.split("\n")[-14:])), Head.options('weight',36))


def refresh2(loop=None, data=None):
    loop.set_alarm_in(2, refresh)
    Ing,Msg = Bili_msg()
    Head.contents[3] = (urwid.Text(Ing), Head.options())
    Head.contents[2] = (urwid.Text(Msg), Head.options())

palette = [
    ('banner', 'black', 'light gray'),
    ('streak', 'black', 'dark red'),
    ('bg', 'black', 'dark blue'),]


#Self infor
mid = 393056819
AA = bili.get_member_info(mid)
Up_inf = urwid.Text("\n\n\n\n\n"+Bili_UPinf(393056819))
粉丝 = urwid.Text(str(bili.get_stat_info(mid)['data']['follower']))
Up_inf = urwid.Pile([Up_inf,粉丝])
Logo = urwid.Text(Logo)
Ing,Msg = Bili_msg()
Ing = urwid.Text(Ing)
Msg = urwid.Text("\n".join(Msg.split("\n")[-15:]))
Head = urwid.Columns([('fixed',16,Up_inf),('fixed',30,Logo),('fixed',10,Ing),('fixed',36,Msg)])

#Veido Infor
Title = urwid.Text("\n".join(["","观看量:","点赞:","回复:","硬币:" ]))
Bv1_N = Bili_v("Python色差",86328254)
Bv2_N = Bili_v("汪汪洗澡",89026731)
Bv3_N = Bili_v("大生态缸",61040198)
Bv4_N = Bili_v("OneNote记",44637823)
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
# 整合
fill = urwid.ListBox(urwid.SimpleListWalker([Head,Vedio_inf,W_Tail,edit,button]))

view = fill


loop = urwid.MainLoop(
    view, palette=[('body', 'dark cyan', '')],
    unhandled_input=keypress)
loop.set_alarm_in(1, refresh)
#loop.set_alarm_in(2, refresh2)
loop.run()
