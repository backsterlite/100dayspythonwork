#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# Read mail template
with open('Input/Letters/starting_letter.txt', mode='r') as template:
    mail_blueprint = template.read()

# Read names
with open("Input/Names/invited_names.txt", mode='r') as names:
    name_list = names.readlines()

# Generate file to send
for name in name_list:
    person = name.strip()
    text = mail_blueprint.replace("[name]", person)
    file_name = f"letter_for_{person}.txt"
    file_path = "Output/ReadyToSend/"
    with open(file_path + file_name, mode='w') as file:
        file.write(text)



