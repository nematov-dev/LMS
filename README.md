# 🎓 [LMS](https://s-lms.uz) API Documentation

## Short Description
Comprehensive RESTful API for managing users, students, teachers, courses, attendance, payments, and statistics in a learning management system (LMS).

---

## 📌 Authentication APIs

- **POST** `/auth/login/` – Authenticate user and return access token.
- **POST** `/auth/logout/` – Logout user by invalidating the token.
- **GET** `/auth/me/` – Retrieve logged-in user information.
- **POST** `/auth/change-password/` – Change user password.
- **POST** `/auth/reset-password/` – Request password reset.
- **POST** `/auth/verify-otp/` – Verify OTP for password reset.
- **POST** `/auth/set-new-password/` – Set a new password after reset.
- **POST** `/auth/token/refresh/` – Refresh authentication token.

---

## 👤 Users APIs

### User Management
- **GET** `/users/` – List all users.
- **POST** `/users/create/student/` – Create a new student.
- **POST** `/users/create/teacher/` – Create a new teacher.
- **POST** `/users/create/superuser/` – Create a new superuser.
- **POST** `/users/create/user/` – Create a new user.
- **DELETE** `/users/delete/user/{id}/` – Delete user.

### Student Management
- **GET** `/users/students/` – List all students.
- **GET** `/users/student/{id}/` – Get student details.
- **PUT** `/users/update/student/{id}/` – Update student.
- **POST** `/users/get-students-by-ids/` – Get students by IDs.
- **GET** `/student-groups/{student_id}/` – List groups a student belongs to.
- **GET** `/api/v1/attendance/student/{student_id}/` – Retrieve student attendance grouped by months.

### Teacher Management
- **GET** `/users/teachers/` – List all teachers.
- **GET** `/users/teacher/{id}/` – Get teacher details.
- **PUT** `/users/update/teacher/{id}/` – Update teacher.
- **POST** `/users/get-teachers-by-ids/` – Get teachers by IDs.
- **GET** `/teacher-groups/{teacher_id}/` – List groups a teacher belongs to.
- **GET** `/teacher-group/{teacher_id}/{group_id}/` – Retrieve information about a specific teacher's group.

---

## 📚 Courses & Groups APIs

- **GET** `/courses/courses/` – List all courses.
- **POST** `/courses/courses/create/course/` – Create a new course.
- **GET** `/courses/courses/{id}/` – Get course details.
- **PUT** `/courses/courses/{id}/update/course/` – Update course.
- **DELETE** `/courses/courses/{id}/delete/course/` – Delete course.
- **POST** `/courses/get-groups-by-ids/` – Get groups by IDs.

### Groups
- **GET** `/courses/groups/` – List all groups.
- **POST** `/courses/groups/create/group/` – Create a new group.
- **GET** `/courses/groups/{id}/` – Get group details.
- **PUT** `/courses/groups/{id}/update/group/` – Update group.
- **DELETE** `/courses/groups/{id}/delete/group/` – Delete group.
- **POST** `/courses/groups/{id}/add-student/` – Add student to group.
- **POST** `/courses/groups/{id}/add-teacher/` – Add teacher to group.
- **POST** `/courses/groups/{id}/remove-student/` – Remove student from group.
- **POST** `/courses/groups/{id}/remove-teacher/` – Remove teacher from group.

---

## 📝 Homework APIs

- **Homeworks**: `/courses/homeworks/`
- **Homework Reviews**: `/courses/homework-reviews/`
- **Homework Submissions**: `/courses/homework-submissions/`

*(Use standard GET, POST, PUT, DELETE methods for each resource.)*

---

## 💰 Payments APIs

- **Payments**: `/payments/payment/`
- **Payment Types**: `/payments/payment-type/`

---

## 📊 Statistics APIs

- **Attendance Statistics**: `/statistics/attendance-statistics/`
- **Courses Statistics**: `/statistics/courses-statistics/`
- **Groups Statistics**: `/statistics/groups-statistics/`
- **Payments Statistics**: `/statistics/payments-statistics/`
- **Students Statistics**: `/statistics/students-statistic/`
- **Teachers Statistics**: `/statistics/teachers-statistic/`

---

## ⚠️ Notes

- Replace `{id}` with the actual resource ID.
- Use appropriate HTTP methods (GET, POST, PUT, DELETE) per endpoint.
- Authentication required for protected routes.

---

## 🚀 How to Use

1. Use an API client (Postman, Insomnia) to make requests.
2. Obtain an access token via `/auth/login/`.
3. Include `Authorization: Bearer <token>` header for protected endpoints.
4. Follow the endpoint paths as listed above for your desired operations.

---


## 🧑🏻‍💻 Developer

- [Saidakbar Nematov](https://nematov.uz)
---

## 📄 License

This API is intended for educational and development purposes.

---

