import webapp2
import logging
import jinja2
import os

#Step 1: Import jinja and os


#Step 1: Set up Jinja Environment
jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)
class Email(object):
    def __init__(self, title, subject, unread):
            self.title = title
            self.subject = subject
            self.unread = unread
emails = [
    Email("Hey, hows it going", "Jeff", True),
    Email("Status", "App", False),
    Email("Click here fore free servers!", "Cloud", True),
    Email("Free gift card for Spotify","Ad", True),
    Email("Email from Registrar", "Bob", False)
]

class inbox(webapp2.RequestHandler):
    def get(self):
        template_vars = {
            'inbox': emails
        }
        template = jinja_env.get_template('templates/inbox.html')
        self.response.write(template.render(template_vars))



app = webapp2.WSGIApplication([
    ('/inbox', inbox),

], debug = True)
