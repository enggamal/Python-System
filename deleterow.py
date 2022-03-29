def delete_row(user_x):
    delete = ""
    with open("/home/gamal/Downloads/python projects/lab_1_python/data.txt", "r") as f:
        lines = f.readlines()
        for i in lines:
            y = list(i.split(','))  
            if y[6] == user_x:
                
                delete = i
                break
    with open("/home/gamal/Downloads/python projects/lab_1_python/data.txt", "w") as f:
        for line in lines:
            print(line)
            if line != delete:
                f.write(line)