import sys
import time

def jalanin_lirik () :
    lirik = [
        ("Dulu sakit, sekarang lega", 0.065),
        ("Cerita lama, aku dah reda", 0.07),
        ("Tak nak pusing, ", 0.085),
        ("Tak nak tanya", 0.085),
        ("Aku kuat, tanpa drama ", 0.09),
        ("Dulu sakit, sekarang lega", 0.066),
        ("Cerita lama, aku dah reda", 0.07),
        ("Tak nak pusing, ", 0.085),
        ("tak nak tanya ", 0.085), 
        ("Aku kuat, tanpa drama", 0.09),
        ("Aku dah lupa, ", 0.083),  
        ("tak ingat lagi ", 0.073), 
        ("Nama kau pun hilang dari hati ", 0.063), 
        ("Aku move on, ", 0.068), 
        ("hidup sendiri ", 0.073), 
        ("Tak perlu kau, ", 0.068),  
        ("aku happy ", 0.068), 
        ("Aku dah lupa, ", 0.083), 
        ("tak ingat lagi ", 0.073), 
        ("Nama kau pun hilang dari hati ", 0.063), 
        ("Aku move on, ", 0.068), 
        ("hidup sendiri ", 0.073), 
        ("Tak perlu kau, ", 0.068), 
        ("aku happy ", 0.068), 



    ]

    delay = [0.3, 0.26, 0.2, 0.3, 0.25, 0.3, 0.3, 0.2, 0.3, 0.12, 0.2, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.26]

    time.sleep(0.1)
    for i, (baris_lagu, delay_karakter) in enumerate(lirik):
        for karakter in baris_lagu :
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(delay_karakter)
        time.sleep(delay[i])    
        print('')


jalanin_lirik()