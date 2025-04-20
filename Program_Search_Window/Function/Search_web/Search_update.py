from Function.WriteFile.WriteFile import WriteFile

def Sh_web_update( type ,text = []  , text_menu = [] , text_menu_web = [] ):
    status = ''
    WriteFile_web = WriteFile(from_file ='Search_web' )
    #--------- Check Emtry -----------
    Input_emtry = False
    for i in text :
        if i == '' :
            Input_emtry = True
    #-------------------------------------------------- Add Button --------------------------------------------------
    if type == 'Button' and not Input_emtry :
        status = WriteFile_web.Write(   file_path= r'E:\Backup_MyPC\Code\save\Pytron\Program_Search_Window\Function\Search_web\Search_web.py' ,
                                        check = {'text' : text[0] ,'web' : text[1] },
                                        word="            "+"{'text' : '"+text[0]+"' , 'command' : web."+text[1]+" , 'type' : 'Button' }," ,
                                        word_find='self.list_create_btn_sh_body'
        )
        if status == 'Success' :
            #------------------------------------------- Add Button Web --------------------------------------------------
            status = WriteFile_web.Write(   file_path= r'E:\Backup_MyPC\Code\save\Pytron\Program_Search_Window\Function\Web\Web.py' ,
                                            check = {'text' : text[0] ,'web' : text[1] },
                                            word="    def "+text[1]+"(self):\n        webbrowser.open('"+text[2]+"')" ,
                                            word_find='class Web'
            )
        return status
    
    #-------------------------------------------------- Add Menu --------------------------------------------------
    elif type == 'Menu' :
        status = WriteFile_web.Write(   file_path= r'E:\Backup_MyPC\Code\save\Pytron\Program_Search_Window\Function\Search_web\Search_web.py' ,
                                        check= {'text' : text[0] ,'web' : text[1] },
                                        word="            "+"{'text' : '"+text[0]+"' , 'command' : web."+text[1]+" , 'type' : 'Menu' , "+
                                            "'sub_mn_text' : ["+""
                                            .join('' if text_menu[ len(text_menu)-1-i ] == 'None' or text_menu[ len(text_menu)-1-i ] == '' else "'"+str(text_menu[ len(text_menu)-1-i ])+"'," for i in range( len(text_menu )))+"],"+
                                            " 'sub_mn_command' : ["+""
                                             .join('' if text_menu[ len(text_menu)-1-i ] == 'None' or text_menu[ len(text_menu)-1-i ] == '' else "'"+str(text_menu[ len(text_menu)-1-i ])+"'," for i in range( len(text_menu )))+"]," +
                                            "}," ,
                                        word_find='self.list_create_btn_sh_body'
        )
        if status == 'Success' :
            #---------------------------------------------------- Add Menu Web  --------------------------------------------------
            status = WriteFile_web.Write(   file_path= r'E:\Backup_MyPC\Code\save\Pytron\Program_Search_Window\Function\Web\Web.py' ,
                                            check= {'text' : text[0] ,'web' : text[1] },
                                            word="    def "+text[1]+"(self):\n        webbrowser.open('"+text[2]+"')" ,
                                            word_find='class Web'
            )

            if status == 'Success' :
                for i in range(len(text_menu)) :
                    if text_menu[len(text_menu)-1-i] == 'None' or text_menu[len(text_menu_web)-1-i] == '' :
                        continue
                    else :
                        status = WriteFile_web.Write(   file_path= r'E:\Backup_MyPC\Code\save\Pytron\Program_Search_Window\Function\Web\Web.py' ,   
                                                        check= {'text' : text_menu[len(text_menu)-1-i] ,'web' : text_menu_web[len(text_menu_web)-1-i] },   
                                                        word="    def "+text_menu[len(text_menu)-1-i]+"(self):\n        webbrowser.open('"+text_menu_web[len(text_menu_web)-1-i]+"')" ,
                                                        word_find='class Web'
                        )
        return status
    return "Plese check your input!"