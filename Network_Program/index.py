from tkinter import *
import tkinter as tk

root = Tk()
root.title('สูตรรวม')
root.minsize(width=400,height=600)
root.configure(background='#FFFFCC')

Data_input = tk.Entry(root,width=20)
Data_label = Label(root,text="ใส่ IP",bg='#FFFFCC')

Data_input_2 = tk.Entry(root,width=20)
Data_label_2 = Label(root,text="ใส่ Request Host",bg='#FFFFCC')
Data_output_2 = Label(root,text="",bg='#FFFFCC')

Data_input_3 = tk.Entry(root,width=20)
Data_label_3 = Label(root,text="ใส่ Request Host",bg='#FFFFCC')

Data_input_4 = tk.Entry(root,width=20)
Data_label_4 = Label(root,text="ใส่ Request Host",bg='#FFFFCC')

Data_input_5 = tk.Entry(root,width=20)
Data_label_5 = Label(root,text="ใส่ Request Host",bg='#FFFFCC')

Data_output = Label(root,text="",bg='#FFFFCC')
Data_output_2 = Label(root,text="",bg='#FFFFCC')
class Data:
    def __init__(self):
        self.data = ''

    def subnet_mask(self,Requesthost):
        subnet = [1,2,4,8,16,32,64,128]
        for i in range(0,len(subnet)):
            process = Requesthost-subnet[i]
            if process < -1:
                result_subnet_int = 0
                for x in range(0,len(subnet)-i):
                    result_subnet_int += subnet[(len(subnet)-1)-x]

                result_subnet = str(result_subnet_int)

                result_pre = str(24+((len(subnet))-i))
                return 'subnet : 255.255.255.'+result_subnet+' /'+result_pre
            
    def next_net_id(self,Iphost,Requesthost):
        subnet = [1,2,4,8,16,32,64,128]
        ip = 0
        for i in range(1,len(Iphost)):
            ip_check = Iphost[len(Iphost)-i]
            if(ip_check == '.'):
                ip = int(Iphost[(len(Iphost)-i)+1:len(Iphost)])
                break
        for i in range(0,len(subnet)):
            process = Requesthost-subnet[i]
            if process < 0:
                result_broadcast = str( ((ip+subnet[i])-2) +2)
                for i in range(1,len(Iphost)):
                    ip_check = Iphost[len(Iphost)-i]
                    if(ip_check == '.'):
                        return Iphost[0:(len(Iphost)-i)+1]+result_broadcast
                    
    def first_last_ip(self,Iphost,Requesthost):
        subnet = [1,2,4,8,16,32,64,128]
        ip = 0
        for i in range(1,len(Iphost)):
            ip_check = Iphost[len(Iphost)-i]
            if(ip_check == '.'):
                ip = int(Iphost[(len(Iphost)-i)+1:len(Iphost)])
                break
        for i in range(0,len(subnet)):
            process = Requesthost-subnet[i]
            if process < 0:
                result_first = str(ip+1)
                result_last = str((ip+subnet[i])-2)
                result_broadcast = str( ((ip+subnet[i])-2) +1)
                for i in range(1,len(Iphost)):
                    ip_check = Iphost[len(Iphost)-i]
                    if(ip_check == '.'):
                        return 'First IP : '+Iphost[0:(len(Iphost)-i)+1]+result_first+'\nLast IP : '+Iphost[0:(len(Iphost)-i)+1]+result_last+\
                                '\nBroadcast IP : '+Iphost[0:(len(Iphost)-i)+1]+result_broadcast
                    
    def Wlan_ip(self,Iphost):
        subnet = [1,2,4,8,16,32,64,128]
        ip = 0
        for i in range(1,len(Iphost)):
            ip_check = Iphost[len(Iphost)-i]
            if(ip_check == '.'):
                ip = int(Iphost[(len(Iphost)-i)+1:len(Iphost)])
                break
        for i in range(0,len(subnet)):
            process = 2-subnet[i]
            if process < 0:
                result_first = str(ip+1)
                result_last = str((ip+subnet[i])-2)
                result_broadcast = str( ((ip+subnet[i])-2) +1)
                for i in range(1,len(Iphost)):
                    ip_check = Iphost[len(Iphost)-i]
                    if(ip_check == '.'):
                        return 'First IP : '+Iphost[0:(len(Iphost)-i)+1]+result_first+'\nLast IP : '+Iphost[0:(len(Iphost)-i)+1]+result_last+\
                                '\nBroadcast IP : '+Iphost[0:(len(Iphost)-i)+1]+result_broadcast        

    def print(self):
            ip = Data_input.get()

            ip_next = Data_input_3.get()
            ip_next_2 = Data_input_4.get()
            ip_next_3 = Data_input_5.get()

            request = int(Data_input_2.get())


            if(len(ip_next) == 0):

                ip_f_l = Data().first_last_ip(ip,request)
                subnet = Data().subnet_mask(request)

                ip_net_next = Data().next_net_id(ip,request)

                wlan = Data().Wlan_ip(ip_net_next)
                subnet_wlan = Data().subnet_mask(2)

                resulte = 'IP : '+ip+'\n'+ip_f_l+'\n'+subnet+\
                        '\n\n------------ wlan ---------------\nIP : '+ip_net_next+'\n'+wlan+'\n'+subnet_wlan

                Data_output.configure(text=resulte)
            elif(len(ip_next_2) == 0):
                request_2 = int(ip_next)

                ip_f_l = Data().first_last_ip(ip,request)
                subnet = Data().subnet_mask(request)

                ip_net_next = Data().next_net_id(ip,request)

                ip_f_l_2 = Data().first_last_ip(ip_net_next,request_2)
                subnet_2 = Data().subnet_mask(request_2)

                ip_net_next_2 = Data().next_net_id(ip_net_next,request_2)

                wlan = Data().Wlan_ip(ip_net_next_2)
                subnet_wlan = Data().subnet_mask(2)

                resulte = 'IP : '+ip+'\n'+ip_f_l+'\n'+subnet+\
                        '\n\n------------ วง 2 ---------------\nIP : '+ip_net_next+'\n'+ip_f_l_2+'\n'+subnet_2+\
                        '\n\n------------ wlan ---------------\nIP : '+ip_net_next_2+'\n'+wlan+'\n'+subnet_wlan

                Data_output.configure(text=resulte)
            elif(len(ip_next_3) == 0):
                request_2 = int(ip_next)
                request_3 = int(ip_next_2)

                ip_f_l = Data().first_last_ip(ip,request)
                subnet = Data().subnet_mask(request)

                ip_net_next = Data().next_net_id(ip,request)

                ip_f_l_2 = Data().first_last_ip(ip_net_next,request_2)
                subnet_2 = Data().subnet_mask(request_2)

                ip_net_next_2 = Data().next_net_id(ip_net_next,request_2)

                ip_f_l_3 = Data().first_last_ip(ip_net_next_2,request_3)
                subnet_3 = Data().subnet_mask(request_3)

                ip_net_next_3 = Data().next_net_id(ip_net_next_2,request_3)

                wlan = Data().Wlan_ip(ip_net_next_3)
                subnet_wlan = Data().subnet_mask(2)

                resulte = '\n\nIP : '+ip+'\n'+ip_f_l+'\n'+subnet+\
                        '\n\n------------ วง 2 ---------------\nIP : '+ip_net_next+'\n'+ip_f_l_2+'\n'+subnet_2+\
                        '\n\n------------ วง 3 ---------------\nIP : '+ip_net_next_2+'\n'+ip_f_l_3+'\n'+subnet_3
                
                resulte_2 = '\n\n------------ wlan ---------------\nIP : '+ip_net_next_3+'\n'+wlan+'\n'+subnet_wlan

                Data_button_2.place(y=250 ,x=300)
                Data_output.configure(text=resulte)
                Data_output_2.configure(text=resulte_2)
            else:
                request_2 = int(ip_next)
                request_3 = int(ip_next_2)
                request_4 = int(ip_next_3)

                ip_f_l = Data().first_last_ip(ip,request)
                subnet = Data().subnet_mask(request)

                ip_net_next = Data().next_net_id(ip,request)

                ip_f_l_2 = Data().first_last_ip(ip_net_next,request_2)
                subnet_2 = Data().subnet_mask(request_2)

                ip_net_next_2 = Data().next_net_id(ip_net_next,request_2)

                ip_f_l_3 = Data().first_last_ip(ip_net_next_2,request_3)
                subnet_3 = Data().subnet_mask(request_3)

                ip_net_next_3 = Data().next_net_id(ip_net_next_2,request_3)

                ip_f_l_4 = Data().first_last_ip(ip_net_next_3,request_4)
                subnet_4 = Data().subnet_mask(request_4)

                ip_net_next_4 = Data().next_net_id(ip_net_next_3,request_4)

                wlan = Data().Wlan_ip(ip_net_next_4)
                subnet_wlan = Data().subnet_mask(2)

                resulte = '\n\nIP : '+ip+'\n'+ip_f_l+'\n'+subnet+\
                        '\n\n------------ วง 2 ---------------\nIP : '+ip_net_next+'\n'+ip_f_l_2+'\n'+subnet_2+\
                        '\n\n------------ วง 3 ---------------\nIP : '+ip_net_next_2+'\n'+ip_f_l_3+'\n'+subnet_3
                
                resulte_2 = '\n\n------------ วง 4 ---------------\nIP : '+ip_net_next_3+'\n'+ip_f_l_4+'\n'+subnet_4+\
                            '\n\n------------ wlan ---------------\nIP : '+ip_net_next_4+'\n'+wlan+'\n'+subnet_wlan

                Data_button_2.place(y=250 ,x=300)
                Data_output.configure(text=resulte)
                Data_output_2.configure(text=resulte_2)

def down_data():
    Data_output.grid_forget()
    Data_output_2.grid()
    Data_button_2.place_forget()
    Data_button_3.place(y=300 ,x=300)
def up_data():
    Data_output.grid()
    Data_output_2.grid_forget()
    Data_button_2.place(y=250 ,x=300)
    Data_button_3.place_forget()




Data_button = tk.Button(master=root,text='Submit',width=5,command=Data().print ,bg='#FFCC99')
Data_button_2 = tk.Button(master=root,text='Down',width=5,command=down_data ,bg='#FFCC99')
Data_button_3 = tk.Button(master=root,text='up',width=5,command=up_data ,bg='#FFCC99')

Data_label.grid(padx=50,pady=5 )
Data_input.grid(padx=250 ,pady=10)       

Data_label_2.grid()
Data_input_2.grid()

Data_button.grid(pady=10)

Data_label_3.grid()
Data_input_3.grid()

Data_label_4.grid()
Data_input_4.grid()

Data_label_5.grid()
Data_input_5.grid()

Data_output.grid()



root.mainloop()