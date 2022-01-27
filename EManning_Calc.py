from unittest import skip


i = 0

def inputscript():
    global currentnum
    global file1
    tempinput = input("Input (number, clear, end): ")
    try:
        currentnum = float(tempinput)
    except ValueError:
        if tempinput == "clear":
            clearscript()
        elif tempinput == "end":
            file1.close()
            exit()
        else:
            file1.write(str(tempinput) + "\n")
            file1.write("error \n")
            file1.close()
            file1 = open("calcdata.txt", "a+")
            print("error")
            inputscript()

def actionscript():
    global action
    global num2
    global currentnum
    global file1
    action = input("Action (+, -, *, /, clear, end): ")
    try:
        actionnumber = float(action)
    except ValueError:
        if action == "clear":
            skip
        elif action == "end":
            skip
        else:
            tempinput2 = input("Number: ")
            try:
                num2 = float(tempinput2)
                file1.write(str(action) + " " + str(num2) + "\n")
            except ValueError:
                if tempinput2 == "clear":
                    clearscript()
                elif tempinput2 == "end":
                    file1.close()
                    exit()
                else:
                    file1.write(str(action) + " " + str(tempinput2) + "\n")
                    file1.write("error \n")
                    file1.close()
                    file1 = open("calcdata.txt", "a+")
                    print("error")
                    inputscript()
                    actionscript()
    

def clearscript():
    global currentnum
    file1.truncate(0)
    print("cleared")
    inputscript()

file1 = open("calcdata.txt", "a+")
inputscript()
file1.write(str(currentnum) + "\n")
file1.close()
while i == 0:
    file1 = open("calcdata.txt", "a+")
    actionscript()
    if action == "+":
        currentnum += num2
        print("output: " + str(currentnum))
    elif action == "-":
        currentnum -= num2
        print("output: " + str(currentnum))
    elif action == "*":
        currentnum *= num2
        print("output: " + str(currentnum))
    elif action == "/":
        currentnum /= num2
        print("output: " + str(currentnum))
    elif action == "clear":
        clearscript()
    elif action == "end":
        file1.close()
        exit()
    else:
        file1.write("error \n")
        print("error")
        print("output: " + str(currentnum))
    file1.write(str(currentnum) + "\n")
    file1.close()