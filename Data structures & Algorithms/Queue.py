#Queue is FIFO

from collections import deque

bank = deque (["Anis" , "Karim", "Bijoy"])

print(bank)

bank.popleft()

print(bank)

