import jinja2
import logging
import os
import webapp2

from google.appengine.ext import ndb
from google.appengine.api import users

#Step 1: Import jinja and os


#Step 1: Set up Jinja Environment
jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)
class Star(ndb.Model):
    """
    Add a few proprties and at least one moethod for movie stars
    """
    actname = ndb.StringProperty(required=True)
    age = ndb.IntegerProperty(required=False)
    oscars = ndb.IntegerProperty(required=True)
    city = ndb.StringProperty(required=False)


    def describe(self):
        """
        Return a string that has actor in a movie
        """
        return "%s is %d years old, has %d oscars, and from %s" % (self.actname, self.age, self.oscars, self.city)

        # template = jinja_env.get_template('templates/home.html')
        # self.response.write(template.render(template_vars))


        # #1. New hander for /populateDatabase
        #     adds a few movies and stars
        # #2 After adding redirect back to '/'


class Movie(ndb.Model):
        """
        title: String for Movie
        runtime: Number of minutes in movie
        rating: From 0 - 10
        """
        title = ndb.StringProperty(required=True)
        runtime = ndb.IntegerProperty(required=True)
        rating = ndb.FloatProperty(required=False, default=0)
        star_keys = ndb.KeyProperty(
            kind = Star,
            required=False,
            repeated=True)
        #def __init__(self, title, runtime, rating):
        #     self.title = title
        #     self.runtime = runtime
        #     self.rating = rating
        def describe(self):
            """
            Return a string describing this movie
            """
            return "%s is %d minute(s) long, with a rating of %f, with actors %s" % (self.title, self.runtime, self.rating, self.star_names)



class populateDatabase(webapp2.RequestHandler):
    def get(self):
        Movie.query().fetch()
        jakejohnson_key = Star(actname='Jake Johnson', age= 50, oscars=0).put()
        print jakejohnson_key.get()
        robdj_key = Star(actname='Robert Downey Jr', age=50, oscars=1).put()

        print robdj_key.get()

        shrek = Movie(
        title ='Shrek',
        runtime = 95,
        rating = 9.9,
        star_keys= [jakejohnson_key, robdj_key]
        )
        shrek.put()

        # print shrek.describe())        \put()
        print

        # spiderman = Movie(
        # title ='Spiderman',
        # runtime = 95,
        # rating = 8.5,
        # star_names= ['Toby Maguire', 'James Franco']
        # )
        # print spiderman.put()
        #
        # # print shrek.describe())        \put()
        # print Movie.query().fetch()
        #
        # keanu = Star(
        # name = 'Keanu Reeves',
        # age = 54,
        # # oscars = 4,)
        #
        # print keanu.put()
        # print Star.query().fetch()



        # actor = Star(
        # title ='Keanu Reeves',
        # age = 54,
        # rating = 8.5,
        #     )
        #     # print shrek.describe()
        # print actor.put()
        #
        # print Star.query().fetch()


        # avengers = Movie(
        # title ='Avengers: Endgame',
        # runtime = 180,
        # rating = 10,
        # # )
        # # # print avengers.describe()
        # avengers.put()
        #



        self.redirect("/")




"""
title: String for Movie
actor: String for actor name
]"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        movie_list = Movie.query().fetch()

        current_user = users.get_current_user()
        signin_link = users.create_login_url('/')


        template_vars = {
        'movies' : movie_list,
        'current_user' : current_user,
        'signin_link' : signin_link,
        }
        # star_list = Star.query().fetch()

        # oscars = {}
        # for star in star_list:
        #     oscars[star.actname] = star.oscars
        # print 'oscars is ', star.oscars


        for movie in movie_list:
            #print movie.list
            print "Title:", movie.title, "rating: ", movie.rating, "Actors: ", movie.star_keys,

            print "Movies", movie_list
            # print star_list

    #     for star in star_list:
    # #print movie.list
    #         print "Actor Name:", star.name, "age: ", star.age
    #
    #         print "Actors", star_list
        #TODO: Get star list from query and fetching
        #Loop through the star_list
        #Populate dictionary with star name and name of oscars



        template = jinja_env.get_template('templates/home.html')
        self.response.write(template.render(template_vars))



app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/populateDatabase', populateDatabase )
], debug = True)
