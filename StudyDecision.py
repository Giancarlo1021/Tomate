import FocusTimer


def continueOr(study, short_break, long_break):
    choice = (input('Would you like to continue focusing? (y/n)\n'))
    while True:
        print(choice)
        if choice == 'y':
            print('“First say to yourself what you would be; and then do what you have to do.”')
            return FocusTimer.timer(study, short_break, long_break)
        elif choice == 'n':
            print('"You have power over your mind — not outside events. Realize this, and you will find strength."')
            break
        else:
            choice = input('Please enter y/n')
