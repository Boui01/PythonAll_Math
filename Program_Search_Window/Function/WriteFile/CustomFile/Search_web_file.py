import re

class Search_web_file : 
    def __init__(self  , file_path  ,word ,word_find:str) :
        self.file_path = file_path
        self.word = word
        self.word_find = word_find

    def Write( self, lines , line_number ):
        if lines[line_number-1] == '\n':
            lines[line_number-1] = self.word + '\n'
        else:
            lines[line_number] = '\n' + lines[line_number].strip()+  self.word + '\n'
        
        # Write the modified and save the file
        with open(self.file_path, 'w') as file:
            file.writelines(lines)
            result = "Success"
            return result

    def Delete( self, lines , line_number ):
        if self.word == 'web_menu' :
            lines[line_number-1] = ''
            lines[line_number] = ''

        elif self.word == 'web' :
            lines[line_number-1] = ''
            lines[line_number] = ''

        else :
            lines[line_number-1] = ''

        with open(self.file_path, 'w') as file:
            file.writelines(lines)
            result = "Success"
            return result