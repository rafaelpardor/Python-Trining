
# Flow control using while, and a if statement.

import random
import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed {} .\n'.format(response))