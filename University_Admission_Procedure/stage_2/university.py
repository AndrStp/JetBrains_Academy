marks = [int(input()) for _ in range(3)]
mean = sum(marks) / len(marks)

print(mean)

if mean < 60.0:
    print('We regret to inform you that we will not be able to offer you admission.')
else:
    print('Congratulations, you are accepted!')
