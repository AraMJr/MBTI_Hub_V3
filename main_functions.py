
import program_functions
import MBTI
import UI


def function_1(input_num):
    # TODO implement guide
    print("\n Work in progress. Patience is a virtue. ")


def function_2():
    if not MBTI.user_type.is_empty():
        print("\nCurrent user MBTI type set to", MBTI.user_type)
    else:
        print("User MBTI type is not currently set.")
    inputted_mbti = input("Enter user MBTI type or enter {0} to quit: ".format(UI.quit)).upper()
    if inputted_mbti.lower() == UI.quit:
        print("Returning to root...")
        UI.ui()
    else:
        print("Checking... ")
        valid = MBTI.check_validity(inputted_mbti)
        if valid:
            print("Input valid. Setting user MBTI...")
            MBTI.user_type = MBTI.mbti(inputted_mbti[0], inputted_mbti[1], inputted_mbti[2], inputted_mbti[3])
            print("User MBTI set to", MBTI.user_type)
        else:
            run_again = program_functions.return_to_root("Invalid input", True)
            if run_again:
                function_2()


def function_3():
    pass


def function_4():
    pass


def function_5(inputted_type):
    version, perceiving, judging, orientation = inputted_type.get_functions()
    print("\n{0}\t{1}\n{2}\t{3}\n{4}\t{5}\n{6}\t{7}".format(
        inputted_type.version, version,
        inputted_type.perceiving, perceiving,
        inputted_type.judging, judging,
        inputted_type.orientation, orientation))
    function_stack = inputted_type.get_cognitive_functions()
    function_names = inputted_type.get_cognitive_names("primary")
    shadow_stack = inputted_type.get_shadow()
    shadow_names = inputted_type.get_cognitive_names("shadow")
    if function_stack is not bool(False) and shadow_stack is not bool(False):
        print("\n{0} Function Stack\n".format(inputted_type))
        print("Primary\t\t{0}\t\t\t{1}\nAlternative\t\t{2}\t\t{3}"
              "\nTertiary\t{4}\t\t\t{5}\nInferior\t\t{6}\t\t{7}".format(
                function_stack[0], function_names[0], function_stack[1], function_names[1],
                function_stack[2], function_names[2], function_stack[3], function_names[3]))
        print("\n{0} Shadow Stack\n".format(inputted_type))
        print("Shadow\t\t{0}\t\t\t{1}\nSecondary\t\t{2}\t\t{3}"
              "\nPolar\t\t{4}\t\t\t{5}\nDemon\t\t\t{6}\t\t{7}".format(
                shadow_stack[0], shadow_names[0], shadow_stack[1], shadow_names[1],
                shadow_stack[2], shadow_names[2], shadow_stack[3], shadow_names[3]))


