file = open("/home/gamal/Downloads/python projects/lab_1_python/data.txt" , 'r')

def get_salaries():
    salaries = 0
    for line in file :
   
        new_line=line.split(",")

        salaries += int(new_line[2])
         
    return salaries

