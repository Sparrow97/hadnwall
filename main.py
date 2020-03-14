
import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3
import serial
import time
import random
import numpy as np
import pyzbar.pyzbar as pyzbar
import cv2




# Функция, позволяющая проговаривать слова
# Принимает параметр "Слова" и прогроваривает их
def talk(words):
	engine = pyttsx3.init()
	engine.say(words)
	engine.runAndWait()

# Вызов функции и передача строки
# именно эта строка будет проговорена компьютером
talk("Здравстуйте, чем я могу помочь вам?")

""" 
	Функция command() служит для отслеживания микрофона.
	Вызывая функцию мы будет слушать что скажет пользователь,
	при этом для прослушивания будет использован микрофон.
	Получение данные будут сконвертированы в строку и далее
	будет происходить их проверка.
"""
def command():
	# Создаем объект на основе библиотеки
	# speech_recognition и вызываем метод для определения данных
	r = sr.Recognizer()

	# Начинаем прослушивать микрофон и записываем данные в source
	with sr.Microphone() as source:
		# Просто вывод, чтобы мы знали когда говорить
		print("Говорите")
		# Устанавливаем паузу, чтобы прослушивание
		# началось лишь по прошествию 1 секунды
		r.pause_threshold = 0.5
		# используем adjust_for_ambient_noise для удаления
		# посторонних шумов из аудио дорожки
		r.adjust_for_ambient_noise(source, duration=1)
		# Полученные данные записываем в переменную audio
		# пока мы получили лишь mp3 звук
		audio = r.listen(source)

	try: # Обрабатываем все при помощи исключений
		""" 
		Распознаем данные из mp3 дорожки.
		Указываем что отслеживаемый язык русский.
		Благодаря lower() приводим все в нижний регистр.
		Теперь мы получили данные в формате строки,
		которые спокойно можем проверить в условиях
		"""
		zadanie = r.recognize_google(audio, language="ru-RU").lower()
		# Просто отображаем текст что сказал пользователь
		print("Вы сказали: " + zadanie)
	# Если не смогли распознать текст, то будет вызвана эта ошибка
	except sr.UnknownValueError:
		# Здесь просто проговариваем слова "Я вас не поняла"
		# и вызываем снова функцию command() для
		# получения текста от пользователя
		talk("Я вас не поняла")
		zadanie = command()

	# В конце функции возвращаем текст задания
	# или же повторный вызов функции
	return zadanie

# Данная функция служит для проверки текста,
# что сказал пользователь (zadanie - текст от пользователя)



def vision():
	cap = cv2.VideoCapture(0)
	font = cv2.FONT_HERSHEY_PLAIN
	_, frame = cap.read()

	decodedObjects = pyzbar.decode(frame)
	for obj in decodedObjects:
		a = obj.data
		if (a == b'MAX LOH'):
			return a


def makeSomething(zadanie, a):
	# Попросту проверяем текст на соответствие
	# Если в тексте что сказал пользователь есть слова
	# "открыть сайт", то выполняем команду
	if 'arduino' in zadanie:
		# Проговариваем текст
		talk("Уже открываю")
		# У000казываем сайт для открытия
		strComPort = 'COM4'
		strComBaud = 9600
		cmdSerial = serial.Serial(strComPort, strComBaud)
		time.sleep(0.5)
		#print(cmdSerial.readline())
		talk("Открыла")



		while True:
			k = '1'
			b = '0'
			#var = command()
			if (a == 1):
				cmdSerial.write(k.encode())
				time.sleep(1)
				talk("включаю")
			elif (a == 'стоп'):
				cmdSerial.write(b.encode())
				time.sleep(1)
				talk("Выключаю, мойгосподин")

			elif (a == 'быстрее'):
				cmdSerial.write(l.encode())
				time.sleep(1)
				talk("СКОРОСТЬ СВЕТА")






	# если было сказано "стоп", то останавливаем прогу
	elif 'закройся' in zadanie:
		# Проговариваем текст
		talk("Да, конечно, без проблем")
		# Выходим из программы
		sys.exit()
	# Аналогично
	elif 'имя' in zadanie:
		talk(" Ka 2")
	elif 'фамилия' in zadanie:
		talk("Ka 3")
		koloda = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4
		import random
		random.shuffle(koloda)
		print('Поиграем в очко?')
		count = 0
		target = 0

		while True:
			choice = input('Будете брать карту? y/n\n')
			if choice == 'y':
				current = koloda.pop()
				print('Вам попалась карта достоинством %d' % current)
				target += current - 1
				count += current
				if count > 21:
					print('Извините, но вы проиграли')
					break
				elif count == 21:
					print('Поздравляю, вы набрали 21!')
					break
				else:
					print('У вас %d очков.' % count)
			elif choice == 'n':
				print('У вас %d очков и вы закончили игру.' % count)
				break

		print('До новых встреч!')
# Вызов функции для проверки текста будет
# осуществляться постоянно, поэтому здесь
# прописан бесконечный цикл while
while True:
	makeSomething(command())

