from google_play_scraper import Sort, reviews_all
import pandas as pd
import time

print("--- 🚀 بداية البرنامج ---")
print("جاري الاتصال بمتجر جوجل وسحب البيانات... ⏳")
print("ملاحظة: هذه العملية قد تستغرق دقيقة أو دقيقتين حسب سرعة النت.. يرجى الانتظار")

# 1. إعدادات سحب البيانات لتطبيق InstaPay
app_id = 'com.egyptianbanks.instapay'

try:
    # 2. سحب جميع التعليقات
    result = reviews_all(
        app_id,
        sleep_milliseconds=0, 
        lang='ar', # اللغة العربية
        country='eg', # دولة مصر
        sort=Sort.NEWEST, # الأحدث
    )

    # 3. تحويل البيانات لجدول
    df = pd.DataFrame(result)

    # 4. اختيار الأعمدة المهمة
    df_clean = df[['userName', 'content', 'score', 'at', 'thumbsUpCount']]

    # 5. حفظ البيانات في ملف إكسيل
    filename = 'instapay_reviews.xlsx'
    df_clean.to_excel(filename, index=False)

    print("-" * 30)
    print(f"✅ تم بنجاح! تم سحب {len(df_clean)} تعليق.")
    print(f"📁 تم حفظ الملف باسم: {filename} في القائمة الجانبية.")

except Exception as e:
    print("❌ حدث خطأ:")
    print(e)