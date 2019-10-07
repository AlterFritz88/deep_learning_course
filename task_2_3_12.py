class Neuron:

    def __init__(self, w, f=lambda x: x):
        self.w = w
        self.activation_func = f

    def forward(self, x):
        self.mem = x
        return self.activation_func(sum([x*y for x, y in zip(x, self.w)]))


    def backlog(self):
        return self.mem


def Test():
    test_neuron = Neuron([2, 3, 4, 5, 6], lambda x: x * x)

    if (test_neuron.forward([1, 2, 3, 4, 5]) == 4900 and test_neuron.backlog() == [1, 2, 3, 4, 5]):
        print("Задание успешно выполнено!")
    else:
        print("Ошибка в решении!")


Test()