import os
import random
import speech_recognition

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5

commands_dict = {
    'commands': {
        'greeting': ['привет', 'приветствую'],
        'create_task': ['добавить задачу', 'заметка', 'задача', 'создать задачу'],
        'play_music': ['включи музыку', 'музыка', 'дискотека']
    }
}

def listen_command():
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
        return query
    except speech_recognition.UnknownValueError:
        return 'Ничего не понял...'


def greeting():
    return 'Ну привет!'

def create_task():
    print('Говори, я записываю!..')
    query = listen_command()

    with open('list_del.txt', 'a') as file:
        file.write(f'* {query}\n')
    return f'Задача {query} добавлена'

def play_music():
    files = os.listdir('music')
    random_file = f'music/{random.choice(files)}'
    os.system(f'start {random_file}')

    return f'Включаю {random_file.split("/")[-1]}!!!'

def main():
    query = listen_command()

    for k, v in commands_dict['commands'].items():
        if query in v:
            print(globals()[k]())

if __name__ == '__main__':
    main()


