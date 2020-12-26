module_variable = "I am a module variable."

def my_func(argument_variable):
    local_variable = "I am a local variable."

    print(module_variable, "... and I can be accessed inside a function.")
    print(argument_variable, "... and I can be passed to a function.")
    print(local_variable, "... and I can ONLY accessed inside a function.")

my_func(argument_variable="I am a argument variable.")