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
        self.app = app
        acebp = Blueprint('ace', __name__, static_folder="static", static_url_path="/ace" + app.static_url_path)
        app.register_blueprint(acebp)
        self.done = (False, False)
        #peizhi
    
    @staticmethod
    def setup(theme="drak", mode="python", exts=["searchbox", "language_tools", "beautify"]):
        if not self.done[0]:
            if theme =="drak":
                theme = "monokai"
            elif theme == "light":
                theme = "xcode"
            self.theme = theme
            self.mode =  mode
            self.exts = exts
    
    @staticmethod
    def load():
        if not self.done[0]:
            if "language_tools" in self.exts:
                self.opt = True
            else:
                self.opt = False
            self.done[0] = True
            extensions = []
            for i in self.exts:
                extensions = "ext-" + i + ".min.js"
            theme = "theme-" + self.theme + ".min.js"
            lang = self.mode + ".min.js"
            mode = "mode-" + self.mode + ".min.js"
            jq = "jquery-3.6.0.min.js"
            tp = ('<script src="', '"></script>')
            jzjbs = []
            jzs = extensions[:]
            jzs.extend([theme, lang, mode, jq])
            for i in jzs:
                jzjbs.append(tp[0] + urlfor("ace.static", filenamee=i) + tp[1])
            wq = ""
            for i in jzjbs:
                wq = wq + i + "\n"
            return Markup(wq)
        return ''
    
    @staticmethod
    def create(name="code", code="print('helloworld')"):
        if self.opt:
            opt = """editor.setOptions({
    enableBasicAutocompletion: true,
    enableSnippets: true,
    enableLiveAutocompletion: true
});"""
        extsccode = ""
        for i in sel.exts:
            extscode = extsccode + 'ace.require("ace/ext/' + i + '");\n'
        
        if not self.done[1]:
            a = '<pre id="content" style="height:415px"></pre><textarea name="' + name + '" id="code" class="code">' + code + '</textarea>'
            b = '<script>var codek = document.getElementById("' + name + '''");
var codes = codek.innerHTML;

var editor = ace.edit("content");
editor.setTheme('ace/theme/''' + self.theme + '''');
let jsMode = ace.require('ace/mode/''' + self.mode + '''').Mode;
editor.session.setMode(new jsMode());
editor.setFontSize(15);
editor.setValue(codes);
editor.moveCursorTo(0, 0);


''' + extscode + opt + '''

var textarea = $('textarea[name="''' + name + '''"]').hide();
editor.getSession().on('change', function(){
  textarea.val(editor.getSession().getValue());
});</script>'''
            return Markup(a + "\n" + b)
        return ''