def esprimo():
    numero = int(input('Ingrese su numero: '))
    contador =0
    for i in range(1, numero+1):
        print(str(numero)+'/'+str(i))
        if i==1 or i==numero:
            continue
        else:
             contador+=1
    if contador > 0 or numero== 1:
            False
            print('No es primo')
    else:
            True
            print('Es primo')
        
        
          
if __name__ == '__main__':
    esprimo()