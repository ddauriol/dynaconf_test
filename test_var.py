from dynaconf import settings


print(settings.DATABASES)
print(settings.DATABASES.DEFAULT)
print(settings.DATABASES.DEFAULT.ENGINE)
print(settings.DATABASES.DEFAULT.NAME)
print(settings.DATABASES.DEFAULT.USER)
print(settings.DATABASES.DEFAULT.PASSWORD)
print(settings.DATABASES.DEFAULT.HOST)
print(settings.DATABASES.DEFAULT.PORT)
    