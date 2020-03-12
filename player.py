import pygame
import numpy as np

def Check_pos_inrange(pos,all_location):
    abs_diff = []
    for location in all_location:
        tmp = []
        tmp=[abs(location[0]-pos[0]),abs(location[1]-pos[1])]
        abs_diff.append(tmp)
    
    return all_location[abs_diff.index(min(abs_diff))]

def check_who_win(current):
    same_w = {}
    same_h = {}
    for data in current:
        if data[0] in same_w:
            same_w[data[0]]+=1
        elif data[0] not in same_w:
            same_w[data[0]]=1

        if data[1] in same_h:
            same_h[data[1]]+=1
        elif data[1] not in same_h:
            same_h[data[1]]=1
    #horizantal check 
    for w in same_w:
        if same_w[w] >=5:
            return True
    #vertical check 
    for h in same_h:
        if same_h[h] >=5:
            return True
    
    check_left_to_right = []
    check_right_to_left=[]
    for data in current:
        tmp = [data[0]+40,data[1]+40]
        while tmp in current:
            check_left_to_right.append(tmp)
            tmp = [tmp[0]+40,tmp[1]+40]

        tmp = [data[0]+40,data[1]-40]
        while tmp in current:
            tmp = [tmp[0]+40,tmp[1]-40]
            check_right_to_left.append(tmp)
        
        if len(check_left_to_right) >=4:
            return True
        if len(check_right_to_left) >=4:
            return True
        check_left_to_right =  list()
        check_right_to_left = list()
    return False
