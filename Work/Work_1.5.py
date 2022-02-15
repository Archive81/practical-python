element_list = []
while True:
    print('''
1.Print list
2.Append to end
3.Insert at specific index
4.Remove form list
5.Sort list
6.Sort reverse list
7.Search in list
8.Exit program        
''')
    option = input('Choose option number:')
    if option == '1':
        print('Your list:', element_list)
    elif option == '2':
        element_list.append(input('Append element:'))
    elif option == '3':
        index = int(input('Choose index:'))
        element_list.insert(index, input('Insert element:'))
    elif option == '4':
        element_list.remove(input('Remove element:'))
    elif option == '5':
        element_list.sort()
    elif option == '6':
        element_list.sort(reverse=True)
    elif option == '7':
        query = input('Search element:')
        if query in element_list:
            print('Element found at index', element_list.index(query))
        else:
            print('Element not found')
    elif option == '8':
        print('Goodbye!')
        exit()

