with open('input.txt', 'r') as f:
    tickets = [ticket.strip() for ticket in f.readlines()]

print(tickets)


def decode_ticket(ticket):
    row = int(ticket[0:7].replace('F', '0').replace('B', '1'), 2)
    seat = int(ticket[7:].replace('L', '0').replace('R', '1'), 2)
    return row, seat


rows_seats = [decode_ticket(ticket) for ticket in tickets]
seat_ids = set([row * 8 + seat for row, seat in rows_seats])

print(f'max seat: {max(seat_ids)}')

all_seat_ids = set(range(min(seat_ids), max(seat_ids)))

print(f'missing seat: {all_seat_ids - seat_ids}')
