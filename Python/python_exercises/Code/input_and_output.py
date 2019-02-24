# These exercises go over input and output to the command line in python

#Output

#Exercise_1: print a sentence to
def print_to_screen(input_to_be_printed):

    #print the content of the variable "input_to_be_printed" to the screen using python's print function



#Exercise_2: print a sentence to the screen, but add "This is my sentence" in front of it
def print_to_screen_2(input_to_be_printed):

    #print "This is my sentence"  and then the content of the variable 'input_to_be_printed' to the screen using python's print function and using comma separation


#Input and Output


#Example:

def Example_input_function():

    # input from keyboard is saved inside variable 'a'
    a = input()
    print(a)

    # input from keyboard is saved inside variable 'b'
    b = input("Please type the input here:")
    print(b)



#Exercise3: ask the user for his name, save it inside the variable 'name' and then print it back to the screen
def what_is_your_name():

    #Ask the user for his name and save the input in the variable 'name'
    name = input("Please type your name \n")  # Note: the '\n' adds a newline to the output.
    #Print the result back to the screen



#Exercise4: ask the user for a number that he wants to multiply by 2 and print out the result
def multiply_by_2():

    # Ask the user to enter a number and save input in a variable called 'number'


    # You need to check that the input is a number!
    if not number.isdigit():
        print("You did not input a number")
        #leave the function early
        return

    # Compute the result of multiplying the number by 2 and save it in a variable 'result'


    # Print out the result (Maybe add a message to the user, such as: "This is your result")




if __name__ == "__main__":

    # Call the function that you want to test here:

    # For example, to call 'print_to_screen':
    #print_to_screen("This is the sentence that I want to print to the screen")


        # Call the function that you want to test here:
        print("Exercise 1: \n")
        #Call the function print_to_screen() of Exercise1 here. Dont forget to give it an input!

        print("\n\n")
        print("Exercise 2: \n")
        #Call the function print_to_screen2() of Exercise1 here. Dont forget to give it an input!

        print("\n\n")
        print("Exercise 3: \n")
        #Call the function what_is_your_name() of Exercise3 here.This function does not need an input

        print("\n\n")
        print("Exercise 4: \n")
        #Call the function multiply_by_2() of Exercise4 here.This function does not need an input
