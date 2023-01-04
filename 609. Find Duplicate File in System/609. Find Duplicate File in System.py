class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        content = defaultdict(list)
        result = []
        
        for dirctories in paths:
            
            dirctories = dirctories.split() #splitting path from file names
            path = dirctories[0]
            
            files_count = len(dirctories)-1 #determine number of files
            
            for file in range(files_count):
                
                file = dirctories[file +1].split('(') #splitting contnet from file name
                
                if not content[file[1]]:    #checking if the content was a duplicate
                    content[file[1]].append(path +'/'+ file[0]) #adding dirictories of same content 
                    continue
                    
                content[file[1]].append(path +'/'+ file[0])
                result.append(file[1]) #puting contents with duplicate on list
            
        
        result = [content[duplicate] for duplicate in list(set(result))]
        
        return result # return the duplicate dirictories
