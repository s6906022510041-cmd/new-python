def example_w_plus_mode():
    with open('example_w+.txt','w+')as file:
        file.write("gg.\n")
        file.write("gg.\n")
        file.seek(0)

        content = file.read()
        print("HSHSH")
        print(content)
example_w_plus_mode()
