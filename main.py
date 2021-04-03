from PIL import Image
import os

files = os.listdir("in")

while True:
    # Выводим достуные файлы из папки in
    for i in range(len(files)):
        print(str(i + 1) + ". " + files[i])
        i += 1
    # Запрашиваем номер файла
    num_photo = input("Номер файла: ")
    photo = files[int(num_photo) - 1]
    # Конфиг
    quality = input("Уровень качества до 99: ")
    shakalik = input("Множитель сжатия: ")
    # Шакалим 
    im = Image.open("in/" + photo)  # Берём фотку
    W, H = im.size  # Размер
    im_preshakal = im.resize((int(W) // int(shakalik), int(H) // int(shakalik)))  # Масштаб
    im_shakal = im_preshakal.convert('RGB')
    im_shakal.save("out/" + photo + 'shakal' + '.jpg', quality=int(quality))  # Шакалим и сохраняем
