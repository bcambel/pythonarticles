import markdown2
import os
from jinja2 import *
from datetime import datetime as dt
import ConfigParser
import datetime
from rss import RSS2, Guid, RSSItem

config = ConfigParser.RawConfigParser()

cur_dir = os.path.dirname(os.path.realpath(__file__))
env = Environment(loader=FileSystemLoader(os.path.join(cur_dir, "templates")))

ARTICLE_PATH = 'articles/'
HTML_OUTPUT_PATH = 'html/'

configfiles = ['article.cfg']
files_read = config.read(configfiles)

rss_items = []

class Article:

    def __init__(self, title, slug, description,level=None,tags=None):
        self.title = title
        self.slug = slug
        self.description = description
        self.tags = tags or []
        self.level = level


def render_plain():
    base = "".join(open("base.html").readlines())
    tail = "".join(open("tail.html").readlines())

    for dirname, dirnames, file_names in os.walk(ARTICLE_PATH):
        for file in file_names:
            output_file = "%s.html" % file[:-3]
            file_path = "%s%s" % (ARTICLE_PATH, file)
            content = "".join(open(file_path).readlines())
            print "{0}{1}{0}".format((20 * "-"), output_file)
            gen_content = markdown2.markdown(content, extras=['fenced-code-blocks'])

            with open('%s%s' % ( HTML_OUTPUT_PATH, output_file), "w+") as post:
                post.write(base)
                post.write(gen_content.encode('ascii', 'xmlcharrefreplace'))
                post.write(tail)
                post.flush()

            print file
            print 30 * "="


def render_jinja():
    articles = []
    index_articles = []
    article_jinja_tmpl = env.get_template("article_detail.html")

    for directory, directories, filenames in os.walk(ARTICLE_PATH):
        for file in filenames:
            title = slug = file[:-3]
            title = title.replace("-", " ").replace("_"," ")
            articles.append(Article(title=title, slug=slug, description=None))

        for article in articles:
            article_settings = {}
            if config.has_section(article.slug):
                article_settings = {i[0]: i[1] for i in config.items(article.slug)}

            article_path = "%s%s.md" % (ARTICLE_PATH, article.slug)
            content = "".join(open(article_path).readlines())
            gen_content = markdown2.markdown(content, extras=['fenced-code-blocks'])
            content = gen_content.encode('ascii', 'xmlcharrefreplace').replace("codehilite","syntax")
            
            article_configuration = dict(content=content, title=article.title, articles=articles,
                                         disqus=True,
                                         url='http://pythonarticles.com/%s.html'%article.slug,
                                         ts=dt.utcnow()
                                         )

            print article_settings
            article_configuration.update(**article_settings)
            print "Current article: %s" % article.title
            article_configuration['tags'] = article_configuration['tag'].split(",")
            # del article_configuration['tag']
            print "=====", article_configuration['tags'],article_configuration['level']

            publish_date = dt.strptime(article_configuration.get("publish_date", ), "%Y-%m-%d")
            index_articles.append(Article(title=article.title,slug=article.slug,
                description=article_configuration.get("description",""),
                level=article_configuration['level'],
                tags=article_configuration['tags'] )
            )

            rss_items.append(
                RSSItem(
                     title = article_configuration.get("title"),
                     link = article_configuration.get("url"),
                     description = article_configuration.get("description"),
                     guid = Guid(article_configuration.get("url")),
                     pubDate = publish_date)
            )

            with open('%s%s.html' % (HTML_OUTPUT_PATH, article.slug), "w+") as article_output:
                article_output.write(
                    article_jinja_tmpl.render(**article_configuration))
                article_output.flush()

    index_jinja_tmpl = env.get_template('index.html')
    index = HTML_OUTPUT_PATH + 'index.html'

    with open(index, "w+") as index:
        index_configs = {i[0]: i[1] for i in config.items("index")}

        index_configs.update(**dict(articles=index_articles, disqus=False, ts=dt.utcnow(),))
        index.write(index_jinja_tmpl.render(**index_configs))
        index.flush()


if __name__ == "__main__":
    render_jinja()

    
    rss = RSS2(
        title = "Python Articles Feed",
        link = "http://pythonarticles.com/rss.xml",
        description = "Latest articles about Python.",
        lastBuildDate = datetime.datetime.utcnow(),

        items = rss_items
    )

    #rss.write_xml(open("html/rss.xml", "w"))

