"""
 gensitemap.py - generate a site map based on googles SiteMap specification
 Protocol:  https://www.google.com/webmasters/sitemaps/docs/en/protocol.html


 variations of note:  metadata (such as how often to index the file) will be in
  filename.metadata.  If you want to override the default frequency and priority,
  create a file called "whatever-the-filename-was".metadata with the xml lines:

<changefreq>whatever</changefreq>
<priority>whatever</priority>

 Output is to stdout.  Redirect to a file if you want to save the output.  Pipe
 through gzip if you want it gzipped.

"""

import os
import string
import time

import xml.sax.saxutils

#
# Document extentions we are interested in generating data for.
#
EXTENSIONS = (".html",)

DOMAIN = "http://pythonarticles.com/"
DEFAULT_FREQ = "daily"
DEFAULT_PRIORITY = "0.5"


def recurse_directories(rootdir=""):
    directory = os.getcwd() + os.sep + rootdir
    for found_file in os.listdir(directory):
        if found_file.startswith("google"):
            continue

        if os.path.isdir(os.getcwd() + os.sep + rootdir + os.sep + found_file):
            recurse_directories(rootdir + os.sep + found_file)
        else:
            found = False
            for each in EXTENSIONS:
                if string.find(found_file, each) > -1 and string.find(found_file, ".metadata") == -1:
                    found = True
                    break

            if found:

                modtime = os.path.getmtime(os.getcwd() + os.sep + rootdir + os.sep + found_file)

                iso_time = time.strftime("%Y-%m-%d", time.localtime(modtime))
                url = xml.sax.saxutils.escape(DOMAIN + string.replace(rootdir, os.sep, "/") + "/" + found_file)

                print "<url>"
                print "  <loc>" + url + "</loc>"
                print "  <lastmod>" + str(iso_time) + "</lastmod>"

                # if there is a filename.metadata file, include that now
                try:
                    f = open(os.getcwd() + os.sep + rootdir + os.sep + found_file + ".metadata")
                    lines = f.readlines()

                    for line in lines:
                        print "  " + line

                except:
                    print "  <changefreq>" + DEFAULT_FREQ + "</changefreq>"
                    print "  <priority>" + DEFAULT_PRIORITY + "</priority>"

                print "</url>";


print "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
print "<urlset xmlns=\"http://www.google.com/schemas/sitemap/0.84\">"

recurse_directories('html')

print "</urlset>"