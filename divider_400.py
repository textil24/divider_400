def divider_400():

    list = ['Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.', 
            'Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together.', 
            "Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance.", 
            'Python supports modules and packages, which encourages program modularity and code reuse.', 
            'The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed.', 'Often, programmers fall in love with Python because of the increased productivity it provides.', 
            'Since there is no compilation step, the edit-test-debug cycle is incredibly fast.', 'Debugging Python programs is easy: a bug or bad input will never cause a segmentation fault.', 'Instead, when the interpreter discovers an error, it raises an exception.', "When the program doesn't catch the exception, the interpreter prints a stack trace.", 
            'A source level debugger allows inspection of local and global variables, evaluation of arbitrary expressions, setting breakpoints, stepping through the code a line at a time, and so on.', "The debugger is written in Python itself, testifying to Python's introspective power.", 
            'On the other hand, often the quickest way to debug a program is to add a few print statements to the source: the fast edit-test-debug cycle makes this simple approach very effective.'
            ]

    new_list_1 = []
    new_list_2 = []
    new_list_3 = []
    new_list_4 = []

    count = 0
    for item in list:
        count += len(item)

        if count <= 400:
            new_list_1.append(item)
        elif count <= 800:
            new_list_2.append(item)
        elif count <= 1200:
            new_list_3.append(item)
        elif count <= 1600:
            new_list_4.append(item)

    
    main_list = []

    res1 = ' '.join(new_list_1)
    res2 = ' '.join(new_list_2)
    res3 = ' '.join(new_list_3)
    res4 = ' '.join(new_list_4)
    
    res_list = [res1, res2, res3, res4]

    for item in res_list:
        main_list.append(item)

    return [x for x in main_list if x.strip()]

result_text = divider_400()
for item in result_text:
    print(len(item))