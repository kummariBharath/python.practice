class Company: #polymorphism
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

job_search(Company("google"))
job_search(organization())
job_search(industry())   
job_search(Company("TCS"))

        
    