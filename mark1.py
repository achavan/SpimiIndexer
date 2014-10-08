import string
import parser1 as par
import tokenizer as tok
print ("heloS")
class BlockNextParser:
    chunksize=0
    filename=""
    chunk=list()
   
   
 

    def __init__(self,memory,filname,docid):
        
        chunksize=12994*memory                                   #######################dynamic memory chunk  can change by passing memory value#############
        filename=filname
        #print(chunksize)
        self.bytes_from_file(filename,chunksize,docid)
        
        

    def bytes_from_file(self,filename1, chunksize1,docid):
        with open(filename1) as f:
            
            while True:
                chunk = f.read(chunksize1)
                if  chunk =="":
                    print("===========================the end======================")
                    break
               # f.seek(chunksize1,1)
                send=par.parser()

                newlist=send.Parser(chunk)
                #print(newlist)
                print("=================================================")

                obj1=tok.Tokenize()
                obj1.tokenize(newlist,docid)
            
            
                
                
                




if __name__ == '__main__':
    print ("iam")

    







        
        
