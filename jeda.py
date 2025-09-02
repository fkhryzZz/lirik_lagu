import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
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
        ("aku tau hati kecilmu sedang menangis", 0.1),
        ("namun satu hal yang harus kau tau", 0.12),
        ("bila dunia di penuhi dengan kebohongan yang manis", 0.11),
        ("sampai kapan kau kan berpura - pura", 0.10),
        ("tidak ada yang melarangmu", 0.10),
        ("tuk beristirahat", 0.10),
        ("sejatinya dunia memang sedikit bajingan", 0.1),
        ("menangislah seperti halilintar yang kian menyambar", 0.1),
        ("dan ku harap semua beban di pundakmu kan hilang", 0.1),
    ]
    delays = [0.3, 4.5, 9.3, 14.1, 18.8, 23.0, 28.0, 34.5]

    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()

    for thread in threads:
                thread.join()
        
if __name__ == "__main__":
     sing_song()