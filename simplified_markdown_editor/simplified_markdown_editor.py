formatters = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'ordered-list', 'unordered-list', 'new-line']
special_commands = ['!help', '!done']

def print_help():
    print('Available formatters:', ' '.join(formatters))
    print('Special commands:', ' '.join(special_commands))

    while True:
        user_input = input('Choose a formatter: ')

        if user_input in formatters:
            # handle formatting
            pass
        elif user_input in special_commands:
            if user_input == '!help':
                print_help()
            elif user_input == '!done':
                # save and exit program
                break
        else:
            print('Unknown formatting type or command')


    def information(self):
        print("Available formatters: plain bold italic header link inline-code ordered-listunordered-list new-line \nSpecial commands!help !done")