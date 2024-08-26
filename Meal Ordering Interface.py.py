#design da loja
print ('            ' 'Bem vindo à loja do Leon Santiago')
print ('')
print ('                ' 'Menu fresquinho de hoje!') 
print ('-' * 58)
print ('| Tamanho  |  Bife acebolado (BA)  |  Filé de frango  (FF) |')
print ('|    P     |       R$ 16.00        |       R$ 15.00        |')
print ('|    M     |       R$ 18.00        |       R$ 17.00        |')
print ('|    G     |       R$ 22.00        |       R$ 21.00        |')

#programa principal

receipt = 0 #acumulador
quantity = 0 #quantidade de marmitas compradas

#loop principal
while True:
   
   flavor = input('Qual o sabor desejado? (BA ou FF):').upper() #sabor

   while flavor != 'BA' and flavor != 'FF': #verificar sabor válido
      print ('Sabor inválido. Tente novamente.') 
      flavor = input('Qual o sabor desejado? (BA ou FF)').upper() #loop de sabor

   size = input('Qual o tamanho desejado? (P/M/G)').upper() #tamanho

   while size != 'P' and size != 'M' and size != 'G': #verificar tam válido
      print ('Tamanho inválido. Tente novamente.')    
      size = input('Qual o tamanho desejado? (P/M/G)').upper() #loop de tamanho


   #acumulador baseado em sabor e tamanho
   if flavor == 'BA' and size == 'P':
      receipt += 16 
  
   elif flavor == 'BA' and size == 'M':
      receipt += 18 
 
   elif flavor == 'BA' and size == 'G':
      receipt += 22

   elif flavor == 'FF' and size == 'P':
      receipt += 15

   elif flavor == 'FF' and size == 'M':
      receipt += 17

   elif flavor == 'FF' and size == 'G':
      receipt += 21

   quantity += 1 #acumulador de unidades de marmita

   cart = input ('Deseja pedir mais algo? (S/N)').upper() #carrinho de compras

   while cart != 'S' and cart != 'N': #loop de validez do carrinho de comprasba
      print ('Não entendi. Tente novamente.') 
      cart = input ('Deseja pedir mais algo? (S/N)').upper() #loop de carrinho

   if cart == 'N'.upper(): #saída do loop
      print (f'Você pediu por {quantity}(s) marmitas. O valor total a ser pago é de: R${receipt}')
      break
   
   print (f'Você pediu por {quantity}(s) marmitas. O valor total a ser pago é de: R${receipt}')