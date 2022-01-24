# -*- encoding=utf-8 -*-

def myprint(xi,yi):
    if xi < x:
        if yi < y:
            if xi%2 == 0:
                if abs(xi+1 - x)+abs(yi - y) <= abs(xi - x)+abs(yi+1 -y):
                    # (level,who_lock) = judge_level(xi+1, yi)
                    level = 9
                    who_lock = 1
                    if level < leveln and who_lock<=2:
                        routepath.append((xi+1,yi))
                        print("111",routepath)
                        return(xi+1,yi)
                    else:
                        # (level,who_lock) = judge_level(xi+1, yi)
                        level = 3
                        who_lock = 1
                        if level < leveln and who_lock<=2:
                            routepath.append((xi,yi+1))
                            print("222",routepath)
                            return(xi,yi+1)
                else:
                    print(1)
                    return None
            else:
                print(2)
                return None
        else:
            print(3)
            return None     
    else:
        print(4)
        return None                             
if __name__ == "__main__":
    routepath = []
    x = 6
    y = 7
    xi = 2
    yi = 5
    leveln = 4
    (m,n) = myprint(xi,yi)
    print(m,n)
