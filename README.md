# file2text

** В рамках данного алгоритма рассматривается три случая входных файлов: **
1. Входной файл - простой выделяемый pdf-файл;

2. Входной файл - изображение;

3. Входной файл - невыделяемый image-like pdf.

Для решения первой задачи используется файл pdf_to_text.py.

Во второй задаче используется запускается файл image_to_text.py.

В последней задаче используется постраничное преобразование pdf-файла в jpg-картинки. С помощью цикла проходимся по картинкам и обновляем полученный результат. Данным алгоритмом занимается image_like_pdf_to_text.py. Если выполнение прервано, то в ветке finally удаляются "временные" картинки и записывается тот результат, который был обработан.

Перед использованием необходимо скачать poppler-0.68.0 и pytesseract, а также записать название необходимого файла в filename.

Дальнейшие направления работы:

1. Использовать библиотеку tempdir для считывания временных картинок;

2. Добавить возможность запуска из командной строки (?);

3. Использовать полный потенциал cv2 для улучшения точности распознавания с помощью компьютерного зрения.
