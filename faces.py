def main():
#1 Ask user for their input
    user_input = input()
#2 call the convert function
    result = convert(user_input)
#3 print the result
    print(result)
def convert(text):
     #This tool swaps the faces an
     new_text = text.replace(":)","🙂").replace(":(","🙁")
     return new_text
# This last line tells python for a
main()
