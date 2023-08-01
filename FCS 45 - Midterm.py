#<Ali Aghawani> <FCS 45> <Midterm>
# Function to read tickets from a text file and return a list of tickets 
def read(fileName): 
    tickets = [] 
    file = open(fileName, 'r') #open() function it s a built-in function  I take it from w3Schools this function for open files it take 2 parameters the first one for the file name you want to open and the second the mode how the the file should be opened
    for x in file:
        ticket_information = x.strip().split(', ') #strip method for avoid the spaces #split for transform the data types to list
        tickets.append(ticket_information) 
    file.close()
    return tickets
 #read() function is designed to read ticket information from a text file and organize it in a list of lists,
 #  where each inner list represents the details of a single ticket. The function abstracts the file handling and parsing details, 
 # making it convenient to retrieve ticket information from the provided text file
