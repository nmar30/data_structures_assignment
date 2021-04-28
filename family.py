class Family:
    def __init__(self):
        self.family = []

    def add_family_member(self):
        print('Enter Family Member!')
        family_member = {
            'fname': input("Enter First Name: "),
            'lname': input("Enter Last Name: "),
            'relationship': input("Enter Relationship: ")
        }
        self.family.append(family_member)

    def print_family_members(self):
        for member in self.family:
            print(member['fname'] + " " + member['lname'] + " Relationship: " + member['relationship'])