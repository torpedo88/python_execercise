my_str = input(str("Please Enter the message ? "))
l_str = len(my_str)
m = int (l_str / 2)

f_char = my_str[0].upper()
l_char = my_str[-1].upper()
m_char = my_str[m].upper()

even_char = my_str[::2].upper()
odd_char = my_str[1::2].upper()
rever_char = my_str[::-1].upper()

print(f"Your input", my_str)
print(f"First Charcter is", f_char)
print(f"Last Charcter is", l_char)
print(f"Middle Charcter is", m_char)
print(f"Even index Charcters are", even_char)
print(f"Odd index Charcters are", odd_char)
print(f"Reversed Charcters are", rever_char)


# test develop branch