#local variable msut be defined in local scope before calling
def spam():
    print(eggs)
    eggs = 'spam'

eggs ='global'
spam()