1. Auth (app_auth)

POST /auth/login/ – Kirish
POST /auth/logout/ – Chiqish
POST /auth/change-password/ – Parolni o‘zgartirish
POST /auth/reset-password/ – Parolni tiklash (OTP orqali)
GET /auth/me/ – Hozirgi foydalanuvchi ma’lumotlarini olish

2. Users (app_users)

GET /users/ – Barcha foydalanuvchilar ro‘yxati
GET /users/{id}/ – Foydalanuvchi ma’lumotlarini olish
POST /users/create/ – Yangi foydalanuvchi yaratish (Admin tomonidan)
PUT /users/{id}/update/ – Foydalanuvchi ma’lumotlarini yangilash
DELETE /users/{id}/delete/ – Foydalanuvchini o‘chirish

3. Courses & Groups (app_courses)

GET /courses/ – Barcha kurslar
GET /courses/{id}/ – Kurs tafsilotlari
POST /courses/create/ – Yangi kurs yaratish
PUT /courses/{id}/update/ – Kurs ma’lumotlarini o‘zgartirish
DELETE /courses/{id}/delete/ – Kursni o‘chirish

GET /groups/ – Barcha guruhlar
GET /groups/{id}/ – Guruh tafsilotlari
POST /groups/create/ – Yangi guruh yaratish
POST /groups/{id}/add-student/ – Talabani guruhga qo‘shish
DELETE /groups/{id}/remove-student/ – Talabani guruhdan chiqarish

4. Payments (app_payments)

GET /payments/ – Barcha to‘lovlar
GET /payments/{id}/ – To‘lov tafsilotlari
POST /payments/create/ – Yangi to‘lov qilish
GET /payments/student/{id}/ – Talabaning barcha to‘lovlari

5. Attendance & Grades (app_attendance)

GET /attendance/ – Barcha davomat ma’lumotlari
GET /attendance/{id}/ – Talabaning davomat tafsilotlari
POST /attendance/mark/ – Talabaning davomatini belgilash

GET /grades/ – Barcha baholar
GET /grades/{id}/ – Talabaning baholari
POST /grades/add/ – Yangi baho qo‘shish
PUT /grades/{id}/update/ – Baho o‘zgartirish

6. Statistics (app_statistics)

Foydalanuvchi statistikasi
GET /statistics/users/ – Jami foydalanuvchilar statistikasi (nechta admin, worker, student bor)
GET /statistics/users/{id}/ – Foydalanuvchining shaxsiy statistikasi

Kurs va guruh statistikasi
GET /statistics/courses/ – Eng ommabop kurslar, eng ko‘p o‘quvchi yozilgan kurslar
GET /statistics/groups/ – Guruhlar soni, faol guruhlar, bekor qilingan guruhlar
GET /statistics/groups/{id}/attendance/ – Guruhning o‘rtacha davomat statistikasi

Talabalar statistikasi
GET /statistics/students/top/ – Eng yuqori baholarga ega talabalar
GET /statistics/students/attendance/ – Eng ko‘p dars qoldirgan talabalar

Davomat va baho statistikasi
GET /statistics/attendance/ – Jami davomat statistikasi (necha foiz darsga qatnashgan)
GET /statistics/attendance/{id}/ – Talabaning o‘rtacha davomat foizi
GET /statistics/grades/ – O‘rtacha baholar statistikasi

To‘lov statistikasi
GET /statistics/payments/ – Umumiy tushum, eng ko‘p to‘lov qilingan oy
GET /statistics/payments/debtors/ – Qarzdor talabalar ro‘yxati