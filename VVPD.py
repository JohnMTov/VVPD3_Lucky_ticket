import random


def lucky(ticket):
    if (int(str(ticket)[0]) + int(str(ticket)[2]) + int(str(ticket)[4]) ==
            int(str(ticket)[1]) + int(str(ticket)[3]) + int(str(ticket)[5])):
        return 'Счастливый'
    else:
        return 'Несчастливый'


def nul(ticket):
    if ticket % 10 == 0 or ticket % 100 < 10 or ticket % 1000 < 100 or ticket % 10000 < 1000:
        return 1
    else:
        return 2

#ticket = input()
ticket = random.randint(100000, 999999)
while nul(ticket) == 1:
    ticket = random.randint(100000, 999999)
print('T = ', ticket)

print(lucky(ticket))
ticketv = ticket + 1
ticketn = ticket - 1
while lucky(ticketv) != 'Счастливый' or nul(ticketv) != 2:
    ticketv += 1
else:
    print(ticketv)

while lucky(ticketn) != 'Счастливый' or nul(ticketn) != 2:
    ticketn -= 1
else:
    print(ticketn)
