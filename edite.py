
def edit_values(user_x,old_value,new_value):
    delete = ""
    old_row = ""
    with open("/home/gamal/Downloads/python projects/lab_1_python/data.txt", "r") as f:
        lines = f.readlines()
        for i in lines:
            y = list(i.split(','))  
            if y[6] == user_x:
                delete = i
                old_row = delete
                indx = y.index(old_value)
                y[int(indx)] = new_value
                i = ",".join(y)
                break
    with open("/home/gamal/Downloads/python projects/lab_1_python/data.txt", "w") as f:
        for line in lines:
            if line != old_row:
                f.write(line)
    with open("/home/gamal/Downloads/python projects/lab_1_python/data.txt", "a") as f:
        f.write('\n'+i)           