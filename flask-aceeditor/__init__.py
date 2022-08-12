from flask import *

#create a aceeditor class
class AceEditor(object):
    def __init__(self, app=None):
        if app != None:
            self.init_app(app)
    
    def init_app(self, app):
        if not hasattr(app, "extensions"):
            app.extensions = {}
        app.extensions["aceeditor"] = self
        app.jinja_env.globals["aceeditor"] = self
        app.jinja_env.globals["ace"] = self
        #peizhi
    
    @staticmethod
    def load(local = False):
        