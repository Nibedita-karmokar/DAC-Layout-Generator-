#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 16:59:41 2022

@author: nibeditakarmokar
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 31 00:32:57 2022

@author: nibeditakarmokar
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 20:20:29 2022

@author: nibeditakarmokar
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 21:21:44 2021

@author: nibeditakarmokar
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 13:27:14 2021

@author: nibeditakarmokar
"""
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib import pyplot as patches
from Global_detailed_routing_main import capacitor_index

import json

class wire:
    scale_factor=1
    def __init__(self, layer, netName, direction):
        self.layer=layer
        self.netName=netName
        self.direction=direction
        
    
    def segment(self, x0, y0, x1, y1, netType, clr):
        rect=[x0*wire.scale_factor, y0*wire.scale_factor, x1*wire.scale_factor, y1*wire.scale_factor]
        
        terminal = {'layer' : self.layer, 'netName' : self.netName, 'rect' : rect}
        if netType in ['drawing', 'pin', 'blockage']:
            terminal['netType']=netType
        else:
            assert "Invalid net type, valid net types include drawing, pin, and blockage"    
            
        if clr is not None:
            terminal['color'] = clr            
        
        return terminal
        
class via:
    scale_factor=1
    def __init__(self, layer, netName):
        self.layer=layer
        self.netName='netName'

       
    
    def segment(self, x0, y0, x1, y1, netType):
        rect=[x0*via.scale_factor, y0*via.scale_factor, x1*via.scale_factor, y1*via.scale_factor]
        
        terminal = {'layer' : self.layer, 'netName' : self.netName, 'rect' : rect}
        if netType in ['drawing', 'pin', 'blockage']:
            terminal['netType']=netType
        else:
            assert "Invalid net type, valid net types include drawing, pin, and blockage"    
            
        return terminal


class unit_cap:
    scale_factor=1
    def __init__(self, layer, netName):
        self.layer=layer
        self.netName=netName
        
    
    def segment(self, x0, y0, x1, y1, netType):
        rect=[x0*unit_cap.scale_factor, y0*unit_cap.scale_factor, x1*unit_cap.scale_factor, y1*unit_cap.scale_factor]
        
        terminal = {'layer' : self.layer, 'netName' : self.netName, 'rect' : rect}
        if netType in ['drawing', 'pin', 'blockage']:
            terminal['netType']=netType
        else:
            assert "Invalid net type, valid net types include drawing, pin, and blockage"    
        
        return terminal
 
        
class LSB:
    def __init__(self, even_connected):
        self.even_connected=even_connected
        self.all_even_connected=[]
        
        self.even_mark=0


        
class MSB:
    def __init__(self, odd_connected):
        self.odd_connected=odd_connected
        self.all_odd_connected=[]
        self.odd_mark=0       


    
    


def takeSecond(elem):
    return elem[1] 



def cap_identity(x, y, capacitor):
    identity=[]
    identity.append(x)
    identity.append(y)
    identity.append(capacitor)
    return identity

def CC_plot(Capcitor, Device_Name, mat, row, column, width, sx, height, sy, color, line_width, cap, Terminal_list):
    for D in Device_Name:    
        for i in range (row):    
            for j in range (column):
                if mat[i][j]==D:

                            
                            
                    xk=((j+1)-((column+1)/2))*(cap.w+sx)
                    yk=(((row+1)/2)-(i+1))*(height+sy)
                    ind=D
                    
                    
                    color_r= color[ind-1]
                    color_num='k'
                    var=str(int(mat[i][j]-1))
    
                    plt.text(xk-(sx/5), yk-(sx/2), var, fontsize=8, color=color_num, fontweight='bold')
                    x1=xk-width/2
                    y1=yk+height/2
                    x2=xk +width/2    #top plate
                    y2=yk+height/2                    
                    plt.plot([x1,x2],[y1,y2], color=color_r, linewidth=line_width) 
                    
                    x3=xk-width/2
                    y3=yk-height/2
                    x4=xk +width/2      #bottom plate
                    y4=yk-height/2
                    plt.plot([x3,x4],[y3,y4], color=color_r, linewidth=line_width)
                    
                    x1_1=xk-width/2
                    y1_1=yk+height/2
                    x2_1=xk-width/2   #top plate
                    y2_1=yk-height/2
                    plt.plot([x1_1,x2_1],[y1_1,y2_1], color=color_r, linewidth=line_width) 
                    
                    x3_1=xk +width/2  
                    y3_1=yk+height/2
                    x4_1=xk +width/2      #bottom plate
                    y4_1=yk-height/2
                    plt.plot([x3_1,x4_1],[y3_1,y4_1], color=color_r, linewidth=line_width)

def top_plate_vertical(x, y, y1, y2, Layers_dict, Terminal_list, cap):
    plt.gca().add_patch(patches.Rectangle((x-Layers_dict['M3']['Width']/2, y-Layers_dict['V2']['VencA_H']-Layers_dict['V2']['WidthY']/2),  Layers_dict['M3']['Width'], abs(y1-y2)+2*Layers_dict['V2']['VencA_H']+Layers_dict['V2']['WidthY'],color='k'))                                                                        
    wire_segment_1=wire('M3', None, Layers_dict['M3']['Direction'])
    Terminal_list.append(wire_segment_1.segment(x-Layers_dict['M3']['Width']/2, y-Layers_dict['V2']['VencA_H']-Layers_dict['V2']['WidthY']/2, x+Layers_dict['M3']['Width']/2, y+abs(y1-y2)+Layers_dict['V2']['VencA_H']+Layers_dict['V2']['WidthY']/2, 'drawing', Layers_dict['M3']['Color'][0]))

def left_array_top_plate_horizontal(x, y2, Layers_dict, Terminal_list, cap):
    plt.gca().add_patch(patches.Rectangle((x-Layers_dict['M3']['Width']/2-Layers_dict['V2']['VencA_L'], y2-Layers_dict['M2']['Width']/2), Layers_dict['M3']['Space']+Layers_dict['M3']['Width']+Layers_dict['M3']['Width']/2+Layers_dict['V2']['VencA_L']+cap.pin_x+cap.overlap, Layers_dict['M2']['Width'], color='pink'))
    wire_segment_1=wire('M2', None, Layers_dict['M2']['Direction'])
    Terminal_list.append(wire_segment_1.segment(x-Layers_dict['M3']['Width']/2-Layers_dict['V2']['VencA_L'], y2-Layers_dict['M2']['Width']/2, x+Layers_dict['M3']['Space']+Layers_dict['M3']['Width']+cap.pin_x+cap.overlap, y2+Layers_dict['M2']['Width']/2, 'drawing', Layers_dict['M2']['Color'][1]))

def right_array_top_plate_horizontal(x, y2, Layers_dict, Terminal_list, cap):
    x1=x-Layers_dict['M3']['Space']-Layers_dict['M3']['Width']
    plt.gca().add_patch(patches.Rectangle((x1-cap.pin_x-cap.overlap, y2-Layers_dict['M2']['Width']/2), Layers_dict['M3']['Space']+Layers_dict['M3']['Width'] +Layers_dict['M3']['Width']/2+Layers_dict['V2']['VencA_L']+cap.pin_x+cap.overlap, Layers_dict['M2']['Width'], color='pink'))
    wire_segment_1=wire('M2', None, Layers_dict['M2']['Direction'])
    Terminal_list.append(wire_segment_1.segment(x1-cap.pin_x-cap.overlap, y2-Layers_dict['M2']['Width']/2, x+Layers_dict['M3']['Width']+Layers_dict['V2']['VencA_L']+cap.overlap, y2+Layers_dict['M2']['Width']/2, 'drawing', Layers_dict['M2']['Color'][1]))

def bottom_plate_vertical(x, y, y1, y2, Layers_dict, Terminal_list, cap):
    plt.gca().add_patch(patches.Rectangle((x-Layers_dict['M1']['Width']/2, y-Layers_dict['V1']['VencA_L']-Layers_dict['V1']['WidthY']/2),  Layers_dict['M1']['Width'], abs(y1-y2)+2*Layers_dict['V1']['VencA_L']+Layers_dict['V1']['WidthY'],color='r')) 
    wire_segment_1=wire('M1', None, Layers_dict['M1']['Direction'])
    Terminal_list.append(wire_segment_1.segment(x-Layers_dict['M1']['Width']/2, y-Layers_dict['V1']['VencA_L']-Layers_dict['V1']['WidthY']/2, x+Layers_dict['M1']['Width']/2, y+abs(y1-y2)+Layers_dict['V1']['WidthY']/2+Layers_dict['V1']['VencA_L'], 'drawing', Layers_dict['M1']['Color'][0]))

def left_array_bottom_plate_horizontal(x, y2, Layers_dict, Terminal_list, cap):
    plt.gca().add_patch(patches.Rectangle((x-Layers_dict['M1']['Width']/2-Layers_dict['V1']['VencA_L'], y2-Layers_dict['M2']['Width']/2), Layers_dict['M1']['Space']+Layers_dict['M1']['Width']+Layers_dict['M1']['Width']/2+Layers_dict['V1']['VencA_H']+cap.pin_x+cap.overlap,  Layers_dict['M2']['Width'], color='b'))
    wire_segment_1=wire('M2', None, Layers_dict['M2']['Direction'])
    Terminal_list.append(wire_segment_1.segment(x-Layers_dict['M1']['Width']/2-Layers_dict['V1']['VencA_L'], y2-Layers_dict['M2']['Width']/2, x+Layers_dict['M1']['Space']+Layers_dict['M1']['Width']+cap.pin_x+cap.overlap, y2+Layers_dict['M2']['Width']/2, 'drawing', Layers_dict['M2']['Color'][0]))
        
def right_array_bottom_plate_horizontal(x, y2, Layers_dict, Terminal_list, cap):
    x1=x-Layers_dict['M1']['Space']-Layers_dict['M1']['Width']
    plt.gca().add_patch(patches.Rectangle((x1-cap.pin_x-cap.overlap, y2-Layers_dict['M2']['Width']/2), Layers_dict['M1']['Space']+Layers_dict['M1']['Width']+Layers_dict['M1']['Width']/2+Layers_dict['V1']['VencA_H']+cap.pin_x+cap.overlap, Layers_dict['M2']['Width'], color='b'))
    wire_segment_1=wire('M2', None, Layers_dict['M2']['Direction'])
    Terminal_list.append(wire_segment_1.segment(x1-cap.pin_x-cap.overlap, y2-Layers_dict['M2']['Width']/2, x+Layers_dict['M1']['Width']+Layers_dict['V1']['VencA_L']+cap.overlap, y2+Layers_dict['M2']['Width']/2, 'drawing', Layers_dict['M2']['Color'][0]))
    
def bottom_plate_via(x, y_via_k, height, Layers_dict, Terminal_list, cap):
    plt.gca().add_patch(patches.Rectangle((x-Layers_dict['V1']['WidthX']/2, y_via_k-Layers_dict['V1']['WidthY']/2), Layers_dict['V1']['WidthX'], Layers_dict['V1']['WidthY'],   color='lime'))
    wire_segment_1=via('V1', None)
    Terminal_list.append(wire_segment_1.segment(x-Layers_dict['V1']['WidthX']/2, y_via_k-Layers_dict['V1']['WidthY']/2, x+Layers_dict['V1']['WidthX']/2, y_via_k+Layers_dict['V1']['WidthY']/2, 'drawing'))   

def top_plate_via(x, y_via_k, height, Layers_dict, Terminal_list, cap):
    plt.gca().add_patch(patches.Rectangle((x-Layers_dict['V2']['WidthX']/2, y_via_k-Layers_dict['V2']['WidthY']/2), Layers_dict['V2']['WidthX'], Layers_dict['V2']['WidthY'],   color='lime'))
    wire_segment_1=via('V2', None)
    Terminal_list.append(wire_segment_1.segment(x-Layers_dict['V2']['WidthX']/2, y_via_k-Layers_dict['V2']['WidthY']/2, x+Layers_dict['V2']['WidthX']/2, y_via_k+Layers_dict['V2']['WidthY']/2, 'drawing'))   

    
def Generalized_plot_top_bottom_3(Capcitor, new_list, Device_Name, mat, row, column, width, sx, height, sy, color, line_width, color_mat, metal_layer_number, wire_width, spacing, Terminal_list, Layers_dict, cap):

    y_val=[]
    #print('Capcitor[i][j].y_coordinate_new', Capcitor[3][0].y_coordinate_new)
    
    for i in range (len(Capcitor)):
        for j in range (len(Capcitor[i])):
            if Capcitor[i][j].y_coordinate_new not in y_val and Capcitor[i][j].y_coordinate_new!=0:
                y_val.append(abs(Capcitor[i][j].y_coordinate_new )) 
    


    y_port=cap.pin_y+Layers_dict['M2']['Width']/2
    y_port_top=cap.pin_y_top+Layers_dict['M2']['Width']/2
    x_port=Layers_dict['M1']['Space']+Layers_dict['M1']['Width']
    x_port_top=Layers_dict['M3']['Space']+Layers_dict['M3']['Width']
    
    
    for i in range (len(Capcitor)): 
        for j in range (len(Capcitor[i])): 
            if Capcitor[i][j].all_marked==1:
                continue        
            stack=[]
            stack_n=[]
            stack_n.append(Capcitor[i][j].identity_n)
            stack.append(Capcitor[i][j].identity)

            p=0
            new_k=j
            
            
            
            while (len(stack_n)!=0):   


                for q in range (len(Capcitor[i])):
                    if stack_n[p]==Capcitor[i][q].identity_n:
                        new_k=q

                                    
                for k in range (len(Capcitor[i])):  
                    d=((stack_n[p][0]-Capcitor[i][k].x_coordinate)**2+(stack_n[p][1]-Capcitor[i][k].y_coordinate)**2)**(1/2)                               
    
                    if d==1  :
    
                        if Capcitor[i][k].all_marked==0:
                            
                            Capcitor[i][k].all_marked=1
                            Capcitor[i][new_k].branch_number=Capcitor[i][new_k].branch_number+1
                            Capcitor[i][k].parent=new_k
                            Capcitor[i][new_k].child.append(k)                                    
                            
    
                            if stack_n[p][0]==Capcitor[i][k].x_coordinate:                               
                                if Capcitor[i][k].x_coordinate_new<=0:
                                    x=Capcitor[i][k].x_coordinate_new-width/2-x_port
                                    y=0

                                    y1=Capcitor[i][k].y_coordinate_new-height/2+y_port   
                                    y2=Capcitor[i][new_k].y_coordinate_new-height/2+y_port                                     
                                    if Capcitor[i][k].y_coordinate_new>Capcitor[i][new_k].y_coordinate_new:
                                        y=y2
                                    else:
                                        y=y1
                                    #print('y1 and y2 here', y1, y2, y)
                                    bottom_plate_vertical(x, y, y1, y2, Layers_dict, Terminal_list, cap)

                                    left_array_bottom_plate_horizontal(x, y1, Layers_dict, Terminal_list, cap)
                                    bottom_plate_via(x, y1, height, Layers_dict, Terminal_list, cap)

                                    left_array_bottom_plate_horizontal(x, y2, Layers_dict, Terminal_list, cap)
                                    bottom_plate_via(x, y2, height, Layers_dict, Terminal_list, cap)
                                    
   
                                    x=Capcitor[i][k].x_coordinate_new-width/2-x_port_top
                                   
                                    y=0
                                    y1=Capcitor[i][k].y_coordinate_new+height/2-y_port_top                                     
                                    y2=Capcitor[i][new_k].y_coordinate_new+height/2-y_port_top 
                                    
                                    if Capcitor[i][k].y_coordinate_new>Capcitor[i][new_k].y_coordinate_new:
                                        y=y2
                                    else:
                                        y=y1
                                    
                                    top_plate_vertical(x, y, y1, y2, Layers_dict, Terminal_list, cap)

                                    left_array_top_plate_horizontal(x, y1, Layers_dict, Terminal_list, cap)
                                    top_plate_via(x, y1, height, Layers_dict, Terminal_list, cap)
                                    
                                    left_array_top_plate_horizontal(x, y2, Layers_dict, Terminal_list, cap)
                                    top_plate_via(x, y2, height, Layers_dict, Terminal_list, cap)
 
                                        
                                else:
                                    x=Capcitor[i][k].x_coordinate_new+width/2+x_port
                                    
                                    y1=Capcitor[i][k].y_coordinate_new-height/2+y_port                                   
                                    y2=Capcitor[i][new_k].y_coordinate_new-height/2+y_port 
                                    y=0
                                    
                                    if Capcitor[i][k].y_coordinate_new>Capcitor[i][new_k].y_coordinate_new:
                                        y=y2 
                                    else:
                                        y=y1
                                    
                                    bottom_plate_vertical(x, y, y1, y2, Layers_dict, Terminal_list, cap)
                                    right_array_bottom_plate_horizontal(x, y2, Layers_dict, Terminal_list, cap)
                                    bottom_plate_via(x, y2, height, Layers_dict, Terminal_list, cap)                                    

                                    right_array_bottom_plate_horizontal(x, y1, Layers_dict, Terminal_list, cap)
                                    bottom_plate_via(x, y1, height, Layers_dict, Terminal_list, cap) 
    
                                    x=Capcitor[i][k].x_coordinate_new+width/2+x_port_top
                                    
                                    y1=Capcitor[i][k].y_coordinate_new+height/2-y_port_top                                     
                                    y2=Capcitor[i][new_k].y_coordinate_new+height/2-y_port_top 

                                    y=0
                                    if Capcitor[i][k].y_coordinate_new>Capcitor[i][new_k].y_coordinate_new:
                                        y=y2 
                                    else:
                                        y=y1

                                    top_plate_vertical(x, y, y1, y2, Layers_dict, Terminal_list, cap)

                                    right_array_top_plate_horizontal(x, y1, Layers_dict, Terminal_list, cap)
                                    top_plate_via(x, y1, height, Layers_dict, Terminal_list, cap) 

                                    right_array_top_plate_horizontal(x, y2, Layers_dict, Terminal_list, cap)
                                    top_plate_via(x, y2, height, Layers_dict, Terminal_list, cap)                                    



                                        
        
    
                            if stack_n[p][1]==Capcitor[i][k].y_coordinate :
                              
                                x1=0
                                x2=0
                                y1=0
                                y2=0
                                x=0
                                if Capcitor[i][k].x_coordinate_new>stack[p][0]:
                                    x1=Capcitor[i][k].x_coordinate_new-width/2
                                    x2=Capcitor[i][new_k].x_coordinate_new+width/2
                                    x=x2
                                else:
                                    x1=Capcitor[i][k].x_coordinate_new+width/2
                                    x2=Capcitor[i][new_k].x_coordinate_new-width/2
                                    x=x1
                                    
                                #if  Capcitor[i][k].y_coordinate_new>=0:                                
                                y1=Capcitor[i][k].y_coordinate_new+height/2
                                y2=Capcitor[i][k].y_coordinate_new+height/2-Layers_dict['M2']['Width']                           
                                    
                                plt.gca().add_patch(patches.Rectangle((x-cap.pin_x-cap.overlap, y2-cap.pin_y_top), abs(x1-x2)+2*cap.pin_x+2*cap.overlap, Layers_dict['M2']['Width'], color='pink'))

                                wire_segment_1=wire('M2', None, Layers_dict['M2']['Direction'])
                                Terminal_list.append(wire_segment_1.segment(x-cap.pin_x-cap.overlap, y2-cap.pin_y_top, x+abs(x1-x2)+cap.pin_x+cap.overlap, y2-cap.pin_y_top+Layers_dict['M2']['Width'], 'drawing', Layers_dict['M2']['Color'][1]))


                                
                                if Capcitor[i][k].x_coordinate_new>stack[p][0]:
                                    x1=Capcitor[i][k].x_coordinate_new-width/2
                                    x2=Capcitor[i][new_k].x_coordinate_new+width/2
                                    x=x2
                                else:
                                    x1=Capcitor[i][k].x_coordinate_new+width/2
                                    x2=Capcitor[i][new_k].x_coordinate_new-width/2
                                    x=x1

                                y1=Capcitor[i][k].y_coordinate_new-height/2 
                                y2=Capcitor[i][k].y_coordinate_new-height/2 

                                plt.gca().add_patch(patches.Rectangle((x-cap.pin_x-cap.overlap, y2+cap.pin_y), abs(x1-x2)+2*cap.pin_x+2*cap.overlap, Layers_dict['M2']['Width'], color='b'))

                                wire_segment_1=wire('M2', None, Layers_dict['M2']['Direction'])
                                Terminal_list.append(wire_segment_1.segment(x-cap.pin_x-cap.overlap, y2+cap.pin_y, x+abs(x1-x2)+cap.pin_x+cap.overlap, y2+cap.pin_y+Layers_dict['M2']['Width'], 'drawing', Layers_dict['M2']['Color'][0]))

                                
    #########eeeeeeeeeeee
                               
                            stack_n.append(Capcitor[i][k].identity_n)      
                            stack.append(Capcitor[i][k].identity)    
                        Capcitor[i][j].all_marked=1 
                        #fff=1 
                        
                        
                stack_n.pop(0)
                stack.pop(0) 


def Split_top_plate(Capacitor, i, j, k, l, detailed_top):
    flag=0
    track=0
    for t in range (len(Capacitor[i][k].inter_connected)):
        for u in range (len(Capacitor[j][l].inter_connected)):                
            if Capacitor[i][k].inter_connect[t][0]==Capacitor[j][l].inter_connect[u][0] or Capacitor[i][k].inter_connect[t][0]-Capacitor[j][l].inter_connect[u][0]==1 or Capacitor[i][k].inter_connect[t][0]-Capacitor[j][l].inter_connect[u][0]==-1:
                (i_index, k_index)=capacitor_index(Capacitor, Capacitor[i][k].inter_connect[t][0], Capacitor[i][k].inter_connect[t][1])
                (j_index, l_index)=capacitor_index(Capacitor, Capacitor[j][l].inter_connect[t][0], Capacitor[j][l].inter_connect[t][1])
                br_fl=0
                for z in range (Capacitor[i_index][k_index].track_detailed_top):
                    for p in range (Capacitor[j_index][l_index].track_detailed_top):
                        if Capacitor[i_index][k_index].track_detailed_top[z]==Capacitor[j_index][l_index].track_detailed_top[p]:
                            track=Capacitor[i_index][k_index].track_detailed_top[z]
                            br_fl=1
                            break 
                    if br_fl==1:
                        break
                flag=1
                
    return track, flag


def Top_plate_routing_plot_Split_DAC(Capcitor, mat, row, column, width, sx, height, sy, color, line_width, center_x, spacing, wire_width, Terminal_list, Layers_dict, cap, detailed_tr_top, horizontal, horizontal_track_new_top, maximum_y):

    total_bottom_length=0
    length_top_1=0
                            
                
    y_port=cap.pin_y+Layers_dict['M2']['Width']/2
    x_port_top=Layers_dict['M3']['Space']+Layers_dict['M3']['Width']
       
    
    wire_length_MSB=0
    wire_length_LSB=0
    top_via_counted=[]
    for i in range (len(Capcitor)): 
        for j in range (len(Capcitor[i])): 
            if Capcitor[i][j].marked_even==1 :                
                continue
            
            #print('what are the i, j',Capcitor[i][j].inter_connect, i,j)
            # if len(Capcitor[i][j].inter_connect)!=0 and i%2==0 and i!=cap.bridge:
            if len(Capcitor[i][j].inter_connect)!=0 and Capcitor[i][0].tag=='LSB' :
                i_j=[]
                i_j.append(i)
                i_j.append(j)
                Capcitor[i][j].inter_connected_even.append(i_j)
                
            stack=[]
            stack_n=[]
            stack_n.append(Capcitor[i][j].inter_connect)            
            stack.append(Capcitor[i][j].inter_connected)
            
            p=0
            while (len(stack)!=0): 
                Capcitor[i][j].marked_even=1
                for l in range (len(Capcitor)):
                    for k in range (len(Capcitor[l])):
                        flag=0                       
                            
                        if len(Capcitor[l][k].inter_connect)!=0 and Capcitor[l][0].tag=='LSB'  and len(Capcitor[i][j].inter_connect)!=0 and Capcitor[i][0].tag=='LSB':
                            
                            for t in range (len(stack[p])):
                                for u in range (len(Capcitor[l][k].inter_connected)):
                                    d=((stack_n[p][t][0]-Capcitor[l][k].inter_connect[u][0])**2+(stack_n[p][t][1]-Capcitor[l][k].inter_connect[u][1])**2)**(1/2)==1  
                                    
                                    if d==1  :
                                        
                                        
                                        if Capcitor[l][k].marked_even==0:
                                            Capcitor[l][k].marked_even=1
                                            #print('stack==', stack[p], 'and interconnect==',Capcitor[l][k].inter_connect)
                                            if stack_n[p][t][0]==Capcitor[l][k].inter_connect[u][0]:
                                                #print('for which cap are u cming', Capcitor[l][k].inter_connect[u], stack_n[p][t])
                                                if Capcitor[l][k].inter_connect[u] not in top_via_counted:
                                                    top_via_counted.append(Capcitor[l][k].inter_connect[u])
                                                    Capcitor[l][k].via_number_top=Capcitor[l][k].via_number_top+1 
                                                if stack_n[p][t] not in top_via_counted:
                                                    (i_index, j_index)=capacitor_index(Capcitor, stack_n[p][t][0], stack_n[p][t][1])
                                                    top_via_counted.append(stack_n[p][t])
                                                    Capcitor[i_index][j_index].via_number_top=Capcitor[i_index][j_index].via_number_top+1 
                                                
                                                wire_length_LSB=wire_length_LSB+sy+height
                                                flag=1
                                                
                                                y1=stack[p][t][1]+height/2-y_port
                                                y2=Capcitor[l][k].inter_connected[u][1]+height/2-y_port
                                                

            
                                                if stack_n[p][t][0]<=center_x:

                                                    x=stack[p][t][0]-width/2-x_port_top
                                                   
                                                    y=0
                                                    y1=stack[p][t][1]+height/2-y_port                                     
                                                    y2=Capcitor[l][k].inter_connected[u][1]+height/2-y_port 
                                                    
                                                    if stack[p][t][1]>Capcitor[l][k].inter_connected[u][1]:
                                                        y=y2
                                                    else:
                                                        y=y1
                
                                                    top_plate_vertical(x, y, y1, y2, Layers_dict, Terminal_list, cap)
                                                    left_array_top_plate_horizontal(x, y2, Layers_dict, Terminal_list, cap)
                                                    left_array_top_plate_horizontal(x, y1, Layers_dict, Terminal_list, cap)
                                                    top_plate_via(x, y2, height, Layers_dict, Terminal_list, cap)  
                                                    top_plate_via(x, y1, height, Layers_dict, Terminal_list, cap)  

                                                    fl_t=horizontal(i, round(x,5), stack[p][t][1], stack[p][t][0], horizontal_track_new_top, sx, y1)
                                                    h_t=fl_t.insert(round(y1,5))
                                                    horizontal_track_new_top.append(h_t)

                                                    fl_t=horizontal(i, round(x,5), Capcitor[l][k].inter_connected[u][1], Capcitor[l][k].inter_connected[u][0], horizontal_track_new_top, sx, y2)
                                                    h_t=fl_t.insert(round(y2,5))
                                                    horizontal_track_new_top.append(h_t)

                                                else:
                                                    x=stack[p][t][0]+width/2+x_port_top
                                                    
                                                    y1=stack[p][t][1]+height/2-y_port                                     
                                                    y2=Capcitor[l][k].inter_connected[u][1]+height/2-y_port 
                
                                                    y=0
                                                    if stack[p][t][1]>Capcitor[l][k].inter_connected[u][1]:
                                                        y=y2 
                                                    else:
                                                        y=y1
                
                                                    top_plate_vertical(x, y, y1, y2, Layers_dict, Terminal_list, cap)
                                                    right_array_top_plate_horizontal(x, y2, Layers_dict, Terminal_list, cap)
                                                    top_plate_via(x, y2, height, Layers_dict, Terminal_list, cap) 
                                                    right_array_top_plate_horizontal(x, y1, Layers_dict, Terminal_list, cap)
                                                    top_plate_via(x, y1, height, Layers_dict, Terminal_list, cap)
                                                    
                                                    fl_t=horizontal(i, round(x,5), stack[p][t][1], stack[p][t][0], horizontal_track_new_top, sx, y1)
                                                    h_t=fl_t.insert(round(y1,5))
                                                    horizontal_track_new_top.append(h_t)

                                                    fl_t=horizontal(i, round(x,5), Capcitor[l][k].inter_connected[u][1], Capcitor[l][k].inter_connected[u][0], horizontal_track_new_top, sx, y2)
                                                    h_t=fl_t.insert(round(y2,5))
                                                    horizontal_track_new_top.append(h_t)
                                                    
                                                length_top_1=length_top_1+sy
                                                total_bottom_length=total_bottom_length+sy
                                                
                                            elif stack_n[p][t][1]==Capcitor[l][k].inter_connect[u][1]:
                                                wire_length_LSB=wire_length_LSB+sx+2*cap.pin_x
                                                
                                                x1=0
                                                flag=1
                
                                                x1=0
                                                x2=0
                                                y1=0
                                                y2=0
                                                x=0
                                                if  Capcitor[l][k].inter_connected[u][0]<stack[p][t][0]:
                                                    x1=stack[p][t][0]-width/2
                                                    x2=Capcitor[l][k].inter_connected[u][0]+width/2
                                                    x=x2
                                                else:
                                                    x1=stack[p][t][0]+width/2
                                                    x2=Capcitor[l][k].inter_connected[u][0]-width/2
                                                    x=x1
                                                    
                                                #if  Capcitor[i][k].y_coordinate_new>=0:                                
                                                y1=stack[p][t][1]+height/2
                                                y2=stack[p][t][1]+height/2-Layers_dict['M2']['Width']                           
                                                    
                                                plt.gca().add_patch(patches.Rectangle((x-cap.pin_x, y2-cap.pin_y_top), abs(x1-x2)+2*cap.pin_x, Layers_dict['M2']['Width'], color='pink'))
                
                                                wire_segment_1=wire('M2', None, Layers_dict['M2']['Direction'])
                                                Terminal_list.append(wire_segment_1.segment(x-cap.pin_x, y2-cap.pin_y_top, x+abs(x1-x2)+cap.pin_x, y2-cap.pin_y_top+Layers_dict['M2']['Width'], 'drawing', Layers_dict['M2']['Color'][1]))

                                                
                                                length_top_1=length_top_1+sx
                                                total_bottom_length=total_bottom_length+sx
                                                
                                            if len(Capcitor[l][k].inter_connect)!=0 and  Capcitor[l][0].tag=='LSB'  and l!=cap.bridge:
                                                l_k=[]
                                                l_k.append(l)
                                                l_k.append(k)
                                                Capcitor[i][j].inter_connected_even.append(l_k)
                                            
                                            stack_n.append(Capcitor[l][k].inter_connect) 
                                            stack.append(Capcitor[l][k].inter_connected)
                                          
                                            
                                        
                                        if flag==1:
                                            break
                                    
                                    if flag==1:
                                        break
                                    
                        
                stack.pop(0) 
                stack_n.pop(0) 


    for i in range (len(Capcitor)): 
        for j in range (len(Capcitor[i])): 
            if Capcitor[i][j].marked_odd==1 :
                
                continue
            
            #print('what are the i, j',Capcitor[i][j].inter_connect, i,j)
            # if len(Capcitor[i][j].inter_connect)!=0 and i%2!=0 and i!=cap.bridge :
            if len(Capcitor[i][j].inter_connect)!=0 and Capcitor[i][0].tag=='MSB'  :
                i_j=[]
                i_j.append(i)
                i_j.append(j)
                Capcitor[i][j].inter_connected_odd.append(i_j)
            stack=[]
            stack_n=[]
            stack_n.append(Capcitor[i][j].inter_connect)            
            stack.append(Capcitor[i][j].inter_connected)
            
            p=0
            while (len(stack)!=0): 
                Capcitor[i][j].marked_odd=1
                for l in range (len(Capcitor)):
                    for k in range (len(Capcitor[l])):
                        flag=0
                        # if len(Capcitor[l][k].inter_connect)!=0 and l%2!=0  and len(Capcitor[i][j].inter_connect)!=0 and i%2!=0 and i!=cap.bridge and l!=cap.bridge:
                        if len(Capcitor[l][k].inter_connect)!=0 and  Capcitor[l][0].tag=='MSB'  and len(Capcitor[i][j].inter_connect)!=0 and Capcitor[i][0].tag=='MSB' :
                            
                            for t in range (len(stack[p])):
                                for u in range (len(Capcitor[l][k].inter_connected)):
                                    d=((stack_n[p][t][0]-Capcitor[l][k].inter_connect[u][0])**2+(stack_n[p][t][1]-Capcitor[l][k].inter_connect[u][1])**2)**(1/2)==1  
                                    
                                    if d==1  :
                                        
    
                                        if Capcitor[l][k].marked_odd==0:
                                            Capcitor[l][k].marked_odd=1
                                            #print('stack==', stack_n[p], 'and interconnect==',Capcitor[l][k].inter_connect)
                                            if stack_n[p][t][0]==Capcitor[l][k].inter_connect[u][0]:
                                                # Capcitor[l][k].via_number_top=Capcitor[l][k].via_number_top+1 
                                                # Capcitor[i][j].via_number_top=Capcitor[i][j].via_number_top+1 
                                                if Capcitor[l][k].inter_connect[u] not in top_via_counted:
                                                    top_via_counted.append(Capcitor[l][k].inter_connect[u])
                                                    Capcitor[l][k].via_number_top=Capcitor[l][k].via_number_top+1 
                                                if stack_n[p][t] not in top_via_counted:
                                                    (i_index, j_index)=capacitor_index(Capcitor, stack_n[p][t][0], stack_n[p][t][1])
                                                    top_via_counted.append(stack_n[p][t])
                                                    Capcitor[i_index][j_index].via_number_top=Capcitor[i_index][j_index].via_number_top+1 

                                                #print('for which cap are u cming MSB', Capcitor[l][k].inter_connect[u], stack_n[p][t])
                                                wire_length_MSB=wire_length_MSB+sy+height
                                                flag=1
                                                
                                                y1=stack[p][t][1]+height/2-y_port
                                                y2=Capcitor[l][k].inter_connected[u][1]+height/2-y_port
                                                

            
                                                if stack_n[p][t][0]<=center_x:

                                                    x=stack[p][t][0]-width/2-x_port_top
                                                   
                                                    y=0
                                                    y1=stack[p][t][1]+height/2-y_port                                     
                                                    y2=Capcitor[l][k].inter_connected[u][1]+height/2-y_port 
                                                    
                                                    if stack[p][t][1]>Capcitor[l][k].inter_connected[u][1]:
                                                        y=y2
                                                    else:
                                                        y=y1
                
                                                    top_plate_vertical(x, y, y1, y2, Layers_dict, Terminal_list, cap)
                                                    left_array_top_plate_horizontal(x, y2, Layers_dict, Terminal_list, cap)
                                                    left_array_top_plate_horizontal(x, y1, Layers_dict, Terminal_list, cap)
                                                    top_plate_via(x, y2, height, Layers_dict, Terminal_list, cap)  
                                                    top_plate_via(x, y1, height, Layers_dict, Terminal_list, cap)  

                                                    fl_t=horizontal(i, round(x,5), stack[p][t][1], stack[p][t][0], horizontal_track_new_top, sx, y1)
                                                    h_t=fl_t.insert(round(y1,5))
                                                    horizontal_track_new_top.append(h_t)

                                                    fl_t=horizontal(i, round(x,5), Capcitor[l][k].inter_connected[u][1], Capcitor[l][k].inter_connected[u][0], horizontal_track_new_top, sx, y2)
                                                    h_t=fl_t.insert(round(y2,5))
                                                    horizontal_track_new_top.append(h_t)

                                                else:
                                                    x=stack[p][t][0]+width/2+x_port_top
                                                    
                                                    y1=stack[p][t][1]+height/2-y_port                                     
                                                    y2=Capcitor[l][k].inter_connected[u][1]+height/2-y_port 
                
                                                    y=0
                                                    if stack[p][t][1]>Capcitor[l][k].inter_connected[u][1]:
                                                        y=y2 
                                                    else:
                                                        y=y1
                
                                                    top_plate_vertical(x, y, y1, y2, Layers_dict, Terminal_list, cap)
                                                    right_array_top_plate_horizontal(x, y2, Layers_dict, Terminal_list, cap)
                                                    top_plate_via(x, y2, height, Layers_dict, Terminal_list, cap) 
                                                    right_array_top_plate_horizontal(x, y1, Layers_dict, Terminal_list, cap)
                                                    top_plate_via(x, y1, height, Layers_dict, Terminal_list, cap)
                                                    
                                                    fl_t=horizontal(i, round(x,5), stack[p][t][1], stack[p][t][0], horizontal_track_new_top, sx, y1)
                                                    h_t=fl_t.insert(round(y1,5))
                                                    horizontal_track_new_top.append(h_t)

                                                    fl_t=horizontal(i, round(x,5), Capcitor[l][k].inter_connected[u][1], Capcitor[l][k].inter_connected[u][0], horizontal_track_new_top, sx, y2)
                                                    h_t=fl_t.insert(round(y2,5))
                                                    horizontal_track_new_top.append(h_t)
                                                    
                                                length_top_1=length_top_1+sy
                                                #total_bottom_length=total_bottom_length+sy
                                                
                                            elif stack_n[p][t][1]==Capcitor[l][k].inter_connect[u][1]:
                                                wire_length_MSB=wire_length_MSB+sx+2*cap.pin_x
                                                x1=0
                                                flag=1
                
                                                x1=0
                                                x2=0
                                                y1=0
                                                y2=0
                                                x=0
                                                if  Capcitor[l][k].inter_connected[u][0]<stack[p][t][0]:
                                                    x1=stack[p][t][0]-width/2
                                                    x2=Capcitor[l][k].inter_connected[u][0]+width/2
                                                    x=x2
                                                else:
                                                    x1=stack[p][t][0]+width/2
                                                    x2=Capcitor[l][k].inter_connected[u][0]-width/2
                                                    x=x1
                                                    
                                                #if  Capcitor[i][k].y_coordinate_new>=0:                                
                                                y1=stack[p][t][1]+height/2
                                                y2=stack[p][t][1]+height/2-Layers_dict['M2']['Width']                           
                                                    
                                                plt.gca().add_patch(patches.Rectangle((x-cap.pin_x, y2-cap.pin_y_top), abs(x1-x2)+2*cap.pin_x, Layers_dict['M2']['Width'], color='pink'))
                
                                                wire_segment_1=wire('M2', None, Layers_dict['M2']['Direction'])
                                                Terminal_list.append(wire_segment_1.segment(x-cap.pin_x, y2-cap.pin_y_top, x+abs(x1-x2)+cap.pin_x, y2-cap.pin_y_top+Layers_dict['M2']['Width'], 'drawing', Layers_dict['M2']['Color'][1]))

                                                
                                                length_top_1=length_top_1+sx
                                                #total_bottom_length=total_bottom_length+sx

                                            l_k=[]
                                            l_k.append(l)
                                            l_k.append(k)                                                
                                            # if len(Capcitor[l][k].inter_connect)!=0 and l%2!=0 and l!=cap.bridge and l_k not in Capcitor[i][j].inter_connected_odd:
                                            # if len(Capcitor[l][k].inter_connect)!=0 and l%2!=0 and l!=cap.bridge :
                                            if len(Capcitor[l][k].inter_connect)!=0 and   Capcitor[l][0].tag=='MSB' :

                                                Capcitor[i][j].inter_connected_odd.append(l_k)
                                            
                                            stack_n.append(Capcitor[l][k].inter_connect) 
                                            stack.append(Capcitor[l][k].inter_connected)
                                          
                                        
                                        if flag==1:
                                            break
                                    
                                    if flag==1:
                                        break
                                    
                        
                stack.pop(0) 
                stack_n.pop(0) 


    obj_LSB=[]
    obj_MSB=[]
    for i in range (len(Capcitor)):        
        for j in range (len(Capcitor[i])):
            if len(Capcitor[i][j].inter_connected_even)!=0: 
                obj_LSB.append(LSB(Capcitor[i][j].inter_connected_even))
                
            if len(Capcitor[i][j].inter_connected_odd)!=0: 
                obj_MSB.append(MSB(Capcitor[i][j].inter_connected_odd))

    all_odd_c=[]
    all_odd_conn=[]
    obj_MSB_1=obj_MSB[0].odd_connected
    length_odd_groups=[]
    for i in range (len(obj_MSB)):
        for j in range (len(obj_MSB[i].odd_connected)):
            length_odd_groups.append(obj_MSB[i].odd_connected[j])
    #print('length_odd_groups',length_odd_groups, obj_MSB_1, obj_MSB_1[0])
    
    obj_MSB_collection=[]
    assigned=[]
    tracks=[]
    detailed_tr_top_odd=[]
    LSB_tracks=[]
    MSB_tracks=[]
    #tracks
    while len(obj_MSB_1)!=len(length_odd_groups):
    #for i in range (len(obj_MSB)):
        
        left_side=[]
        right_side=[] 
        flag=0
        l_list=[]
        select_one_side=0
        
        for l in range (len(obj_MSB)):
            for i in range (len(obj_MSB_1)):
                flag_break=0
            
                i_l=[]
                i_l.append(obj_MSB_1[0])
                i_l.append(obj_MSB[l].odd_connected[0])
                i_k=[]
                i_k.append(obj_MSB[l].odd_connected[0])
                i_k.append(obj_MSB_1[0]) 
                
                # if i_l not in all_odd_c and i_k not in all_odd_c and obj_MSB[l].odd_connected[0] not in all_odd_conn:                 
                #if i_l not in all_odd_c and i_k not in all_odd_c :                 
                if  obj_MSB[l].odd_connected[0] not in obj_MSB_1 and i_l not in assigned and i_k not in assigned:                 
                    for k in range (len(obj_MSB[l].odd_connected)): 
                    
                                       
                        for t in range (len(Capcitor[obj_MSB_1[i][0]][obj_MSB_1[i][1]].inter_connected)):
                            for u in range (len(Capcitor[obj_MSB[l].odd_connected[k][0]][obj_MSB[l].odd_connected[k][1]].inter_connected)):
                                if Capcitor[obj_MSB_1[i][0]][obj_MSB_1[i][1]].inter_connect[t][0]-Capcitor[obj_MSB[l].odd_connected[k][0]][obj_MSB[l].odd_connected[k][1]].inter_connect[u][0]==0 or Capcitor[obj_MSB_1[i][0]][obj_MSB_1[i][1]].inter_connect[t][0]-Capcitor[obj_MSB[l].odd_connected[k][0]][obj_MSB[l].odd_connected[k][1]].inter_connect[u][0]==1 or Capcitor[obj_MSB_1[i][0]][obj_MSB_1[i][1]].inter_connect[t][0]-Capcitor[obj_MSB[l].odd_connected[k][0]][obj_MSB[l].odd_connected[k][1]].inter_connect[u][0]==-1:
                                    l_list.append(l)
                                        
                                    flag=1                                        
                                    (i_index, j_index)=capacitor_index(Capcitor, Capcitor[obj_MSB_1[i][0]][obj_MSB_1[i][1]].inter_connect[t][0], Capcitor[obj_MSB_1[i][0]][obj_MSB_1[i][1]].inter_connect[t][1])
                                    
                                    (l_index, k_index)=capacitor_index(Capcitor, Capcitor[obj_MSB[l].odd_connected[k][0]][obj_MSB[l].odd_connected[k][1]].inter_connect[u][0], Capcitor[obj_MSB[l].odd_connected[k][0]][obj_MSB[l].odd_connected[k][1]].inter_connect[u][1])
                                
                                if Capcitor[obj_MSB_1[i][0]][obj_MSB_1[i][1]].inter_connect[t][0]-Capcitor[obj_MSB[l].odd_connected[k][0]][obj_MSB[l].odd_connected[k][1]].inter_connect[u][0]==0 or Capcitor[obj_MSB_1[i][0]][obj_MSB_1[i][1]].inter_connect[t][0]-Capcitor[obj_MSB[l].odd_connected[k][0]][obj_MSB[l].odd_connected[k][1]].inter_connect[u][0]==-1:                                    
                                    flag_break=1
                                             

                                    l_s=[]
                                    l_s.append(i_index)
                                    l_s.append(j_index)
                                    l_s.append(l_index)
                                    l_s.append(k_index)                                    
                                    left_side.append(l_s)

                                        
                                    h_tracks_l=[]
                                    track_one=0
                                    for tr in range (1, len(Capcitor[left_side[p][0]][left_side[p][1]].track_detailed_top)):
                                        for tr_1 in range (1, len(Capcitor[left_side[p][2]][left_side[p][3]].track_detailed_top)):
                                            # if Capcitor[left_side[p][0]][left_side[p][1]].track_detailed_top[tr]==Capcitor[left_side[p][2]][left_side[p][3]].track_detailed_top[tr_1] and Capcitor[left_side[p][0]][left_side[p][1]].track_detailed_top[tr] not in detailed_tr_top:
                                            if Capcitor[left_side[p][0]][left_side[p][1]].track_detailed_top[tr]==Capcitor[left_side[p][2]][left_side[p][3]].track_detailed_top[tr_1] and Capcitor[left_side[p][0]][left_side[p][1]].track_detailed_top[tr] not in detailed_tr_top:
                                                track_one=Capcitor[left_side[p][0]][left_side[p][1]].track_detailed_top[tr]
                                                detailed_tr_top_odd.append(track_one)
                                                tracks.append(track_one)
                                                break
                                        if track_one!=0:
                                            break        
                                            
                                    track_l=track_one
                                    

                                    
                                    y_value_j=Capcitor[left_side[p][0]][left_side[p][1]].y_coordinate_new
                                    x_value_j=Capcitor[left_side[p][0]][left_side[p][1]].x_coordinate_new
                                    htrack=y_value_j+((cap.h)/2)-cap.pin_y_top-Layers_dict['M2']['Width']/2
                                    
                                    track_number=Capcitor[left_side[p][0]][left_side[p][1]].channel_width_l
                                    sx_channel=(track_number+1)*(Layers_dict['M3']['Space']+Layers_dict['M3']['Width'])                
                                    fl=horizontal(left_side[p][0], track_one, y_value_j, x_value_j, horizontal_track_new_top, sx_channel, htrack)
                                    
                                    new_f=fl.horizontal_routing_top_Split()
                                    collision_track=0
                                    
                                    if new_f==1:
                                        Capcitor[left_side[p][0]][left_side[p][1]].via_number_top=Capcitor[left_side[p][0]][left_side[p][1]].via_number_top+1 
                                        collision_track=cap.pin_y_top+Layers_dict['M2']['Space']+Layers_dict['M2']['Width']+Layers_dict['V2']['VencA_H']
                                        htrack=fl.horizontal_track_assign_top()
                                        cap.a_t_h_ratio.append(round(htrack,5))
                                        
                                                                  
                                    h_t=fl.insert(round(htrack,5))
                                    horizontal_track_new_top.append(h_t)
                                    h_tracks_l.append(round(htrack,5))
                                    
                                    Horizontal_track_plot_top(track_one, htrack, cap.w, cap.h, x_value_j, y_value_j, cap.line_w, 'r', new_f, Layers_dict, Terminal_list, cap)
                                    
                                            
                                    q=p
                                    #for q in range (len(left_side)):
                                        #   if left_side[p][0]==left_side[q][0] and left_side[p][1]==left_side[q][1]:
                                    y_value_p=Capcitor[left_side[q][2]][left_side[q][3]].y_coordinate_new
                                    x_value_p=Capcitor[left_side[q][2]][left_side[q][3]].x_coordinate_new
                                    htrack_o=y_value_p+((cap.h)/2)-cap.pin_y_top-Layers_dict['M2']['Width']/2
                                    
                                    track_number=Capcitor[left_side[q][2]][left_side[q][3]].channel_width_l
                                    sx_channel=(track_number+1)*(Layers_dict['M3']['Space']+Layers_dict['M3']['Width'])                
                                    fl=horizontal(left_side[q][2], track_one, y_value_p, x_value_p, horizontal_track_new_top, sx_channel, htrack)
                                    
                                    new_f=fl.horizontal_routing_top_Split()
                                    collision_track_2=0
                                    if new_f==1:
                                        Capcitor[left_side[q][2]][left_side[q][3]].via_number_top=Capcitor[left_side[q][2]][left_side[q][3]].via_number_top+1                                         
                                        collision_track_2=cap.pin_y_top+Layers_dict['M2']['Space']+Layers_dict['M2']['Width']+Layers_dict['V2']['VencA_H']
                                        htrack_o=fl.horizontal_track_assign_top()
                                        cap.a_t_h_ratio.append(round(htrack_o,5))
                                    
                                    htrack_list_1=[]
                                    htrack_list_1.append(round(htrack,5))
                                    htrack_list_1.append(round(htrack_o,5))
                                    
                                    MSB_track_dict={}
                                    
                                    MSB_track_dict['track']=track_one
                                    MSB_track_dict['htrack']=htrack_list_1
                                    
                                    MSB_tracks.append(MSB_track_dict)
                                    
                                    wire_2=abs(x_value_j-track_one)-(cap.w/2)+cap.pin_x+abs(x_value_p-track_one)-(cap.w/2)+cap.pin_x
                                    
                                    wire_length_MSB=wire_length_MSB+wire_2+collision_track+collision_track_2
                                    h_tracks_l.append(round(htrack_o,5)) 
                                                          
                                    h_t=fl.insert(round(htrack_o,5))
                                    horizontal_track_new_top.append(h_t)
                                    Horizontal_track_plot_top(track_one, htrack_o, cap.w, cap.h, x_value_p, y_value_p, cap.line_w, 'r', new_f, Layers_dict, Terminal_list, cap)
                                    
                                    color_r='r'
                                    index=0
                                    if len(h_tracks_l)!=0:    
                                        max_l=max(h_tracks_l)
                                        min_l=min(h_tracks_l)
                            
                                        var='D'+str(int(Capcitor[left_side[q][2]][left_side[q][3]].cap_name))
                                        trunk_routing(track_one, min_l, max_l, Layers_dict, Terminal_list, cap, color_r, index, var)                
                                        for ht in range (len(h_tracks_l)):
                                            x=track_one 
                                            y=h_tracks_l[ht]
                                            top_plate_via(x, y, height, Layers_dict, Terminal_list, cap)
                                    
                                    for kk in range (len(obj_MSB_1)):
                                    #obj_MSB[i].all_odd_connected.append(obj_MSB_1[kk])
                                        all_odd_conn.append(obj_MSB_1[kk])
                                        if obj_MSB_1[kk] not in obj_MSB_collection:
                                            obj_MSB_collection.append(obj_MSB_1[kk])
                                    
                        
                                    
                                    for l_k in range (len(l_list)):
                                        i_lk=[]
                                        i_lk.append(obj_MSB_1[i][0])
                                        i_lk.append(obj_MSB[l_list[l_k]].odd_connected[0])
                                        all_odd_c.append(i_lk)
                                        for kk in range (len(obj_MSB[l_list[l_k]].odd_connected)):
                                            #obj_MSB[i].all_odd_connected.append(obj_MSB[l_list[l_k]].odd_connected[kk])
                                            all_odd_conn.append(obj_MSB[l_list[l_k]].odd_connected[kk])
                                            if obj_MSB[l_list[l_k]].odd_connected[kk] not in obj_MSB_collection:
                                                obj_MSB_collection.append(obj_MSB[l_list[l_k]].odd_connected[kk])
                                
                                    # if Capcitor[obj_MSB[i].odd_connected[j][0]][obj_MSB[i].odd_connected[j][1]].inter_connect[t][0]-Capcitor[obj_MSB[l].odd_connected[k][0]][obj_MSB[l].odd_connected[k][1]].inter_connect[u][0]==0 or Capcitor[obj_MSB[i].odd_connected[j][0]][obj_MSB[i].odd_connected[j][1]].inter_connect[t][0]-Capcitor[obj_MSB[l].odd_connected[k][0]][obj_MSB[l].odd_connected[k][1]].inter_connect[u][0]==1:                                    
                                if  Capcitor[obj_MSB_1[i][0]][obj_MSB_1[i][1]].inter_connect[t][0]-Capcitor[obj_MSB[l].odd_connected[k][0]][obj_MSB[l].odd_connected[k][1]].inter_connect[u][0]==0 or Capcitor[obj_MSB_1[i][0]][obj_MSB_1[i][1]].inter_connect[t][0]-Capcitor[obj_MSB[l].odd_connected[k][0]][obj_MSB[l].odd_connected[k][1]].inter_connect[u][0]==1:                                    
                                    flag_break=1
                                    r_s=[]
                                    r_s.append(i_index)
                                    r_s.append(j_index)
                                    r_s.append(l_index)
                                    r_s.append(k_index)                                    
                                    right_side.append(r_s)
                                    
                                    track_one=0
                
                                    h_tracks_r=[]
                                    for tr in range (1, len(Capcitor[right_side[p][0]][right_side[p][1]].track_detailed_top)):
                                        for tr_1 in range (1, len(Capcitor[right_side[p][2]][right_side[p][3]].track_detailed_top)):
                                            if Capcitor[right_side[p][0]][right_side[p][1]].track_detailed_top[tr]==Capcitor[right_side[p][2]][right_side[p][3]].track_detailed_top[tr_1] and Capcitor[right_side[p][0]][right_side[p][1]].track_detailed_top[tr] not in detailed_tr_top:
                                                track_one=Capcitor[right_side[p][0]][right_side[p][1]].track_detailed_top[tr]
                                                detailed_tr_top_odd.append(track_one)
                                                tracks.append(track_one)
                                                break
                                        if track_one!=0:
                                            break        
                                            
                                    track_l=track_one

                                    y_value_j=Capcitor[right_side[p][0]][right_side[p][1]].y_coordinate_new
                                    x_value_j=Capcitor[right_side[p][0]][right_side[p][1]].x_coordinate_new
                                    htrack=y_value_j+((cap.h)/2)-cap.pin_y_top-Layers_dict['M2']['Width']/2
                                    
                                    track_number=Capcitor[right_side[p][0]][right_side[p][1]].channel_width_l
                                    sx_channel=(track_number+1)*(Layers_dict['M3']['Space']+Layers_dict['M3']['Width'])                
                                    fl=horizontal(right_side[p][0], track_one, y_value_j, x_value_j, horizontal_track_new_top, sx_channel, htrack)
                                    
                                    new_f=fl.horizontal_routing_top_Split()
                                    collision_track=0
                                    if new_f==1: 
                                        Capcitor[right_side[p][0]][right_side[p][1]].via_number_top=Capcitor[right_side[p][0]][right_side[p][1]].via_number_top+1                                         
                                        collision_track=cap.pin_y_top+Layers_dict['M2']['Space']+Layers_dict['M2']['Width']+Layers_dict['V2']['VencA_H']
                                        htrack=fl.horizontal_track_assign_top()
                                        cap.a_t_h_ratio.append(round(htrack,5))
                                                
                                                                      
                                    h_t=fl.insert(round(htrack,5))
                                    horizontal_track_new_top.append(h_t)
                                    h_tracks_r.append(round(htrack,5))
                                    
                                    
                                    Horizontal_track_plot_top(track_one, htrack, cap.w, cap.h, x_value_j, y_value_j, cap.line_w, 'r', new_f, Layers_dict, Terminal_list, cap)
                                    
                                    #wire_2=abs(x_value_j-track_one)-(cap.w/2)+cap.pin_x +Capcitor[right_side[0][0]][right_side[0][1]].inter_connect_length
                                    q=p
                                    #for q in range (len(right_side)):
                                        #if right_side[p][0]==right_side[q][0] and right_side[p][1]==right_side[q][1]:
                                    y_value_p=Capcitor[right_side[q][2]][right_side[q][3]].y_coordinate_new
                                    x_value_p=Capcitor[right_side[q][2]][right_side[q][3]].x_coordinate_new
                                    htrack_o=y_value_p+((cap.h)/2)-cap.pin_y_top-Layers_dict['M2']['Width']/2
                                    
                                    track_number=Capcitor[right_side[q][2]][right_side[q][3]].channel_width_l
                                    sx_channel=(track_number+1)*(Layers_dict['M3']['Space']+Layers_dict['M3']['Width'])                
                                    fl=horizontal(right_side[q][2], track_one, y_value_p, x_value_p, horizontal_track_new_top, sx_channel, htrack)
                                    
                                    new_f=fl.horizontal_routing_top_Split()
                                    collision_track_2=0
                                    if new_f==1:
                                        Capcitor[right_side[q][2]][right_side[q][3]].via_number_top=Capcitor[right_side[q][2]][right_side[q][3]].via_number_top+1                                         
                                        collision_track_2=cap.pin_y_top+Layers_dict['M2']['Space']+Layers_dict['M2']['Width']+Layers_dict['V2']['VencA_H']
                                        htrack_o=fl.horizontal_track_assign_top()
                                        cap.a_t_h_ratio.append(round(htrack_o,5))

                                    htrack_list_1=[]
                                    htrack_list_1.append(round(htrack,5))
                                    htrack_list_1.append(round(htrack_o,5))

                                    MSB_track_dict={}
                                    
                                    MSB_track_dict['track']=track_one
                                    MSB_track_dict['htrack']=htrack_list_1
                                    
                                    MSB_tracks.append(MSB_track_dict)


                                    wire_2=abs(x_value_j-track_one)-(cap.w/2)+cap.pin_x+abs(x_value_p-track_one)-(cap.w/2)+cap.pin_x
                                    
                                    wire_length_MSB=wire_length_MSB+wire_2+collision_track+collision_track_2
                                        
                                    h_tracks_r.append(round(htrack_o,5))
                                                         
                                    h_t=fl.insert(round(htrack_o,5))
                                    horizontal_track_new_top.append(h_t)
                                    Horizontal_track_plot_top(track_one, htrack_o, cap.w, cap.h, x_value_p, y_value_p, cap.line_w, 'r', new_f, Layers_dict, Terminal_list, cap)
                                    color_r='r'
                                    index=0
                                    if len(h_tracks_r)!=0:    
                                        max_l=max(h_tracks_r)
                                        min_l=min(h_tracks_r)
                            
                                        var='D'+str(int(Capcitor[right_side[q][2]][right_side[q][3]].cap_name))
                                        trunk_routing(track_one, min_l, max_l, Layers_dict, Terminal_list, cap, color_r, index, var)                
                                        for ht in range (len(h_tracks_r)):
                                            x=track_one 
                                            y=h_tracks_r[ht]
                                            top_plate_via(x, y, height, Layers_dict, Terminal_list, cap)
                    
                                    for kk in range (len(obj_MSB_1)):
                                        all_odd_conn.append(obj_MSB_1[kk])
                                        if obj_MSB_1[kk] not in obj_MSB_collection:
                                            obj_MSB_collection.append(obj_MSB_1[kk])
                                    
                        
                                    
                                    for l_k in range (len(l_list)):
                                        for kk in range (len(obj_MSB[l_list[l_k]].odd_connected)):
                                            all_odd_conn.append(obj_MSB[l_list[l_k]].odd_connected[kk])
                                            if obj_MSB[l_list[l_k]].odd_connected[kk] not in obj_MSB_collection:
                                                obj_MSB_collection.append(obj_MSB[l_list[l_k]].odd_connected[kk])


                                if flag_break==1:
                                    break
                            if flag_break==1:
                                break
                        if flag_break==1:
                            break
                    if flag_break==1:
                        break
            if flag_break==1:
                break
                    
        
        for ll in range (len(l_list)):
            i_ll=[]
            i_ll.append(obj_MSB_1[0])        
            i_ll.append(obj_MSB[l_list[ll]].odd_connected[0])    
            if i_ll not in assigned:
                assigned.append(i_ll)
                # print('what is in i_l', obj_MSB_1, obj_MSB_1[i], i)
  

        obj_MSB_1=obj_MSB_collection
        obj_MSB_1.sort()


    all_even_c=[]
    all_even_conn=[]
    obj_LSB_1=obj_LSB[0].even_connected
    length_even_groups=[]
    for i in range (len(obj_LSB)):
        for j in range (len(obj_LSB[i].even_connected)):
            length_even_groups.append(obj_LSB[i].even_connected[j])
    #print('length_even_groups',length_even_groups, obj_LSB_1, obj_LSB_1[0])
    
    obj_LSB_collection=[]
    assigned=[]
    tracks=[]
    while len(obj_LSB_1)!=len(length_even_groups):
    #for i in range (len(obj_MSB)):
        
        left_side=[]
        right_side=[] 
        flag=0
        l_list=[]
        select_one_side=0
        p=0
        
        for l in range (len(obj_LSB)):
            for i in range (len(obj_LSB_1)):
                flag_break=0
            
                i_l=[]
                i_l.append(obj_LSB_1[0])
                i_l.append(obj_LSB[l].even_connected[0])
                i_k=[]
                i_k.append(obj_LSB[l].even_connected[0])
                i_k.append(obj_LSB_1[0]) 
                
                
                if  obj_LSB[l].even_connected[0] not in obj_LSB_1 and i_l not in assigned and i_k not in assigned:                 
                    for k in range (len(obj_LSB[l].even_connected)):                     
                                       
                        for t in range (len(Capcitor[obj_LSB_1[i][0]][obj_LSB_1[i][1]].inter_connected)):
                            for u in range (len(Capcitor[obj_LSB[l].even_connected[k][0]][obj_LSB[l].even_connected[k][1]].inter_connected)):
                                if Capcitor[obj_LSB_1[i][0]][obj_LSB_1[i][1]].inter_connect[t][0]-Capcitor[obj_LSB[l].even_connected[k][0]][obj_LSB[l].even_connected[k][1]].inter_connect[u][0]==0 or Capcitor[obj_LSB_1[i][0]][obj_LSB_1[i][1]].inter_connect[t][0]-Capcitor[obj_LSB[l].even_connected[k][0]][obj_LSB[l].even_connected[k][1]].inter_connect[u][0]==1 or Capcitor[obj_LSB_1[i][0]][obj_LSB_1[i][1]].inter_connect[t][0]-Capcitor[obj_LSB[l].even_connected[k][0]][obj_LSB[l].even_connected[k][1]].inter_connect[u][0]==-1:
                                    l_list.append(l)
                                        
                                    flag=1                                        
                                    (i_index, j_index)=capacitor_index(Capcitor, Capcitor[obj_LSB_1[i][0]][obj_LSB_1[i][1]].inter_connect[t][0], Capcitor[obj_LSB_1[i][0]][obj_LSB_1[i][1]].inter_connect[t][1])
                                    
                                    (l_index, k_index)=capacitor_index(Capcitor, Capcitor[obj_LSB[l].even_connected[k][0]][obj_LSB[l].even_connected[k][1]].inter_connect[u][0], Capcitor[obj_LSB[l].even_connected[k][0]][obj_LSB[l].even_connected[k][1]].inter_connect[u][1])
                                
                                if Capcitor[obj_LSB_1[i][0]][obj_LSB_1[i][1]].inter_connect[t][0]-Capcitor[obj_LSB[l].even_connected[k][0]][obj_LSB[l].even_connected[k][1]].inter_connect[u][0]==0 or Capcitor[obj_LSB_1[i][0]][obj_LSB_1[i][1]].inter_connect[t][0]-Capcitor[obj_LSB[l].even_connected[k][0]][obj_LSB[l].even_connected[k][1]].inter_connect[u][0]==-1:                                    
                                    flag_break=1
                                    l_s=[]
                                    l_s.append(i_index)
                                    l_s.append(j_index)
                                    l_s.append(l_index)
                                    l_s.append(k_index)                                    
                                    left_side.append(l_s)
                                        
                                    h_tracks_l=[]
                                    track_one=0

                                    for tr in range (2, len(Capcitor[left_side[p][0]][left_side[p][1]].track_detailed_top)):
                                        for tr_1 in range (2, len(Capcitor[left_side[p][2]][left_side[p][3]].track_detailed_top)):
                                            if Capcitor[left_side[p][0]][left_side[p][1]].track_detailed_top[tr]==Capcitor[left_side[p][2]][left_side[p][3]].track_detailed_top[tr_1] and Capcitor[left_side[p][0]][left_side[p][1]].track_detailed_top[tr] not in detailed_tr_top_odd and Capcitor[left_side[p][0]][left_side[p][1]].track_detailed_top[tr] not in detailed_tr_top:
                                                track_one=Capcitor[left_side[p][0]][left_side[p][1]].track_detailed_top[tr]
                                                tracks.append(track_one)
                                                break
                                        if track_one!=0:
                                            break        
                                            
                                    track_l=track_one

                                    y_value_j=Capcitor[left_side[p][0]][left_side[p][1]].y_coordinate_new
                                    x_value_j=Capcitor[left_side[p][0]][left_side[p][1]].x_coordinate_new
                                    htrack=y_value_j+((cap.h)/2)-cap.pin_y_top-Layers_dict['M2']['Width']/2
                                    
                                    track_number=Capcitor[left_side[p][0]][left_side[p][1]].channel_width_l
                                    sx_channel=(track_number+1)*(Layers_dict['M3']['Space']+Layers_dict['M3']['Width'])                
                                    fl=horizontal(left_side[p][0], track_one, y_value_j, x_value_j, horizontal_track_new_top, sx_channel, htrack)
                                    
                                    new_f=fl.horizontal_routing_top_Split()
                                    collision_track=0
                                    if new_f==1:
                                        Capcitor[left_side[p][0]][left_side[p][1]].via_number_top=Capcitor[left_side[p][0]][left_side[p][1]].via_number_top+1                                         
                                        collision_track=cap.pin_y_top+Layers_dict['M2']['Space']+Layers_dict['M2']['Width']+Layers_dict['V2']['VencA_H']
                                        htrack=fl.horizontal_track_assign_top()
                                        cap.a_t_h_ratio.append(round(htrack,5))
                                        
                                                                  
                                    h_t=fl.insert(round(htrack,5))
                                    horizontal_track_new_top.append(h_t)
                                    h_tracks_l.append(round(htrack,5))
                                    
                                    Horizontal_track_plot_top(track_one, htrack, cap.w, cap.h, x_value_j, y_value_j, cap.line_w, 'b', new_f, Layers_dict, Terminal_list, cap)
                                    
                                    #wire_2=abs(x_value_j-track_one)-(cap.w/2)+cap.pin_x +Capcitor[left_side[p][0]][left_side[p][1]].inter_connect_length
                                    q=p
                                    #for q in range (len(left_side)):
                                        #   if left_side[p][0]==left_side[q][0] and left_side[p][1]==left_side[q][1]:
                                    y_value_p=Capcitor[left_side[q][2]][left_side[q][3]].y_coordinate_new
                                    x_value_p=Capcitor[left_side[q][2]][left_side[q][3]].x_coordinate_new
                                    htrack_o=y_value_p+((cap.h)/2)-cap.pin_y_top-Layers_dict['M2']['Width']/2
                                    
                                    track_number=Capcitor[left_side[q][2]][left_side[q][3]].channel_width_l
                                    sx_channel=(track_number+1)*(Layers_dict['M3']['Space']+Layers_dict['M3']['Width'])                
                                    fl=horizontal(left_side[q][2], track_one, y_value_p, x_value_p, horizontal_track_new_top, sx_channel, htrack)
                                    
                                    new_f=fl.horizontal_routing_top_Split()
                                    
                                    collision_track_2=0
                                    if new_f==1: 
                                        Capcitor[left_side[q][2]][left_side[q][3]].via_number_top=Capcitor[left_side[q][2]][left_side[q][3]].via_number_top+1                                         
                                        collision_track_2=cap.pin_y_top+Layers_dict['M2']['Space']+Layers_dict['M2']['Width']+Layers_dict['V2']['VencA_H']
                                        htrack_o=fl.horizontal_track_assign_top()
                                        cap.a_t_h_ratio.append(round(htrack_o,5))

                                    htrack_list_1=[]
                                    htrack_list_1.append(round(htrack,5))
                                    htrack_list_1.append(round(htrack_o,5))


                                    LSB_track_dict={}
                                    
                                    LSB_track_dict['track']=track_one
                                    LSB_track_dict['htrack']=htrack_list_1
                                    LSB_tracks.append(LSB_track_dict)
                                            
                                    wire_2=abs(x_value_j-track_one)-(cap.w/2)+cap.pin_x+abs(x_value_p-track_one)-(cap.w/2)+cap.pin_x
                                    
                                    wire_length_LSB=wire_length_LSB+wire_2+collision_track+collision_track_2

                                    h_tracks_l.append(round(htrack_o,5)) 
                                                          
                                    h_t=fl.insert(round(htrack_o,5))
                                    horizontal_track_new_top.append(h_t)
                                    Horizontal_track_plot_top(track_one, htrack_o, cap.w, cap.h, x_value_p, y_value_p, cap.line_w, 'b', new_f, Layers_dict, Terminal_list, cap)
                                    
                                    color_r='b'
                                    index=0
                                    if len(h_tracks_l)!=0:    
                                        max_l=max(h_tracks_l)
                                        min_l=min(h_tracks_l)
                            
                                        var='D'+str(int(Capcitor[left_side[q][2]][left_side[q][3]].cap_name))
                                        trunk_routing(track_one, min_l, max_l, Layers_dict, Terminal_list, cap, color_r, index, var)                
                                        for ht in range (len(h_tracks_l)):
                                            x=track_one 
                                            y=h_tracks_l[ht]
                                            top_plate_via(x, y, height, Layers_dict, Terminal_list, cap)
                                    
                                    for kk in range (len(obj_LSB_1)):
                                    #obj_MSB[i].all_odd_connected.append(obj_MSB_1[kk])
                                        all_even_conn.append(obj_LSB_1[kk])
                                        if obj_LSB_1[kk] not in obj_LSB_collection:
                                            obj_LSB_collection.append(obj_LSB_1[kk])
                                    
                        
                                    
                                    for l_k in range (len(l_list)):
                                        i_lk=[]
                                        i_lk.append(obj_LSB_1[i][0])
                                        i_lk.append(obj_LSB[l_list[l_k]].even_connected[0])
                                        all_odd_c.append(i_lk)
                                        for kk in range (len(obj_LSB[l_list[l_k]].even_connected)):
                                            #obj_MSB[i].all_odd_connected.append(obj_MSB[l_list[l_k]].odd_connected[kk])
                                            all_even_conn.append(obj_LSB[l_list[l_k]].even_connected[kk])
                                            if obj_LSB[l_list[l_k]].even_connected[kk] not in obj_LSB_collection:
                                                obj_LSB_collection.append(obj_LSB[l_list[l_k]].even_connected[kk])
                                
                                    # if Capcitor[obj_MSB[i].odd_connected[j][0]][obj_MSB[i].odd_connected[j][1]].inter_connect[t][0]-Capcitor[obj_MSB[l].odd_connected[k][0]][obj_MSB[l].odd_connected[k][1]].inter_connect[u][0]==0 or Capcitor[obj_MSB[i].odd_connected[j][0]][obj_MSB[i].odd_connected[j][1]].inter_connect[t][0]-Capcitor[obj_MSB[l].odd_connected[k][0]][obj_MSB[l].odd_connected[k][1]].inter_connect[u][0]==1:                                    
                                if  Capcitor[obj_LSB_1[i][0]][obj_LSB_1[i][1]].inter_connect[t][0]-Capcitor[obj_LSB[l].even_connected[k][0]][obj_LSB[l].even_connected[k][1]].inter_connect[u][0]==1:                                    
                                    flag_break=1
                                    r_s=[]
                                    r_s.append(i_index)
                                    r_s.append(j_index)
                                    r_s.append(l_index)
                                    r_s.append(k_index)                                    
                                    right_side.append(r_s)

                                    
                                    track_one=0
                
                                    h_tracks_r=[]
                                    for tr in range (1, len(Capcitor[right_side[p][0]][right_side[p][1]].track_detailed_top)):
                                        for tr_1 in range (1, len(Capcitor[right_side[p][2]][right_side[p][3]].track_detailed_top)):
                                            if Capcitor[right_side[p][0]][right_side[p][1]].track_detailed_top[tr]==Capcitor[right_side[p][2]][right_side[p][3]].track_detailed_top[tr_1] and Capcitor[right_side[p][0]][right_side[p][1]].track_detailed_top[tr] not in detailed_tr_top_odd and  Capcitor[right_side[p][0]][right_side[p][1]].track_detailed_top[tr] not in detailed_tr_top:
                                                track_one=Capcitor[right_side[p][0]][right_side[p][1]].track_detailed_top[tr]
                                                #detailed_tr_top.append(track_one)
                                                tracks.append(track_one)
                                                break
                                        if track_one!=0:
                                            break        
                                            
                                    track_l=track_one

                                    y_value_j=Capcitor[right_side[p][0]][right_side[p][1]].y_coordinate_new
                                    x_value_j=Capcitor[right_side[p][0]][right_side[p][1]].x_coordinate_new
                                    htrack=y_value_j+((cap.h)/2)-cap.pin_y_top-Layers_dict['M2']['Width']/2
                                    
                                    track_number=Capcitor[right_side[p][0]][right_side[p][1]].channel_width_l
                                    sx_channel=(track_number+1)*(Layers_dict['M3']['Space']+Layers_dict['M3']['Width'])                
                                    fl=horizontal(right_side[p][0], track_one, y_value_j, x_value_j, horizontal_track_new_top, sx_channel, htrack)
                                    
                                    new_f=fl.horizontal_routing_top_Split()
                                    collision_track=0
                                    if new_f==1:
                                        Capcitor[right_side[p][0]][right_side[p][1]].via_number_top=Capcitor[right_side[p][0]][right_side[p][1]].via_number_top+1                                         
                                        collision_track=cap.pin_y_top+Layers_dict['M2']['Space']+Layers_dict['M2']['Width']+Layers_dict['V2']['VencA_H']
                                        htrack=fl.horizontal_track_assign_top()
                                        cap.a_t_h_ratio.append(round(htrack,5))
                                                
                                                                      
                                    h_t=fl.insert(round(htrack,5))
                                    horizontal_track_new_top.append(h_t)
                                    h_tracks_r.append(round(htrack,5))
                                    
                                    
                                    Horizontal_track_plot_top(track_one, htrack, cap.w, cap.h, x_value_j, y_value_j, cap.line_w, 'b', new_f, Layers_dict, Terminal_list, cap)
                                    
                                    #wire_2=abs(x_value_j-track_one)-(cap.w/2)+cap.pin_x +Capcitor[right_side[0][0]][right_side[0][1]].inter_connect_length
                                    q=p
                                    #for q in range (len(right_side)):
                                        #if right_side[p][0]==right_side[q][0] and right_side[p][1]==right_side[q][1]:
                                    y_value_p=Capcitor[right_side[q][2]][right_side[q][3]].y_coordinate_new
                                    x_value_p=Capcitor[right_side[q][2]][right_side[q][3]].x_coordinate_new
                                    htrack_o=y_value_p+((cap.h)/2)-cap.pin_y_top-Layers_dict['M2']['Width']/2
                                    
                                    track_number=Capcitor[right_side[q][2]][right_side[q][3]].channel_width_l
                                    sx_channel=(track_number+1)*(Layers_dict['M3']['Space']+Layers_dict['M3']['Width'])                
                                    fl=horizontal(right_side[q][2], track_one, y_value_p, x_value_p, horizontal_track_new_top, sx_channel, htrack)
                                    
                                    new_f=fl.horizontal_routing_top_Split()
                                    collision_track_2=0
                                    
                                    if new_f==1: 
                                        Capcitor[right_side[q][2]][right_side[q][3]].via_number_top=Capcitor[right_side[q][2]][right_side[q][3]].via_number_top+1                                         
                                        collision_track_2=cap.pin_y_top+Layers_dict['M2']['Space']+Layers_dict['M2']['Width']+Layers_dict['V2']['VencA_H']
                                        htrack_o=fl.horizontal_track_assign_top()
                                        cap.a_t_h_ratio.append(round(htrack_o,5))

                                    htrack_list_1=[]
                                    htrack_list_1.append(round(htrack,5))
                                    htrack_list_1.append(round(htrack_o,5))


                                    LSB_track_dict={}
                                    
                                    LSB_track_dict['track']=track_one
                                    LSB_track_dict['htrack']=htrack_list_1
                                    LSB_tracks.append(LSB_track_dict)

                                    wire_2=abs(x_value_j-track_one)-(cap.w/2)+cap.pin_x+abs(x_value_p-track_one)-(cap.w/2)+cap.pin_x
                                    
                                    wire_length_LSB=wire_length_LSB+wire_2+collision_track+collision_track_2

                                        
                                    h_tracks_r.append(round(htrack_o,5))
                                                         
                                    h_t=fl.insert(round(htrack_o,5))
                                    horizontal_track_new_top.append(h_t)
                                    Horizontal_track_plot_top(track_one, htrack_o, cap.w, cap.h, x_value_p, y_value_p, cap.line_w, 'b', new_f, Layers_dict, Terminal_list, cap)
                                    color_r='b'
                                    index=0
                                    if len(h_tracks_r)!=0:    
                                        max_l=max(h_tracks_r)
                                        min_l=min(h_tracks_r)
                            
                                        var='D'+str(int(Capcitor[right_side[q][2]][right_side[q][3]].cap_name))
                                        trunk_routing(track_one, min_l, max_l, Layers_dict, Terminal_list, cap, color_r, index, var)                
                                        for ht in range (len(h_tracks_r)):
                                            x=track_one 
                                            y=h_tracks_r[ht]
                                            top_plate_via(x, y, height, Layers_dict, Terminal_list, cap)
                    
                                    for kk in range (len(obj_LSB_1)):
                                        all_odd_conn.append(obj_LSB_1[kk])
                                        if obj_LSB_1[kk] not in obj_LSB_collection:
                                            obj_LSB_collection.append(obj_LSB_1[kk])
                                    
                        
                                    
                                    for l_k in range (len(l_list)):
                                        for kk in range (len(obj_LSB[l_list[l_k]].even_connected)):
                                            all_odd_conn.append(obj_LSB[l_list[l_k]].even_connected[kk])
                                            if obj_LSB[l_list[l_k]].even_connected[kk] not in obj_LSB_collection:
                                                obj_LSB_collection.append(obj_LSB[l_list[l_k]].even_connected[kk])


                                if flag_break==1:
                                    break
                            if flag_break==1:
                                break
                        if flag_break==1:
                            break
                    if flag_break==1:
                        break
            if flag_break==1:
                break
                    
        for ll in range (len(l_list)):
            i_ll=[]
            i_ll.append(obj_LSB_1[0])        
            i_ll.append(obj_LSB[l_list[ll]].even_connected[0])    
            if i_ll not in assigned:
                assigned.append(i_ll)
  

        obj_LSB_1=obj_LSB_collection
        obj_LSB_1.sort()


    vertical_track_lsb=[]
    for i in range (len(LSB_tracks)):
        Capcitor[0][0].via_number_top=Capcitor[0][0].via_number_top+1         
        htracks_lsb=[]
        htracks_lsb.append(LSB_tracks[i]['htrack'][0])
        htracks_lsb.append(LSB_tracks[i]['htrack'][1])
        for j in range (i+1, len(LSB_tracks)):
            if LSB_tracks[i]['track']==LSB_tracks[j]['track'] and LSB_tracks[j]['track'] not in vertical_track_lsb:
                Capcitor[0][0].via_number_top=Capcitor[0][0].via_number_top+1  
                vertical_track_lsb.append(LSB_tracks[j]['track'])
                htracks_lsb.append(LSB_tracks[j]['htrack'][0])
                htracks_lsb.append(LSB_tracks[j]['htrack'][1])
        
        max_lsb_h=max(htracks_lsb)
        min_lsb_h=min(htracks_lsb)
        
        wire_length_LSB=wire_length_LSB+abs(max_lsb_h-min_lsb_h)
        
    vertical_track_msb=[]
    for i in range (len(MSB_tracks)):
        Capcitor[1][0].via_number_top=Capcitor[1][0].via_number_top+1  
        htracks_msb=[]
        htracks_msb.append(MSB_tracks[i]['htrack'][0])
        htracks_msb.append(MSB_tracks[i]['htrack'][1])        
        for j in range (i+1, len(MSB_tracks)):
            if MSB_tracks[i]['track']==MSB_tracks[j]['track'] and MSB_tracks[j]['track'] not in vertical_track_msb:
                Capcitor[1][0].via_number_top=Capcitor[1][0].via_number_top+1  
                vertical_track_lsb.append(MSB_tracks[j]['track'])
                htracks_msb.append(MSB_tracks[j]['htrack'][0])
                htracks_msb.append(MSB_tracks[j]['htrack'][1])
            
        
        max_msb_h=max(htracks_msb)
        min_msb_h=min(htracks_msb)
        
        wire_length_MSB=wire_length_MSB+abs(max_msb_h-min_msb_h)
        


    return wire_length_LSB, wire_length_MSB
                            
    
def Top_plate_routing_plot(Capcitor, mat, row, column, width, sx, height, sy, color, line_width, center_x, spacing, wire_width, Terminal_list, Layers_dict, cap):
    length_top_1=0
    all_2_groups=[]
    total_bottom_length=0

    y_port=cap.pin_y_top+Layers_dict['M2']['Width']/2
    x_port_top=Layers_dict['M3']['Space']+Layers_dict['M3']['Width']
    for i in range (column//2+1):
        i_mirror=column-i-1
        for j in range (row-1):
            groups_1=[]
            groups_2=[]
            groups_mirror_1=[]
            groups_mirror_2=[]        
            group_tog=[]      
            group_tog_inv=[]  
            group_tog_mirror=[]      
            group_tog_mirror_inv=[]          
    
            ident=cap_identity(i, j, int(mat[j][i]))
            ident_1=cap_identity(i, j+1, int(mat[j+1][i]))            
            
            j_mirror=row-j-1
            j_mirror_1=row-j-2
    
            ident_mirror=cap_identity(i_mirror, j_mirror, int(mat[j_mirror][i_mirror]))
            ident_mirror_1=cap_identity(i_mirror, j_mirror_1, int(mat[j_mirror_1][i_mirror]))
            
            if int(mat[j][i])!=0 and int(mat[j+1][i])!=0:
                for i_1 in range (len(Capcitor)):
                    for j_1 in range (len(Capcitor[i_1])):
                        if ident ==Capcitor[i_1][j_1].identity_n:
                            for j_2 in range (len(Capcitor[i_1])):
                                if Capcitor[i_1][j_1].identity_n in Capcitor[i_1][j_2].inter_connect:
                                    int_group=[]
                                    int_group.append(i_1)
                                    int_group.append(j_2)
                                    groups_1.append(int_group)                            
                        if ident_mirror ==Capcitor[i_1][j_1].identity_n:
                            for j_2 in range (len(Capcitor[i_1])):
                                if Capcitor[i_1][j_1].identity_n in Capcitor[i_1][j_2].inter_connect:
                                    int_group=[]
                                    int_group.append(i_1)
                                    int_group.append(j_2)
                                    groups_mirror_1.append(int_group)                                
                           
                for i_1 in range (len(Capcitor)):
                    for j_1 in range (len(Capcitor[i_1])):
                        if ident_1 ==Capcitor[i_1][j_1].identity_n:
                            for j_2 in range (len(Capcitor[i_1])):
                                if Capcitor[i_1][j_1].identity_n in Capcitor[i_1][j_2].inter_connect:
                                    int_group=[]
                                    int_group.append(i_1)
                                    int_group.append(j_2) 
                                    groups_2.append(int_group)
                        if ident_mirror_1 ==Capcitor[i_1][j_1].identity_n:
                            for j_2 in range (len(Capcitor[i_1])):
                                if Capcitor[i_1][j_1].identity_n in Capcitor[i_1][j_2].inter_connect:
                                    int_group=[]
                                    int_group.append(i_1)
                                    int_group.append(j_2) 
                                    groups_mirror_2.append(int_group)            
                          
                
                group_tog.append(groups_1)
                group_tog.append(groups_2)
                group_tog_inv.append(groups_2)
                group_tog_inv.append(groups_1)
                group_tog_mirror.append(groups_mirror_1)
                group_tog_mirror.append(groups_mirror_2)
                group_tog_mirror_inv.append(groups_mirror_2)
                group_tog_mirror_inv.append(groups_mirror_1)            

                if groups_1!=groups_2 and group_tog not in all_2_groups and group_tog_inv not in all_2_groups and groups_mirror_1!=groups_mirror_2 and group_tog_mirror not in all_2_groups and group_tog_mirror_inv not in all_2_groups:
                    

                    tog=[]
                    tog.append(groups_1)
                    tog.append(groups_2)
                    all_2_groups.append(tog)
                    tog_mirror=[]
                    tog_mirror.append(groups_mirror_1)
                    tog_mirror.append(groups_mirror_2)
                    all_2_groups.append(tog_mirror)

                    
                    (i_index, j_index)=capacitor_index(Capcitor, i, j)
                    (i_index_2, j_index_2)=capacitor_index(Capcitor, i, j+1)
                    
                    x_new=Capcitor[i_index][j_index].x_coordinate_new
                    y_new=Capcitor[i_index][j_index].y_coordinate_new+height/2-y_port                    
                    
                    y_new_2=Capcitor[i_index_2][j_index_2].y_coordinate_new+height/2-y_port                    

                    (i_index_mirror, j_index_mirror)=capacitor_index(Capcitor, i_mirror, j_mirror)
                    (i_index_mirror_2, j_index_mirror_2)=capacitor_index(Capcitor, i_mirror, j_mirror_1)
                    
                    x_new_mirror=Capcitor[i_index_mirror][j_index_mirror].x_coordinate_new
                    y_new_mirror=Capcitor[i_index_mirror][j_index_mirror].y_coordinate_new+height/2-y_port        
                    y_new_mirror_2=Capcitor[i_index_mirror_2][j_index_mirror_2].y_coordinate_new+height/2-y_port                      
      
                    length_top_1=2*sy+length_top_1

                    top_plate_vertical(x_new-width/2-x_port_top, y_new_2, y_new, y_new_2, Layers_dict, Terminal_list, cap)
                    left_array_top_plate_horizontal(x_new-width/2-x_port_top, y_new, Layers_dict, Terminal_list, cap)
                    left_array_top_plate_horizontal(x_new-width/2-x_port_top, y_new_2, Layers_dict, Terminal_list, cap)
                    
                    top_plate_via(x_new-width/2-x_port_top, y_new, height, Layers_dict, Terminal_list, cap)
                    top_plate_via(x_new-width/2-x_port_top, y_new_2, height, Layers_dict, Terminal_list, cap)                    

                    top_plate_vertical(x_new_mirror+width/2+x_port_top, y_new_mirror, y_new_mirror, y_new_mirror_2, Layers_dict, Terminal_list, cap)
                    right_array_top_plate_horizontal(x_new_mirror+width/2+x_port_top, y_new_mirror, Layers_dict, Terminal_list, cap)
                    right_array_top_plate_horizontal(x_new_mirror+width/2+x_port_top, y_new_mirror_2, Layers_dict, Terminal_list, cap)
                    
                    top_plate_via(x_new_mirror+width/2+x_port_top, y_new_mirror, height, Layers_dict, Terminal_list, cap)
                    top_plate_via(x_new_mirror+width/2+x_port_top, y_new_mirror_2, height, Layers_dict, Terminal_list, cap) 
                    


    return length_top_1, total_bottom_length





def Horizontal_track_plot(track, htrack, width, height, x_value, y, line_width, color, flag,  Layers_dict, Terminal_list, cap):
    x=0
    min_h=htrack
    if x_value<track:
        x=x_value+width/2 
        if flag==0:
            plt.gca().add_patch(patches.Rectangle((x-cap.pin_x-cap.overlap, y-cap.h/2+cap.pin_y), cap.pin_x+cap.overlap+abs(x-track)+Layers_dict['M1']['Width']/2+Layers_dict['V2']['VencA_H'],  Layers_dict['M2']['Width'], color=color))
            wire_segment_1=wire('M2', None, Layers_dict['M2']['Direction'])
            Terminal_list.append(wire_segment_1.segment(x-cap.pin_x-cap.overlap, y-cap.h/2+cap.pin_y, x+abs(x-track)+cap.overlap+Layers_dict['M1']['Width']/2+Layers_dict['V2']['VencA_H'], y-cap.h/2+Layers_dict['M2']['Width']+cap.pin_y, 'drawing', Layers_dict['M2']['Color'][0]))

        else:
            min_h=htrack
            plt.gca().add_patch(patches.Rectangle((x_value-Layers_dict['M1']['Width']/2-Layers_dict['V1']['VencA_H'], htrack-Layers_dict['M2']['Width']/2), abs(x_value-track)+cap.overlap+Layers_dict['M1']['Width']+2*Layers_dict['V1']['VencA_H'],  Layers_dict['M2']['Width'], color=color))
            wire_segment_1=wire('M2', None, Layers_dict['M2']['Direction'])
            Terminal_list.append(wire_segment_1.segment(x_value-Layers_dict['M1']['Width']/2-Layers_dict['V1']['VencA_H'], htrack-Layers_dict['M2']['Width']/2, x_value+cap.overlap+abs(x_value-track)+Layers_dict['M1']['Width']/2+Layers_dict['V1']['VencA_H'], htrack+Layers_dict['M2']['Width']/2, 'drawing', Layers_dict['M2']['Color'][0]))

            plt.gca().add_patch(patches.Rectangle((x_value-Layers_dict['M1']['Width']/2, htrack-Layers_dict['M2']['Width']/2-Layers_dict['V1']['VencA_H']),  Layers_dict['M1']['Width'], abs(min_h-y)-cap.h/2+2*Layers_dict['V1']['VencA_L']+2*Layers_dict['V1']['WidthY']+cap.pin_y,color=color)) 
            wire_segment_1=wire('M1', None, Layers_dict['M1']['Direction'])
            Terminal_list.append(wire_segment_1.segment(x_value-Layers_dict['M1']['Width']/2, htrack-Layers_dict['M2']['Width']/2-Layers_dict['V1']['VencA_H'], x_value+Layers_dict['M1']['Width']/2, y-cap.h/2+cap.pin_y+2*Layers_dict['V1']['VencA_L']+2*Layers_dict['V1']['WidthY'], 'drawing', Layers_dict['M1']['Color'][1]))

            plt.gca().add_patch(patches.Rectangle((x_value-Layers_dict['V1']['WidthX']/2, htrack-Layers_dict['V1']['WidthY']/2), Layers_dict['V1']['WidthX'], Layers_dict['V1']['WidthY'],   color='lime'))
            wire_segment_1=via('V1', None)
            Terminal_list.append(wire_segment_1.segment(x_value-Layers_dict['V1']['WidthX']/2, htrack-Layers_dict['V1']['WidthY']/2, x_value+Layers_dict['V1']['WidthX']/2, htrack+Layers_dict['V1']['WidthY']/2, 'drawing'))   

                   
    else:
        x=x_value-width/2
        if flag==0:
            plt.gca().add_patch(patches.Rectangle((x-abs(x-track)-Layers_dict['M1']['Width']/2-Layers_dict['V1']['VencA_H'], y-cap.h/2+cap.pin_y), cap.pin_x+cap.overlap+abs(x-track)+Layers_dict['V1']['VencA_H']+Layers_dict['M2']['Width']/2, Layers_dict['M2']['Width'], color=color))
            wire_segment_1=wire('M2', None, Layers_dict['M2']['Direction'])
            Terminal_list.append(wire_segment_1.segment(x-abs(x-track)-Layers_dict['M1']['Width']/2-Layers_dict['V1']['VencA_H'], y-cap.h/2+cap.pin_y, x+cap.pin_x+cap.overlap, y-cap.h/2+cap.pin_y+Layers_dict['M2']['Width'], 'drawing', Layers_dict['M2']['Color'][0]))

        else:
            min_h=htrack
            plt.gca().add_patch(patches.Rectangle((track-Layers_dict['M1']['Width']/2-Layers_dict['V1']['VencA_H'], htrack-Layers_dict['M2']['Width']/2), abs(x_value-track)+Layers_dict['M1']['Width']+2*Layers_dict['V1']['VencA_H'],  Layers_dict['M2']['Width'], color=color))
            wire_segment_1=wire('M2', None, Layers_dict['M2']['Direction'])
            Terminal_list.append(wire_segment_1.segment(track-Layers_dict['M1']['Width']/2-Layers_dict['V1']['VencA_H'], htrack-Layers_dict['M2']['Width']/2, x_value+abs(x_value-track)+Layers_dict['M1']['Width']+2*Layers_dict['V1']['VencA_H'], htrack+Layers_dict['M2']['Width']/2, 'drawing', Layers_dict['M2']['Color'][0]))

            plt.gca().add_patch(patches.Rectangle((x_value-Layers_dict['M1']['Width']/2, htrack-Layers_dict['M2']['Width']/2-Layers_dict['V1']['VencA_H']),  Layers_dict['M1']['Width'], abs(min_h-y)-cap.h/2+2*Layers_dict['V1']['VencA_L']+2*Layers_dict['V1']['WidthY']+cap.pin_y,color=color)) 
            wire_segment_1=wire('M1', None, Layers_dict['M1']['Direction'])
            Terminal_list.append(wire_segment_1.segment(x_value-Layers_dict['M1']['Width']/2, htrack-Layers_dict['M2']['Width']/2-Layers_dict['V1']['VencA_H'], x_value+Layers_dict['M1']['Width']/2, htrack+2*Layers_dict['V1']['VencA_L']+2*Layers_dict['V1']['WidthY']/2, 'drawing', Layers_dict['M1']['Color'][1]))

            plt.gca().add_patch(patches.Rectangle((x_value-Layers_dict['V1']['WidthX']/2, htrack-Layers_dict['V1']['WidthY']/2), Layers_dict['V1']['WidthX'], Layers_dict['V1']['WidthY'],   color='lime'))
            wire_segment_1=via('V1', None)
            Terminal_list.append(wire_segment_1.segment(x_value-Layers_dict['V1']['WidthX']/2, htrack-Layers_dict['V1']['WidthY']/2, x_value+Layers_dict['V1']['WidthX']/2, htrack+Layers_dict['V1']['WidthY']/2, 'drawing'))   
    
    plt.gca().add_patch(patches.Rectangle((track-Layers_dict['V1']['WidthX']/2, min_h-Layers_dict['V1']['WidthY']/2), Layers_dict['V1']['WidthX'], Layers_dict['V1']['WidthY'],   color='lime'))
    wire_segment_1=via('V1', None)
    Terminal_list.append(wire_segment_1.segment(track-Layers_dict['V1']['WidthX']/2, min_h-Layers_dict['V1']['WidthY']/2, track+Layers_dict['V1']['WidthX']/2, min_h+Layers_dict['V1']['WidthY']/2, 'drawing'))   

def Horizontal_track_plot_top(track, htrack, width, height, x_value, y, line_width, color, flag,  Layers_dict, Terminal_list, cap):
    x=0
    min_h=htrack
    if x_value<track:
        x=x_value+width/2 
        if flag==0:
            plt.gca().add_patch(patches.Rectangle((x-cap.pin_x-cap.overlap, y+cap.h/2-cap.pin_y-Layers_dict['M2']['Width']), cap.pin_x+cap.overlap+abs(x-track)+Layers_dict['M3']['Width']/2+Layers_dict['V2']['VencA_H'],  Layers_dict['M2']['Width'], color=color))
            wire_segment_1=wire('M2', None, Layers_dict['M2']['Direction'])
            Terminal_list.append(wire_segment_1.segment(x-cap.pin_x-cap.overlap, y+cap.h/2-cap.pin_y-Layers_dict['M2']['Width'], x+cap.overlap+abs(x-track)+Layers_dict['M3']['Width']/2+Layers_dict['V2']['VencA_H'], y+cap.h/2-cap.pin_y, 'drawing', Layers_dict['M2']['Color'][0]))

        else:
            
            plt.gca().add_patch(patches.Rectangle((x_value-Layers_dict['M3']['Width']/2-Layers_dict['V2']['VencA_H'], htrack-Layers_dict['M2']['Width']/2), abs(x_value-track)+cap.overlap+Layers_dict['M3']['Width']+2*Layers_dict['V2']['VencA_H'],  Layers_dict['M2']['Width'], color=color))
            wire_segment_1=wire('M2', None, Layers_dict['M2']['Direction'])
            Terminal_list.append(wire_segment_1.segment(x_value-Layers_dict['M3']['Width']/2-Layers_dict['V2']['VencA_H'], htrack-Layers_dict['M2']['Width']/2, x_value+cap.overlap+abs(x_value-track)+Layers_dict['M3']['Width']/2+Layers_dict['V2']['VencA_H'], htrack+Layers_dict['M2']['Width']/2, 'drawing', Layers_dict['M2']['Color'][0]))

            plt.gca().add_patch(patches.Rectangle((x_value-Layers_dict['M3']['Width']/2, y+cap.h/2-cap.pin_y-Layers_dict['M2']['Width']-Layers_dict['V2']['VencA_H']),  Layers_dict['M3']['Width'], abs(min_h-y)-cap.h/2+2*Layers_dict['V2']['VencA_L']+2*Layers_dict['V2']['WidthY']+cap.pin_y,color=color)) 
            wire_segment_1=wire('M3', None, Layers_dict['M3']['Direction'])
            Terminal_list.append(wire_segment_1.segment(x_value-Layers_dict['M3']['Width']/2, y+cap.h/2-cap.pin_y-Layers_dict['M2']['Width']-Layers_dict['V2']['VencA_H'], x_value+Layers_dict['M3']['Width']/2, htrack+Layers_dict['V2']['VencA_L']+Layers_dict['V2']['WidthY']/2, 'drawing', Layers_dict['M3']['Color'][1]))

            plt.gca().add_patch(patches.Rectangle((x_value-Layers_dict['V2']['WidthX']/2, htrack-Layers_dict['V2']['WidthY']/2), Layers_dict['V2']['WidthX'], Layers_dict['V2']['WidthY'],   color='lime'))
            wire_segment_1=via('V2', None)
            Terminal_list.append(wire_segment_1.segment(x_value-Layers_dict['V2']['WidthX']/2, htrack-Layers_dict['V2']['WidthY']/2, x_value+Layers_dict['V2']['WidthX']/2, htrack+Layers_dict['V2']['WidthY']/2, 'drawing'))   
               
    else:
        x=x_value-width/2
        if flag==0:
            plt.gca().add_patch(patches.Rectangle((x-abs(x-track)-Layers_dict['M3']['Width']/2-Layers_dict['V2']['VencA_H'], y+cap.h/2-cap.pin_y-Layers_dict['M2']['Width']), cap.pin_x+cap.overlap+abs(x-track)+Layers_dict['V2']['VencA_H']+Layers_dict['M2']['Width']/2, Layers_dict['M2']['Width'], color=color))
            wire_segment_1=wire('M2', None, Layers_dict['M2']['Direction'])
            Terminal_list.append(wire_segment_1.segment(x-abs(x-track)-Layers_dict['M3']['Width']/2-Layers_dict['V2']['VencA_H'], y+cap.h/2-cap.pin_y-Layers_dict['M2']['Width'], x+cap.pin_x+cap.overlap, y+cap.h/2-cap.pin_y-Layers_dict['M2']['Width'], 'drawing', Layers_dict['M2']['Color'][0]))

        else:
            min_h=htrack
            plt.gca().add_patch(patches.Rectangle((track-Layers_dict['M3']['Width']/2-Layers_dict['V2']['VencA_H'], htrack-Layers_dict['M2']['Width']/2), abs(x_value-track)+cap.overlap+Layers_dict['M3']['Width']+2*Layers_dict['V2']['VencA_H'],  Layers_dict['M2']['Width'], color=color))
            wire_segment_1=wire('M2', None, Layers_dict['M2']['Direction'])
            Terminal_list.append(wire_segment_1.segment(track-Layers_dict['M3']['Width']/2-Layers_dict['V2']['VencA_H'], htrack-Layers_dict['M2']['Width']/2, x_value+cap.overlap+abs(x_value-track)+Layers_dict['M3']['Width']+2*Layers_dict['V2']['VencA_H'], htrack+Layers_dict['M2']['Width']/2, 'drawing', Layers_dict['M2']['Color'][0]))

            plt.gca().add_patch(patches.Rectangle((x_value-Layers_dict['M3']['Width']/2, y+cap.h/2-cap.pin_y-Layers_dict['M2']['Width']-Layers_dict['V2']['VencA_H']),  Layers_dict['M3']['Width'], abs(min_h-y)-cap.h/2+2*Layers_dict['V2']['VencA_L']+2*Layers_dict['V2']['WidthY']+cap.pin_y,color=color)) 
            wire_segment_1=wire('M3', None, Layers_dict['M3']['Direction'])
            Terminal_list.append(wire_segment_1.segment(x_value-Layers_dict['M3']['Width']/2, y+cap.h/2-cap.pin_y-Layers_dict['M2']['Width']-Layers_dict['V2']['VencA_H'], x_value+Layers_dict['M3']['Width']/2, htrack+Layers_dict['V2']['VencA_L']+Layers_dict['V2']['WidthY']/2, 'drawing', Layers_dict['M3']['Color'][1]))

            plt.gca().add_patch(patches.Rectangle((x_value-Layers_dict['V2']['WidthX']/2, htrack-Layers_dict['V2']['WidthY']/2), Layers_dict['V2']['WidthX'], Layers_dict['V2']['WidthY'],   color='lime'))
            wire_segment_1=via('V2', None)
            Terminal_list.append(wire_segment_1.segment(x_value-Layers_dict['V2']['WidthX']/2, htrack-Layers_dict['V2']['WidthY']/2, x_value+Layers_dict['V2']['WidthX']/2, htrack+Layers_dict['V2']['WidthY']/2, 'drawing'))   

    plt.gca().add_patch(patches.Rectangle((track-Layers_dict['V2']['WidthX']/2, min_h-Layers_dict['V2']['WidthY']/2), Layers_dict['V2']['WidthX'], Layers_dict['V2']['WidthY'],   color='lime'))
    wire_segment_1=via('V2', None)
    Terminal_list.append(wire_segment_1.segment(track-Layers_dict['V2']['WidthX']/2, min_h-Layers_dict['V2']['WidthY']/2, track+Layers_dict['V2']['WidthX']/2, min_h+Layers_dict['V2']['WidthY']/2, 'drawing'))   

def trunk_routing(x, y, min_h, Layers_dict, Terminal_list, cap, color_r, index, var):
    color_l=color_r
    if index%2==0:
        color_l=Layers_dict['M1']['Color'][0]
    else:
        color_l=Layers_dict['M1']['Color'][1]        
    plt.gca().add_patch(patches.Rectangle((x-Layers_dict['M1']['Width']/2, y-Layers_dict['M2']['Width']/2-Layers_dict['V1']['VencA_H']),  Layers_dict['M1']['Width'], abs(min_h-y)+Layers_dict['M2']['Width']+2*Layers_dict['V1']['VencA_H'],color=color_r)) 
    wire_segment_1=wire('M1', var, Layers_dict['M1']['Direction'])
    Terminal_list.append(wire_segment_1.segment(x-Layers_dict['M1']['Width']/2, y-Layers_dict['M2']['Width']/2-Layers_dict['V1']['VencA_H'], x+Layers_dict['M1']['Width']/2, y+abs(min_h - y)+Layers_dict['M2']['Width']+2*Layers_dict['V1']['VencA_H'], 'pin', color_l))

def trunk_routing_via(x, min_h, Layers_dict, Terminal_list, cap):
    plt.gca().add_patch(patches.Rectangle((x-Layers_dict['V1']['WidthX']/2, min_h-Layers_dict['V1']['WidthY']/2), Layers_dict['V1']['WidthX'], Layers_dict['V1']['WidthY'],   color='lime'))
    wire_segment_1=via('V1', None)
    Terminal_list.append(wire_segment_1.segment(x-Layers_dict['V1']['WidthX']/2, min_h-Layers_dict['V1']['WidthY']/2, x+Layers_dict['V1']['WidthX']/2, min_h+Layers_dict['V1']['WidthY']/2, 'drawing'))   
    
def bridge_routing_via(x, y, Layers_dict, Terminal_list, cap):
    plt.gca().add_patch(patches.Rectangle((x-Layers_dict['V1']['WidthX']/2, y-Layers_dict['V1']['WidthY']/2), Layers_dict['V1']['WidthX'], Layers_dict['V1']['WidthY'],   color='lime'))
    wire_segment_1=via('V1', None)
    Terminal_list.append(wire_segment_1.segment(x-Layers_dict['V1']['WidthX']/2, y-Layers_dict['V1']['WidthY']/2, x+Layers_dict['V1']['WidthX']/2, y+Layers_dict['V1']['WidthY']/2, 'drawing'))   



def Bridge_connection(wire_list, minimum_y, height, sy, horizontal_track_number, color, assigned_track, Via_Num, Device_Name, line_width, total_bottom_length, All_conn, Only_per_cap_ratio, Layers_dict, Terminal_list, cap, Capacitor):

    parasitic_mark=[] 
    connecting_w=[]
    con_w=[]
    con_w_b=[]
    final_dot_bottom=[]
    
    Bridge_wires=[]
   # Bridge_wires.append()
   
   
    
    trunk_wire_length=[]
    last_h=[]
    visited=[]
    for i in range(len(wire_list)-1):
        for j in range (i+1, len(wire_list)):
            len_1=len(wire_list[i][1])
            len_2=len(wire_list[j][1])
                   
            if wire_list[i][1][len_1-1]==wire_list[j][1][len_2-1]:
                
                htrack_l=minimum_y-height/2-(Layers_dict['M2']['Space']+Layers_dict['M2']['Width'])

                ind=wire_list[i][1][len_1-1]
                color_r= color[ind-1]    
                color_r_1= color[ind-1]    
                if wire_list[i][1][len_1-1] not in con_w:
                    if round(htrack_l,5) in assigned_track:
                        for h_track in range (1,50):
                            htrack_l=minimum_y-height/2-(h_track*(Layers_dict['M2']['Space']+Layers_dict['M2']['Width']))
                                                                    
                            if round(htrack_l,5) in assigned_track:
                                continue
                            assigned_track.append(round(htrack_l, 5))
                            
                            break
                    else:                    
                        htrack_l=htrack_l
                        assigned_track.append(round(htrack_l,5))
                else:
                    for k in range (len(con_w_b)):
                        if wire_list[i][1][len_1-1]==con_w_b[k][1]:    
                            htrack_l=con_w_b[k][0]
                            break
                    
                con_t=[]
                con_t.append(htrack_l)
                con_t.append(wire_list[i][1][len_1-1])
                con_w_b.append(con_t)
                if wire_list[i][1][0] not in visited:
                    visited.append(wire_list[i][1][0])
                    Via_Num=Via_Num+1 

                con_w.append(wire_list[i][1][len_1-1])
                
                h_list_h=[]
                for lis_n in range (1, len(wire_list[i][1])-1):
                    h_list_h.append(wire_list[i][1][lis_n])
                    
                min_h=max(h_list_h)
                
                h_list_h_j=[]
                for lis_n in range (1, len(wire_list[j][1])-1) :
                    h_list_h_j.append(wire_list[j][1][lis_n])
                    

                min_h_j=max(h_list_h_j) 
                
                var='D'+str(int(wire_list[i][1][len_1-1]))
                
                trunk_routing(wire_list[i][1][0], htrack_l, min_h, Layers_dict, Terminal_list, cap, color_r, wire_list[i][2], var)
                trunk_routing_via(wire_list[i][1][0], min_h, Layers_dict, Terminal_list, cap)
                
                trunk_routing(wire_list[j][1][0], htrack_l, min_h_j, Layers_dict, Terminal_list, cap, color_r_1, wire_list[i][2], var)
                trunk_routing_via(wire_list[j][1][0],  min_h_j, Layers_dict, Terminal_list, cap)

                x=0
                #x1=
                if wire_list[i][1][0]<wire_list[j][1][0]:
                    x=wire_list[i][1][0]
                else:
                    x=wire_list[j][1][0]                    

                y2=htrack_l
                
                plt.gca().add_patch(patches.Rectangle((x-Layers_dict['M1']['Width']/2-Layers_dict['V1']['VencA_H'], y2-Layers_dict['M2']['Width']/2), abs(wire_list[i][1][0]-wire_list[j][1][0])+2*Layers_dict['V1']['VencA_H']+Layers_dict['M2']['Width'], Layers_dict['M2']['Width'], color=color_r))
                wire_segment_1=wire('M2', 'pin', Layers_dict['M2']['Direction'])
                Terminal_list.append(wire_segment_1.segment(x-Layers_dict['M1']['Width']/2-Layers_dict['V1']['VencA_H'], y2-Layers_dict['M2']['Width']/2, x+abs(wire_list[i][1][0]-wire_list[j][1][0])+Layers_dict['V1']['VencA_H']+Layers_dict['M2']['Width']/2, y2+Layers_dict['M2']['Width']/2, 'drawing', Layers_dict['M2']['Color'][0]))

                bridge_routing_via(wire_list[i][1][0],  htrack_l, Layers_dict, Terminal_list, cap)
                bridge_routing_via(wire_list[j][1][0],  htrack_l, Layers_dict, Terminal_list, cap)                
                
                last_h.append(htrack_l)

                bridge_wire=abs(wire_list[i][1][0]-wire_list[j][1][0]) 
                if wire_list[i][1][len_1-1] not in parasitic_mark:
                    parasitic_mark.append(wire_list[i][1][len_1-1])
                    trunk=[]
                    trunk.append(htrack_l)
                    trunk.append(wire_list[i][1][len_1-1])
                    trunk_wire_length.append(trunk)
                    
                    
                
                if wire_list[i][1][len_1-1] not in final_dot_bottom:
                    final_dot_bottom.append(wire_list[i][1][len_1-1])
    
                Bridge_wires.append(htrack_l)
                
                w=[]
                w.append(bridge_wire)
                w.append(wire_list[i][1])
                w.append(wire_list[j][1])
                connecting_w.append(w) 
    
                
    
    Bridge_wires_new=set(Bridge_wires)
    Bridge_wires_1_new=list(Bridge_wires_new)
    Bridge_wires_1_new.sort(reverse=True) 
    
    Wire_per_cap=[]
    for i in range(len(wire_list)):
        len_1=len(wire_list[i][1])
        if wire_list[i][1][len_1-1] not in final_dot_bottom:
            h_list_h=[]

            final_dot_bottom.append(wire_list[i][1][len_1-1])
            for lis_n in range (1, len(wire_list[i][1])-1) :
                h_list_h.append(wire_list[i][1][lis_n])
            ind=wire_list[i][1][len_1-1]
            color_r= color[ind-1]
            
            min_h=max(h_list_h)
            htrack_l=minimum_y-height/2-(Layers_dict['M2']['Space']+Layers_dict['M2']['Width'])
            w_per_cap=[]
            wr=abs(min_h-minimum_y)+wire_list[i][0]
            w_per_cap.append(wr)
            w_per_cap.append(wire_list[i][1][len_1-1])
            Wire_per_cap.append(w_per_cap) 
            Only_per_cap_ratio.append(w_per_cap)
            
            var='D'+str(int(wire_list[i][1][len_1-1]))

            trunk_routing(wire_list[i][1][0], htrack_l, min_h, Layers_dict, Terminal_list, cap, color_r, wire_list[i][2], var)
            trunk_routing_via(wire_list[i][1][0],  min_h, Layers_dict, Terminal_list, cap)                
        
            if len(wire_list[i][1])>3:
                for j in range (2, len(wire_list[i][1])-1):
                    trunk_routing_via(wire_list[i][1][0],  wire_list[i][1][j], Layers_dict, Terminal_list, cap)            

        elif wire_list[i][1][len_1-1] in parasitic_mark:
            for j in range (len(trunk_wire_length)):
                if trunk_wire_length[j][1]==wire_list[i][1][len_1-1]:
                    h_list_h=[]
                    
                    for lis_n in range (1, len(wire_list[i][1])-1) :
                        h_list_h.append(wire_list[i][1][lis_n])
                    
                    min_h=max(h_list_h)
                    w_per_cap=[]
                    wr=abs(min_h-minimum_y)+wire_list[i][0]
                    w_per_cap.append(wr)
                    w_per_cap.append(wire_list[i][1][len_1-1])   
                    Wire_per_cap.append(w_per_cap)
                    break
    
    bridge_first_last=[]
    new_connecting_wire=[]            
    for i in range (len(Device_Name)):
        cont=[]
        
        for j in range (len(connecting_w)):
            len_1=len(connecting_w[j][1])
            
            if Device_Name[i]==connecting_w[j][1][len_1-1]:
                cont.append(connecting_w[j][0])

        max_c=0
        if len(cont)>1:
            max_c=max(cont)
            
        elif len(cont)==1:
            
            max_c=cont[0]
        if len(cont)!=0:
            for k in range (len(connecting_w)):
                len_2=len(connecting_w[k][1])
                if Device_Name[i]==connecting_w[k][1][len_2-1]:    
                            
                    if max_c==connecting_w[k][0]: 
                        wire_v=0
                        for kk in range (len(Wire_per_cap)):
                            if Wire_per_cap[kk][1]==Device_Name[i]:
                                wire_v=wire_v+Wire_per_cap[kk][0]
                                
                        Via_Num=Via_Num+1
                        c_w=[]
                        c_w.append(max_c)
                        c_w.append(connecting_w[k][1])        
                        c_w.append(connecting_w[k][2])
                        wire_v=wire_v+connecting_w[k][0]
                        w_per_cap=[]
                        w_per_cap.append(wire_v)
                        w_per_cap.append(Device_Name[i]) 
                        Only_per_cap_ratio.append(w_per_cap)
                        new_connecting_wire.append(c_w)
                        b_w=[]
                        b_w.append(connecting_w[k][1][0])
                        b_w.append(connecting_w[k][2][0])
                        bridge_first_last.append(b_w)
    
    Only_per_cap_ratio.sort(key=takeSecond)
    
    return bridge_first_last, Only_per_cap_ratio, last_h, Bridge_wires_1_new, Via_Num, total_bottom_length, new_connecting_wire


def trunk_routing_top(x, htrack, y, Layers_dict, Terminal_list, cap, color_r, var):
    plt.gca().add_patch(patches.Rectangle((x-Layers_dict['M3']['Width']/2, htrack-Layers_dict['M2']['Width']/2-Layers_dict['V2']['VencA_H']),  Layers_dict['M3']['Width'], abs(htrack-y)+2*Layers_dict['V2']['VencA_L']+Layers_dict['V2']['WidthY'],color=color_r)) 
    wire_segment_1=wire('M3', var, Layers_dict['M3']['Direction'])
    Terminal_list.append(wire_segment_1.segment(x-Layers_dict['M3']['Width']/2, htrack-Layers_dict['M2']['Width']/2-Layers_dict['V2']['VencA_H'], x+Layers_dict['M3']['Width']/2, y+Layers_dict['V2']['WidthY']+2*Layers_dict['V2']['VencA_L'], 'pin', Layers_dict['M3']['Color'][1]))



def Bridge_connection_top(wire_list, maximum_y, height, sy, horizontal_track_number, color, assigned_track, Via_Num, Device_Name, line_width, total_bottom_length, All_conn, Only_per_cap_ratio, Layers_dict, Terminal_list, cap, Capacitor):

    parasitic_mark=[] 
    connecting_w=[]
    con_w=[]
    con_w_b=[]
    final_dot_bottom=[]
    
    Bridge_wires=[]
    trunk_wire_length=[]
    last_h=[]
    visited=[]
    for i in range(len(wire_list)-1):
        for j in range (i+1, len(wire_list)):
            len_1=len(wire_list[i][1])
            len_2=len(wire_list[j][1])
                   
            if wire_list[i][1][len_1-1]==wire_list[j][1][len_2-1]:
                
    
                htrack_u=maximum_y+((height)/2)+(Layers_dict['M2']['Space']+Layers_dict['M2']['Width'])
                ind=wire_list[i][1][len_1-1]
                color_r= color[ind-1]            
                if wire_list[i][1][len_1-1] not in con_w:
                    if round(htrack_u,5) in assigned_track:
                        for h_track in range (1,50):
                            htrack_u=maximum_y+height/2+(h_track*(Layers_dict['M2']['Space']+Layers_dict['M2']['Width']))
                                                                    
                            if round(htrack_u,5) in assigned_track:
                                continue
                            assigned_track.append(round(htrack_u, 5))
                            
                            break
                    else:                    
                        htrack_u=htrack_u
                        assigned_track.append(round(htrack_u,5))
                else:
                    for k in range (len(con_w_b)):
                        if wire_list[i][1][len_1-1]==con_w_b[k][1]:    
                            htrack_u=con_w_b[k][0]
                            break

                    
                con_t=[]
                con_t.append(htrack_u)
                con_t.append(wire_list[i][1][len_1-1])
                con_w_b.append(con_t)
                if wire_list[i][1][0] not in visited:
                    visited.append(wire_list[i][1][0])
                    Via_Num=Via_Num+1            
                con_w.append(wire_list[i][1][len_1-1])
                
                h_list_h=[]
                for lis_n in range (1, len(wire_list[i][1])-1):
                    h_list_h.append(wire_list[i][1][lis_n])
                    
                min_h=min(h_list_h)
                
                h_list_h_j=[]
                for lis_n in range (1, len(wire_list[j][1])-1) :
                    h_list_h_j.append(wire_list[j][1][lis_n])
                    

                min_h_j=min(h_list_h_j) 
                
                var='D'+str(int(wire_list[i][1][len_1-1]))
               
                trunk_routing_top(wire_list[i][1][0], min_h, htrack_u, Layers_dict, Terminal_list, cap, color_r, var)
                trunk_routing_via(wire_list[i][1][0], min_h, Layers_dict, Terminal_list, cap)
                
                trunk_routing_top(wire_list[j][1][0], min_h_j,  htrack_u, Layers_dict, Terminal_list, cap, color_r, var)
                trunk_routing_via(wire_list[j][1][0],  min_h_j, Layers_dict, Terminal_list, cap)
                x=0

                if wire_list[i][1][0]<wire_list[j][1][0]:
                    x=wire_list[i][1][0]
                else:
                    x=wire_list[j][1][0]                    

                y2=htrack_u
                
                plt.gca().add_patch(patches.Rectangle((x-Layers_dict['M1']['Width']/2-Layers_dict['V1']['VencA_H'], y2-Layers_dict['M2']['Width']/2), abs(wire_list[i][1][0]-wire_list[j][1][0])+2*Layers_dict['V1']['VencA_H']+Layers_dict['M2']['Width'], Layers_dict['M2']['Width'], color=color_r))
                wire_segment_1=wire('M2', None, Layers_dict['M2']['Direction'])
                Terminal_list.append(wire_segment_1.segment(x-Layers_dict['M1']['Width']/2-Layers_dict['V1']['VencA_H'], y2-Layers_dict['M2']['Width']/2, x+abs(wire_list[i][1][0]-wire_list[j][1][0])+Layers_dict['V1']['VencA_H']+Layers_dict['M2']['Width']/2, y2+Layers_dict['M2']['Width']/2, 'drawing', Layers_dict['M2']['Color'][0]))

                bridge_routing_via(wire_list[i][1][0],  htrack_u, Layers_dict, Terminal_list, cap)
                bridge_routing_via(wire_list[j][1][0],  htrack_u, Layers_dict, Terminal_list, cap)                
                
                last_h.append(htrack_u)

                bridge_wire=abs(wire_list[i][1][0]-wire_list[j][1][0]) 
                if wire_list[i][1][len_1-1] not in parasitic_mark:
                    parasitic_mark.append(wire_list[i][1][len_1-1])
                    trunk=[]
                    trunk.append(htrack_u)
                    trunk.append(wire_list[i][1][len_1-1])
                    trunk_wire_length.append(trunk)
                    
                    
                
                if wire_list[i][1][len_1-1] not in final_dot_bottom:
                    final_dot_bottom.append(wire_list[i][1][len_1-1])
    
                Bridge_wires.append(htrack_u)
                
                w=[]
                w.append(bridge_wire)
                w.append(wire_list[i][1])
                w.append(wire_list[j][1])
                connecting_w.append(w) 
    
                
    
    Bridge_wires_new=set(Bridge_wires)
    Bridge_wires_1_new=list(Bridge_wires_new)
    Bridge_wires_1_new.sort(reverse=True) 
    
    Wire_per_cap=[]

    for i in range(len(wire_list)):
        len_1=len(wire_list[i][1])
        if wire_list[i][1][len_1-1] not in final_dot_bottom:
            h_list_h=[]

            final_dot_bottom.append(wire_list[i][1][len_1-1])
            for lis_n in range (1, len(wire_list[i][1])-1) :
                h_list_h.append(wire_list[i][1][lis_n])
            ind=wire_list[i][1][len_1-1]
            color_r= color[ind-1]        
            min_h=min(h_list_h)
            htrack_u=maximum_y+height/2+(Layers_dict['M2']['Space']+Layers_dict['M2']['Width'])
            w_per_cap=[]
            wr=abs(min_h-maximum_y)+wire_list[i][0]
            w_per_cap.append(wr)
            w_per_cap.append(wire_list[i][1][len_1-1])
            Wire_per_cap.append(w_per_cap) 
            Only_per_cap_ratio.append(w_per_cap)
            
            var='D'+str(int(wire_list[i][1][len_1-1]))
            trunk_routing_top(wire_list[i][1][0], min_h, htrack_u, Layers_dict, Terminal_list, cap, color_r, var)
            trunk_routing_via(wire_list[i][1][0],  min_h, Layers_dict, Terminal_list, cap)                
            
            if len(wire_list[i][1])>3:
                for j in range (1, len(wire_list[i][1])-1):
                    trunk_routing_via(wire_list[i][1][0],  wire_list[i][1][j], Layers_dict, Terminal_list, cap)            

        elif wire_list[i][1][len_1-1] in parasitic_mark:
            for j in range (len(trunk_wire_length)):
                if trunk_wire_length[j][1]==wire_list[i][1][len_1-1]:
                    h_list_h=[]
                    
                    for lis_n in range (1, len(wire_list[i][1])-1) :
                        h_list_h.append(wire_list[i][1][lis_n])
                    
                    min_h=max(h_list_h)
                    w_per_cap=[]
                    wr=abs(min_h-maximum_y)+wire_list[i][0]
                    w_per_cap.append(wr)
                    w_per_cap.append(wire_list[i][1][len_1-1])   
                    Wire_per_cap.append(w_per_cap)

                    break
    
    bridge_first_last=[]
    new_connecting_wire=[]            
    for i in range (len(Device_Name)):
        cont=[]
        
        for j in range (len(connecting_w)):
            len_1=len(connecting_w[j][1])
            
            if Device_Name[i]==connecting_w[j][1][len_1-1]:
                cont.append(connecting_w[j][0])

        max_c=0
        if len(cont)>1:
            max_c=max(cont)
            
        elif len(cont)==1:
            
            max_c=cont[0]
        if len(cont)!=0:

            for k in range (len(connecting_w)):
                len_2=len(connecting_w[k][1])
                if Device_Name[i]==connecting_w[k][1][len_2-1]:
    
                            
                    if max_c==connecting_w[k][0]: 
                        wire_v=0
                        for kk in range (len(Wire_per_cap)):
                            if Wire_per_cap[kk][1]==Device_Name[i]:
                                wire_v=wire_v+Wire_per_cap[kk][0]
                                
                        Via_Num=Via_Num+1
                        c_w=[]
                        c_w.append(max_c)
                        c_w.append(connecting_w[k][1])        
                        c_w.append(connecting_w[k][2])
                        wire_v=wire_v+connecting_w[k][0]
                        w_per_cap=[]
                        w_per_cap.append(wire_v)
                        w_per_cap.append(Device_Name[i])
                        Only_per_cap_ratio.append(w_per_cap)
                        new_connecting_wire.append(c_w)
                        b_w=[]
                        b_w.append(connecting_w[k][1][0])
                        b_w.append(connecting_w[k][2][0])
                        bridge_first_last.append(b_w)
    
    Only_per_cap_ratio.sort(key=takeSecond)
    
    return bridge_first_last, Only_per_cap_ratio, last_h, Bridge_wires_1_new, Via_Num, total_bottom_length, new_connecting_wire


