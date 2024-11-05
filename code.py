class Person:
    # Konstruktor untuk inisialisasi atribut
    def __init__(self, name, umur):
        self.__name = name        # Atribut private
        self.__umur = umur        # Atribut private

    # Getter untuk nama
    def get_name(self):
        return self.__name

    # Setter untuk nama
    def set_name(self, name):
        self.__name = name

    # Getter untuk umur
    def get_umur(self):
        return self.__umur

    # Setter untuk umur
    def set_umur(self, umur):
        if umur > 0:
            self.__umur = umur
        else:
            print("Umur harus positif!")

    def display_info(self):
        print(f"Nama: {self.get_name()}, Umur: {self.get_umur()}")

# Kelas anak (subclass)
class Student(Person):
    def __init__(self, name, umur, student_id):
        super().__init__(name, umur)  # Memanggil konstruktor kelas induk
        self.__student_id = student_id  # Atribut private

    # Getter untuk ID mahasiswa
    def get_student_id(self):
        return self.__student_id

    def display_info(self):
        super().display_info()  # Memanggil method dari kelas induk
        print(f"ID Mahasiswa: {self.get_student_id()}")

# Fungsi untuk membuat mahasiswa
def create_students():
    students = []
    
    # Menambahkan mahasiswa dengan ID unik
    students.append(Student("Salsabila", 20, "2362400"))
    students.append(Student("Rizky", 21, "2362500"))
    students.append(Student("zulkifli", 22, "2362600"))
    students.append(Student("sofia", 20, "2362700"))
    
    return students

# Membuat daftar mahasiswa
student_list = create_students()

# Menampilkan informasi semua mahasiswa
for student in student_list:
    student.display_info()