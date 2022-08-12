from flask import *


# create a aceeditor class
class AceEditor(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        if not hasattr(app, "extensions"):
            app.extensions = {}
        app.extensions["aceeditor"] = self
        app.jinja_env.globals["aceeditor"] = self
        app.jinja_env.globals["ace"] = self
        acebp = Blueprint('ace', __name__, static_folder="static", static_url_path="/ace" + app.static_url_path)
        app.register_blueprint(acebp)
        self.done = (False, False)

    @staticmethod
    def load():
        jzs = ["ace.min.js",
               "mode-python.min.js",
               "theme-monokai.min.js",
               "theme-xcode.min.js",
               "python.min.js",
               "ext-searchbox.min.js",
               "ext-language_tools.min.js",
               "ext-beautify.min.js",
               "jquery-3.6.0.min.js"
               ]
        tp = ('<script src="', '"></script>')
        jzjbs = []
        for i in jzs:
            jzjbs.append(tp[0] + url_for("ace.static", filenamee=i) + tp[1])
        wq = ""
        for i in jzjbs:
            wq = wq + i + "\n"
        return Markup(wq)

    @staticmethod
    def create(name="code", code="print('helloworld')"):
        a = '<pre id="content" style="height:415px"></pre><textarea name="' + name + '" id="' + name + \
            '''" class="code">''' + code + '''</textarea><button onclick="ghzt()">白天/黑夜</button><script>
var codek = document.getElementById("''' + name + '''");
var codes = codek.innerHTML;

var editor = ace.edit("content");
editor.setTheme('ace/theme/xcode');
let jsMode = ace.require('ace/mode/python').Mode;
editor.session.setMode(new jsMode());
editor.setFontSize(15);
editor.setValue(codes);
editor.moveCursorTo(0, 0);
ace.require("ace/ext/searchbox");
ace.require("ace/ext/language_tools");
ace.require("ace/ext/beautify");
editor.setOptions({
    enableBasicAutocompletion: true,
    enableSnippets: true,
    enableLiveAutocompletion: true
});

var textarea = $('textarea[name="''' + name + '''"]').hide();
editor.getSession().on('change', function(){
  textarea.val(editor.getSession().getValue());
});

var ztnum = 1;
function ghzt(){
    if (ztnum === 1){
        ztnum = 2;
        editor.setTheme('ace/theme/monokai');
    }else{
        ztnum = 1;
        editor.setTheme('ace/theme/xcode');
    }
}
</script>'''
        return Markup(a)
