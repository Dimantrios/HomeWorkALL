# ======================== Task 1 ========================

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
set_c = {7, 8, 9, 10, 11}

res = []
for item_a in set_a:
    res.append(item_a)
for item_b in set_b:
    res.append(item_b)
for item_c in set_c:
    res.append(item_c)
print('\n', '==== Set ====', '\n', 'Task 1', '\n', 'res =', set(res))

# ======================== Task 2 ========================

set_a_b = set_a - set_b
set_b_c = set_b - set_c
set_a_c = set_a - set_c

print('\n', 'Task 2', '\n', 'set_a_b =', set_a_b, '\n', 'set_b_c =', set_b_c, '\n', 'set_a_c =', set_a_c)

# ======================== Task 3 ========================

res_a_b = set_a.intersection(set_b)
res_b_c = set_b.intersection(set_c)
res_a_c = set_a.intersection(set_c)

print('\n', 'Task 3', '\n', 'res_a_b =', res_a_b, '\n', 'res_b_c =', res_b_c, '\n', 'res_a_c =', res_a_c)

# ======================== Task 4 ========================

set1 = {1, 2}

print('\n', 'Task 4', '\n', set1.isdisjoint(set_a))
print('', set1.isdisjoint(set_b))
print('', set1.isdisjoint(set_c))


# ======================== Task 5 ========================

res1 = set()
res2 = set()

for item_par in res:
   if item_par % 2 == 0:
       res1.add(item_par)
   else:
       res2.add(item_par)
print('\n', 'Task 5', '\n', 'res1 =', res1, '\n', 'res2 =', res2)

# ======================== Dict ==========================

dict_a = {
    'key_1': 'value_1',
    'key_2': 'value_2',
    'key_3': 'value_3',
    'key_4': 'value_4',
    'key_5': 'value_5'
}

dict_b = {
    'key_6': 'value_6',
    'key_7': 'value_7',
    'key_8': 'value_8',
    'key_9': 'value_9',
    'key_10': 'value_10'
}

dict_c = {
    'key_4': 'value_4',
    'key_5': 'value_5',
    'key_6': 'value_6',
    'key_7': 'value_7',
    'key_8': 'value_8'
}

# ======================== Task 1 ========================

res = {}
res.update(dict_a)
res.update(dict_b)

print('\n', '==== Dict ====', '\n', 'Task 1', '\n', 'res = ', res)


# ======================== Task 2 ========================

res = {}
keys_a = list(dict_a.keys())
values_b = list(dict_b.values())
res = dict(zip(keys_a, values_b))

print('\n', 'Task 2', '\n', 'res = ', res)


# ======================== Task 3 ========================

res = {}
keys_a = list(dict_a.keys())
values_b = list(dict_b.values())
res = dict(zip(values_b, keys_a))

print('\n', 'Task 3', '\n', 'res = ', res)

# ======================== Task 4 ========================

res = { 'key_1': 'value_1', 'key_2': 'value_2', 'key_3': 'value_3', 'key_4': 'value_4', 'key_5': 'value_5',
        'key_6': 'value_6' , 'key_7': 'value_7', 'key_8': 'value_8', 'key_9': 'value_9', 'key_10': 'value_10'}

k = list(res.keys())
v = list(res.values())
k1 = []
v1 = []

for key in k:
    if int(key[-1]) % 2 != 0:
        k1.append(key)
for values in v:
    if int(values[-1]) % 2 != 0:
        v1.append(values)
res = dict(zip(k1, v1))
print('\n', 'Task 4', '\n', 'res = ', res)

# ======================== Task 5 ========================

res = []

dub_keys_a = []
dub_keys_b = []

keys_a = list(dict_a.keys())
keys_b = list(dict_b.keys())
keys_c = list(dict_c.keys())

for keys_a_dub in keys_a:
    for keys_c_dub in keys_c:
        if keys_a_dub == keys_c_dub:
            dub_keys_a.append(keys_a_dub)

for keys_b_dub in keys_b:
    for keys_c_dub in keys_c:
        if keys_b_dub == keys_c_dub:
            dub_keys_b.append(keys_b_dub)

amount_keys_a = len(dub_keys_a)
amount_keys_b = len(dub_keys_b)

final_values = (amount_keys_a, amount_keys_b)
final_keys = ( 'dict_a', 'dict_b' )

res = dict(zip(final_keys, final_values))

print('\n', 'Task 5', '\n', 'res = ', res)
# ==========================================================
