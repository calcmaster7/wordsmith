# wordsmith
The world's first vocabulary journal builder! Wordsmith gives you the definition of a word while simultaneously keeping an ever expanding journal of all the words you've ever learned on disk! 

This command line program continuously asks you to give it a word to define, makes requests to a dictionary API, and saves the word/definition to a forever growing text file on disk! Oh, and most importantly, it tells you the definition of the word live in the terminal! 

# Usage
pip install -r requirements.txt

python word_smith.py vocab_journal.txt

# Vocab Journal
vocab_journal.txt can be a vocabulary journal you have already been keeping before even coming across this code, or it can be a completey blank file. The file also doesn't have to exist yet -- if you are starting up your vocab journal for the first time, just include any name you want for your vocabulary list as the second command line argument.  As I did above. The next time you read, pass in the name of this same file and the words/definitions will simply be added to the end in a nice format. I included my recently created vocabulary list just so you can see what it looks like. I was reading a A Hitchhikers Guide to the Galaxy by the way. 

# Coming Soon!!!
I want the program to output the audio pronunciation for every word the user puts in.



# Usage
python word_smith.py vocablist.txt
