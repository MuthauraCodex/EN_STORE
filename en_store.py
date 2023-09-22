# A python script to execute a simple inventory management system

import sys
import os
import fileinput


def Home():
    print('                    Welcome to EN_STORE!                     ')
    print('=============================================================')
    print('1. View Inventory')
    print('2. Add Inventory')
    print('3. Remove Inventory')
    print('4. Update Inventory')
    print('5. Search Inventory')
    print('00. Exit')
    Choice = int(input('Please enter your option:          '))
    selectitems(Choice)


def selectitems(Choice):
    if Choice == 1:
        View()
    elif Choice == 2:
        Add()
    elif Choice == 3:
        Remove()
    elif Choice == 4:
        Update()
    elif Choice == 5:
        Search()
    elif Choice == 00:
        Exit()


def Exit():
    Exit = exit()


def View():
    InFile = open('data/inventory.txt', 'r')
    item_name = InFile.readline()
    print('                     Viewing Inventory!                      ')
    print('=============================================================')
    while item_name !='':
        item_description = InFile.readline()
        item_name = item_name.rstrip('\n')
        item_description = item_description.rstrip('\n')
        item_quantity = InFile.readline()
        item_name = item_name.rstrip('\n')
        item_quantity = item_quantity.rstrip('\n')
        item_price = InFile.readline()
        item_name = item_name.rstrip('\n')
        item_price = item_price.rstrip('\n')
        print('Item:                 ', item_name)
        print('Description:          ', item_description)
        print('Quantity:             ', item_quantity)
        print('Price in KES:         ', item_price)
        print('=============================================================')
        item_name = InFile.readline()
    InFile.close()

    Choice = int(input('Enter 0 to return to Homepage:          '))
    if Choice == 0:
        Home()
    else:
        exit()


def Add():
    file = open('data/inventory.txt', 'a')
    print('                     Adding Inventory!                       ')
    print('=============================================================')
    item_name = input('Enter the Name of the Product:          ')
    item_description = input('Enter the Description of the Product:          ')
    item_quantity = input('Enter the Quantity of the Product:          ')
    item_price = input('Enter the Unit Price of the Product in (KES):          ')
    file.write(item_name + '\n')
    file.write(item_description + '\n')
    file.write(item_quantity + '\n')
    file.write(item_price + '\n')
    file.close()
    Choice = int(input('Enter 0 to return to Homepage:          '))
    if Choice == 0:
        Home()
    else:
        exit()


def Remove():
    print('                   Removing Inventory!                       ')
    print('=============================================================')
    item_name = input('Enter the Name of the Product:          ')

    file = fileinput.input('data/inventory.txt', inplace=True)

    for line in file:
        if item_name in line:
            for i in range(3):
                next(file, None)
        else:
            print(line.strip('\n'), end='\n')
    item_name
    Choice = int(input('Enter 0 to return to Homepage:          '))
    if Choice == 0:
        Home()
    else:
        exit()


def Update():
    print('                   Updating Inventory!                       ')
    print('=============================================================')
    item_name = input('Enter the Name of the Product:          ')
    item_quantity = int(input('To Update Inventory levels Enter the Quantity to Add; or Enter - for Less:          '))

    with open('data/inventory.txt', 'r') as f:
        filedata = f.readlines()

    replace = ''
    noline = 0
    count = 0
    f = open('data/inventory.txt', 'r')
    file = f.read() .split('\n')
    for i, line in enumerate(file):
        if item_name in line:
            for b in file[i+2:i+3]:
                value = int(b)
                change = value + (item_quantity)
                replace = b.replace(b, str(change))
                noline = count
            count = i + 2
    f.close()

    filedata[count] = replace + '\n'

    with open('data/inventory.txt', 'w') as f:
        for line in filedata:
            f.write(line)


    Choice = int(input('Enter 0 to return to Homepage:          '))
    if Choice == 0:
        Home()
    else:
        exit()


def Search():
    print('                   Searching Inventory!                      ')
    print('=============================================================')
    item_name = input('Enter the Name of the Product to Search:          ')

    f = open('data/inventory.txt', 'r')
    search = f.readlines()
    f.close
    for i, line in enumerate(search):
        if item_name in line:
            for b in search[i:i+1]:
                print('Item:               ', b, end='')
            for c in search[i+2:i+3]:
                print('Quantity:           ', c, end='')
                print('=============================================================')

    Choice = int(input('Enter 0 to return to Homepage:          '))
    if Choice == 0:
        Home()
    else:
        exit()

Home()

