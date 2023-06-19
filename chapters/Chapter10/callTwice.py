def callTwice(func):
    func()
    func()


def sayHello():
    print("hi")


def sayGoodbye():
    print("bye")


callTwice(sayHello)
callTwice(sayGoodbye)
