import webapp2
import logging
import jinja2
import os

#Step 1: Import jinja and os


#Step 1: Set up Jinja Environment
jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)
class MainPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/home.html')
        self.response.write(template.render())

    def post(self):
        name = self.request.get("name")
        like_cs = self.request.get("cs")
        is_senior = self.request.get("senior")

        if like_cs and is_senior:
            advice = "You should apply to CSSI."
        elif like_cs:
            advice = "When you are a senior, apply to CSSI!"
        else:
            advice = "You should consider Computer Science!"

#Set up template vars and render the template
        template_vars = {
        "name": name,
        "advice": advice,
        }

        template = jinja_env.get_template('templates/results.html')
        self.response.write(template.render(template_vars))


app = webapp2.WSGIApplication([
    ('/', MainPage),

], debug = True)
