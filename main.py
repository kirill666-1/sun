# Инициализируем пустую матрицу для хранения результатов
    result_matrix = []
    for i in range(result_rows):
        # Создаем строку с нулевыми значениями
        row = [0] * result_cols
        # Добавляем строку в результирующую матрицу
        result_matrix.append(row)

    # Заполняем результирующую матрицу вычисленными значениями
    for result in results:
        (i, j), value = result
        result_matrix[i][j] = value  # Присваиваем значение элементу матрицы

    # Записываем результирующую матрицу в файл
    with open('result_matrix.txt', 'w') as f:
        for row in result_matrix:
            # Преобразуем числа в строки
            str_numbers = [str(num) for num in row]
            # Объединяем числа через пробел и добавляем перевод строки
            line = ' '.join(str_numbers) + '\n'
            # Записываем строку в файл
            f.write(line)

# Проверяем, является ли данный скрипт основным (а не импортированным модулем)
if name == 'main':
    # Запускаем основную функцию
    main()