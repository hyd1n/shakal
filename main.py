from PIL import Image
import os
import json
from time import sleep
try:
    with open("config.json", "r") as read_file:
        settings = json.load(read_file)
except:
    print("У вас нет файла с конфигом, создаю конфиг по умолчанию")
    with open("config.json", "w") as write_file:
        json.dump({
        "showimage": "yes"
        }, write_file)
# Проверка на наличие нужных папок
if not os.path.isdir("in"):
    print("У вас нет папки in, создаю")
    os.mkdir("in")
if not os.path.isdir("out"):
    print("У вас нет папки out, создаю")
    os.mkdir("out")

files = os.listdir("in")
while True:
    print("Текущая деректория:", os.getcwd())
    # Выводим достуные файлы из папки in
    for i in range(len(files)):
        print(str(i + 1) + ". " + files[i])
        i += 1
    # Запрашиваем номер файла
    num_photo = input("\nНомер файла: ")
    photo = files[int(num_photo) - 1]
    # Конфиг
    im = Image.open("in/" + photo)  # Берём фотку
    W, H = im.size  # Размер
    print("Размер фотки: " + str(W) + "x" + str(H))
    quality = input("Уровень качества до 100 (100 - текущее качество): ")
    shakalik = input("Множитель сжатия: ")
    # Шакалим 
    im_preshakal = im.resize((int(W) // int(shakalik), int(H) // int(shakalik)))  # Масштаб
    print("Сжимаю до " + str(int(W) // int(shakalik)) + "x" + str(int(H) // int(shakalik)))
    im_shakal = im_preshakal.convert('RGB')
    if settings['showimage'] == 'yes':
        im_shakal.show()
    im_shakal.save("out/" + photo + 'shakal' + '.jpg', quality=int(quality))  # Шакалим и сохраняем
    print("Файл сохранён по пути:" + "out/" + photo + 'shakal' + '.jpg')
    sleep(1)
    os.system('cls')
