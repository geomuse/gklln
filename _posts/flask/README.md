下面是为期 **15 天的 Flask 教学课程规划表**，适合初学者循序渐进掌握 Flask 的基本用法、用户认证、RESTful API、数据库整合、部署等核心技能：

---

## 🧭 **Flask 15 天学习课程总览**

| 主题                      | 学习内容                              | 项目/练习               | 状态
| ----------------------- | --------------------------------- | --------------|----- |
| Flask 简介与环境搭建           | 安装 Flask，创建虚拟环境，Hello World 应用    | 第一个 Flask 项目        | ok
| 路由与视图函数                 | URL 路由、动态参数、返回 HTML               | 创建多个路由页面        | ok
| 模板引擎 Jinja2             | 使用 `render_template`，变量/控制语句      | 构建简单主页模板            | ok
| 表单与请求数据                 | `request` 对象，GET/POST 表单提交        | 简易留言板表单             | ok 
| 重定向与闪现消息                | `redirect`、`url_for`、`flash`      | 登录重定向示例             | ok
| 静态文件管理                  | 引入 CSS/JS/图片                      | 美化页面样式              | ok
| Blueprint 模块化           | 使用 `Blueprint` 进行模块化开发            | 分离用户与管理模块           |
| 数据库基础（Flask-SQLAlchemy） | 创建模型、增删查改、迁移      | 建立用户模型并操作数据库        |
| 数据库进阶（关系与查询）            | 一对多/多对多关系，复杂查询     | 用户与文章模型关联           |
| 用户注册与登录（Flask-WTF）      | 表单类、自定义验证器、提交表单     | 实现注册/登录功能           |
| 用户认证管理（Flask-Login）     | 登录状态保持、保护路由、登出                    | 用户认证系统              |
| RESTful API 基础          | 使用 `@app.route` 创建 API，返回 JSON    | 创建 `/api/posts` 接口  |
| 使用 Flask-RESTful        | 类视图方式构建 API，使用 `Resource`         | 完善 API 接口（GET/POST） |
| 错误处理与日志                 | `404`, `500` 自定义页面，日志记录           | 自定义错误页模板            |
| Flask 部署实战              | 使用 Gunicorn + Nginx 或 Render 平台部署 | 部署你的 Flask 项目       |

---

## 📘 教学材料建议

* **基础文档**：[Flask 官方文档](https://flask.palletsprojects.com/)
* **配套库**：

  * `Flask-WTF`: 表单处理
  * `Flask-Login`: 用户认证
  * `Flask-Migrate`: 数据库迁移
  * `Flask-RESTful`: 构建 REST API
  * `Flask-SQLAlchemy`: ORM 数据库管理

---

## 🔨 项目练习建议（贯穿式）

你可以在整个 15 天期间构建一个完整的博客或任务管理系统作为主线项目，功能包含：

* 用户注册与登录
* 发文/留言
* API 支持（供移动端使用）
* 管理后台
* 样式美化
* 最后部署上线

---

是否需要我为这个 15 天课程提供**每天的代码示范或教材讲解内容**？你可以说「开始 Day 1」，我就会一步一步带你学习。
