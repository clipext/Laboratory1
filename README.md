
*Парсер*

Нужно реализовать преобразование выражение в инфиксной нотации в [обратную польскую запись](https://ru.wikipedia.org/wiki/%D0%9E%D0%B1%D1%80%D0%B0%D1%82%D0%BD%D0%B0%D1%8F_%D0%BF%D0%BE%D0%BB%D1%8C%D1%81%D0%BA%D0%B0%D1%8F_%D0%B7%D0%B0%D0%BF%D0%B8%D1%81%D1%8C)

Примеры
```
"1 + 2 * 3" -> "1 2 3 * +"
"1 + 2 * 3 + 4" -> "1 2 3 * + 4 +"
```

Функция, реализующая преобразование находится в файле parse.py, под названием parse.
Функция принимает на вход строку и возвращает строку.
Все токены (числа и арифметические символы) разделены ровно одним пробелом.
Допустимые арифметические знаки: `'*', '/', '+', '-', '(', ')'`.
Допустимы как целые числа, так и числа с плавающей запятойю Разделитель дробной части - `.`.

Для выполнения задания необходимо (но недостаточно) прохождение всех тестов из файла test_parser.py


*Исполнитель*

Нужно выполнить выражение записанное в [обратной польской записи](https://ru.wikipedia.org/wiki/%D0%9E%D0%B1%D1%80%D0%B0%D1%82%D0%BD%D0%B0%D1%8F_%D0%BF%D0%BE%D0%BB%D1%8C%D1%81%D0%BA%D0%B0%D1%8F_%D0%B7%D0%B0%D0%BF%D0%B8%D1%81%D1%8C)

Примеры
```
"1 2 3 * +" -> 7
"3.0 2 / 3 2 / -" -> 0.5
```

Функция, реализующая исполнение находится в файле execute.py, под названием execute.
Функция принимает на вход строку и возвращает число.
Все токены (числа и арифметические символы) разделены ровно одним пробелом.
Допустимые арифметические знаки: `'*', '/', '+', '-'`.
Допустимы как целые числа, так и числа с плавающей запятойю Разделитель дробной части - `.`.
Операторы имеют различное поведение для целых чисел и чисел с плавающей запятой.

Для выполнения задания необходимо (но недостаточно) прохождение всех тестов из файла test_execute.py


