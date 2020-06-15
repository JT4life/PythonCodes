'''1.String ::: usa is a country | USA IS A COUNTRY  
            ------------------------->  
        WRITE IN THE FILE WORD BY WORD AFTER CONVERT IT IN UPPER CASE OR LOWER CASE  
---USING FUNCTION ---  
---CLASS --  
---------------------------  
        READ THE DATA FROM FILE ---  
        USA  
        IS  
        A  
        COUNTRY ''' 


class a:
    def w(self):
        word = "usa is a country"
        word1 = ""
        if word[0].islower():
            word1 = word.replace("usa is a country","USA IS A COUNTRY")
            print(word.upper())
        else:
            word1 = word.replace("USA IS A COUNTRY","usa is a country")
            print(word.lower())
        try:
            fh=open("USA.txt", "w")
            fh.write(word1)
            fh.close()
        except Exception as e:
            print("Error =",e)
            
    def q(self):
        fh=open("USA.txt", "r")
        print(fh.read(3))
        print(fh.read(3))
        print(fh.read(2))
        print(fh.read(12))
      
        
z = a()
z.w()
z.q()
