

class ExampleException(Exception):
    pass

def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner

# @coroutine
def subgen():
    while True:
        try:
            message = yield
        except StopIteration:
            break
        except ExampleException:
            print("It's an example exception")
        else:
            print(".........", message)

    return "Returned from subgen"

@coroutine
def delegator(g):
    # while True:               #вручную, вместо yield from
    #     try:
    #         data = yield
    #         g.send(data)
    #     except StopIteration as s:
    #         # g.throw(s)
    #         pass
    #     except ExampleException as e:
    #         g.throw(e)
    result = yield from g          #если есть yield from, то инициализирующий декоратор у подгенератора убираем
    print(result)


sg = subgen()
g = delegator(sg)

g.send("VBAB")
g.send("VBABsv")
g.throw(ExampleException)
g.throw(StopIteration)


