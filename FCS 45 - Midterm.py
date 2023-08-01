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
def display_statistics(x): #x here is the tickets
    # Function to know the highest number and do statistics
    count = {} #empty dict to keep track of the count of tickets for each event ID.
    for ticket in x:   
        event_id = ticket[1]  
        if event_id in count: #It then checks whether the event_id is already present in the event_count dictionary.
            count[event_id] += 1 # If it is, the count of tickets for that event ID is incremented by 1.
        else:
            count[event_id] = 1 # it's not present, a new entry is added to the dictionary with the event_id as the key and an initial count of 1.
     #After processing all the tickets, the event_count dictionary contains the count of tickets for each event ID.
    if count:
        max_id = max(count, key=count.get) #know it from w3schools #() function along with the key argument, which specifies a function (event_count.get) that calculates the value used for comparison
        print(f" the Id of the highest number of tickets is: {max_id}") #The event ID with the highest count is stored in the variable max_id and now he will printed
    else:
        print("No Ticket found")
#display_statistics() function calculates the count of tickets for each event ID,
#  identifies the event ID with the highest count, and displays the result to the user.
#  This provides insights into the most popular event based on the number of tickets issued.

