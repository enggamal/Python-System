file = open("/home/gamal/Downloads/python projects/lab_1_python/data.txt" , 'r')

def get_line(enteremail,enterpassword):
   for line in file :
   
      new_line=line.split(",")

      if enteremail == new_line[6] and enterpassword == new_line[7]:
         
         return new_line