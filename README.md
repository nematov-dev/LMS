# API Endpoints

## 1. Auth (app_auth)

### Login
**Endpoint:** `POST /auth/login/`  
**Description:** Kirish.  

### Logout
**Endpoint:** `POST /auth/logout/`  
**Description:** Chiqish.  

### Change Password
**Endpoint:** `POST /auth/change-password/`  
**Description:** Parolni o‘zgartirish.  

### Reset Password
**Endpoint:** `POST /auth/reset-password/`  
**Description:** Parolni tiklash (OTP yuboradi).

### OTP verify
**Endpoint:** `POST /auth/verify-otp/`  
**Description:** OTP ni tasdiqlash.

### Set new password
**Endpoint:** `POST /auth/set-new-password/`  
**Description:** Yangi parolni saqlash.

### Get Current User
**Endpoint:** `GET /auth/me/`  
**Description:** Hozirgi foydalanuvchi ma’lumotlarini olish.  

### Token Refresh
**Endpoint:** `POST /auth/token/refresh/`  
**Description:** JWT yangilash . 

---

## 2. Users (app_users)

### Get All Users
**Endpoint:** `GET /users/`  
**Description:** Barcha foydalanuvchilar ro‘yxatini olish.  

### Get Single User
**Endpoint:** `GET /user/{id}/`  
**Description:** Foydalanuvchi ma’lumotlarini olish.  

### Create User
**Endpoint:** `POST /users/create/user/`  
**Description:** Yangi foydalanuvchi yaratish (Admin tomonidan).  

### Update User
**Endpoint:** `PUT users/update/user/{id}/`  
**Description:** Foydalanuvchi ma’lumotlarini yangilash.  

### Delete User
**Endpoint:** `DELETE /users/delete/user/{id}/`  
**Description:** Foydalanuvchini o‘chirish.  

### Workers

#### Get All Workers
**Endpoint:** `GET /users/workers/`  
**Description:** Barcha workerlar ro‘yxati.  

#### Get Single Worker
**Endpoint:** `GET /users/worker/{id}/`  
**Description:** Bitta worker ma’lumotlari.  

#### Create Worker
**Endpoint:** `POST /users/workers/create/`  
**Description:** Yangi worker yaratish.  

#### Update Worker
**Endpoint:** `PUT /users/workers/{id}/update/`  
**Description:** Worker ma’lumotlarini o‘zgartirish.  

### Teachers

#### Get All Teachers
**Endpoint:** `GET /users/teachers/`  
**Description:** Barcha o‘qituvchilar ro‘yxatini olish.  

#### Get Single Teacher
**Endpoint:** `GET /users/teacher/{id}/`  
**Description:** Bitta o‘qituvchi ma’lumotlarini olish.  

#### Create Teacher
**Endpoint:** `POST /users/create/teacher/`  
**Description:** Yangi o‘qituvchi yaratish.  

#### Update Teacher
**Endpoint:** `PUT /users/update/teacher/{id}/`  
**Description:** O‘qituvchi ma’lumotlarini yangilash.  

### Students

#### Get All Students
**Endpoint:** `GET /users/students/`  
**Description:** Barcha talabalar ro‘yxatini olish.  

#### Get Single Student
**Endpoint:** `GET /users/student/{id}/`  
**Description:** Bitta talaba ma’lumotlarini olish.  

#### Create Student
**Endpoint:** `POST /users/create/student/`  
**Description:** Yangi talaba yaratish.  

#### Update Student
**Endpoint:** `PUT /users/update/student/{id}/`  
**Description:** Talaba ma’lumotlarini yangilash.  

---

## 3. Departments

### Get All Departments
**Endpoint:** `GET users/departments/`  
**Description:** Barcha bo‘limlar ro‘yxatini olish.  

### Get Single Department
**Endpoint:** `GET users/departments/{id}/`  
**Description:** Bitta bo‘lim ma’lumotlarini olish.  

### Create Department
**Endpoint:** `POST /users/departments/create/department/`  
**Description:** Yangi bo‘lim yaratish.  

### Update Department
**Endpoint:** `PUT /users/departments/{id}/update/department/`  
**Description:** Bo‘lim ma’lumotlarini yangilash.

### Delete Department
**Endpoint:** `DELETE /users/departments/{id}/delete/department/`  
**Description:** Bo‘lim ma’lumotlarini o'chirish.

### Department add Worker
**Endpoint:** `POST /users/departments/{id}/add-worker/`  
**Description:** Bo‘limga worker qo'shish.

---

## 4. Courses & Groups (app_courses)

### Courses

#### Get All Courses
**Endpoint:** `GET /courses/`  
**Description:** Barcha kurslar ro‘yxatini olish.  

#### Get Course Details
**Endpoint:** `GET /courses/{id}/`  
**Description:** Kurs tafsilotlarini olish.  

#### Create Course
**Endpoint:** `POST /courses/create/`  
**Description:** Yangi kurs yaratish.  

#### Update Course
**Endpoint:** `PUT /courses/{id}/update/`  
**Description:** Kurs ma’lumotlarini o‘zgartirish.  

#### Delete Course
**Endpoint:** `DELETE /courses/{id}/delete/`  
**Description:** Kursni o‘chirish.  

### Groups

#### Get All Groups
**Endpoint:** `GET /groups/`  
**Description:** Barcha guruhlar ro‘yxatini olish.  

#### Get Group Details
**Endpoint:** `GET /groups/{id}/`  
**Description:** Guruh tafsilotlarini olish.  

#### Create Group
**Endpoint:** `POST /groups/create/`  
**Description:** Yangi guruh yaratish.  

#### Add Student to Group
**Endpoint:** `POST /groups/{id}/add-student/`  
**Description:** Talabani guruhga qo‘shish.  

#### Remove Student from Group
**Endpoint:** `DELETE /groups/{id}/remove-student/`  
**Description:** Talabani guruhdan chiqarish.  

---

## 5. Payments (app_payments)

### Get All Payments
**Endpoint:** `GET /payments/`  
**Description:** Barcha to‘lovlar.  

### Get Payment Details
**Endpoint:** `GET /payments/{id}/`  
**Description:** To‘lov tafsilotlari.  

### Create Payment
**Endpoint:** `POST /payments/create/`  
**Description:** Yangi to‘lov qilish.  

### Get Student Payments
**Endpoint:** `GET /payments/student/{id}/`  
**Description:** Talabaning barcha to‘lovlari.  

---

## 6. Attendance & Grades (app_attendance)

### Attendance

#### Get All Attendance
**Endpoint:** `GET /attendance/`  
**Description:** Barcha davomat ma’lumotlari.  

#### Get Student Attendance
**Endpoint:** `GET /attendance/{id}/`  
**Description:** Talabaning davomat tafsilotlari.  

#### Mark Attendance
**Endpoint:** `POST /attendance/mark/`  
**Description:** Talabaning davomatini belgilash.  

### Grades

#### Get All Grades
**Endpoint:** `GET /grades/`  
**Description:** Barcha baholar.  

#### Get Student Grades
**Endpoint:** `GET /grades/{id}/`  
**Description:** Talabaning baholari.  

#### Add Grade
**Endpoint:** `POST /grades/add/`  
**Description:** Yangi baho qo‘shish.  

#### Update Grade
**Endpoint:** `PUT /grades/{id}/update/`  
**Description:** Baho o‘zgartirish.