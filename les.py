def les(size):
    step=""
    for i in range(size):
        for j in range(i):
            step += str(j)
        print(step)
        step = ''
les(5)