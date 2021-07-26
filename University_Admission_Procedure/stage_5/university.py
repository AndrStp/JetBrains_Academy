class University:
    def __init__(self):
        self.departments = sorted(['Biotech', 'Chemistry', 'Engineering', 'Mathematics', 'Physics'])
        self.dep_exam = {
            'Biotech': 2,
            'Chemistry': 2,
            'Engineering': 4,
            'Mathematics': 3,
            'Physics': 1}
        self.places = None
        self.ROUNDS = 3
        self.admitted = {}

    @staticmethod
    def read_applicants() -> list:
        """Returns the list of all applicants with their gpa and priorities"""
        with open('applicants.txt', 'r', encoding='utf-8') as f:
            data = f.read().split('\n')
            applicants = []
            for row in data:
                row_splt = row.split()
                name = [row_splt[0] + ' ' + row_splt[1]]
                exams = [float(x) for x in row_splt[2:6]]
                priorities = row_splt[6:]
                applicants.append(name + exams + priorities)
        return applicants

    def sort_by_priority(self, applicants, priority, department) -> list:
        """Return the list of applicants sorted by the priority, gpa, full name"""
        dep_applicants = [applt for applt in applicants if applt[priority] == department]
        dep_exam = self.dep_exam[department]
        sorted_dep_applicants = sorted(dep_applicants, key=lambda x: (-x[dep_exam], x[0]))
        return sorted_dep_applicants

    def fill_departments(self, applicants) -> None:
        """Return the list of departments with filled students"""
        accepted = []
        for i in range(self.ROUNDS):
            for department, dep_name in enumerate(self.departments):
                self.admitted.setdefault(dep_name, [])
                free_places = self.places - len(self.admitted[dep_name])
                dep_applicants = self.sort_by_priority(applicants, i + 5, dep_name)[:free_places]

                # remove unnecessary info
                dep_applicants_processed = [[x[0]] + [x[self.dep_exam[dep_name]]] for x in dep_applicants]

                self.admitted[dep_name].extend(dep_applicants_processed)
                accepted.extend([appl[0] for appl in dep_applicants])
                # sort admitted students
                self.admitted[dep_name] = sorted(self.admitted[dep_name], key=lambda x: (-x[1], x[0]))
            applicants = [appl for appl in applicants if appl[0] not in accepted]

    def display_admitted(self) -> None:
        """Displays the admitted students to the department of their choice (priority_1)"""
        for department in self.admitted.keys():
            print(department)
            for student in self.admitted[department]:
                print(student[0], student[1])
            print()

    def admission(self) -> None:
        """Runs admission process"""
        self.places = int(input())
        applicants = self.read_applicants()
        self.fill_departments(applicants)
        self.display_admitted()


if __name__ == '__main__':
    uni = University()
    uni.admission()
