from Function.WriteFile.WriteFile import WriteFile
import re

class MySQL_language:
    def __init__(self, text) :
        self.text_translate = text
        pass
    def Translate(self, From) :
        if From == 'Laravel' :
            return self.Translate_Laravel( )

    def Translate_Laravel(self ) :

        def get_parenthesis(text , type = 'column') :
            #  (any character) start
            #  \ use front special character / when have special character
            # .* get any character behide this 
            #  ? (any character) not get more when see character behide ? this
            #  () can use of don't use \  | but when use only such as ( or ) must use \ such as \( or \)
            #  (any character) end "
            if type == 'column' :
                return re.findall(r"\((.*?)\)", text)
            elif type == 'table' :
                return re.findall(r"'(.*?)'", text)
        
        def check_sub_command(text , get_pts , start) :
            command = re.compile('->')
            primary = re.compile('primary')
            foreign = re.compile('foreign')
            nullable = re.compile('nullable')
            unique = re.compile('unique')


            if command.search(text[start:start+len('->')]) :
                if primary.search(text[start:start+len('->')+len('primary')]) :
                    return str(get_pts[0])+ '  PRIMARY KEY'
                elif foreign.search(text[start:start+len('->')+len('foreign')]) :
                    return str(get_pts[0])+ '  FOREIGN KEY'
                elif nullable.search(text[start:start+len('->')+len('nullable')]) :
                    return str(get_pts[0])+ '  NOT NULL'
                elif unique.search(text[start:start+len('->')+len('unique')]) :
                    return str(get_pts[0])+ '  UNIQUE'
                else :
                    return str(get_pts[0])                        
            else :
                return str(get_pts[0])


        new_text = ''
        open_command = re.compile(r'\$table->')
        create = re.compile('Schema::create')
        string = re.compile('string' )
        integer = re.compile('integer')
        timestamp = re.compile('timestamp')
        date = re.compile('date')
        softDeletes = re.compile('softDeletes')
        for i in range ( len(self.text_translate) ) :

            if create.search(self.text_translate[i:i+len('Schema::create')]) :
                get_pts = get_parenthesis(self.text_translate[i:i+len('Schema::create')+80], type = 'table')
                new_text += '\n'+'TABLE NAME  '+str(get_pts) + '\n'
            else :
                if open_command.search(self.text_translate[i:i+len('$table->')]) :                        
                    new_text += '\n'    
                    if string.search(self.text_translate[i+len('$table->') : i+len('$table->')+len('string')]) :
                        get_pts = get_parenthesis(self.text_translate[i+len('$table->') : i+len('$table->')+len('string')+80])                    
                        new_text +=  'VARCHAR  '+ check_sub_command(self.text_translate , get_pts , i+len('$table->')+len('string')+len(get_pts[0])+2)

                    elif integer.search(self.text_translate[i+len('$table->') : i+len('$table->')+len('integer')]) :
                        get_pts = get_parenthesis(self.text_translate[i+len('$table->'):i+len('$table->')+len('integer')+80])
                        new_text += 'INTEGER  '+ check_sub_command(self.text_translate , get_pts , i+len('$table->')+len('integer')+len(get_pts[0])+2)

                    elif timestamp.search(self.text_translate[i+len('$table->') : i+len('$table->')+len('timestamp')]) :
                        get_pts = get_parenthesis(text = self.text_translate[i+len('$table->'):i+len('$table->')+len('timestamp')+80])
                        new_text += 'DATE  '+ check_sub_command(self.text_translate , get_pts , i+len('$table->')+len('timestamp')+len(get_pts[0])+2)

                    elif date.search(self.text_translate[i+len('$table->') : i+len('$table->')+len('date')]) :    
                        get_pts = get_parenthesis(text = self.text_translate[i+len('$table->') : i+len('$table->')+len('date')+80])
                        new_text += 'DATE  '+ check_sub_command(self.text_translate , get_pts , i+len('$table->')+len('date')+len(get_pts[0])+2)

                    elif softDeletes.search(self.text_translate[i:i+len('softDeletes')]) :
                        get_pts = 'deleted_at'
                        new_text += 'DATE  '
     
            
        return {'result' : True , 'text' : new_text}