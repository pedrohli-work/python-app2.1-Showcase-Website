# python-app2.1-Showcase-Website
Showcase Website with Email Contact Form is a modern, responsive web application built using Streamlit.

# Showcase Website with Streamlit

This is a simple **showcase website** created with [Streamlit](https://streamlit.io/) that displays team members from a CSV file and includes a contact form that sends emails using Gmail's SMTP service.

## ✨ Features

- Responsive three-column layout for displaying team members
- Form with email, topic selection, and message box
- Automatic email sending with SMTP over SSL
- Easy to customize with your own data (CSV and images)

## 🖼️ Screenshots

| Team Showcase | Contact Form |
|---------------|--------------|
| ![team](images/sample1.png) | ![form](images/sample2.png) |

## 🛠️ Technologies Used

- Python 3
- Streamlit
- pandas
- smtplib / ssl

## 📁 Project Structure


## 📧 Email Configuration

You must generate an **App Password** on your Google Account to use Gmail SMTP.

1. Enable 2FA on your Gmail
2. Go to: https://myaccount.google.com/apppasswords
3. Generate a new password for "Mail" and "Windows Computer"
4. Replace the `password` variable in `send_email.py` with your app password

> ⚠️ Never commit real passwords or secrets to your repository.

---

## 🚀 How to Run

```bash
pip install streamlit pandas
streamlit run app.py
