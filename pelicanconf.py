AUTHOR = 'Jack Hayes'
SITENAME = 'Jack Hayes Digital Storytelling Portfolio'
SITEURL = "" # For local development
PATH = "content"
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'
THEME = "notmyidea"

# URLs and Paths
RELATIVE_URLS = True
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
SLUGIFY_SOURCE = 'basename'        # FIX 1: Use filename for URLs
INDEX_SAVE_AS = 'blog_index.html'  # FIX 2: Stop blog index conflict

# Static files
STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {'extra/favicon.ico': {'path': 'favicon.ico'}}

# Menu
MENUITEMS = (
    ('Home', '/'),
    ('Writing', '/writing.html'),
    ('Maps', '/maps.html'),
    ('Apps', '/apps.html'),
    ('Presentations', '/presentations.html'),
    ('Software', '/software.html'),
    ('Misc', '/misc.html'),
)

# Disable unused pages
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
TAG_SAVE_AS = ''
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DEFAULT_PAGINATION = False

# Feed generation is not needed for a portfolio
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Markdown settings
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.attr_list': {},
        'markdown.extensions.extra': {},
    },
    'output_format': 'html5',
}