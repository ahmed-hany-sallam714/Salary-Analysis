# ===========================================
# مشروع تحليل الرواتب حسب العمر، السنين، عدد الساعات، والإنجازات
# الهدف: عرض رسوم بيانية توضح العلاقة بين الرواتب ومجموعة من المتغيرات الزمنية والمهنية
# الأدوات المستخدمة: pandas, numpy, matplotlib
# ===========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ================== الرسم الأول ==================
# مقارنة بين الرواتب حسب العمر والسنة في نفس الرسم

x = [10, 20, 30, 40, 50, 60, 70]  # القيم المشتركة (تمثل أعمار أو سنوات)
y_age = [3300, 4500, 7600, 8300, 9400, 9900, 10900]  # الرواتب حسب العمر
y_year = [3390, 5500, 7900, 8700, 9300, 9000, 10900]  # الرواتب حسب السنة

fig, ax = plt.subplots(figsize=(8, 5))
ax.set_title("Salary Comparison: Age vs Year")
ax.set_xlabel("Age / Year")
ax.set_ylabel("Salary")
ax.plot(x, y_age, marker="o", linestyle="--", linewidth=3, color="red")  # خط الرواتب بالعمر
ax.plot(x, y_year, linewidth=3, color="blue")  # خط الرواتب بالسنة
ax.grid()
ax.legend(["Salary by Age", "Salary by Year"])  # وسيلة الإيضاح
plt.tight_layout()
plt.show()

# ================== الرسم الثاني ==================
# رسم مزدوج لمقارنة الرواتب بالعمر والسنوات بشكل منفصل

x1 = x
y1_age = [3900, 4500, 7800, 8300, 9400, 9900, 10000]
y1_year = [3390, 5500, 7900, 8700, 9300, 9000, 10900]

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 5), sharex=True)

# الرسم الخاص بالعمر
ax[0].set_title("Salary by Age")
ax[0].set_xlabel("Age")
ax[0].set_ylabel("Salary")
ax[0].plot(x1, y1_age, marker="o", linewidth=3, color="red")
ax[0].legend(["Age"])
ax[0].grid()

# الرسم الخاص بالسنوات
ax[1].set_title("Salary by Year")
ax[1].set_xlabel("Year")
ax[1].set_ylabel("Salary")
ax[1].plot(x1, y1_year, marker="o", linewidth=3, color="blue")
ax[1].legend(["Year"])
ax[1].grid()

plt.tight_layout()
plt.show()

# ================== الرسم الثالث ==================
# 4 رسوم في شبكة توضح الرواتب حسب العمر، السنة، عدد الساعات، والإنجازات

# بيانات الرواتب حسب كل متغير
y_by_age = [3900, 4500, 7800, 8300, 9400, 9900, 10000]
y_by_year = [3390, 5590, 7990, 8900, 9300, 9900, 10900]
y_by_hours = [3900, 5800, 7900, 8300, 9400, 9800, 10000]
y_by_achievements = [1234, 2356, 3456, 4567, 5679, 6874, 7345]

fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(10, 8), sharex=True)

# الرسم 1: حسب العمر
ax[0,0].set_title("Salary by Age")
ax[0,0].set_xlabel("Age")
ax[0,0].set_ylabel("Salary")
ax[0,0].plot(x, y_by_age, linewidth=3, color="blue", marker="o")
ax[0,0].legend(["Age"])
ax[0,0].grid()

# الرسم 2: حسب السنة
ax[0,1].set_title("Salary by Year")
ax[0,1].set_xlabel("Year")
ax[0,1].set_ylabel("Salary")
ax[0,1].plot(x, y_by_year, linewidth=3, color="red", marker="o")
ax[0,1].legend(["Year"])
ax[0,1].grid()

# الرسم 3: حسب عدد ساعات العمل
ax[1,0].set_title("Salary by Hours")
ax[1,0].set_xlabel("Hours")
ax[1,0].set_ylabel("Salary")
ax[1,0].plot(x, y_by_hours, linewidth=3, color="black", marker="o")
ax[1,0].legend(["Hours"])
ax[1,0].grid()

# الرسم 4: حسب عدد الإنجازات
ax[1,1].set_title("Salary by Achievements")
ax[1,1].set_xlabel("Achievements")
ax[1,1].set_ylabel("Salary")
ax[1,1].plot(x, y_by_achievements, linewidth=3, color="green", marker="o")
ax[1,1].legend(["Achievements"])
ax[1,1].grid()

plt.tight_layout()
fig.savefig("salaries.png")  # حفظ الرسم النهائي كصورة
plt.show()
