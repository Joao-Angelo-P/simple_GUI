def decolabel(func):
    sa = ''
    def modificar(self):
        nonlocal sa
        _str = func(self)
        
        p = 'parent'
       
        for i in _str.split('.'):
            
            if not i:
                sa += f'Tk({str.capitalize(p)}) > '

            if i and i != _str.split('.')[-1]:
                sa += str.capitalize(f'{i[1:]}(') + str.capitalize(f'{p})')+ ' > '
                
            if i == _str.split('.')[-1]:
                sa += str.capitalize(f'{i[1:]}')
                
        return sa
    return modificar
  
