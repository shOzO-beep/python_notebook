try:
        def menu():
          while True:
            print("====МЕНЮ ВЫБОРА====\n"\
                "1.Добавить заметку\n" \
                "2.Прочитать заметки\n" \
                "3.Удалить заметки\n" \
                "4.Выйти")
            

        
            command = int(input("Введите цифру:"))

            if command == 1:
                def add_note():
                    user = input("Написать заметку:")
                    with open("notes.txt", "a", encoding="utf-8") as file:
                        content = file.write(user + "\n")
                        print("Заметка записана!")

                add_note()

            elif command == 2: 
                def read_notes():
                    try:
                      with open("notes.txt", "r", encoding="utf-8") as file:
                        notes=file.read()
                      if notes:
                        print("Твои заметки:")
                        print(notes)

                      else:
                        print("Заметок пока нет")

                    except FileNotFoundError:
                      print("Файл ещё не создан!")

                read_notes()

            elif command == 3:
                def delete_notes():
                  with open("notes.txt", "w", encoding="utf-8") as file:
                    notes=file.write("")
                  print("Заметки очищены!")

                delete_notes()

            elif command == 4:
                print("До встречи!")  
                break  


         
           
        menu()
except ValueError:
   print("Введите число!")