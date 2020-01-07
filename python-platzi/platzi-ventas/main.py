import sys
import csv
import os

CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA = ['name','company', 'email', 'position']
clients = []

def __initialize_clients_from_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames = CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)

def _save_client_to_storage():
    tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

        os.remove(CLIENT_TABLE)
    os.rename(tmp_table_name, CLIENT_TABLE)

# Create a client
def create_client(client):
    global clients

    # if the name is not in the variable, then it will be added.
    if client not in clients:
        clients.append(client)
    else:
        print('The client is already in the client\'s list')

# Print list of clients
def list_clients():
    print('uid\t | name\t | company\t | email\t | position')
    print('*' * 70)

    for idx, client in enumerate(clients):
        print(' {uid}\t | {name}\t | {company}\t | {email}\t | {position} '.format(
            uid         =   idx,
            name        =   client['name'],
            company     =   client['company'],
            email       =   client['email'],
            position    =   client['position'],
        ))

# Update client
def update_client(client_id, update_client):
    global clients

    if len(clients)-1 >= client_id:
        clients[client_id] = update_client
    else:
        print('Client is not in the list.')

# Delete client
def delete_client(client_id):
    global clients

    for idx, _ in enumerate(clients):
        if idx == client_id:
            del clients[idx]
            break

# Search client
def serch_client(client_name):
    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True

def _get_client_field(field_name, message = 'What is the client {}?: '):
    field = None

    while not field:
        field = input(message.format(field_name))

    return field

def _get_client_from_user():
    client = {
        'name'      :   _get_client_field('name'),
        'company'   :   _get_client_field('company'),
        'email'     :   _get_client_field('email'),
        'position'  :   _get_client_field('position'),
    }

    return client

def main():
    print('Welcome to Platzi-Store')
    print('*' * 30)
    print('What would you like to do?')
    print('[C]-Create client')
    print('[L]-List clients')
    print('[U]-Update client')
    print('[D]-Delete client')
    print('[S]-Search client')
    print('\nEnter a letter command')


if __name__ == '__main__':
    __initialize_clients_from_storage()
    main()

    command = input().upper()


    if command == 'C': # Create client
        client = _get_client_from_user()
        create_client(client)

    elif command == 'L': # List clients
        list_clients()

    elif command == 'U': # Update client
        client_id = int(_get_client_field('id'))
        updated_client = _get_client_from_user()
        update_client(client_id, updated_client)

    elif command == 'D': # Delete
        client_id = int(_get_client_field('id'))
        delete_client(client_id)

    elif command == 'S': # Search
        client_name = _get_client_field('name')
        found = serch_client(client_name)

        if found:
            print(f'The client {client_name} is in the clients list')
        else:
            print(f'The client {client_name} is not in the list')
    else:
        print('Invalid command')
    
    _save_client_to_storage()
