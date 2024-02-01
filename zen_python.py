# The Zen of Python is a collection of 19 guiding principles for writing computer programs that influence the design of the Python programming language. These principles were written by software engineer Tim Peters and posted on the Python mailing list in 1999 1.

# Here are the 19 principles along with examples:

#     Beautiful is better than ugly. - Code should be easy to read and understand. For instance, use descriptive variable names instead of single letters.

# # Bad
# x = 5
# y = 6
# sum = x + y

# # Good
# first_number = 5
# second_number = 6
# total = first_number + second_number

#     Explicit is better than implicit. - Code should clearly express its intentions. For instance, use explicit return statements instead of relying on the default return value of None.

# # Bad
# def add(x, y):
#     return x + y

# # Good
# def add(x, y):
#     result = x + y
#     return result

#     Simple is better than complex. - Keep your code simple and avoid unnecessary complexity. For instance, use simple conditionals instead of nested ones.

# # Bad
# if user_is_authenticated and user_has_permission:
#     perform_action()

# # Good
# if not user_is_authenticated:
#     redirect_to_login()
# elif not user_has_permission:
#     show_error()
# else:
#     perform_action()

#     Complex is better than complicated. - Complex code is easier to understand than complicated code. For instance, use list comprehensions instead of loops where possible.

# # Bad
# squares = []
# for i in range(10):
#     squares.append(i ** 2)

# # Good
# squares = [i ** 2 for i in range(10)]

#     Flat is better than nested. - Avoid deep nesting of conditional statements. For instance, use continue and break statements to prevent unnecessary indentation.

# # Bad
# for i in range(10):
#     if i % 2 == 0:
#         print(i)

# # Good
# for i in range(10):
#     if i % 2 != 0:
#         continue
#     print(i)

#     Sparse is better than dense. - Use blank lines to separate sections of code and make it easier to read.

#     Readability counts. - Code is read more often than it is written, so prioritize making it easy to read.

#     Special cases aren't special enough to break the rules. - Don't introduce exceptions to the rules of the language just for your convenience.

#     Although practicality beats purity. - Sometimes it's okay to sacrifice pure principles for practical reasons.

#     Errors should never pass silently. - Always handle errors and exceptions properly.

# try:
#     risky_operation()
# except Exception as e:
#     print(f"An error occurred: {e}")

#     Unless explicitly silenced. - Unless you explicitly silence an exception, it should propagate up the call stack.

#     In the face of ambiguity, refuse the temptation to guess. - When faced with an unclear situation, ask for clarification instead of making assumptions.

#     There should be one-- and preferably only one --obvious way to do it. - This principle encourages consistency in the language's syntax and semantics.

#     Although that way may not be obvious at first unless you're Dutch. - The Zen of Python acknowledges that the best solution isn't always immediately apparent.

#     Now is better than never. - Prioritize shipping a working product over perfecting every detail.

#     Although never is often better than right now. - It's important to take time to plan and structure your code well.

#     If the implementation is hard to explain, it's a bad idea. - Code should be self-explanatory. If it's not, consider refactoring.

#     If the implementation is easy to explain, it may be a good idea. - Simplicity is key in coding.

#     Namespaces are one honking great idea -- let's do more of those! - This principle emphasizes the importance of encapsulation and modularity in code organization 245.

# These principles can be accessed directly from the Python interpreter by typing import this 2345.
