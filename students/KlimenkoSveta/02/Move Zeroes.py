def floyd(f, x0):
    # Основная часть алгоритма: находим повторение x_i = x_2i.
    # Заяц движется вдвое быстрее черепахи
    # и расстояние между ними увеличивается на единицу от шага к шагу.
    # Однажды они окажутся внутри цикла, и тогда расстояние между ними
    # будет делиться на λ.
    tortoise = f(x0) # f(x0) является элементом, следующим за x0.
    hare = f(f(x0))
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(f(hare))
  
    # В этот момент позиция черепахи ν, 
    # которая равна расстоянию между черепахой и зайцем,
    # делится на период λ. Таким образом, заяц, двигаясь 
    # по кольцу на одну позицию за один раз, 
    # и черепаха, опять начавшая движение со стартовой точки x0 и
    # приближающаяся к кольцу, встретятся в начале кольца
    # Находим позицию μ встречи.    
    mu = 0
    tortoise = x0
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(hare)   # Заяц и черепаха двигаются с одинаковой скоростью
        mu += 1
 
    # Находим длину кратчайшего цикла, начинающегося с позиции x_μ
    # Заяц движется на одну позицию вперёд, 
    # в то время как черепаха стоит на месте.
    lam = 1
    hare = f(tortoise)
    while tortoise != hare:
        hare = f(hare)
        lam += 1
 
    return lam, mu