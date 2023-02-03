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
    min_len = min(map(len, args))
    res = []
    for index in range(min_len):
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
    res = []
    if len(iterables) == 1:
        """ Тут можливо етеруватись по кожному елементу без другого for? Лише з одним for."""
        for i in iterables:
            for i2 in i:
                res.append(func(i2))
        return res
    else:
        range_list = []
        for i in iterables:
            range_list.append(list(i))
        res = func(range_list)
    return res

print('\n', 'Task with map: ', '\n')
print(list(map(int, '1234567890')) == my_map(int, '1234567890'))
print(list(map(min, range(10), range(20, 30), range(25, 15, -1))) == my_map(min, range(10), range(20, 30), range(25, 15, -1)))
# =========== filter =============================================================================

def my_filter(func, *iterable):
    res = []
    if func is None:
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

def my_enumerate(iterables, start=0):
    e_set = set()
    res = []
    for i in iterables:
        if i not in e_set:
            e_set.add(i)
            res.append((start, i))
            start += 1
    return res

print('\n', 'Task with enumerate: ', '\n')
print(list(enumerate('1234567890', 1)) == my_enumerate('1234567890', 1))

# =========== Range =======================================================================

def my_range(start, stop=None, step=None):
    """
     Не зрозумів як краще порівнювати Int та NoneType у цьому випадку ------------
    """
    res = []
    if step is None and stop is not None and start > stop:
        return res
    elif start >= 0 and stop is None and step is None:
        values = -1
        while values < start - 1:
            values += 1
            res.append(values)
        return res

    elif step is None and start is not None and stop is not None and start < stop:
        values = start
        res.append(values)
        while values < stop - 1:
            values += 1
            res.append(values)
        return res
    elif stop is not None and start < stop and step is not None and step > 0:
        values = start
        res.append(values)
        while values < stop - 1:
            values += step
            res.append(values)
        return res
    elif stop is not None and start > stop and step is not None and step > 0:
        return res
    elif stop is not None and start > stop and step is not None and step < 0:
        values = start
        res.append(values)
        while values > stop + 1:
            values += step
            res.append(values)
        return res

print('\n', 'Task with range: ', '\n')
print(list(range(10)) == my_range(10))
print(list(range(10, 20)) == my_range(10, 20))
print(list(range(10, 20, 3)) == my_range(10, 20, 3))
print(list(range(20, 10, 3)) == my_range(20, 10, 3))
print(list(range(20, 10, -3)) == my_range(20, 10, -3))
print(list(range(20, 10)) == my_range(20, 10))