```python
from flask import Flask

app = Flask(_name_)

@app.route('/')
def home():
    return "ربات با موفقیت اجرا شد!"

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=10000)
```
