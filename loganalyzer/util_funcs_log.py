import csv
from datetime import datetime
from .util_models import Log

logs = []

# sunucu ilk ayağa kalktığında bir kere çalıştırır ve logs listesine logları ekler
def scan_file():

    with open("hn_logs.tsv") as file:
        
        tsv_file = csv.reader(file, delimiter="\t")

        for line in tsv_file:
            log = Log(line[0], line[1])
            logs.append(log)

# date_string tarihindeki logları tarar ve unique olanları döndürür
def scan_logs(date_string):
    
    filtered_logs = []
    log_texts_seen = set()  
    duplicate_texts = set()
    
    for log in logs:
        if log.date.find(date_string) != -1: # eğer logun tarihi date_string içeriyorsa logu filtered_logs listesine ekler
            filtered_logs.append(log)
            # eğer logun texti tekrardan gözüktüyse duplicate_texts setine ekler
            if log.text in log_texts_seen:
                duplicate_texts.add(log.text)
                #print(log.text)
            else:
                log_texts_seen.add(log.text)
    
    # unique logları bulur
    unique_logs = [log for log in filtered_logs if log.text not in duplicate_texts]

    return len(unique_logs)

