class Company:
    def __init__(self,name):
        self.name=name
    def hire(self):
        return f"{self.name} started to hire freshers"
class organization:
    def hire(self):
        return "organization started hiring"
class industry:
    def hire(self):
        return "industry started to hire" 
def job_search(job):
    print(job.hire())       
        
    