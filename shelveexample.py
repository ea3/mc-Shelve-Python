import shelve

with shelve.open('ShelfTest') as fruit:
    fruit['orange'] = "a sweet, orange, citrus fruit"
    fruit['apple'] = "good for makign cider"
    fruit['lemon'] = "a sour fruit"
    fruit['grape'] = "a small sweet fruit"
    fruit['lime'] = "a sour green citrus fruit"

    print(fruit["lemon"])
    print(fruit["grape"])
print(fruit)



