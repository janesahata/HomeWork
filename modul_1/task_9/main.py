def _func_line(size):
    return "#"*size

def _func_special(size):
    space_line = "_" * (size - 4)
    return "##" + space_line + "##"

def _func_middle_line(size):
    return _func_line(size-1) + "_"

def _func_left(size):
    space_line = "_"*size
    return "##" + space_line

def _func_right(size):
    space_line = "_"*size
    return space_line + "##"

def _func_char_a():
    "########"
    "##____##"
    "########"
    "##____##"
    line_one = _func_line(8)
    space_line = _func_special(8)

    print(line_one)
    print(space_line)
    print(line_one)
    print(space_line)
    return

def _func_char_b():
    "#######"
    "##_____##"
    "######_"
    "##_____##"
    "#######"
    line_one = _func_line(7)
    space_line = _func_special(8)
    middle_line = _func_middle_line(7)

    print(line_one)
    print(space_line)
    print(middle_line)
    print(space_line)
    print(line_one)
    return

def _func_char_s():
    "########"
    "##_____"
    "#######"
    "_____##"
    "#######"

    line_one = _func_line(8)
    space_line = _func_special(5)
    left_line = _func_left(5)
    right_line = _func_right(5)


    print(line_one)
    print(left_line)
    print(line_one)
    print(right_line)
    print(line_one)
    return


_char_dict = {
    'a': _func_char_a,
    'b': _func_char_b,
    's': _func_char_s
}

value = "abs"

for char in value:
    res = _char_dict[char]
    print(res())
