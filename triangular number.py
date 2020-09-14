def triangular_number(num):
    i = 1
    trig_num = 0
    while trig_num < num:
        trig_num += i
        i += 1
    return trig_num
