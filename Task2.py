#Task 2: Your Mood Today Ask the user how they feel today. 
#If they say "happy", print "That's great to hear!", 
#and if they say "sad", print "I hope your day gets better!". 
#Ensure your if statement is properly indented. 
#INT: Use the input() function to ask the user how they feel! 

user_name = input("What is your name?") + "!"
feelings=''
feelings = input("How do you feel today?")
if feelings == "happy" or feelings == "Happy":
    print("That's great to hear", user_name)
elif feelings =="sad" or feelings == "Sad":
    print("I hope your day gets better", user_name)
else:
    print("I'm sorry, but", feelings, "is not a correct input " + user_name)
    

