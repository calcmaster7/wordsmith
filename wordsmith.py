#  This code continuously makes requests to a dictionary API , and saves the word and definition to a forever growing text file on disk!

from pyfiglet import Figlet
import sys 
import requests
import json
import os

print("-" * 50)
figlet = Figlet()
figlet.getFonts()
figlet.setFont(font="slant")
print(figlet.renderText("WORD_SMITH"))
print("📚 📖 ᒡ◯ᵔ◯ 📚 📖 ᒡ◯ᵔ◯ᒢ 📚 📖 ᒡ◯ᵔ◯ᒢ 📚 📖 ᒡ◯ᵔ◯ᒢ 📚 📖 ᒡ◯ᵔ◯ᒢᒢ 📚 📖 ᒡ◯ᵔ◯ᒢᒢ")
print("Welcome to WORD_SMITH! The World's First Vocabulary Journal Builder!")
print("📖 ᒡ◯ᵔ◯ 📚 📖 ᒡ◯ᵔ◯ 📚 📖 ᒡ◯ᵔ◯ 📚 📖 ᒡ◯ᵔ◯ 📚 📖 ᒡ◯ᵔ◯ 📚 📖 ᒡ◯ᵔ◯ 📚")
print("-"* 50)


if len(sys.argv)  == 2:

    while True:
        new_word = input("enter a word that you want to add to your list or press q to quit: ")
        if new_word.lower() == "q":
            sys.exit("Goodbye!")
        
        response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{new_word}")
        o = response.json()
        if os.path.exists(sys.argv[1]):
            append_or_write = 'a'
        else:
            append_or_write = 'w'

        with open(sys.argv[1], append_or_write) as file:
            file.write("-" * 50)
            file.write("\n")
            file.write(new_word)
            file.write("\n")
            file.write("-"* 50)
            file.write("\n")
            print("-" * 50)
            print(f"The  definitions of {new_word} is: ")

            try:
                for i in range(len(o[0]["meanings"][0]["definitions"])):
                    file.write(f"definition {str(i+1)}:")
                    print(f"definition {str(i+1)}: ")
                    file.write("\n")
                    print(o[0]["meanings"][0]["definitions"][i]["definition"])
                    file.write(o[0]["meanings"][0]["definitions"][i]["definition"])
                    file.write("\n")
                file.write("-"* 50)
                file.write("\n")
            except KeyError:
                print("Sorry our dictionary does not have that word!")
                continue

          
        
        print(f"{new_word} was added to your list!")
        print("-" * 50)
        

else:
    print("You  forgot to put in a file!")
    sys.exit()

