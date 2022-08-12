# flask-aceeditor

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
{{ ace.create(name="code") }}<!-- name默认是"code" -->
```

##### 注：提交表单时，字段是你当时创建时传入的参数name