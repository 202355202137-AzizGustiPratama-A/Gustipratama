import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text , delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("I hold imagination cover all the sadness", 0.16),
        ("I don't feel something special", 0.16),
        ("Turn off the phone to get some special", 0.13),
        ("Never thought i'd living in true", 0.12),
        ("The truth that has been so blue", 0.13),
        ("It was a blink of an eye find a way how say goodbye", 0.14),
        ("I've got to take me away from all sadness", 0.14),
      
    ]
    delays = [1.7, 4.6, 9.0, 13.4, 16.4, 25.5, 29.3, ]

    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i],speed))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()