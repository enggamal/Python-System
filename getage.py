file = open("/home/gamal/Downloads/python projects/lab_1_python/data.txt" , 'r')
def get_age(employeename):
   for line in file :
   
        new_line=line.split(",")
        
        if employeename == new_line[1]:
            age = new_line[3]

            return age