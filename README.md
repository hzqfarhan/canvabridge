# 📌 Canva → Telegram Webhook Forwarder (Flask)

**Short Description:**  
A Flask-based webhook receiver for Canva that forwards webhook events to a Telegram channel via the Telegram Bot API. Useful for real-time monitoring of Canva incidents or updates through Telegram.

---

## ✅ Features
- Receives Canva webhooks (JSON payload)
- Forwards messages to Telegram automatically
- HTML-safe formatting for clean Telegram output
- Simple Flask server; lightweight and fast
- Works on Render, Railway, Replit, VPS, and localhost

---

## 📌 Tech Stack
| Component | Purpose |
|-----------|---------|
| **Flask** | Web server handling webhook requests |
| **Telegram Bot API** | Sends messages to Telegram |
| **Python Requests** | API call to Telegram |
| **Render / Replit (optional)** | Hosting |

---

## 📌 Requirements (Install)
```sh
pip install flask requests
