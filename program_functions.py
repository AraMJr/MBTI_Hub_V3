
import UI


def return_to_root(error_message=None, status=bool(False)):
    run_again = None
    if error_message is not None:
        print('\nError: {0} \nRerunning function... '.format(error_message))
    if status:
        r_input = input("\nRun again? y/n: ").lower()
        if r_input == 'y':
            run_again = bool(True)
        elif r_input == 'n':
            run_again = bool(False)
            t_input = input("\nReturn to root? y/n: ").lower()
            if t_input == 'n':
                run_again = terminate_program()
            elif t_input == 'y':
                run_again = bool(True)
            else:
                run_again = return_to_root("Invalid input", status)
        else:
            return_to_root("Invalid input", bool(True))
    else:
        run_again = bool(True)
    return run_again


def terminate_program(short=bool(False)):
    if short:
        print("\nTerminating program...\nProgram terminated. Goodbye.")
    else:
        valid = input("\nTerminating program... Are you sure? y/n: ")
        if valid == 'y':
            print("Program terminated. Goodbye.")
            exit(0)
        elif valid == 'n':
            UI.ui()
        else:
            run_again = return_to_root("Invalid input", short)
            return run_again


