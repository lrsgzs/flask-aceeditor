# flask-aceeditor

## Because of this library (flask-aceeditor), it can be easily called when using the ace editor!

### Install

```shell
$ pip install flask-aceeditor
````

### use

````python
from flask_aceeditor import *
...
aceeditor = AceEditor(app)
````

#### Load js file

```html
...
{{ ace.load() }}<!--be sure to precede the code using the ace editor! ! ! -->
...
````

#### Create editor (with color change button)

```html
...
{{ ace.create(name="code", code="print('hello')") }}
<!-- name default is "code" code is code, default is "print('Hello World!')" -->
````

##### Note: When submitting the form, the field is the parameter name you passed in when you created it

## 因为这个库(flask-aceeditor)，所以在使用ace编辑器能很方便地调用了！

### 安装

```shell
$ pip install flask-aceeditor
```

### 使用

```python
from flask_aceeditor import *
...
aceeditor = AceEditor(app)
```

#### 加载js文件

```html
...
{{ ace.load() }}<!--一定要在使用ace编辑器的代码前面！！！-->
...
```

#### 创建编辑器（有颜色变换按钮）

```html
...
{{ ace.create(name="code", code="print('hello')") }}
<!-- name默认是"code" code是代码，默认是"print('Hello World!')" -->
```

##### 注：提交表单时，字段是你当时创建时传入的参数name