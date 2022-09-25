currentnum = 0
reset = True

def clear():
    global reset
    file1 = open("calcdata.txt", "a+")
    file1.truncate(0)
    print("cleared")
    reset = True

def error():
    global reset
    file1 = open("calcdata.txt", "a+")
    file1.write(f"{str(tempInput)}\nERROR \n")
    file1.close()
    print("ERROR BAD INPUT")
    reset = True

while True:
    while reset:
        tempInput = input("Input (number, clear, end): ")
        try:
            currentnum = float(tempInput)
            file1 = open("calcdata.txt", "a+")
            file1.write(f"{str(currentnum)} \n")
            file1.close
            reset = False
        except ValueError:
            if tempInput.upper() == "CLEAR":
                clear()
                continue
            if tempInput.upper() == "END":
                exit()
            error()
            
    action = input("Action (+, -, *, /, clear, end): ")
    if action.upper() == "CLEAR":
        clear()
        continue
    if action.upper() == "END":
        exit()

    tempInput2 = input("Input (number, clear, end): ")
    try:
        num2 = float(tempInput2)
    except ValueError:
        if tempInput2.upper() == "CLEAR":
            clear()
            continue
        if tempInput2.upper() == "END":
            exit()
        error()
        continue

    if action == "+":
        file1 = open("calcdata.txt", "a+")
        file1.write(f"+ {num2}\n")
        file1.close()
        currentnum += num2
        print(f"output: {str(currentnum)}")
    elif action == "-":
        file1 = open("calcdata.txt", "a+")
        file1.write(f"- {num2}\n")
        file1.close()
        currentnum -= num2
        print(f"output: {str(currentnum)}")
    elif action == "*":
        file1 = open("calcdata.txt", "a+")
        file1.write(f"* {num2}\n")
        file1.close()
        currentnum *= num2
        print(f"output: {str(currentnum)}")
    elif action == "/":
        file1 = open("calcdata.txt", "a+")
        file1.write(f"/ {num2}\n")
        file1.close()
        currentnum /= num2
        print(f"output: {str(currentnum)}")
    else:
        error()
        continue
    file1 = open("calcdata.txt", "a+")
    file1.write(f"{str(currentnum)} \n")
    file1.close()