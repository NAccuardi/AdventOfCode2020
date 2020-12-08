with open('input.txt') as f:
    responses = f.read().strip().split('\n\n')

print(responses)

print(sum(len(set.union(*map(set, x.split('\n')))) for x in responses))
print(sum(len(set.intersection(*map(set, x.split('\n')))) for x in responses))