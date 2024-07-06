def add_contacts(args, contact):
    name, phone = args
    if name not in contact:
        contact[name] = phone
        return 'Contact added'
    else:
        return 'Сontact already created'


def change_contact(args, contact):
    name, new_phone = args
    
    if name in contact:
        contact[name] = new_phone
        return 'Contact updated'
    else:
        return 'Contact not found'

    
def show_phone(args, contact):
    name = args[0] 
    if name in contact:
        return contact[name]
    else:
        return 'Contact not found'
    

def show_all(contact): 
    if not contact:
        return 'Contacts not found'
    else:
        contacts_info = ''
        for name, phone in contact.items(): 
             contacts_info += f'Name : {name}, Phone : {phone}\n'
    return contacts_info
        
    