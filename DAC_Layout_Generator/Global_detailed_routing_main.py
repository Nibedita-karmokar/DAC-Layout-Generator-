#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 31 22:13:51 2022

@author: nibeditakarmokar
"""


#Selecting track for detailed routing
def track_selection(track, detailed_track):
    assigned_track=0
    index=0
    for i in range (len(track)):
        if round(track[i],5) not in detailed_track :
            assigned_track=track[i]
            detailed_track.append(round(track[i],5))
            index=i
            break
    return assigned_track, detailed_track, index

#Selecting track for detailed routing
def track_selection_Filter(track, detailed_track):
    assigned_track=0
    index=0
    for i in range (len(track)):
        if round(track[i],5) not in detailed_track :
            assigned_track=track[i]
            detailed_track.append(round(track[i],5))
            index=i
            break
    return assigned_track, detailed_track, index


#Marking the capacitor whose global routing is performed
def Global_route_performed(Capacitor, i, j, side):
    for kl in range (len(Capacitor[i])):
        if Capacitor[i][kl].identity_n in Capacitor[i][j].inter_connect:
            Capacitor[i][kl].global_route_mark=1 
            Capacitor[i][kl].top_sign=side
            Capacitor[i][kl].bottom_sign=side 
            Capacitor[i][kl].parent_j=j

#Selecting channel           
def Selected_channel(Capacitor, i, j, ind_j):
    for kl in range (len(Capacitor[i])):
        if Capacitor[i][kl].identity_n in Capacitor[i][j].inter_connect:
            Capacitor[i][kl].selected_channel=ind_j 

#Selecting track for global routing
def Global_route_track_selection(flag, Capacitor, i, j, ind_j, global_track):
    
    if flag==1:
        for tr in range (len(Capacitor[i][ind_j].track_left_global)):
            if Capacitor[i][ind_j].track_left_global[tr] not in global_track :
                global_track.append(Capacitor[i][ind_j].track_left_global[tr])
                Global_route_performed(Capacitor, i, j, -1)
                break 
    else:
        for tr in range (len(Capacitor[i][ind_j].track_right_global)):
            if Capacitor[i][ind_j].track_right_global[tr] not in global_track :                                    
                global_track.append(Capacitor[i][ind_j].track_right_global[tr]) 
                Global_route_performed(Capacitor, i, j, 1)
                
                break   
    return global_track

#Selecting track for the capacitors for which they share channel in both left and right sides
def Global_route_track_selection_same_x(flag, Capacitor, i, j, ind_j, global_track):
    
    if flag==1:
        for tr in range (len(Capacitor[i][ind_j].track_left_global)):
            if Capacitor[i][ind_j].track_left_global[tr] not in global_track :
                global_track.append(Capacitor[i][ind_j].track_left_global[tr])
                Global_route_performed(Capacitor, i, j, -1)
                break 
    else:
        for tr in range (len(Capacitor[i][ind_j].track_right_global)):
            if Capacitor[i][ind_j].track_right_global[tr] not in global_track :                                    
                global_track.append(Capacitor[i][ind_j].track_right_global[tr])
                Global_route_performed(Capacitor, i, j, 1)
                break   
    return global_track

#Selecting track for unequal channel spacing
def Global_route_track_selection_unequal(flag, Capacitor, i, j, ind_j, global_track, obj_channel):
    
    if flag==1:
        for tr in range (len(Capacitor[i][ind_j].track_left_global)):
            if Capacitor[i][ind_j].track_left_global[tr] not in global_track :
                global_track.append(Capacitor[i][ind_j].track_left_global[tr])
                obj_channel[Capacitor[i][ind_j].x_coordinate].track_left.append(Capacitor[i][ind_j].track_left_global[tr])
                Global_route_performed(Capacitor, i, j, -1)
                break 
    else:
        for tr in range (len(Capacitor[i][ind_j].track_right_global)):
            if Capacitor[i][ind_j].track_right_global[tr] not in global_track :                                    
                global_track.append(Capacitor[i][ind_j].track_right_global[tr]) 
                obj_channel[Capacitor[i][ind_j].x_coordinate].track_right.append(Capacitor[i][ind_j].track_right_global[tr])
                Global_route_performed(Capacitor, i, j, 1)
                break   
    return global_track

#Selecting track for the capacitors for which they share channel in both left and right sides for unequal channel spacing
def Global_route_track_selection_same_x_unequal(flag, Capacitor, i, j, ind_j, global_track, obj_channel):
    
    if flag==1:
        for tr in range (len(Capacitor[i][ind_j].track_left_global)):
            if Capacitor[i][ind_j].track_left_global[tr] not in global_track :
                global_track.append(Capacitor[i][ind_j].track_left_global[tr])
                obj_channel[Capacitor[i][ind_j].x_coordinate].track_left.append(Capacitor[i][ind_j].track_left_global[tr])
                
                Global_route_performed(Capacitor, i, j, -1)
                break 
    else:
        for tr in range (len(Capacitor[i][ind_j].track_right_global)):
            if Capacitor[i][ind_j].track_right_global[tr] not in global_track :                                    
                global_track.append(Capacitor[i][ind_j].track_right_global[tr])
                obj_channel[Capacitor[i][ind_j].x_coordinate].track_right.append(Capacitor[i][ind_j].track_right_global[tr])
                
                Global_route_performed(Capacitor, i, j, 1)
                break   
    return global_track                   

#Finding out x and y values
def xy_value(track, inter_connect_array, width):                    
    y_list=[]
    y_min=0
    f=0

    if len(inter_connect_array)>1:
        for i in range (len(inter_connect_array)):
            
            if abs(inter_connect_array[i][0]-track)<width:
                f=1
                y_list.append(inter_connect_array[i][1])  
    elif len(inter_connect_array)==1:
        y_min=inter_connect_array[0][1]
        
    if f==1:
        y_min=min(y_list)                              
    x_list=[]                            
    for t in range (len(inter_connect_array)):
        x_list.append(inter_connect_array[t])
    x_value=0

    for x_c in range (len(x_list)):
        if x_list[x_c][1]==y_min:
            if abs(x_list[x_c][0]-track)<width:  
                x_value=x_list[x_c][0]
                
    return x_value, y_min

def xy_value_top(track, inter_connect_array, width):                    
    y_list=[]
    y_max=0
    f=0

    if len(inter_connect_array)>1:
        for i in range (len(inter_connect_array)):
            
            if abs(inter_connect_array[i][0]-track)<width:
                f=1
                y_list.append(inter_connect_array[i][1])  
    elif len(inter_connect_array)==1:
        y_max=inter_connect_array[0][1]
        
    if f==1:
        y_max=max(y_list)                              
    x_list=[]                            
    for t in range (len(inter_connect_array)):
        x_list.append(inter_connect_array[t])
    x_value=0

    for x_c in range (len(x_list)):
        if x_list[x_c][1]==y_max:
            if abs(x_list[x_c][0]-track)<width:  
                x_value=x_list[x_c][0]
                break
                
    return x_value, y_max

def capacitor_index(Capacitor, x, y):
    i_index=0
    j_index=0
    for i in range (len(Capacitor)):
        for j in range (len(Capacitor[i])):
            if Capacitor[i][j].x_coordinate==x and Capacitor[i][j].y_coordinate==y:
                i_index=i
                j_index=j               
                break
        if i_index!=0:
            break
    return  i_index, j_index 
                
# def Track_number_in_channel(Capacitor, row, column, global_tracks, x, y, Xc, connected_com):
#     unique_track=set(global_tracks)
#     unique_tracks=list(unique_track)
#     unique_tracks.sort()
    
#     assigned_track=[]
#     left_channel_track_number=0
#     right_channel_track_number=0
#     flag=0
#     left_tracks=[]
#     right_tracks=[]
#     fl=0
    
    
#     #j_ind=0

#     for i in range (len(Capacitor)):
#         for j in range (len(Capacitor[i])):
#             if Capacitor[i][j].x_coordinate==x:
#                 fl=1
#                 #j_ind=j
#                 for k in range (len(Capacitor[i][j].track_left_global)):
#                     left_tracks.append(Capacitor[i][j].track_left_global[k])
#                 for k in range (len(Capacitor[i][j].track_right_global)):
#                     right_tracks.append(Capacitor[i][j].track_right_global[k])
#             if fl==1:
#                 break
#         if fl==1:
#             break
                                
#     x_mirror=column-x-1
#     y_mirror=row-y-1
#     left_assign_tr=[]
#     right_assign_tr=[]
    
#     (i_index, j_index)=capacitor_index(Capacitor, x_mirror, y_mirror)
    
    
#     if Capacitor[i_index][j_index].global_route_mark!=0 and Capacitor[i_index][j_index].bottom_sign==1:
#         flag=1

#     elif Capacitor[i_index][j_index].global_route_mark!=0 and Capacitor[i_index][j_index].bottom_sign==-1:
#         flag=0
        
#     elif x==0 :        
#         flag=0
        
    
#     else:    
#         for tr in range (len(unique_tracks)):
#             if unique_tracks[tr] not in assigned_track:
#                 if unique_tracks[tr] in left_tracks :
#                     left_channel_track_number=left_channel_track_number+1
#                     assigned_track.append(unique_tracks[tr])
#                     left_assign_tr.append(unique_tracks[tr]) 

#                 elif unique_tracks[tr] in right_tracks:
#                     right_channel_track_number=right_channel_track_number+1
#                     assigned_track.append(unique_tracks[tr])
#                     right_assign_tr.append(unique_tracks[tr])


#         if right_channel_track_number==left_channel_track_number and x<Xc:
#             flag=1 
#         if right_channel_track_number==left_channel_track_number and x>Xc:
#             flag=0 
#         if right_channel_track_number>left_channel_track_number and connected_com==1 and abs(Xc-x)<1 and right_channel_track_number==1:
#             flag=0               
#         if right_channel_track_number>left_channel_track_number:
#             flag=1
#         if right_channel_track_number<left_channel_track_number:
#             flag=0            
#         if right_channel_track_number==left_channel_track_number and left_channel_track_number==1 and x<Xc:
#             flag=0
#         if right_channel_track_number==left_channel_track_number and abs(Xc-x)<1:
#             flag=0
            
#     return flag
#Calculating the trakc number in each channel


def Track_number_in_channel(Capacitor, row, column, global_tracks, x, y, Xc, c):
    unique_track=set(global_tracks)
    unique_tracks=list(unique_track)
    unique_tracks.sort()
    
    assigned_track=[]
    left_channel_track_number=0
    right_channel_track_number=0
    flag=0
    left_tracks=[]
    right_tracks=[]
    fl=0

    for i in range (len(Capacitor)):
        for j in range (len(Capacitor[i])):
            if Capacitor[i][j].x_coordinate==x:
                fl=1
                for k in range (len(Capacitor[i][j].track_left_global)):
                    left_tracks.append(Capacitor[i][j].track_left_global[k])
                for k in range (len(Capacitor[i][j].track_right_global)):
                    right_tracks.append(Capacitor[i][j].track_right_global[k])
            if fl==1:
                break
        if fl==1:
            break
                                
    x_mirror=column-x-1
    y_mirror=row-y-1
    left_assign_tr=[]
    right_assign_tr=[]
    
    (i_index, j_index)=capacitor_index(Capacitor, x_mirror, y_mirror)
#    if i_index+1==4:
    
    if Capacitor[i_index][j_index].global_route_mark!=0 and Capacitor[i_index][j_index].bottom_sign==1:
        flag=1
    elif Capacitor[i_index][j_index].global_route_mark!=0 and Capacitor[i_index][j_index].bottom_sign==-1:
        flag=0
    else:    
        for tr in range (len(unique_tracks)):
            if unique_tracks[tr] not in assigned_track:
                if unique_tracks[tr] in left_tracks :
                    left_channel_track_number=left_channel_track_number+1
                    assigned_track.append(unique_tracks[tr])
                    left_assign_tr.append(unique_tracks[tr])

                elif unique_tracks[tr] in right_tracks:
                    right_channel_track_number=right_channel_track_number+1
                    assigned_track.append(unique_tracks[tr])
                    right_assign_tr.append(unique_tracks[tr])

            
        if right_channel_track_number>left_channel_track_number:
            flag=1

        elif right_channel_track_number==left_channel_track_number and left_channel_track_number==1 and x<Xc:
            flag=0
            
        elif right_channel_track_number==left_channel_track_number:
            if abs(Xc-x)<1:
                flag=1
    return flag


def Track_number_in_channel_2(Capacitor, row, column, global_tracks, i, j, Xc):
    unique_track=set(global_tracks)
    unique_tracks=list(unique_track)
    unique_tracks.sort()
    
    assigned_track=[]
    left_channel_track_number=0
    right_channel_track_number=0
    flag=0
    left_tracks=[]
    right_tracks=[]
    Track_num=0


    for k in range (len(Capacitor[i][j].track_left_global)):
        left_tracks.append(Capacitor[i][j].track_left_global[k])
    for k in range (len(Capacitor[i][j].track_right_global)):
        right_tracks.append(Capacitor[i][j].track_right_global[k])

                                
 
    for tr in range (len(unique_tracks)):
        if unique_tracks[tr] not in assigned_track:
            if unique_tracks[tr] in left_tracks :
                left_channel_track_number=left_channel_track_number+1
                assigned_track.append(unique_tracks[tr])

            elif unique_tracks[tr] in right_tracks:
                right_channel_track_number=right_channel_track_number+1
                assigned_track.append(unique_tracks[tr])
            
    if right_channel_track_number>left_channel_track_number: 
        flag=1
        Track_num=left_channel_track_number
    elif right_channel_track_number<left_channel_track_number: 
        flag=0
        Track_num=right_channel_track_number
    elif right_channel_track_number==left_channel_track_number:
        flag=1
        Track_num=left_channel_track_number        


    elif right_channel_track_number==left_channel_track_number:
        if abs(Xc-Capacitor[i][j].x_coordinate)<1:
            flag=1
            Track_num=left_channel_track_number

    return flag, Track_num


def Global_track_selection_equal_distance(Capacitor, row, column, global_track, distance_equal, i, j, k, center_x):
    j_index_initial=0
    j_index=0
    k_index=0
    flag_track=0
    Track_num=100
    l_index=0
    for l in range (len(distance_equal)):
        for rr_1 in range (len(Capacitor[i])):
            if Capacitor[i][rr_1].identity_n in Capacitor[i][j].inter_connect:  
                if Capacitor[i][rr_1].y_coordinate==distance_equal[l][1] and Capacitor[i][rr_1].x_coordinate==distance_equal[l][2]:
                    j_index_initial=rr_1
                    break 
                
        (flag_track_2, Track_num_2)=Track_number_in_channel_2(Capacitor, row, column, global_track, i, j_index_initial, center_x)

        if Track_num>Track_num_2:
            Track_num=Track_num_2
            flag_track=flag_track_2
            l_index=l
            j_index=j_index_initial

    for rr_1 in range (len(Capacitor[i])):
        if Capacitor[i][rr_1].identity_n in Capacitor[i][k].inter_connect:  
            if Capacitor[i][rr_1].y_coordinate==distance_equal[l_index][3] and Capacitor[i][rr_1].x_coordinate==distance_equal[l_index][4]:
                k_index=rr_1
                break            
    
    con_j=[]
    con_j.append(j_index)
    con_j.append(k_index)
    Capacitor[i][j_index].connected_pins.append(con_j)
    con_index_c=[]
    con_index_c.append(k_index)
    con_index_c.append(j_index)                                            
    Capacitor[i][k_index].connected_pins.append(con_index_c) 
    
    if flag_track==1:
        for tr in range (len(Capacitor[i][j_index].track_left_global)):
            if Capacitor[i][j_index].track_left_global[tr] not in global_track :

                global_track.append(Capacitor[i][j_index].track_left_global[tr])
                Global_route_performed(Capacitor, i, j, -1)
                Global_route_performed(Capacitor, i, k, -1)
                break     
    else:
        for tr in range (len(Capacitor[i][j_index].track_right_global)):
            if  Capacitor[i][j_index].track_right_global[tr] not in global_track:                                  

                global_track.append(Capacitor[i][j_index].track_right_global[tr])       
                Global_route_performed(Capacitor, i, j, 1)
                Global_route_performed(Capacitor, i, k, 1)
                break
            
    return j_index, k_index, global_track


def Right_shared_channel_span(Capacitor, max_track, i, j, ind_j, global_tracks, right_channel_index):
    for t_a in range (max_track): 
        if Capacitor[i][ind_j].track_right_global[t_a] not in global_tracks   and Capacitor[i][ind_j].global_route_mark==0 :

            global_tracks.append(Capacitor[i][ind_j].track_right_global[t_a])
            
            Global_route_performed(Capacitor, i, j, 1)   
            Selected_channel(Capacitor, i, j, ind_j)    
                             
            b=0
            for index_c in right_channel_index:                                                
                con_j=[]
                con_j.append(ind_j)
                con_j.append(index_c)
                Capacitor[i][ind_j].connected_pins.append(con_j)
                con_index_c=[]
                con_index_c.append(index_c)
                con_index_c.append(ind_j)                                            
                Capacitor[i][index_c].connected_pins.append(con_index_c)                  

                for k_in in range (len(Capacitor[i])):
                    if Capacitor[i][index_c].identity_n in Capacitor[i][k_in].inter_connect:
                        Global_route_performed(Capacitor, i, k_in, 1) 
                        Selected_channel(Capacitor, i, k_in, ind_j) 
                        b=1                                                                              

            if b==1:
                break                             

def Left_shared_channel_span(Capacitor, max_track, i, j, ind_j, global_tracks, left_channel_index):
    for t_a in range (max_track): 
        if Capacitor[i][ind_j].track_left_global[t_a] not in global_tracks  and Capacitor[i][ind_j].global_route_mark==0 :

            global_tracks.append(Capacitor[i][ind_j].track_left_global[t_a])
            Global_route_performed(Capacitor, i, j, -1)
            Selected_channel(Capacitor, i, j, ind_j)                                     
            b=0
            for index_c in left_channel_index:                                                
                con_j=[]
                con_j.append(ind_j)
                con_j.append(index_c)
                Capacitor[i][ind_j].connected_pins.append(con_j)
                con_index_c=[]
                con_index_c.append(index_c)
                con_index_c.append(ind_j)                                            
                Capacitor[i][index_c].connected_pins.append(con_index_c)  
                
                for k_in in range (len(Capacitor[i])):
                    if Capacitor[i][index_c].identity_n in Capacitor[i][k_in].inter_connect:
                        Global_route_performed(Capacitor, i, k_in, 1) 
                        Selected_channel(Capacitor, i, k_in, ind_j)                           
                        b=1                                                                                 
            if b==1:
                break                             


    
def Detailed_route_performed(obj, i, j):
    for k in range (len(obj[i])):
        if obj[i][k].identity in obj[i][j].inter_connected:
            obj[i][k].detailed_route_mark=1    

def track_assignment_DAC(obj, i, j, track_bottom):
    for k in range (len(obj[i])):
        if obj[i][k].identity in obj[i][j].inter_connected:
            obj[i][k].final_track_bottom=track_bottom                 

def track_assignment(obj, i, j, track_bottom, track_top):
    for k in range (len(obj[i])):
        if obj[i][k].identity in obj[i][j].inter_connected:
            obj[i][k].final_track_bottom=track_bottom     
            obj[i][k].final_track_top=track_top

def topological(root, inter_connect_array):
    dfs_tree=[]
    visited = []   
    ind_save=0

    for i in range (len(inter_connect_array)):
        if root == inter_connect_array[i]:
            ind_save=i
    
    stack=[]    
    stack.append(root)

    while (len(stack)):
        s=stack[-1]
        stack.pop()
        
        if s not in visited:
            for i in range (len(inter_connect_array)):
                if s == inter_connect_array[i]:
                    ind_save=i 
                    dfs_tree.append(inter_connect_array[i])
            visited.append(inter_connect_array[ind_save])
        for i in range (len(inter_connect_array)):
            if inter_connect_array[i] not in visited:
                d=((s[0]-inter_connect_array[i][0])**2+(s[1]-inter_connect_array[i][1])**2)**(1/2)  
                if d==1:                             
                    stack.append(inter_connect_array[i])
    return dfs_tree
            


def delay_calculation(htrack, htrack_l, track, x, y, tree, inter_connect_array, inter_length, res_per_length, cap_per_length, unit_cap, sy, sx, branch_delay, res_per_via, all_conn):
    delay=((abs(htrack-htrack_l)+abs(x-track))*res_per_length+res_per_via)*(inter_length*cap_per_length+len(inter_connect_array)*unit_cap+(abs(htrack-htrack_l)+abs(x-track))*cap_per_length)*10**(-15)  
    if all_conn==1:
        delay=0
    d_l=0 
    len_r=0            
    for hh in range (len(tree)-1):        
        if tree[hh+1][0]==tree[hh][0]:
            if abs(tree[hh+1][1]-tree[hh][1])==1:
                len_r=len_r+sy
                d_l=d_l+(len_r*res_per_length+res_per_via)*(unit_cap+sy*cap_per_length)*10**(-15)  

        elif tree[hh+1][1]==tree[hh][1] :
            if abs(tree[hh+1][0]-tree[hh][0])==1: 
                len_r=len_r+sx
                d_l=d_l+(len_r*res_per_length+res_per_via)*(unit_cap+sx*cap_per_length)*10**(-15)  
    
    
    delay=d_l+branch_delay+delay
    
    return delay

