import smtplib
from email.message import EmailMessage
from string import Template  # 可以用變數去替代string裡的東西
from pathlib import Path  # 類似os.path

# read_text可以把東西讀成string
# 用Template再包起來方便之後用變數取代內容
html = Template(Path("index.html").read_text())

# email object
email = EmailMessage()
email["from"] = "handsome boy"
email["to"] = "weilee19960506@gmail.com"
email["subject"] = "I love you"
# content可以是任何型態，連html也可以
email.set_content("hi hi hi!")
# substitute可以用有多parameter，可以用dict去存
# set_context的第二個parameter可以寫是什麼型態的content
email.set_content(html.substitute({"name": "debby"}), "html")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    # smtp protocol的開頭是要一個hello message
    smtp.ehlo()
    # tls是一種加密
    smtp.starttls()
    # 登入(帳號密碼)
    # 這裡使用的密碼是app密碼，不是email的密碼
    # 可以到這邊看怎樣產生 https://support.google.com/accounts/answer/185833
    smtp.login("myclouddrive398@gmail.com", "fgtevjjukbubytak")
    # 把email object寄出
    smtp.send_message(email)
    print("all good")


