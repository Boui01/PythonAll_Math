import re
from Function.WriteFile.CustomFile.Search_web_file import Search_web_file
class WriteFile:
    def __init__(self , from_file) :
        #text = input("Enter some text to write to the file: ")
        self.from_file = from_file
        pass
    #------------------------------------------------- Read File -------------------------------------------
    def Read ( self , file_path ):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return lines
        

    #-------------------------------------------------- Find File -------------------------------------------   
    def Find ( self ,  file_path  , word_find , word_find2 = '' , word_find3 = '' ):
        with open(file_path, 'r') as file:
            line_number = 0
            found = False
            result = "Founded"
            pattern = re.compile(rf'\b{re.escape(word_find)}\b', re.IGNORECASE)            
            pattern2 = re.compile(rf'\b{re.escape(word_find)}\b', re.IGNORECASE)
            pattern3 = re.compile(rf'\b{re.escape(word_find)}\b', re.IGNORECASE)


            for line in file:
                line_number += 1
                if pattern.search(line) and ( True if word_find2 == '' else pattern2.search(line)  ) and ( True if word_find3 == '' else pattern3.search(line) ):
                    print(f"Found '{word_find}' on line {line_number}: {line.strip()}")
                    found = True
                    break
            if not found:
                print(f"'{word_find}' not found in the file.")
                result = "Not found"
                return {'found' : found , 'text' : result}
            
            return {'found' : found , 'text' : result}
        

    #------------------------------------------------- Write File -------------------------------------------    
    def  Write( self  , file_path  ,word:str ,word_find ):
        try:
            if word_find != '' :
                with open(file_path, 'r') as file:
                    line_number = 0
                    found = False
                    # Compile regex to search for whole word matches, case-insensitive
                    pattern = re.compile(rf'\b{re.escape(word_find)}\b', re.IGNORECASE)

                    # Write the modified and save the file
                    for line in file:
                        line_number += 1
                        if pattern.search(line):
                            print(f"Found '{word_find}' on line {line_number}: {line.strip()}")
                            found = True
                            
                            with open(file_path, 'r') as file:
                                lines = file.readlines()
                            
                            # Check if the line number is within the range of the file
                            if line_number < 1 or line_number > len(lines):
                                print(f"Line {line_number} is out of range. The file has {len(lines)} lines.")
                                result = "Fail out rage"+f"\nLine {line_number} is out of range. The file has {len(lines)} lines."
                                return result
                            
                            if self.from_file == 'Search_web':
                                search_web_file = Search_web_file( file_path = file_path ,word = word ,word_find = word_find )
                                return search_web_file.Write(lines = lines , line_number = line_number )
                            else : 
                                lines[line_number] = '\n' + lines[line_number].strip()+  word + '\n'
                                
                                # Write the modified and save the file
                                with open(file_path, 'w') as file:
                                    file.writelines(lines)
                                    result = "Success"
                                    return result
                                
                        print(f"Inserted '{word}' into line {line_number}.")
                    # return word not found       
                    if not found:
                        print(f"'{word_find}' not found in the file.")
                        result = "Found Fail"+f"'\n{word_find}' not found in the file."
                        return result


            else:
                result = "Plese enter word!"
                return result 
        except FileNotFoundError:
            print(f"The file '{file_path}' was not found.")
            result = "File not found"+f"\nThe file '{file_path}' was not found."
            return result
        except Exception as e:
            print(f"An error occurred: {e}")
            result = "Error"+f"\nAn error occurred: {e}"
            return result
        

    #--------------------------------- Delete Word ------------------------------------------------    
    def Delete( self,file_path  ,word:str ,word_find ):
        try:            
            if word_find != '':
                with open(file_path, 'r') as file:
                    line_number = 0
                    found = False
                    # Compile regex to search for whole word matches, case-insensitive
                    pattern = re.compile(rf'\b{re.escape(word_find)}\b', re.IGNORECASE)

                    for line in file:
                        line_number += 1
                        if pattern.search(line):
                            print(f"Found '{word_find}' on line {line_number}: {line.strip()}")
                            found = True
                            
                            with open(file_path, 'r') as file:
                                lines = file.readlines()
                            
                            # Check if the line number is within the range of the file
                            if line_number < 1 or line_number > len(lines):
                                print(f"Line {line_number} is out of range. The file has {len(lines)} lines.")
                                result = "Fail out rage"
                                return result
                            
                            # Custom file from
                            if self.from_file == 'Search_web':
                                search_web_file = Search_web_file( file_path = file_path ,word = word ,word_find = word_find )
                                return search_web_file.Delete(lines = lines , line_number = line_number )
                            else :
                                lines[line_number-1] = ''
                                # Write the modified and save the file
                                with open(file_path, 'w') as file:
                                    file.writelines(lines)
                                    result = "Success"
                            print(f"Inserted '{word}' into line {line_number}.")

                    if not found:
                        print(f"'{word_find}' not found in the file.")
                        result = "Found Fail"
                        return result
                    return result

            else:
                result = "Plese enter word!"
                return result 
        except FileNotFoundError:
            print(f"The file '{file_path}' was not found.")
            result = "File not found"
            return result
        except Exception as e:
            print(f"An error occurred: {e}")
            result = "Error"
            return result