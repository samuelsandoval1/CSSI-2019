import webapp2
import jinja2
import os

env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('templates/start.html')
        self.response.write(template.render())

class RunHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('templates/run.html')
        self.response.write(template.render())

class TroubleHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('templates/trouble.html')
        self.response.write(template.render())

class GameoverHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('templates/gameover.html')
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/' , MainHandler),
    ('/run' , RunHandler),
    ('/trouble' , TroubleHandler),
    ('/gameover' , GameoverHandler),
], debug = True)
