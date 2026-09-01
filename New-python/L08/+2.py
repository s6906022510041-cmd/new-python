def example_w_plus_mode():
    with open('example_a+.txt','a+')as file:
        file.seek(0)
        content = file.read()
        print('C :')
        print(content)

        file.write('A end.\n')

        file.seek(0)
        updated_contens = file
        print('\nupdated_contens :')
        print(updated_contens)