def main():
    num_applicants, num_places = int(input()), int(input())

    applicants = []
    for _ in range(num_applicants):
        f_name, s_name, gpa = input().split()
        name = ' '.join([f_name, s_name])
        gpa = float(gpa)
        applicants.append([name, gpa])

    sorted_applicants = sorted(applicants, key=lambda x: (-x[1], x[0]))

    print('Successful applicants:')
    for i in range(num_places):
        print(sorted_applicants[i][0])


main()
