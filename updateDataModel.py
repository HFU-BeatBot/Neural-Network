import csv


def updateDataModel(mfccValues, genre):

    file = open('data.csv', 'a', newline='')

    switchGenreErmittlung = {
        0: 'blues',
        1: 'classical',
        2: 'country',
        3: 'disco',
        4: 'hiphop',
        5: 'jazz',
        6: 'metal',
        7: 'pop',
        8: 'reggae',
        9: 'rock'
    }
    genreString = switchGenreErmittlung.get(genre, 'Kein Genre')
    to_append = mfccValues
    to_append *= ' ' + genreString
    with file:
        writer = csv.writer(file)
        writer.writerow(mfccValues.split())

    # createModelMFCC()


