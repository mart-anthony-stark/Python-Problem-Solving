class Email:
    company = "google"

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


class Emails:
    def __init__(self) -> None:
        self.email_list = []
        self.email_input = True

    def generate(self) -> None:
        print("============= EMAIL LIST GENERATOR =============\n")
        while self.email_input:
            choice = input("Do you want to add a name? (yes/no): ")

            if(choice.lower() == "yes"):
                fname = input("Enter first name: ")
                lname = input("Enter last name: ")
                newEmail = Email(firstname=fname, lastname=lname)
                self.email_list.append(newEmail)
            elif(choice.lower() == "no"):
                self.email_input = False

        print("=================================================")
        print("===========       GENERATED EMAILS      =========")
        print("=================================================")
        for i, email in enumerate(self.email_list):
            print(str(i+1) + ". " + email.firstname.lower() +
                email.lastname.lower()+"@"+email.company+".com")
