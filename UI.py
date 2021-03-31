
import program_functions
import main_functions
import MBTI


quit = "q"


def ui():
    exempted_functions = {2}
    run = bool(True)
    while run:
        function_input = root()
        print('\nRunning function {0}... '.format(function_input))
        if function_input in submenu_switcher.keys():
            get_submenu(function_input)
        else:
            get_function(function_input)
        if function_input not in exempted_functions:
            run = program_functions.return_to_root(None, bool(True))
        else:
            print("\nReturning to root...")


def root():
    valid_inputs = function_switcher.keys()
    print('\n{0} \n {1} \n {2} \n {3} \n {4} \n {5} \n {6} '.format(
        "The following are a list of possible functions",
        "1. View Guide (Help)",
        "2. Enter user MBTI type",
        "3. Run distribution",
        "4. Run search",
        "5. Retrieve type information",
        "0. Terminate program"
    ))
    function_input = int(input("Enter number for desired function: "))
    if function_input not in valid_inputs:
        run_again = program_functions.return_to_root("Invalid input")
        if run_again:
            function_input = root()
    return function_input


def default():
    return program_functions.return_to_root


def get_function(function_number):
    return function_switcher.get(function_number, default)()


def get_submenu(submenu_number):
    return submenu_switcher.get(submenu_number, default())()


def submenu_1():
    input_num = int(input("\nEnter number for function you wish to learn about: "))
    main_functions.function_1(input_num)


def submenu_3():
    pass


def submenu_5():
    main_functions.function_5(MBTI.user_type)


def type_input_submenu():
    pass


function_switcher = {
    0: program_functions.terminate_program,
    1: main_functions.function_1,
    2: main_functions.function_2,
    3: main_functions.function_3,
    4: main_functions.function_4,
    5: main_functions.function_5
}


submenu_switcher = {
    0: type_input_submenu,
    1: submenu_1,
    3: submenu_3,
    5: submenu_5
}

