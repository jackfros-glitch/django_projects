'''ads.Comment.ad: (fields.E303) Reverse query name for 'ads.Comment.ad' clashes with field name 'ads.Ads.comment'.
        HINT: Rename field 'ads.Ads.comment', or add/change a related_name argument to the definition for field 'ads.C
omment.ad'.
get url's are idempotent
'''
import csv

from unesco.models import Site, Region, State, Category, Iso

def run():
    fhand = open("unesco/whc-sites-2018-clean.csv")
    reader = csv.reader(fhand)
    next(reader)
    #clean the database
    Site.objects.all().delete()
    Region.objects.all().delete()
    State.objects.all().delete()
    Category.objects.all().delete()
    Iso.objects.all().delete()

    for row in reader:
        print(row)

        c, created = Category.objects.get_or_create(name=row[7])
        s, created = State.objects.get_or_create(name=row[8])
        r, created = Region.objects.get_or_create(name=row[9])
        i, created = Iso.objects.get_or_create(name=row[10])

        try :
            y = int(row[3])
        except:
            y = None


        try :
            a = float(row[6])
        except:
            a = None


        site = Site(name=row[0], description=row[1], justification=row[2],
                year=y, longitude=row[4], latitude=row[5], area_hectares=a,
                category=c, state=s,region=r,iso=i)
        site.save()