import mark1 as im
import pickle

import os


docid=0
def main():
##     block=im.BlockNextParser(10,"reut2-002.sgm",docid)
     path="C:/Users/a_chav/Downloads/reuters21578.tar/reuters21578"
     for filename in os.listdir(path):
        if filename.endswith(".sgm"):
             docid=docid+1
            block=im.BlockNextParser(10,filename,docid)


     #=================================================Creating main  index fro0m  merging small index===========================#
def InvertedIndex():
     mainindex=dict()
     path="C:/Users/a_chav/Downloads/reuters21578.tar/reuters21578"
     count=0
     for filename in os.listdir(path):
          if filename.endswith(".p"):
             mainindex=pickle.load(open(filename,"rb"))
             pickle.dump(mainindex,open("mainindex.p","a"))
             count=count+1
             print(count)
     
     #=================================================Searching and index for given query===========================#
def IndexSearcehr(token):
     path="C:/Users/a_chav/Downloads/reuters21578.tar/reuters21578"
     Readindex=dict();
     
     Readindex=pickle.load(open("mainindex.p","rb"))
     for key in Readindex.keys():
	if key==token:
             print(Readindex[key])
             
     
##################################lossy compression ########################################     
     
def LossyCompression() :
     path="C:/Users/a_chav/Downloads/reuters21578.tar/reuters21578"
     Readindex=dict();
     #=================================Delelting the numeric value===========================#
     Readindex=pickle.load(open("mainindex.p","rb"))
     for key in Readindex.keys():
	if key.isdigit():
		del Readindex[key]

     #====================================Deleteing StopWords=================================#
     with open("Stopword.txt") as f:	
     Readstopfile=f.read().decode('windows-1252')
     sotplist=list()
     stoplist=Readstopfile.split(",")
     for stopkey in stoplist:
          for key in Readindex.keys():
               if stopkey==key:
                    del Readindex[key]
                    

    
    
    
if __name__ == '__main__':
     
     main()
     InvertedIndex()
     LossyCompression()
     query_term="i want a woman"
     Querytoken=list()
     termlist1=list()
        for doc in querysplit:
            docid1=querysplit.index(doc)
            doc=doc.lower()
            for char in string.punctuation:
                doc=doc.replace(char,"")
            for abc in "\n\t":
                doc=doc.replace(abc," ")
            for token in doc.split(" "):
                Querytoken.append(token)
   
     for token in Querytoken
     IndexSearcehr(token)



