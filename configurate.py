from json import dump


def enter(a, settings):
    settings[a] = 5
    while 50 < settings[a] or settings[a] < 10:
        settings[a] = int(input("{0}(from 10 to 50): ".format(a.capitalize())))


def foo():
    print("\nConfiguration:")

    with open(".settings.conf", 'w', ) as file:
        settings = {}
        enter('resolution', settings)
        enter('speed', settings)
        dump(settings, file)

    print("Done configuration")


if __name__ == '__main__':
    foo()
