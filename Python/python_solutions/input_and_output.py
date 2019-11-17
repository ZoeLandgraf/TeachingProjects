# These exercises go over input and output to the command line in python


#Output

#Exercise_1: print a sentence to
def print_to_screen(input_to_be_printed):

    #print the content of the variable "input_to_be_printed" to the screen using python's print function
    print(input_to_be_printed)


#Exercise_2: print a sentence to the screen, but add "This is my sentence" in front of it
def print_to_screen2(input_to_be_printed):

    #print "This is my sentence"  and then the content of the variable 'input_to_be_printed' to the screen using python's print function and using comma separation
    print("This is my sentence", input_to_be_printed)


#Input and Output


#Example:

def Example_input_function():

    # input from keyboard is saved inside variable 'a'
    a = input()
    print(a)

    b = input("Please type the input here:")
    print(b)



#Exercise3: ask the user for his name, save it inside the variable 'name' and then print it back to the screen
def what_is_your_name():

    #Ask the user for his name and save the input in the variable 'name'
    name = input("Please type your name \n")
    #Print the result back to the screen
    print(name)


#Exercise4: ask the user for a number that he wants to multiply by 2 and print out the result
def multiply_by_2():

    number = input("Please enter a number\n")

    # You need to check that the input is a number!
    if not number.isdigit():
        print("You did not input a number")
        #leave the function early
        return

    # Compute the result of multiplying the number by 2 and save it in a variable 'result'
    result = int(number)*2

    # Print out the result (Maybe add a message to the user, such as: "This is your result")
    print("Your number multiplied by 2 is: ", result)



if __name__ == "__main__":

    # Call the function that you want to test here:
    print("Exercise 1: \n")
    print_to_screen("This is the sentence that I want to print to the screen")
    print("\n\n")
    print("Exercise 2: \n")
    print_to_screen2("This is the sentence that I want to print to the screen")
    print("\n\n")
    print("Exercise 3: \n")
    what_is_your_name()
    print("\n\n")
    print("Exercise 4: \n")
    multiply_by_2()
    print("\n\n")
