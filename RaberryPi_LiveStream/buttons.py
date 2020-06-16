#!/usr/bin/env python3
import urwid, sys
#from Setupview import loop
def Read_ToDolsit():
    TODO = open(sys.path[0]+"/ToDolist",'r').read().split('\n')[:-1]
    Result = []
    for i in TODO:
        Result += [i.split()]
    return Result

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
        urwid.connect_signal(locals()["P_line"+str(Num)], 'click', buttons.Botton_listP[Num-1])
        urwid.connect_signal(locals()["M_line"+str(Num)], 'click', buttons.Botton_listM[Num-1])
        #
        Sub_list += [locals()["P_line"+str(Num)],locals()["M_line"+str(Num)]]
        Column_list += [urwid.Columns(Sub_list)]
    A = urwid.Pile(Column_list)
    return A

def List2str(List):
    Result2 = ""
    for i in List:
        Result2 += '\t'.join(i) + '\n'
    return Result2

def bottons_1P(button):
    List = Read_ToDolsit()
    List[0][2] = str(int(List[0][2])+1)
    Str_list = List2str(List)
    F = open(sys.path[0]+"/ToDolist",'w')
    F.write(Str_list)
    TODO = Read_ToDolsit()
    fill = urwid.Filler(TODO_col(TODO))
    loop.widget = fill
    #loop.set_alarm_in(1, self.refresh)

def bottons_1M(button):
    print("1-")

def bottons_2P(button):
    print("2+")

def bottons_2M(button):
    raise urwid.ExitMainLoop()

def bottons_3P(button):
    raise urwid.ExitMainLoop()

def bottons_3M(button):
    raise urwid.ExitMainLoop()

Botton_listP = [bottons_1P,bottons_2P,bottons_3P]
Botton_listM = [bottons_1M,bottons_2M,bottons_3M]
