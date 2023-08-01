#<Ali Aghawani> <FCS 45> <Midterm>
import datetime #we use it to use the for time , for get_current_date function (datetime.date.today)
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
def book_ticket(tickets, ticket_id, event_id, username, timestamp, priority): #The function here take 6 parameters 
    # Function to book a new ticket and add it to the list of tickets
    tickets.append([ticket_id, event_id, username, timestamp, priority])  #The function starts by creating a new list that represents the details of the new ticket to be booked. The details are stored as elements in the list in the following order: ticket_id, event_id, username, timestamp, and priority. This new list is created as [ticket_id, event_id, username, timestamp, priority].
    print("Thank you")
    print(f"Ticket {ticket_id} has been booked")
#book_ticket() function is used to book a new ticket and add it to the list of existing tickets. 
# It receives the necessary information about the new ticket (ticket ID, event ID, username, timestamp, and priority) as arguments and appends this information as a new list to the tickets list. 
# The function provides user feedback by printing a message confirming the successful booking of the new ticket.
def get_current_date():
    # Returns the current date in the format 'YYYY-MM-DD'
    return datetime.date.today().isoformat() #form stackoverflow I know it 
def get_sort_key(ticket):
    # Function to get the sort key for displaying all tickets
    return (ticket[3], ticket[1])
def display_all_tickets(tickets):
    # Function to display all tickets ordered by event's date and event ID
    today = get_current_date() #the current date as we mentioned before 
    sorted_tickets = sorted(tickets, key=get_sort_key)
    for ticket in sorted_tickets:
        if ticket[3] >= today:  #For each ticket, it checks if the event date (index 3 of the ticket list) is greater than or equal to the today date.
            print(", ".join(ticket))
#display_all_tickets() function displays all the tickets in the tickets list ordered by their event dates and event IDs.
#  It filters out tickets whose event dates are in the past, ensuring that only tickets for today and future events are displayed. 
# This provides an organized and up-to-date list of tickets for the users to view.
def get_priority(ticket):
    # Function to get the priority for sorting today's events
    return int(ticket[4])
def run_events(tickets):
    # Function to display today's events, sorted by priority, and remove them from the list
    today = get_current_date() #as we mentioned before
    today_events = [] # today_events to store tickets that have today's date as their event date.
    for ticket in tickets: #It iterates over each ticket in the tickets list and checks if the event date matches the today date.
        if ticket[3] == today: #check if yes equal to today
            today_events.append(ticket) #If the ticket's event date is today, it is added to the today_events list.
        if not today_events: 
            print("No events today.")   #After processing all tickets, it checks if there are any events for today in the today_events list. If there are no events for today, it prints "No events today."
        return today_events.sort(key=get_priority) #The today_events list is sorted by ticket priority using the sort() method and a custom key function get_priority.
    for ticket in today_events:
        print(", ".join(ticket)) #or each ticket in today_events, it prints the ticket information to the console using ", ".join(ticket).
        tickets.remove(ticket) #The remove() method is used to remove the today's events from the original tickets list, ensuring they won't be displayed again in subsequent runs of the program.
#run_events() function displays today's events sorted by priority and then removes these events from the original tickets list.
#  If no events are found for today, it prints a message indicating that there are no events for today.
#  The function provides an organized way to display today's events and manage the list of tickets by removing the events that have already occurred
def disable_ticket(tickets, ticket_id): # tickets (the list of all tickets) and ticket_id (the ID of the ticket to be disabled).
    # Function to disable a ticket
    for ticket in tickets:
        if ticket[0] == ticket_id:   
            tickets.remove(ticket) #If a ticket with the specified ticket_id is found (ticket[0] == ticket_id), it is removed from the tickets list using the remove() method.
            print(f"Ticket {ticket_id} has been disabled and not considered anymore.")
            return print(f"Ticket {ticket_id} not found.")
#disable_ticket() function disables a ticket by removing it from the tickets list if it exists. 
# It provides user feedback on whether the ticket was successfully disabled or if the ticket with the specified ticket_id was not found. 
# However, it's important to be cautious when modifying a list while iterating over it, as it can lead to unexpected issues.
