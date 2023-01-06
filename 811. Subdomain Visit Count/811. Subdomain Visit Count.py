class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        domain = defaultdict(list)
        
        for cpdomain in cpdomains:
            
            cpdomain = cpdomain.split()                 #split domain and count
            count = int(cpdomain[0])                    
            cpdomain = cpdomain[1].split('.')[::-1]     #split each domain
            
            subdomain = ''
            
            for dom in cpdomain:    
                
                if subdomain:
                    subdomain = '.' + subdomain
                
                subdomain = dom + subdomain
                
                if not domain[subdomain]:           #each domain count
                    domain[subdomain] = count
                    continue
                
                domain[subdomain] += count          #domain count is added if there is duplicate
                
        
        result = [str(domain[dom]) +' '+ dom for dom in domain.keys()] #changeing the result to list
        
        return result
