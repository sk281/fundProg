principal_amount = int(input('principal amount: '))
interest_rate = float(input('interest rate: '))
time = 2
frequency = int(input('frequency: '))

formulation = principal_amount * ((1 + (interest_rate/frequency) )**(time * frequency))
# ** expoente

print(formulation)


