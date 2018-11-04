#!/usr/bin/env python3

def string_matrix(_a):
    mat = ""
    for i in range(len(_a)):
        s = ""
        for j in range(len(_a[i])):
            s = s + str(_a[i][j]) + " "
        mat = mat + (s.strip()) + "\n"
    return mat

def transpose(_a):
    for i in range(len(_a)):
        for j in range(i, len(_a[i])):
            temp = _a[j][i]
            _a[j][i] = _a[i][j]
            _a[i][j] = temp

def main():
    try:
        _f = open("./transpose.txt", "w+")
        _g = open("./matrices.txt", "r+")
        for line in _g:
            if line.startswith("-"):
                flag = True
                _n = int(line[1:])
                _a = []
                _f.write(str(_n)+'\n')
                continue
            if flag:
                _row = list(map(int, line.split(' ')))
                assert(len(_row) == _n), "Invalid Input\n Must enter matrix in a formatted way."
                _a.append(_row)
                if len(_a) == _n:
                    transpose(_a)
                    flag = False
                    _f.write(string_matrix(_a))
            else:
                _f.write('\n')
    except AssertionError as e:
        print(e)
        exit(1)
if __name__ == '__main__':
    main()
