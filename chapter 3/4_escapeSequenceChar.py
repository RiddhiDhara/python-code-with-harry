# one imp thing about print statement : 
# print statement has a end="" parameter which tells end the line with ""

# sequence of character after \ is called escape sequence characters

sen = "Riddhi is a good boy \nbut not a bad boy"
print(sen)

sen = "Riddhi is a good boy \tbut not a bad boy"
print(sen)

sen = "Riddhi is a good boy \\but not a bad boy"
print(sen)

sen = "Riddhi is a good boy \" 'but' not a bad boy"
print(sen)

# ====================list of escape characters

# Escape Sequence	Description
# \'	Single quote (')
# \"	Double quote (")
# \\	Backslash (\)
# \n	Newline (line break)
# \t	Tab (horizontal tab)
# \r	Carriage return
# \b	Backspace
# \f	Form feed
# \v	Vertical tab
# \ooo	Octal value (e.g., \101 for 'A')
# \xhh	Hexadecimal value (e.g., \x41 for 'A')
# \N{name}	Unicode character by name (e.g., \N{COPYRIGHT SIGN} → ©)
# \uXXXX	Unicode character with 16-bit hex (e.g., \u03A9 → Ω)
# \UXXXXXXXX	Unicode character with 32-bit hex (e.g., \U0001F600 → 😀)

