from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    hello = 0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    name = simpledialog.askstring(title='Greeter', prompt="do you know how to write code")
    #      // 3.  Use an if statement to check if their answer is correct
    if name== "yes":
        hello = hello+1
    #      // 4.  if the user's answer was correct, add one to their score 
    name1 = simpledialog.askstring(title='Greeter', prompt="do you play a sport")
    if name1== "yes":
        hello = hello+1
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer

    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    
    # Run the window's .mainloop() method
    window.mainloop()
