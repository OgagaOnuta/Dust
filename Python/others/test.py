import ctypes

lib = ctypes.CDLL("./mylib.so")
lib.hello()

el = ['hello', 'world']

lib.print_list(el)
