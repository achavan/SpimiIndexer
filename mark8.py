
import string
import pickle

##############################################################SPimi Implementation#########################################################

class spimi:
    dictionary=dict()
    postinglist=list()
    count=0

    def __init__(self):
        tokenstream=list()
    def ADDToDictionary(self,term,doc_id):
        self.postinglist=self.dictionary.get(term,[])
        self.postinglist.append(doc_id)

        self.dictionary[term]=self.postinglist


        #print(self.postinglist)
    
        

    def spimi(self,tokenstream,doc_id):
        #f=open(output_file,"w")
        
        for token in tokenstream:
            for doc in token.split(" "):
                #print(doc)
                if not doc in self.dictionary:
                    self.ADDToDictionary(doc,doc_id)
                self.postinglist=self.dictionary.get(doc,[])
                if not doc_id in self.postinglist:
                    self.postinglist.append(doc_id)
        allterms=self.dictionary.keys()
        allterms.sort()
        newdict=dict()
        print(doc_id)
        
        for t in allterms:
            newdict[t]=self.dictionary[t]
        self.IndexWriter(newdict)
##############################################################Writing small indexes on the hard disk#####################################

    def IndexWriter(self,newlist):

        print("============================================================================new index created =========================================")
        spimi.count=spimi.count+1
        pickle.dump(newlist,open("index%d"%spimi.count+".p","wb"))
        
        
        
