# =========== my_all ================================================================================

def my_all(iterable):
   for element in iterable:
       if not element:
           return False
   return True
print(' Task with all:', '\n')
print(all([]) == my_all([]))
print(all([True, False]) == my_all([True, False]))
print(all([True, True]) == my_all([True, True]))
print(all([False, False]) == my_all([False, False]))

# =========== any ================================================================================

def my_any(iterable):
   for element in iterable:
      if element:
           return True
   return False
print('\n', 'Task with any: ', '\n')
print(any([]) == my_any([]))
print(any([True, False]) == my_any([True, False]))
print(any([True, True]) == my_any([True, True]))
print(any([False, False]) == my_any([False, False]))

# =========== zip ================================================================================

def my_zip(*args):
    min_el = args[0]
    for i in args:
        if i == []:
            no_args = []
            return no_args
        elif int(len(i)) < int(len(min_el)):
            min_el = i
    res = []
    for index in range(len(min_el)):
        tmp = []
        for coll in args:
            tmp.append(coll[index])
            continue
        res.append(tuple(tmp))
        continue
    k = list(res)
    return k
print('\n', 'Task with zip: ', '\n')
print(list(zip(range(10), range(15), range(8))) == my_zip(range(10), range(15), range(8)))
print(list(zip(range(10), range(15), [])) == my_zip(range(10), range(15), []))
print(list(zip(range(10))) == my_zip(range(10)))

# =========== map ================================================================================

def my_map(func, *iterables):
    for i in iterables:
        res = []
        if i == str(i):
            r = list(i)
            for i2 in r:
                int_i2 = func(i2)
                res.append(int_i2)
            return res
        else:
            for r in iterables:
                min_el = iterables[0]
                if list(r) < list(min_el):
                    min_el = r
                continue
    L = list(min_el)
    return L
print('\n', 'Task with map: ', '\n')
print(list(map(int, '1234567890')) == my_map(int, '1234567890'))
print(list(map(min, range(10), range(20, 30), range(25, 15, -1))) == my_map(min, range(10), range(20, 30), range(25, 15, -1)))

# =========== filter =============================================================================

def my_filter(func, *iterable):
    res = []
    if func == None:
        for i in iterable:
            for i2 in i:
                if not i2:
                    continue
                res.append(i2)
                continue
        return list(res)
    else:
        for i in iterable:
            for i2 in list(i):
                if func(i2) == True:
                    res.append(i2)
        return list(res)
print('\n', 'Task with filter: ', '\n')
print(list(filter(None, [0, 1, '', 2, 3, [], 5, {}, None, 6, False])) == my_filter(None, [0, 1, '', 2, 3, [], 5, {}, None, 6, False]))
print(list(filter(lambda a: a % 2 == 0, range(10+1))) == my_filter(lambda a: a % 2 == 0, range(10+1)))

# =========== sum  =============================================================================

def my_sum(*args):
    k = 0
    l_0 = list(args[0])
    for i in l_0:
        if i == l_0:
            k = i
        else:
            k = k + i
        continue
    return k
print('\n', 'Task with sum: ', '\n')
print(sum(range(10)) == my_sum(range(10)))
print(sum([]) == my_sum([]))

# =========== enumerate =======================================================================

def my_enumerate(iterables, *args):
    res = []
    res.append((*args, iterables[0]))
    i = args
    for a in iterables:
        if a == iterables[0]:
            continue
        else:
            if i == args:
                i = args[0] + (1,)[0]
                res.append((i, a))
            else:
                i = i + 1
                res.append((i, a))
                continue
    return res
print('\n', 'Task with enumerate: ', '\n')
print(list(enumerate('1234567890', 1)) == my_enumerate('1234567890', 1))

# =========== Range =======================================================================

def my_range(*args):
    res = []
    if len(args) == 1 and res == []:
        args_values = []
        args_values.append(*args)
        res = [0]
        values = 0
        while values < args_values[0] - 1:
            values += 1
            res.append(values)
            continue
        return res
    elif len(args) == 2:
        unpac1, unpac2 = args
        values = unpac1
        res.append(values)
        if unpac1 < unpac2:
            while values < unpac2 - 1:
                values += 1
                res.append(values)
                continue
            return res
        else:
            res = []
            return res
    elif len(args) == 3 and args[2] > 0 and args[0] > args[1]:
        res = []
        return res
    elif len(args) == 3 and args[2] < 0:
        unpac1, unpac2, unpac3 = args
        values = unpac1
        res.append(values)
        if unpac1 > unpac2:
            while values > unpac2 + 1:
                values += unpac3
                res.append(values)
                continue
            return res
    elif len(args) == 3 and args[2] > 0:
        unpac1, unpac2, unpac3 = args
        values = unpac1
        res.append(values)
        if unpac1 < unpac2:
            while values < unpac2 - 1:
                values += unpac3
                res.append(values)
                continue
            return res
print('\n', 'Task with range: ', '\n')
print(list(range(10)) == my_range(10))
print(list(range(10, 20)) == my_range(10, 20))
print(list(range(10, 20, 3)) == my_range(10, 20, 3))
print(list(range(20, 10, 3)) == my_range(20, 10, 3))
print(list(range(20, 10, -3)) == my_range(20, 10, -3))
print(list(range(20, 10)) == my_range(20, 10))