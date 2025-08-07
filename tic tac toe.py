def print_board(b):
    print("\n  1 2 3")
    for i, r in enumerate(b):
        print(f"{i+1} {'|'.join(r)}")
        if i < 2: print("  -+-+-")
    print()

def check_win(b, p):
    return any(all(c == p for c in r) for r in b) or \
           any(all(b[j][i] == p for j in range(3)) for i in range(3)) or \
           all(b[i][i] == p for i in range(3)) or \
           all(b[i][2-i] == p for i in range(3))

def check_draw(b):
    return all(c != ' ' for r in b for c in r)

def main():
    b = [[' ']*3 for _ in range(3)]
    p = 'X'
    print_board(b)
    while True:
        m = input(f"Player {p}, move (row col): ").split()
        if len(m) != 2 or not all(x.isdigit() for x in m): continue
        r, c = int(m[0])-1, int(m[1])-1
        if r not in range(3) or c not in range(3) or b[r][c] != ' ': continue
        b[r][c] = p
        print_board(b)
        if check_win(b, p): print(f"{p} wins!"); break
        if check_draw(b): print("Draw!"); break
        p = 'O' if p == 'X' else 'X'

if __name__ == "__main__":
    main()
