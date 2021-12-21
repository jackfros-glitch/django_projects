import csv

from cats.models import Cat, Breed

def run():
    fhand = open('cats/meow.csv')
    reader = csv.reader(fhand)
    next(reader)

    #clean our database
    Cat.objects.all().delete()
    Breed.objects.all().delete()

    for row in reader:
        print(row)
        b, created = Breed.objects.get_or_create(name=row[1])

        cat = Cat(nickname=row[0], breed=b, weight=row[2])
        cat.save()


