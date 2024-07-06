from parser import parse_input
from handler import *

def main():
    contacts = {}
    
    print('Welcome to my assistant bot!')
    while True:
        user_input = input('Enter a command: ')
        command, *args = parse_input(user_input)
        
        match command:
            case 'hello': 
                print('How can I help you?')
            case 'add': 
                print(add_contacts(args, contacts))
            case 'change': 
                print(change_contact(args, contacts))
            case 'phone':
                print(show_phone(args, contacts))            
            case 'all':
                print(show_all(contacts))
            case 'exit' | 'close': 
                print('Good bye!')
                break
            case _ :
                print('Invalid command')


if __name__ == '__main__':
    main()
    
    

