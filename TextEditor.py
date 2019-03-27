class AppendOperation:
    def __init__(self, txt, text : list):
        self.txt = txt
        self.text = text

    def evaluate(self):
        # for ch in self.txt:
        #     self.text.append(ch)
        # self.text + list(self.txt)
        return self.text + list(self.txt)

    def undo(self):
        return self.text[:len(self.text) - len(self.txt)]


class RemoveOperation:
    def __init__(self, length, text : list):
        self.length = length
        self.text = text
        self.backUp = []

    def evaluate(self):
        textlen = len(self.text)
        self.backUp = self.text[textlen - self.length:]
        return self.text[:textlen - self.length]

    def undo(self):
        return self.text + self.backUp


class PrintOperation:
    def __init__(self, index, text):
        self.index = index
        self.text = text

    def evaluate(self):
        print(self.text[self.index - 1])

    def undo(self):
        return self.text


if __name__ == '__main__':
    N = input()
    info = []
    stack = []
    for i in range(int(N)):
        inputstring  = input()
        tokens = inputstring.split(" ")
        query = tokens[0]
        if query == "1":
            op = AppendOperation(tokens[1], info)
            stack.append(op)
            info = op.evaluate()
        elif query == "2":
            op = RemoveOperation(int(tokens[1]),info)
            stack.append(op)
            info = op.evaluate()
        elif query == "3":
            op = PrintOperation(int(tokens[1]),info)
            op.evaluate()
        elif query == "4":
            op = stack.pop()
            info = op.undo()
