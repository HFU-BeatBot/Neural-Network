import csv

def modify_csv(filename, column_index, words, max):
    new_rows = []
    genreCounter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Überspringe die Kopfzeile

        for row in csv_reader:
            i = 0
            while(i < 10):
                if row[column_index] == words[i]:
                    if genreCounter[i] < max:
                        new_rows.append(row)
                        genreCounter[i] += 1
                i += 1

    new_filename = 'neue_datei.csv'
    with open(new_filename, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(header)
        csv_writer.writerows(new_rows)

    print(f"Die modifizierte CSV-Datei wurde unter '{new_filename}' gespeichert.")


# Beispielaufruf
filename = '/Users/tomherrmann/Developer/BeatBot/Neural-Network/FMA/ten_genres_old_plus_fma_data.csv'
column_index = 41  # Index der Spalte, die überprüft werden soll (0-basiert)
words = ['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']
max = 1300
modify_csv(filename, column_index, words, max)

