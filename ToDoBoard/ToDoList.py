#!/usr/bin/env python3

import urwid, sys, buttons

# exit the program
def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()


'''
bottons
'''

def bottons_1P(button):
    List = Read_ToDolsit()
    List[0][2] = str(int(List[0][2])+1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_1M(button):
    List = Read_ToDolsit()
    List[0][2] = str(int(List[0][2])-1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_2P(button):
    List = Read_ToDolsit()
    List[1][2] = str(int(List[1][2])+1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_2M(button):
    List = Read_ToDolsit()
    List[1][2] = str(int(List[1][2])-1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_3P(button):
    List = Read_ToDolsit()
    List[2][2] = str(int(List[2][2])+1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_3M(button):
    List = Read_ToDolsit()
    List[2][2] = str(int(List[2][2])-1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_4P(button):
    List = Read_ToDolsit()
    List[3][2] = str(int(List[3][2])+1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_4M(button):
    List = Read_ToDolsit()
    List[3][2] = str(int(List[3][2])-1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_5P(button):
    List = Read_ToDolsit()
    List[4][2] = str(int(List[4][2])+1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_5M(button):
    List = Read_ToDolsit()
    List[4][2] = str(int(List[4][2])-1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_6P(button):
    List = Read_ToDolsit()
    List[5][2] = str(int(List[5][2])+1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_6M(button):
    List = Read_ToDolsit()
    List[5][2] = str(int(List[5][2])-1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_7P(button):
    List = Read_ToDolsit()
    List[6][2] = str(int(List[6][2])+1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_7M(button):
    List = Read_ToDolsit()
    List[6][2] = str(int(List[6][2])-1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_8P(button):
    List = Read_ToDolsit()
    List[7][2] = str(int(List[7][2])+1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_8M(button):
    List = Read_ToDolsit()
    List[7][2] = str(int(List[7][2])-1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_9P(button):
    List = Read_ToDolsit()
    List[8][2] = str(int(List[8][2])+1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

def bottons_9M(button):
    List = Read_ToDolsit()
    List[8][2] = str(int(List[8][2])-1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    F.close()
    # refresh
    loop.widget = Setupview()

Botton_listP = [bottons_1P,bottons_2P,bottons_3P,bottons_4P,bottons_5P,bottons_6P,bottons_7P,bottons_8P,bottons_9P]
Botton_listM = [bottons_1M,bottons_2M,bottons_3M,bottons_4M,bottons_5M,bottons_6M,bottons_7M,bottons_8M,bottons_9M]


'''
Botton is done
'''

def List2str(List):
    Result2 = ""
    for i in List:
        Result2 += '\t'.join(i) + '\n'
    return Result2

# reading Task from ToDoList

def Read_ToDolsit():
    TODO = open(sys.path[0]+"/ToDolist",'r').read().split('\n')[:-1]
    Result = []
    for i in TODO:
        Result += [i.split()]
    return Result

def Bar_line(Sub,Bar_Max=20):
    if int(Sub[2])<= int(Sub[1]):
        Bar_G = int(int(Sub[2])*Bar_Max/int(Sub[1]))
        Bar_R = Bar_Max - Bar_G
        Bar_B = 0
    elif int(Sub[2]) > int(Sub[1]):
        Bar_G = Bar_Max-1
        Bar_R = 1
        Bar_B = int((int(Sub[2])-int(Sub[1]))*Bar_Max/int(Sub[1]))
        #print(int((int(Sub[2])-int(Sub[1]))*Bar_Max/int(Sub[1])))
    Sub_bar  = [('fixed',40,urwid.Text([('Green_BG', " "* Bar_G),('Red_BG', " "*Bar_R),('Blue_BG', " "*Bar_B)]))]
    return Sub_bar

def BigTxt(TXT):
    txt = urwid.BigText(
                ('banner',TXT), urwid.font.HalfBlock5x4Font())
    view = urwid.Padding(txt, 'center', width='clip')
    view = urwid.AttrMap(view, 'Blue_BG')
    return view#urwid.Columns([view])

def TODO_col(TODO):
    Num = 0
    Column_list = []
    for Sub in TODO:
        Num += 1
        Sub_list = []
        for i in Sub:
            Sub_list += [urwid.Text(i)]
        # bottons:
        locals()["P_line"+str(Num)]= urwid.Button(u'+')
        locals()["M_line"+str(Num)]= urwid.Button(u'-')
        # resbond:
        urwid.connect_signal(locals()["P_line"+str(Num)], 'click', Botton_listP[Num-1])
        urwid.connect_signal(locals()["M_line"+str(Num)], 'click', Botton_listM[Num-1])
        #
        Sub_list = [('fixed',5,locals()["P_line"+str(Num)]),('fixed',5,locals()["M_line"+str(Num)])] + Sub_list
        # Bar determination:
        Sub_bar  = Bar_line(Sub)
        Column_list += [urwid.Columns(Sub_list + Sub_bar)]
    return Column_list

def Button_C():
    def Clean(botton):
        List = Read_ToDolsit()
        for i in List:
            i[2] = str(0)
        Str_list = List2str(List)
        F = open(sys.path[0]+"/ToDolist",'w')
        F.write(Str_list)
        F.close()
        # refresh
        loop.widget = Setupview()
    Button_clean = urwid.Button(u"Clear")
    urwid.connect_signal(Button_clean, 'click', Clean)
    return Button_clean

def Setupview():
    Header = BigTxt("What's Next???")
    TODO = Read_ToDolsit()
    ToDOcol_list = TODO_col(TODO)
    Button_clean = Button_C()
    ToDoWidget = urwid.Pile([Header] + ToDOcol_list+[Button_clean])
    fill = urwid.Filler(ToDoWidget)
    return fill

palette = [
    ('banner', 'black', 'light gray'),
    ('Red_BG', 'dark red', 'dark red'),
    ('Green_BG', 'dark green', 'dark green'),
    ('Blue_BG', 'dark blue', 'dark blue'),
    ('streak', 'black', 'dark red'),
    ('bg', 'black', 'dark blue'),]


fill = Setupview()
loop = urwid.MainLoop(fill, palette, unhandled_input=exit_on_q)
loop.run()
