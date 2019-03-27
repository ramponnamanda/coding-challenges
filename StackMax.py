
if __name__ == '__main__':
    N = input()
    stack = [[0,0]]
    for i in range(int(N)):
        inputstring  = input()
        tokens = inputstring.split(" ")
        query = tokens[0]
        if query == "1":
            item = int(tokens[1])
            maxval = max(item, stack[-1][1])
            stack.append([item, max(item, maxval)])
        elif query == "2":
            stack.pop()
        elif query == "3":
            print(stack[-1][1])