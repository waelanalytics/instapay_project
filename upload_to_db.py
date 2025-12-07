import pandas as pd
import mysql.connector

print("--- 🚀 بدء عملية نقل البيانات إلى قاعدة البيانات ---")

try:
    # 1. قراءة ملف الإكسيل
    print("1️⃣  جاري قراءة ملف البيانات (Excel)...")
    # تأكد أن اسم الملف هنا يطابق اسم الملف الموجود عندك
    df = pd.read_excel('instapay_reviews.xlsx')
    
    # تنظيف بسيط: تحويل التاريخ لنص لضمان قبوله في قاعدة البيانات
    df['at'] = df['at'].astype(str)
    # ملء أي خانات فارغة في النص
    df['content'] = df['content'].fillna('')
    df['userName'] = df['userName'].fillna('Unknown')

    # 2. الاتصال بقاعدة البيانات
    print("2️⃣  جاري الاتصال بـ MySQL...")
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",  # 👈 ضع كلمة مرور MySQL هنا
        database="InstaPay_Project",
        charset='utf8mb4'
    )
    cursor = conn.cursor()

    # 3. إدخال البيانات
    print("3️⃣  جاري إدخال البيانات (قد يستغرق دقيقة)...")
    
    sql = "INSERT INTO reviews (user_name, content, score, review_date, thumbs_up) VALUES (%s, %s, %s, %s, %s)"

    # عداد لمتابعة التقدم
    counter = 0
    
    for index, row in df.iterrows():
        val = (row['userName'], row['content'], row['score'], row['at'], row['thumbsUpCount'])
        cursor.execute(sql, val)
        counter += 1
        
        # طباعة رسالة كل 5000 صف
        if counter % 5000 == 0:
            print(f"   ⏳ تم إدخال {counter} صف...")

    conn.commit()
    print("-" * 30)
    print(f"✅ تمت العملية بنجاح! تم حفظ {counter} تعليق في قاعدة البيانات.")

    cursor.close()
    conn.close()

except mysql.connector.Error as err:
    print(f"❌ خطأ في MySQL: {err}")
    print("تأكد أن كلمة المرور صحيحة وأن اسم قاعدة البيانات InstaPay_Project موجود.")
except Exception as e:
    print(f"❌ حدث خطأ عام: {e}")