class Student:
    # Статические поля
    default_id = ''
    default_name = 'No name'
    default_DOB = ''
    default_address = ' No address'
    default_phone = 'No phone'
    default_faculty = 'No faculty'
    default_course = 'No course'
    default_group = 'No group'

    def __init__(self, id, name, dob, address, phone, faculty, course, group):
        self.id_student = id
        self.name_student = name
        self.dob_student = dob
        self.address_student = address
        self.phone_student = phone
        self.faculty_student = faculty
        self.course_student = course
        self.group_student = group
        # print('New object created!')

    def get_id(self):
        return self.id_student

    def get_name(self):
        return self.name_student

    def get_data(self):
        return self.dob_student

    def get_address(self):
        return self.address_student

    def get_phone(self):
        return self.phone_student

    def get_faculty(self):
        return self.faculty_student

    def get_course(self):
        return self.course_student

    def get_group(self):
        return self.group_student

    def student_age(self, curr_year=2021):
        return curr_year - self.get_data()


def info(item):
    print(f'Name: {Allthestudents[item].get_name()}')
    print(f'Phone {Allthestudents[item].get_phone()}')
    print(f'Age: {str(Allthestudents[item].student_age())} years')
    print(f'Student id: {Allthestudents[item].get_id()}')
    print('---------------')


Allthestudents = [Student('8s97svu', 'Vanlov I.I.', 1997, 'Saigon', '456321', 'TF', 5, 534),
                  Student('s4bt5tv', 'Andreev A.D', 1997, 'Saigon', '456321', 'TF', 5, 534),
                  Student('m8rx2jz', 'Nikitin M.D', 2000, 'Saigon', '456321', 'TF', 2, 234),
                  Student('w3jy4hd', 'Sergeev A.S.', 1999, 'Saigon', '456321', 'TF', 3, 334),
                  Student('et5d6hb', 'Pavlov A.P', 1997, 'Saigon', '456321', 'MF', 5, 544),
                  Student('tm7nj1r', 'Artimov B.B', 1999, 'Saigon', '456321', 'TF', 3, 334),
                  Student('u7psn6g', 'Denisov I.T.', 1997, 'Saigon', '456321', 'TF', 5, 534),
                  Student('qh25pj5', 'Atov D.A', 2000, 'Saigon', '456321', 'TF', 2, 234),
                  Student('vk957e4', 'Nastasieva N.C', 1999, 'Saigon', '456321', 'MF', 5, 544),
                  Student('r7seh4p', 'Natalieva I.O.', 1997, 'Saigon', '456321', 'TF', 5, 534),
                  Student('x4qb9d2', 'Vodilov G.A', 2000, 'Saigon', '456321', 'TF', 5, 534),
                  Student('s3wb4hq', 'Andrus A.D', 1999, 'Saigon', '456321', 'MF', 5, 544),
                  Student('t7zfe5n', 'Nikaton M.D', 1997, 'Saigon', '456321', 'TF', 5, 534),
                  Student('a7hw7uq', 'Serge W.S.', 1997, 'Saigon', '456321', 'MF', 5, 544),
                  Student('k9xz4hc', 'Pravilov A.P', 2000, 'Saigon', '456321', 'MF', 3, 344),
                  Student('lhu79wx', 'Artinov B.B', 1999, 'Saigon', '456321', 'TF', 5, 534),
                  Student('3wbn4f5', 'Delisov F.T.', 1997, 'Saigon', '456321', 'MF', 5, 544),
                  Student('7vm978j', 'Artamonov R.A', 2000, 'Saigon', '456321', 'TF', 2, 234),
                  Student('fd6c9rc', 'Nastasieva N.C', 1999, 'Saigon', '456321', 'TF', 2, 234),
                  Student('ayy7y74', 'Nastalieva I.O.', 1999, 'Saigon', '456321', 'TF', 2, 234),
                  Student('r6qd5e9', 'Vavilov F.A', 2000, 'Saigon', '456321', 'TF', 5, 534)]


def search_group_student(g):
    for i in range(len(Allthestudents)):
        if Allthestudents[i].get_group() == g:
            info(i)


def search_faculty_student(f):
    for i in range(len(Allthestudents)):
        if Allthestudents[i].get_faculty() == f:
            info(i)


f_s = (input('Select faculty TF or MF \n'))
search_faculty_student(f_s)
g_s = (int(input('Select group from: 234, 334, 534, 344, 544  \n')))
search_group_student(g_s)