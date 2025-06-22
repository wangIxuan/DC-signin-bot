# Discord 出席機器人（部署於 Render）

## ✅ 功能簡介
- Discord 使用者輸入 `/出席`，會跳出 5 個按鈕（19:30、19:45、20:00、領土期間、無法出席）
- 點選後會將 Discord 名稱與時間傳送到 Google 表單
- 每個人只能簽到一次

## 🚀 Render 免費部署教學

### 1. 註冊 Render 帳號
- 前往 https://render.com 註冊帳號

### 2. 建立 Web Service
- 點選「New → Web Service」
- 上傳此專案 zip 或從 GitHub 部署
- 設定如下：
  - Environment: `Python`
  - Build Command: `pip install -r requirements.txt`
  - Start Command: `python keep_alive.py & python main.py`

### 3. 設定環境變數（Environment）
到 Render 後台 → Environment 分頁 → 新增這些變數：

| Key | Value |
|-----|-------|
| `DISCORD_TOKEN` | 你的 Discord Bot Token |
| `GOOGLE_FORM_URL` | 表單網址（formResponse） |
| `DISCORD_NAME_ENTRY` | entry.xxx 對應 Discord 名稱欄位 |
| `TIME_ENTRY` | entry.xxx 對應出席時間欄位 |

### 4. 上線完成！
Render 會自動啟動機器人，24 小時運作。

