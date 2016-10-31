def format(t):
    a = (t // 600)
    b = (((t % 600) / 10) / 10)
    c = '0'
    if (t > 10):
        c = str(t)[(-2)]
    d = str(t)[(-1)]
    formatedTime = (((((str(a) + ':') + str(b)) + c) + '.') + d)
    return formatedTime

def stopwatch_format(t):
    """
    Convert tenths of seconds to formatted time
    """
    minute = t // 600
    second = t // 10 % 60
    tenth = t % 10
    if second < 10:
        second = '0' + str(second)
    return str(minute) + ':' + str(second) + '.' + str(tenth)


for i in range(6000):
    if stopwatch_format(i) != format(i):
        print i, stopwatch_format(i), format(i)

   #print stopwatch_format(i)