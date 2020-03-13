d = {
    str("Orange"): [6],
    str("Apple"): [0],
    str("Pear"): [32],
    str("Lemon"): [15]
}
b = {
    str("Orange"): [4],
    str("Apple"): [2],
    str("Pear"): [1.5],
    str("Lemon"): [3] 
}
print(d)
print(b)

value = sum(map(sum, d.values()))
print("Oбщая стоимость от первоначальной цены:",value)
value = sum(map(sum, b.values()))
print("Oбщая стоимость от второстепенной цены:",value)