# interface
class WebPage():
    def __init__(self, theme):
        self.theme = theme

    def get_content(self):
        raise NotImplementedError

class About(WebPage):
    def __init__(self, *args, **kwargs):
        super(About, self).__init__(*args, **kwargs)

    def get_content(self):
        return "{} page in {}".format(self.__class__.__name__, self.theme.get_color())

class Careers(WebPage):
    def __init__(self, *args, **kwargs):
        super(Careers, self).__init__(*args, **kwargs)

    def get_content(self):
        return "{} page in {}".format(self.__class__.__name__, self.theme.get_color())


# Interface
class Theme():
    def get_color(self):
        raise NotImplementedError

class DarkTheme(Theme):
    def get_color(self):
        return "Dark Black"

class LightTheme(Theme):
    def get_color(self):
        return "Off White"

class AquaTheme(Theme):
    def get_color(self):
        return "Light Blue"


if __name__ == "__main__":
    dark_theme = DarkTheme()

    about = About(dark_theme)
    careers = Careers(dark_theme)

    print(about.get_content())
    print(careers.get_content())
