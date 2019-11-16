import webapp2
import logging
import jinja2
import os

#Step 1: Import jinja and os


#Step 1: Set up Jinja Environment
jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/madlibs.html')
        self.response.write(template.render())

    def post(self):
        template_vars = {
            "name": self.request.get("classmate"),
            "activity": self.request.get("activity"),
            "planetname": self.request.get("planetname"),
            "noun": self.request.get("noun"),
            "hero": self.request.get("hero"),
            "verb": self.request.get("verb"),


        }
        template = jinja_env.get_template('templates/story.html')
        self.response.write(template.render(template_vars))

app = webapp2.WSGIApplication([
    ('/', MainPage),


], debug = True)
