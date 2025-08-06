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
| Blueprint 模块化           | 使用 `Blueprint` 进行模块化开发            | 分离用户与管理模块           | no
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
明白了！你希望從 **資料庫與 SQLAlchemy 教學開始，不需再講 Flask 基礎（如路由、模板等）**，那我們將課程聚焦於 **Flask + SQLAlchemy 資料模型、資料操作、登入驗證與進階資料關聯**。

---

## ✅ 教學前提假設：

* 你已具備 Flask 開發基本概念（例如 `route`, `render_template`, `request`, `blueprint`）
* 開發環境已安裝好 `Flask`，接下來從安裝並使用 `Flask-SQLAlchemy` 開始

---

# 🧠 Flask-SQLAlchemy & 資料庫開發：15 天課程規劃

---

### 🗓️ Day 1：環境與 SQLAlchemy 安裝設定

* 安裝 `Flask-SQLAlchemy`
* 設定 `SQLALCHEMY_DATABASE_URI`
* 使用 SQLite 作為開發資料庫
* 初始化 `db = SQLAlchemy(app)`
* 建立 `models.py` 模型檔案

---

### 🗓️ Day 2：建立基本資料模型（User）

* 定義 User 模型：`id`, `username`, `password`
* 欄位類型說明：`Integer`, `String`, `Boolean`, `DateTime`
* 使用 `db.create_all()` 建立資料表
* 建立與使用開發用資料庫 `data.db`

---

### 🗓️ Day 3：建立初始資料（Create）

* 透過表單新增 User 資料
* 寫入資料庫的步驟：

  ```python
  user = User(username="jack", password="1234")
  db.session.add(user)
  db.session.commit()
  ```
* 錯誤處理與重複帳號防呆
* Flash 成功與失敗訊息

---

### 🗓️ Day 4：查詢資料（Read）

* 使用 `.query.all()` 取得全部使用者
* `.query.filter_by()` 與 `.query.get()`
* 用迴圈在 HTML 顯示所有使用者
* 排序：`order_by(User.username.desc())`

---

### 🗓️ Day 5：修改資料（Update）

* 找出特定使用者 `.query.get(id)`
* 修改使用者密碼
* `db.session.commit()` 更新資料
* 製作 `/edit/<id>` 編輯頁面

---

### 🗓️ Day 6：刪除資料（Delete）

* `.query.get(id)` 找人
* `db.session.delete(user)`
* `db.session.commit()`
* 在 `/users` 頁面為每位使用者加上刪除按鈕

---

### 🗓️ Day 7：擴展欄位與時間戳

* 在 User 模型中加入 `email` 與 `created_at`
* 使用 `datetime.utcnow()` 記錄註冊時間
* 顯示人性化時間：`{{ user.created_at.strftime('%Y-%m-%d') }}`

---

### 🗓️ Day 8：資料驗證（簡易）

* 手動檢查 `username`, `password` 是否為空
* 手動檢查 `email` 格式
* 只用 Python 做基本驗證（進階留給 Flask-WTF）

---

### 🗓️ Day 9：模型方法與封裝邏輯

* 在 User 類中加入方法，如：

  ```python
  def check_password(self, pwd):
      return self.password == pwd
  ```
* 可讀性強，可供登入驗證使用
* 讓資料操作更物件導向

---

### 🗓️ Day 10：登入邏輯實作

* 表單送出後查詢使用者：

  ```python
  user = User.query.filter_by(username=form.username.data).first()
  ```
* 比對密碼正確性
* 正確則導向儀表板，否則 flash 錯誤訊息

---

### 🗓️ Day 11：使用 Flask-Login 登入保護

* 安裝並初始化 `Flask-Login`
* 建立 `UserMixin` 繼承
* 建立 `login_user()`, `logout_user()`, `login_required`
* 使用者登入狀態持續保留

---

### 🗓️ Day 12：註冊與登入整合

* 將註冊資料寫入資料庫
* 註冊成功後自動登入或導向登入頁
* 登入後導向 `/dashboard`
* 登出後導向 `/`

---

### 🗓️ Day 13：資料關聯設計（一對多）

* 建立 `Post` 模型，與 `User` 做一對多
* User → 多篇文章
* ForeignKey 建立關聯：`user_id = db.Column(db.Integer, db.ForeignKey('user.id'))`

---

### 🗓️ Day 14：資料關聯操作與顯示

* 使用 `user.posts` 取得該使用者文章
* 用 `post.user.username` 反查作者
* 在文章列表顯示作者名稱與建立時間

---

### 🗓️ Day 15：整合小專案 – 使用者系統 + 部落格

整合項目：

* 註冊、登入、登出
* 使用者列表、刪除使用者
* 使用者可發文
* 每篇文章顯示作者與時間
* 儀表板僅限登入者瀏覽（用 `@login_required`）

---

## 📘 總結：你將學會

* Flask-SQLAlchemy 完整操作流程
* ORM 的概念與應用
* 建立與使用多種模型（User / Post 等）
* 資料關聯（ForeignKey 與 relationship）
* 製作登入系統與會員管理功能
* 基礎部落格/留言板實作

---

需要我從 **Day 1（SQLAlchemy 安裝與設定）** 開始詳細講解嗎？
你也可以說：「請開始 Day 1」或「給我 Day 1 教材」。我會一步步幫你建立完整後端資料庫操作能力。

