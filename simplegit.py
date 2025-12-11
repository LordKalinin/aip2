def featurea(name):
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    third_name = input("Введите отчество: ")
    return name, surname, third_name
def featureb():
    age = input("Ваш возраст: ")
    if int(age) < 18:
        return False
    bio = input("Ваше описание: ")
    return bio
