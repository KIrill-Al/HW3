"""4. Дан файл, содержащий сведения о книгах:
1) фамилия автора
2) название
3) год издания
4) цена книги
Распечатать записи с заданным годом издания, упорядоченные по алфавиту, а если таковых нет, то выдать соответствующее сообщение;
Отсортировать записи в порядке возрастания цены книги."""
import sys


def create_file_output(books, name):
    """Создаёт файл с результатом в виде форматированного списка книг"""
    str1 = ''
    try:
        autor_len = max([len(book[0]) for book in books])
        name_len = max([len(book[1]) for book in books])
        year_len = max([len(book[2]) for book in books])
        price_len = max([len(book[3]) for book in books])
    except ValueError:
        with open(name + '.txt', 'w') as file_out:
            file_out.write('Результаты отсутствуют. \
                Выберите другой год либо проверьте корректность исходных данных (source.txt)')
    except Exception as ex:
        with open(name + '.txt', 'w') as file_out:
            for i in sys.exc_info():
                str1 += str(i) + '\n'
            file_out.write('Возникла ошибка чтения данных:\n' + str1)
    else:
        str1 = str1 + 'Автор'.ljust(autor_len, ' ') + '\t' + 'Название'.ljust(name_len, ' ') + \
            '\t' + 'Год'.ljust(year_len, ' ') + '\t' + 'Цена'.ljust(price_len, ' ') + '\n'
        with open(name + '.txt','w') as file_out:
            for book in books:
                str1 += book[0].ljust(autor_len, ' ') + '\t' + book[1].ljust(name_len, ' ') + \
                    '\t' + book[2].ljust(year_len, ' ') + '\t' + book[3].ljust(price_len, ' ') + '\n'
            file_out.write(str1)


try:
    file = open('source.txt')
except FileNotFoundError:
    print('Файл "source.txt" не найден.')
    exit()
else:
    #  создаём список списков с информацией о каждой книге
    books = list(book.split(';') for book in list(file.read().split('\n')))
    #  убираем пустой элемент в конце списка (появляется из-за eof)
    if books[len(books)-1][len(books[len(books)-1])-1] == '':
        books.pop()
    file.close()

year = input('Введите год книги: ')
try:
    output1 = list(filter(lambda book: book[2] == year, books))  # список книг по выбранному году
    output2 = list(filter(lambda book: book[2] != year, books))  # остальные книги
except IndexError:
    print('Проверьте корректность исходных данных (source.txt)')
    print('Необходимый формат данных:' + '\n' + 'Автор1;Название1;Год;Цена' + \
          '\n' + 'Автор2;Название2;Год;Цена')
else:
    output1.sort()  # первый сортируем по алфавиту
    output2.sort(key=lambda book: book[3])  # второй - по цене
    #  создаём файлы с результатами
    create_file_output(output1, 'result_data')
    create_file_output(output2, 'result_other')
