from datetime import datetime

AUTHOR = "fabse"
AUTHOR_WEBSITE = "http://www.example.com"
SITENAME = "fabse-hack"
#SITEURL = 'test.com'
SITETITLE = "fabse hack"
SITESUBTITLE = "welcome to fabse hack website"
#SITEDESCRIPTION = "Flex - The minimalist Pelican theme."
# SITELOGO = ''
FAVICON = '/images/fabsehack.ico'
BROWSER_COLOR = "#333333"
PATH = 'content'

ARTICLE_METADATA = ('Title', 'Date', 'Author', 'Category', 'Tags')
TIMEZONE = 'Europe/Berlin'
THEME = "pelican-theme/"
THEME_COLOR = 'dark'
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True
USE_LESS = True
USE_GOOGLE_FONTS = False
PYGMENTS_STYLE = "monokai"
PYGMENTS_STYLE_DARK = 'monokai'
DEFAULT_LANG = 'de'
SUMMARY_MAX_LENGTH = 10

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


LINKS = (('Blog', 'https://fabse-hack.github.io/'),
         ('Testing', 'https://fabse-hack.github.io/'))


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

ROBOTS = "index, follow"
PATH = "content"
OUTPUT_PATH = "blog/"
DISABLE_URL_HASH = True

# PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['pelican_youtube']
# JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
# I18N_TEMPLATES_LANG = "de"
# OG_LOCALE = "de_DE"
#LOCALE = "de_DE"

DATE_FORMATS = {
    "de": "%d %B %Y",
}

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

GITHUB_CORNER_URL = "https://github.com/fabse-hack"

SOCIAL = (
    ("github", "https://github.com/fabse-hack"),
    ("youtube", "https://youtube.com/fabse-hack"),
    ("rss", "/blog/feeds/all.atom.xml"),
)

MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)

CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike 4.0 International License",
    "version": "4.0",
    "slug": "by-sa",
    "icon": True,
    "language": "en_US",
}


COPYRIGHT_YEAR = datetime.now().year

# DISQUS_SITENAME = "flex-pelican"
# ADD_THIS_ID = "ra-55adbb025d4f7e55"
# STATIC_PATHS = ["images", "extra/ads.txt", "extra/CNAME"]

EXTRA_PATH_METADATA = {
    "extra/ads.txt": {"path": "ads.txt"},
    "extra/CNAME": {"path": "CNAME"},
}
