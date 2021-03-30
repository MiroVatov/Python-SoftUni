
class Stack:

    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    # peek()method will show us the top value in the Stack

    def peek(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        new_data = ', '.join(str(s) for s in self.data[::-1])
        return f"[{str(new_data)}]"


st = Stack()
data_to_push = 'carrot', 'apple'
st.push(data_to_push)
print(st.peek())
print(st.is_empty())
print(st)