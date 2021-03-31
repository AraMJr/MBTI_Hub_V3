
mbti_dictionary = {
    'I': "Introverted",
    'E': "Extroverted",
    'N': "Intuition",
    'S': "Sensing",
    'T': "Thinking",
    'F': "Feeling",
    'P': "Perceiving",
    'J': "Judging"
}

opposite_functions = {
    "Ni": "Se",
    "Si": "Ne",
    "Fe": "Ti",
    "Te": "Fi"
}


# check_validity checks if inputted mbti type is valid and will return a bool.
# Normally will assume character 'X' is valid unless inputted with a bool(False) as second argument
# where it will mark 'X's as invalid


def check_validity(input_mbti, x_val=bool(True)):
    valid_inputs = []
    for key in mbti_dictionary.keys():
        valid_inputs.append(key)
    counter = 0
    if len(input_mbti) != 4:
        return bool(False)
    while counter < 4:
        if x_val:
            if input_mbti[counter] is not valid_inputs[counter * 2] and \
                    input_mbti[counter] is not valid_inputs[(counter * 2) + 1] and \
                    input_mbti[counter] != "X":
                return bool(False)
        else:
            if input_mbti[counter] is not valid_inputs[counter * 2] and \
                    input_mbti[counter] is not valid_inputs[(counter * 2) + 1]:
                return bool(False)
        counter += 1
    return bool(True)

# get_opposite returns value or key of inputted function from opposite_functions.
# if a key is inputted, it will return the value. if a value is inputted it will return the key.


def get_opposite(function):
    try:
        return opposite_functions[function]
    except KeyError:
        for key, value in opposite_functions.items():
            if value == function:
                return key


class mbti:
    def __init__(self, version="X", perceiving="X", judging="X", orientation="X"):
        self.version = version
        self.perceiving = perceiving
        self.judging = judging
        self.orientation = orientation

    def __str__(self):
        return self.version + self.perceiving + self.judging + self.orientation

    def is_empty(self):
        if self.version == "X" and self.perceiving == "X" and self.judging == "X" and self.orientation == "X":
            return bool(True)

    def get_functions(self):
        if not self.is_empty():
            return mbti_dictionary[self.version], mbti_dictionary[self.perceiving], \
                   mbti_dictionary[self.judging], mbti_dictionary[self.orientation]

    def get_cognitive_functions(self):
        primary_function_list = []
        function_stack = ["X", "X", "X", "X"]
        if self.orientation == "J":
            function_list = opposite_functions.keys()
        elif self.orientation == "P":
            function_list = opposite_functions.values()
        else:
            return bool(False)
        for c_function in function_list:
            if self.perceiving in c_function or self.judging in c_function:
                primary_function_list.append(c_function)
        if self.version == "I":
            checker = "i"
        elif self.version == "E":
            checker = "e"
        else:
            return bool(False)
        for c_function in primary_function_list:
            if checker in c_function:
                function_stack[0] = c_function
                function_stack[3] = get_opposite(c_function)
                primary_function_list.remove(c_function)
                function_stack[1] = primary_function_list[0]
                function_stack[2] = get_opposite(function_stack[1])
        return function_stack

    def get_shadow(self):
        primary_stack = self.get_cognitive_functions()
        shadow_stack = []
        for function in primary_stack:
            function_list = list(function)
            function_list[1] = get_opposite(function)[1]
            shadow_stack.append("".join(function_list))
        return shadow_stack

    # get_cognitive_names will return the names of each function in the function stack by referencing mbti_dictionary.
    # it has an optional second argument, primary_or_shadow,
    # which will determine whether the function stack in question is the primary stack or the shadow stack

    def get_cognitive_names(self, primary_or_shadow="primary"):
        if primary_or_shadow == "primary":
            function_stack = self.get_cognitive_functions()
        elif primary_or_shadow == "shadow":
            function_stack = self.get_shadow()
        else:
            return bool(False)
        function_names = []
        for function in function_stack:
            word_1 = mbti_dictionary[function[1].upper()]
            word_2 = mbti_dictionary[function[0]]
            function_names.append(word_1 + " " + word_2)
        return function_names

    def get_polar(self):
        shadow_stack = self.get_shadow()
        shadow_names = self.get_cognitive_names()
        return shadow_stack[2], shadow_names[2]


user_type = mbti()  # defines user type as global to be used across program

