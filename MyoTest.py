i = False
while(i == False):
    try:
        input_file = open("pleasework.txt", 'r')
        for line in input_file:
            print(line)
        input_file.close()
    except:
        print("Failed")
