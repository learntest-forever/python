# -*- encoding=utf-8 -*-

import time


def getpoints():
    pass
    # pass
    # 三、路径规划：
    # 获取自己地块坐标，初始化时为主城坐标11块地,根据主城中心块x奇偶获取11块坐标值： 遍历地块信息，wholock = 0 或 1则存入myland = [(x,y,who_lock),(x1,y1,who_lock)],为简单，前期可不考虑加同盟问题
    # 查找可占领地块坐标 ：输入要打地块等级（leveln）， 遍历地块文件，找到 level = leveln & wholock = 0 ,获取坐标xn yn (dest_x,dest_y)
    # 查下目标地块附近最近的可连地块xy: 遍历myland，以xn yn 与myland 中每块地 start_x start_y计算距离， min_distance = abs(xn-start_x) + abs(yn-start_y)  得到(目标点xy,可连地xy，距离d) 存入距离列表distance [(x，y,start_x，start_y,d1)]；
    # 遍历distance 查询 d最小的 可连地坐标 start_x,start_y；
    # 判断路线routepath初始为空， 可占用点追加[(x1,y1),(x2,y2)]:
        # 当x为偶数时，斜向右下方 x+1 y不变
        # 当x为奇数时，斜向右下方 x+1 y+1
        # 2 5
        #     3 5
        #         4 6
        #             5 6
        #                 6 7
        #                     7 7
    # dest_x  dest_y 为目标地块xy坐标, start_x start_y (start_x ,start_y)为距离最近可连接点坐标；
    # leveln 为目标地块等级

# start_x,start_y, dest_x,dest_y
def getroute(start_x,start_y, dest_x,dest_y,leveln,routepath):
    if start_x == dest_x and start_y == dest_y:
        return routepath
    if start_x < dest_x:
        if start_y < dest_y:
            if start_x%2 == 0:
                # 判断 (start_x+1,start_y) 与 (start_x，start_y+1) 哪个距离目标x y近；
                if abs(start_x+1 - dest_x)+ abs(start_y - dest_y) <= abs(start_x - dest_x) + abs(start_y+1 - dest_y):
                    (level,who_lock) = judge_level(start_x+1, start_y)
                    if level < leveln and who_lock<=2:
                        routepath.append((start_x+1,start_y))
                        # 查询最新可连地坐标 start_x+1,start_y
                        getroute(start_x+1,start_y,dest_x,dest_y,routepath)
                        # return(start_x+1,start_y,routepath)
                    else:
                        (level,who_lock) = judge_level(start_x+1, start_y)
                        if level < leveln and who_lock<=2:
                            routepath.append((start_x,start_y+1))
                            getroute(start_x+1,start_y,dest_x,dest_y,routepath)
                            # return(start_x+1,start_y)
                        else:
                            # 判断 (start_x-1,start_y) 与 (start_x+1，start_y-1) 哪个距离目标x y近；
                            if abs(start_x-1 - dest_x)+abs(start_y - dest_y) <= abs(start_x+1 - dest_x)+abs(start_y-1 - dest_y)
                                (level,who_lock) = judge_level(start_x+1, start_y)
                                if level < leveln and who_lock<=2:
                                    routepath.append((start_x-1,start_y))
                                    getroute(start_x-1,start_y,dest_x,dest_y,routepath)

                                else:
                                    (level,who_lock) = judge_level(start_x+1, start_y)
                                    if level < leveln and who_lock<=2:
                                        routepath.append((start_x+1,start_y-1))
                                        递归查询最新可连地坐标 start_x+1,start_y-1
                                    else:
                                        if |start_x-1 - x|+|start_y-1 - y| <= |start_x - x|+|start_y-1 -y|
                                            (level,who_lock) = judge_level(start_x+1, start_y)
                                            if level < leveln and who_lock<=2:
                                                routepath.append((start_x+1,start_y))
                                                递归查询最新可连地坐标 start_x+1,start_y
                                            else:
                                                (level,who_lock) = judge_level(start_x+1, start_y)
                                                if level < leveln and who_lock<=2:
                                                    routepath.append((start_x+1,start_y-1))
                                                    递归查询最新可连地坐标 start_x+1,start_y-1



        # elif start_y > y:
        #     判断start_x+1,y地块等级level
        #     if level < leveln and who_lock<=2:
        #         routepath.append((start_x+1,start_y))
        #     else：
        #         print("无法通过，需要绕路")
        #         if start_x%2==0：
        #             判断 start_x, start_y+1 等级
        #         else:
        #             判断 start_x+1, start_y+1 等级
        # elif start_y == y:
        #     判断start_x+1, y
        #     if level < leveln and who_lock<=2:
        #         routepath.append((start_x+1,start_y))
        #     else：
        #         print("无法通过，需要绕路")
        #         if start_x%2==0：
        #             判断 start_x+1, start_y-1 等级
        #         else:
        #             判断 start_x+1, start_y+1 等级


def judge_level(x,y):
    level = 1
    who_lock = 0
    return(level,who_lock)


def genmap(x,y,num):
    mapfile = []
    for i in range(num):

        find_pic_10()


        if point_infos == None:
            print("未找到对应图片，请确认")
        else:
            dest_node = gen_destnode(point_infos.left,point_infos.top,point_infos.width,point_infos.height)
            start_mnq(dest_node[0],dest_node[1])
            pyautogui.moveTo(1,1,duration=0.3)
        pass
    pass