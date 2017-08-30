import thu_learn
import pymysql
import time
import smtplib
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from html.parser import HTMLParser
from thu_learn import *
import time
offs=1
stop=1
while stop==1:
  name='fanyq15' ###学堂账号
  mima='Fan179175'###学堂密码
  mail='1004039684@qq.com'###接受邮箱（必须将发送邮箱设置为白名单）
  login(name,mima)
  semester = Semester(current=True)
  if offs==1:
    db = pymysql.connect("localhost","root","aa701022","system" )###数据库密码，账号，地址
    cursor = db.cursor()
    sql = "INSERT INTO people(name,mima,mail) VALUES ('%s', '%s', '%s')" %(name,mima,mail)
    try:
      cursor.execute(sql)
      db.commit()
    except:
      db.rollback()
    db.close()
    del cursor  
    del db
    
    
  for course in semester.courses:
       for message in course.messages:
          if offs==1:    
              d=message.details
              d=d.replace("\\","")
              d=d.replace("\'","")
              d=d.replace("\"","")
              d=d.replace("\a","")
              d=d.replace("\b","")
              d=d.replace("\f","")
              d=d.replace("\n","")
              d=d.replace("\r","")
              d=d.replace("\t","")
              d=d.replace("\v","")
              d=d.replace("\ooo","")
              d=d.replace("(","")   
              d=d.replace(")","")
              d=d.replace("（","")
              d=d.replace("）","")
              d=d.replace("'","")
              d=d.replace(";","")
              d=d.replace("‘","")
              d=d.replace("’","")
              d=d.replace("”","")
              d=d.replace("“","")
              db = pymysql.connect("localhost","root","aa701022","system",charset="utf8")###数据库密码，账号，地址
              cursor = db.cursor()
              sql2 = "INSERT INTO notice(name,title,class,contant) VALUES ('%s', '%s', '%s', '%s');" %(name,message.title,course.name,d)
              try:
                cursor.execute(sql2)
                db.commit()
              except:
                db.rollback()
              db.close()
              del cursor
              del db
          else:
              #stop=2
              d=message.details
              d=d.replace("\\","")
              d=d.replace("\'","")
              d=d.replace("\"","")
              d=d.replace("\a","")
              d=d.replace("\b","")
              d=d.replace("\f","")
              d=d.replace("\n","")
              d=d.replace("\r","")
              d=d.replace("\t","")
              d=d.replace("\v","")
              d=d.replace("\ooo","")
              d=d.replace("(","")   
              d=d.replace(")","")
              d=d.replace("（","")
              d=d.replace("）","")
              d=d.replace("'","")
              d=d.replace(";","")
              d=d.replace("‘","")
              d=d.replace("’","")
              d=d.replace("”","")
              d=d.replace("“","")
              db = pymysql.connect("localhost","root","aa701022","system",charset="utf8")###数据库密码，账号，地址
              cursor = db.cursor()
              sql3 = "SELECT * FROM notice  WHERE name='%s' AND class='%s' AND title='%s' AND contant='%s';" %(name,course.name,message.title,d)
              try:
                cursor.execute(sql3)
                results = cursor.fetchall()
                a=results.__str__()
                if a=="()":
                   db.close()
                   del cursor
                   del db 
                   db = pymysql.connect("localhost","root","aa701022","system",charset="utf8")###数据库密码，账号，地址
                   cursor = db.cursor()
                   localtime = time.asctime( time.localtime(time.time()) )
                   sql2 = "INSERT INTO notice(name,title,class,contant) VALUES ('%s', '%s', '%s', '%s');" %(name,message.title,course.name,d)
                   mail_in="%s，你好，这里有新的课程通知：\n\n课程名：%s\n\n通知标题：%s\n\n通知内容：%s\n\n\n\n%s"%(name,course.name,message.title,d,localtime)
                   msg = MIMEText(mail_in,'plain','utf-8')
                   from_addr = 'THU_notice@163.com'      ###发送邮件邮箱
                   password = 'aa701022'                 ###发送邮件密码
                   to_addr = '1004039684@qq.com'         ###接受邮箱
                   smtp_server = 'smtp.163.com'          ###smtp服务器地址
                   msg['From'] = from_addr
                   msg['To'] = to_addr
                   msg['Subject'] = '新的课程通知！'
                   server = smtplib.SMTP(smtp_server,25)
                   server.set_debuglevel(1)
                   server.login(from_addr,password)
                   server.sendmail(from_addr,[to_addr],msg.as_string())
                   server.quit()
                   try:
                     cursor.execute(sql2)
                     db.commit()
                   except:
                     db.rollback()
                   del sql2
              except:
                print ("Error: unable to fetch data")      
              db.close()
              del cursor
              del db 
              del sql3
  offs=2