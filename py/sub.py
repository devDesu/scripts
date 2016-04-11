#encoding=UTF-8

dev = U'Dialogue: 0,0:03:41.15,0:03:41.20,Sign #15,,0,0,0,,{\c&HB3AEB8&\blur0.5\fay-0.005\fax0.02\fs21\pos(598.51,700.59)}Северный выход Маруночи'

def form_time(SUB_ST, OFST):
    listed = SUB_ST.split(':')
    hours = int(listed[0])
    mins = int(listed[1])
    secs = float(listed[2])
    secs += OFST
    if(secs >= 60.0):
        secs -= 60.0
        mins += 1
    if(mins >= 60):
        mins -= 60
        hours += 1
    time_str = str(hours)+':'
    mins =str(mins) if mins>=10 else '0'+str(mins)
    time_str += mins+':'
    secs = str(secs) if secs>=10.0 else '0'+str(secs)
    secs = secs if len(secs)==5 else secs+'0'
    time_str += secs
    return time_str

def subs(SUB_ST, OFST):
    sub_list = SUB_ST.split(',')
    start_time = sub_list[1]
    end_time = sub_list[2]
    print(start_time, end_time)
    EDITED_start_time = form_time(start_time, OFST)
    EDITED_end_time = form_time(end_time, OFST)
    SUB_ST_E = SUB_ST[0:11]+EDITED_start_time+','+EDITED_end_time+SUB_ST[33:]
    print(SUB_ST_E)
    

subs(dev, 10)
