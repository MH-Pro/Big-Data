#Begin
#This is a Simple ChatBot Program Written in Python

#This is the dataset along with question and answers. i.e {"Question":"Answer"}
d={"hello":"Hi","how are you":"Im am fine how about you.","bye":"Good Bye","introduce yourself":"I am a Simple Chatbot."}

while True: # A Forever Loop to run the program until user says good bye.
        a=input(">> ") # Takes input from user and stores it in a Variable
        if "bye" in a.lower(): # Condition if user write bye
                print(d[a.lower()]) # Then Print the answer
                exit() # and Exit
        elif a.lower() not in d: # Else if user's answer is not found in dataset.
                print("I wasn't able to find your answer in my dataset.") # Print answer not found in dataset.
        else: # Else
                print(d[a.lower()]) # Give the user the answer to his question.
#END
