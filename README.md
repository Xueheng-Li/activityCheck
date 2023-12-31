
![应用截图](https://xueheng.site:10001/-RF9kvmXtH7)

一个界面简洁的活动打卡网页应用。用户可以通过这个应用进行活动的添加、删除和插入操作，同时也可以查看所有的活动。

手机端浏览器显示界面友好。

## 文件结构

项目包含以下文件：

- `app.py`: 这是 Flask 应用的主文件，包含了所有的路由和视图函数。
- `csv_utils.py`: 这个文件包含了一些实用函数，用于读取和写入 CSV 文件，以及处理活动数据。
- `templates/index.html`: 这是应用的主页面模板，包含了各种表单用于添加、删除和插入活动，以及一个用于显示活动的表格。

## 如何运行

首先，你需要安装 Flask。你可以通过以下命令进行安装：

```bash
pip install flask
```

或者

```bash
pip install -r requirements.txt
```

然后，你可以通过运行 `app.py` 文件来启动应用：

```bash
python app.py
```

应用默认会在本地的 9093 端口运行。


