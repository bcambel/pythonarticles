import markdown2
import os
from jinja2 import *
from datetime import datetime as dt
import ConfigParser

config = ConfigParser.RawConfigParser()

cur_dir = os.path.dirname(os.path.realpath(__file__))
env = Environment(loader=FileSystemLoader(os.path.join(cur_dir, "templates")))

ARTICLE_PATH = 'articles/'
HTML_OUTPUT_PATH = 'html/'

configfiles = ['article.cfg']
files_read = config.read(configfiles)


class Article:
    title = ''
    slug = ''

    def __init__(self, title, slug):
        self.title = title
        self.slug = slug


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
    article_jinja_tmpl = env.get_template("article_detail.html")

    for directory, directories, filenames in os.walk(ARTICLE_PATH):
        for file in filenames:
            title = slug = file[:-3]
            title = title.replace("-", " ").replace("_"," ")
            articles.append(Article(title=title, slug=slug))

        for article in articles:
            article_settings = {}
            if config.has_section(article.slug):
                article_settings = {i[0]: i[1] for i in config.items(article.slug)}

            article_path = "%s%s.md" % (ARTICLE_PATH, article.slug)
            content = "".join(open(article_path).readlines())
            gen_content = markdown2.markdown(content, extras=['fenced-code-blocks'])
            content = gen_content.encode('ascii', 'xmlcharrefreplace')

            article_configuration = dict(content=content, title=article.title, articles=articles,
                                         disqus=True,
                                         url='http://pythonarticles.com/%s.html'%article.slug,
                                         ts=dt.utcnow()
                                         )

            print article_settings
            article_configuration.update(**article_settings)

            with open('%s%s.html' % (HTML_OUTPUT_PATH, article.slug), "w+") as article_output:
                article_output.write(
                    article_jinja_tmpl.render(**article_configuration))
                article_output.flush()

    index_jinja_tmpl = env.get_template('index.html')
    index = HTML_OUTPUT_PATH + 'index.html'

    with open(index, "w+") as index:
        index.write(index_jinja_tmpl.render(articles=articles, disqus=False, ts=dt.utcnow()))
        index.flush()


if __name__ == "__main__":
    render_jinja()

