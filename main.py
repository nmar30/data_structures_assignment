from sweepstakes import Sweepstakes
from family import Family
from linkedlist import LinkedList
from binarytree import BinaryTree

def months_of_year():
    months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
    print(months[2])

def celebrate_birthdate():
    locations = {'Olive Garden', 'Bahamas', 'Montreal'}
    print('Please enter 3 locations you would like to celebrate your birthday!')
    i = 0
    while i < 3:
        locations.add(input(f'Please enter location #{i+1}: '))
        i += 1
    for location in locations:
        print(location)


# months_of_year()
#
# celebrate_birthdate()
#
# sweepstakes1 = Sweepstakes()
# sweepstakes1.pick_winner()

# family1 = Family()
# family1.add_family_member()
# family1.add_family_member()
# family1.print_family_members()

# linked_list1 = LinkedList()
# linked_list1.append_node(55)
# linked_list1.append_node(60)
# linked_list1.append_node(65)
# linked_list1.depend_node(50)
# linked_list1.contains_node(60)
# linked_list1.contains_node(45)

binary_tree1 = BinaryTree()
binary_tree1.append_node(50)
binary_tree1.append_node(75)
binary_tree1.append_node(60)
binary_tree1.append_node(30)
# binary_tree1.contains_node(50)
# binary_tree1.contains_node(35)