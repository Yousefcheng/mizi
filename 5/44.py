'''
    
'''
from datetime import datetime


start=input().split()
end=input().split()

start=[int(i) for i in start]
end=[int(i) for i in end]


if __name__ == '__main__':
    cur_day = datetime(start[0],start[1],start[2] )
    next_day = datetime(end[0], end[1],end[2])
    print((next_day - cur_day).days)  # 1
    # print("ok")
