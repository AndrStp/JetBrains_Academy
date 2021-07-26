class University:
    def __init__(self):
        self.departments = {
            'Biotech': [2, 1],
            'Chemistry': [2],
            'Engineering': [3, 4],
            'Mathematics': [3],
            'Physics': [1, 3]}
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
                exams = [float(x) for x in row_splt[2:7]]
                priorities = row_splt[7:]
                applicants.append(name + exams + priorities)
        return applicants

    @staticmethod
    def mean(lst) -> float:
        return sum(lst) / len(lst)

    def sort_by_priority(self, applicants: list, priority: int, dept: str) -> list:
        """Return the list of applicants sorted by the priority, gpa, full name"""
        dep_appls = [applt for applt in applicants if applt[priority] == dept]
        dep_appls_exams = [[applt[0]] + [max(self.mean([applt[exam] for exam in self.departments[dept]]), applt[5])] for applt in dep_appls]
        sorted_dep_appls = sorted(dep_appls_exams, key=lambda x: (-x[1], x[0]))
        return sorted_dep_appls

    def fill_departments(self, applicants: list) -> None:
        """Return the list of departments with filled students"""
        accepted = []
        for i in range(self.ROUNDS):
            for dep_name in self.departments.keys():
                self.admitted.setdefault(dep_name, [])
                free_places = self.places - len(self.admitted[dep_name])
                dep_applicants = self.sort_by_priority(applicants, i + 6, dep_name)[:free_places]
                self.admitted[dep_name].extend(dep_applicants)
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

    def save_admissions(self):
        """Save the students admitted to the departments to the separate files
        named after the department name"""
        for department in self.admitted.keys():
            with open(f'{department}.txt', 'w', encoding='utf-8') as dep:
                for applicant in self.admitted[department]:
                    applicant[1] = str(applicant[1])
                    dep.write(' '.join(applicant) + '\n')

    def admission(self) -> None:
        """Runs admission process"""
        self.places = int(input())
        applicants = self.read_applicants()
        self.fill_departments(applicants)
        self.display_admitted()
        self.save_admissions()


if __name__ == '__main__':
    uni = University()
    uni.admission()
