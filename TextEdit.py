if __name__ == '__main__':
    N = int(input())
    stack = []
    text = ''
    for i in range(N):
        l = list(input().split())
        query = int(l[0])
        if query == 1:
            stack.append(len(l[1]))
            text += l[1]
        if query == 2:
            length = int(l[1])
            stack.append(text[len(text) - length:])
            text = text[:len(text) - length]
        if query == 3:
            print(text[int(l[1]) - 1])
        if query == 4:
            item = stack.pop()
            if type(item) is int:
                text = text[:len(text) - item]
            else:
                text += item