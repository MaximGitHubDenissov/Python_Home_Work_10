import operations as oper

def parsing(text):
    my_list = []
    digits = ''
    for elm in text:
        if elm.isdigit():
            digits+=elm
        else:
            my_list.append(digits)
            my_list.append(elm)
            digits =''
    my_list.append(digits)
    return my_list

def calculation(lst):
    if '/' in lst:
        lst[lst.index('/')-1] = oper.devis_func(lst[lst.index('/')-1], lst[lst.index('/')+1])
        lst.pop(lst.index('/')+1)
        lst.pop(lst.index('/'))
    if '*' in lst:
        lst[lst.index('*')-1] = oper.mult_func(lst[lst.index('*')-1], lst[lst.index('*')+1])
        lst.pop(lst.index('*')+1)
        lst.pop(lst.index('*'))

    if '+' in lst:
        lst[lst.index('+')-1] = oper.addition_func(lst[lst.index('+')-1], lst[lst.index('+')+1])
        lst.pop(lst.index('+')+1)
        lst.pop(lst.index('+'))
    if '-' in lst:
        lst[lst.index('-')-1] = oper.subtrac_func(lst[lst.index('-')-1], lst[lst.index('-')+1])
        lst.pop(lst.index('-')+1)
        lst.pop(lst.index('-'))
    return lst



