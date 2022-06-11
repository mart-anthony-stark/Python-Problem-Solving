class Email:
    company = "google"

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self) -> str:  # Formatted email (fnamelname@company.com)
        return f"{self.firstname.lower()}{self.lastname.lower()}@{self.company}.com"


# Method for new email input
def create_email():
    fname = input("Enter first name: ")
    lname = input("Enter last name: ")
    return Email(firstname=fname, lastname=lname)

# Show numbered email
def show_email_list():
    print("=================================================")
    print("===========       GENERATED EMAILS      =========")
    print("=================================================")
    for i, email in enumerate(email_list):
        print(str(i+1) + ". " + email.firstname.lower() +
              email.lastname.lower()+"@"+email.company+".com")


email_list = []
email_input = True
print("============= EMAIL LIST GENERATOR =============\n")
while email_input:
    choice = input("\nDo you want to add a name? (yes/no): ")

    if(choice.lower() == "yes"):
        email_list.append(create_email())
    elif(choice.lower() == "no"):
        email_input = False
        show_email_list()
