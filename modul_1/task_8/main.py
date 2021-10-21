def _func_line(size):
    return "#"*size

def _func_special(size):
    space_line = "_"*size
    return "#" + space_line + "#"

def _func_midle_line(size):
    return _func_line(size-1) + "_"

def _func_char_b():
    "#######"
    "#_____#"
    "######_"
    "#_____#"
    "#######"
    line_one = _func_line(7)
    space_line = _func_special(5)
    midle_line =_func_midle_line(7)

    print(line_one)
    print(space_line)
    print(midle_line)
    print(space_line)
    print(line_one)
    return


_func_char_b()



