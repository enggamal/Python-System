file = open("/home/gamal/Downloads/python projects/lab_1_python/data.txt" , 'r')

def emailscheck(email):
    repeated_email = []
    emails =[]
    for line in file :
   
        new_line=line.split(",")

        emails.append(new_line[6])
    for item in emails:
        if item == email:
            return 0
    return 1

      