

import string
##Mechanishm to select only the conteent within the body#####



class parser :
     
     def Parser(self,chunk):
          #print ("iam here")
          collection=list()
          terms=list()
          
          while True:
               try:
                    
                    i=chunk.index("<BODY>")+6
                    
                    try:
                         j=chunk.index("</BODY>")
                        
                         collection.append(chunk[i:j])
                         chunk=chunk[j+7:]
                         
                         
                    except:
                        collection.append(chunk[i:])                                 #try  gives exception if <BODY>  not found#
                        return collection
                        break
               except :
                    try:
                        
                         k=chunk.index("</BODY>")
                         #print (k)
                         collection.append(chunk[:k])
                         return collection
                         break
                         #chunk=chunk[:k]
                         
                         
                     
                    except:
                        

                         return collection
                         break
               
          

     

if __name__ == '__main__':
     chunk=list()
     anish=" iam an idiot </BODY>"
     par=parser()
     par.Parser(anish)

          

     
        
        
        
