



def gen_func():
    html = yield "http://projectsedu.com"
    #print(html)
    yield 2
    yield 3
    return "bobby"

if __name__ == "__main__":

    gen = gen_func()
    print(next(gen))
    url = next(gen)
    #print(url)
    print(next(gen))
    html = "bobby"
    gen.send(html) # send

