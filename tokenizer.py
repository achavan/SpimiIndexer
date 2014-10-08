import string


import mark8 as sp

            
######################## Preprocessing of tokens############################
class Tokenize:
    tookenstream=list()
    
    def tokenize(self,tookenstream,docid):
        termlist1=list()
        for doc in tookenstream:
            doc_id=tookenstream.index(doc)
            doc=doc.lower()
            for char in string.punctuation:
                doc=doc.replace(char,"")
            for abc in "\n\t":
                doc=doc.replace(abc," ")
            for token in doc.split(" "):
                termlist1.append(token)
                #print(token)
        index=sp.spimi()
        index.spimi(termlist1,docid)

        
   
