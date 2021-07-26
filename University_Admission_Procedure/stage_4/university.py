class University:
    def __init__(self):
        self.departments = sorted(['Biotech', 'Chemistry', 'Engineering', 'Mathematics', 'Physics'])
        self.places = None
        self.ROUNDS = 3
        self.admitted = {}

    def read_applicants(self) -> list:
        """Returns the list of all applicants with their gpa and priorities"""
        with open('applicant_list.txt', 'r', encoding='utf-8') as f:
            data = f.read().split('\n')
            applicants = []
            for row in data:
                f_name, s_name, gpa, priority_1, priority_2, priority_3 = row.split()
                name = ' '.join([f_name, s_name])
                gpa = float(gpa)
                applicants.append([name, gpa, priority_1, priority_2, priority_3])
        return applicants

    def sort_by_priority(self, applicants, priority, department) -> list:
        """Return the list of applicants sorted by the priority, gpa, full name"""
        dep_applicants = [applt for applt in applicants if applt[priority] == department]
        sorted_dep_applicants = sorted(dep_applicants, key=lambda x: (-x[1], x[0]))
        return sorted_dep_applicants

    def fill_departments(self, applicants) -> None:
        """Return the list of departments with filled students"""
        accepted = []
        for i in range(self.ROUNDS):
            for department, dep_name in enumerate(self.departments):
                self.admitted.setdefault(dep_name, [])
                free_places = self.places - len(self.admitted[dep_name])
                dep_applicants = self.sort_by_priority(applicants, i + 2, dep_name)[:free_places]
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

    def admission(self) -> None:
        """Runs admission process"""
        self.places = int(input())
        applicants = self.read_applicants()
        self.fill_departments(applicants)
        self.display_admitted()

if __name__ == '__main__':
    uni = University()
    uni.admission()
