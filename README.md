# API Documentation

### Authentication APIs

- **POST** `/auth/login/` - Authenticate user and return access token.
- **POST** `/auth/logout/` - Logout user by invalidating the token.
- **GET** `/auth/me/` - Retrieve logged-in user information.
- **POST** `/auth/change-password/` - Change user password.
- **POST** `/auth/reset-password/` - Request password reset.
- **POST** `/auth/verify-otp/` - Verify OTP for rest-password.
- **POST** `/auth/set-new-password/` - Set a new password after reset.
- **POST** `/auth/token/refresh/` - Refresh authentication token.

---

## Users APIs

### User Management

- **GET** `/users/` - List all users.
- **POST** `/users/create/student/` - Create a new student.
- **POST** `/users/create/teacher/` - Create a new teacher.
- **POST** `/users/create/superuser/` - Create a new superuser.
- **POST** `/users/create/user/` - Create a new user.
- **DELETE** `/users/delete/user/{id}/` - Delete user.

### Student Management

- **GET** `/users/students/` - List all students.
- **GET** `/users/student/{id}/` - Get student details.
- **PUT** `/users/update/student/{id}/` - Update student.
- **POST** `/users/get-students-by-ids/` - Get students by IDs.
- **GET** `/student-groups/{student_id}/` - Retrieves the list of groups that a specific student is enrolled in.

### Teacher Management

- **GET** `/users/teachers/` - List all teachers.
- **GET** `/users/teacher/{id}/` - Get teacher details.
- **PUT** `/users/update/teacher/{id}/` - Update teacher.
- **POST** `/users/get-teachers-by-ids/` - Get teachers by IDs.
- **GET** `/teacher-groups/{teacher_id}/` - Retrieves the list of groups that a specific teacher is enrolled in.

---

### Attendance APIs

- **GET** `/attendances/attendance/` - Retrieve all attendance.
- **POST** `/attendances/attendance/create/attendance/` - Create a new attendance.
- **GET** `/attendances/attendance/{id}/` - Retrieve attendance details by ID.
- **DELETE** `/attendances/attendance/{id}/delete/attendance/` - Delete an attendance.
- **PUT** `/attendances/attendance/{id}/update/attendance/` - Update an attendance.

### Attendance Status APIs

- **GET** `/attendances/status/` - List all statuses.
- **POST** `/attendances/status/create/status/` - Create new status.
- **GET** `/attendances/status/{id}/` - Get status details.
- **DELETE** `/attendances/status/{id}/delete/status/` - Delete status.
- **PUT** `/attendances/status/{id}/update/status/` - Update status.

---

### Courses APIs

- **GET** `/courses/courses/` - List all courses.
- **POST** `/courses/courses/create/course/` - Create a new course.
- **GET** `/courses/courses/{id}/` - Get course details.
- **DELETE** `/courses/courses/{id}/delete/course/` - Delete a course.
- **PUT** `/courses/courses/{id}/update/course/` - Update course.
- **POST** `/courses/get-groups-by-ids/` - Get groups by IDs.

### Groups APIs

- **GET** `/courses/groups/` - List all groups.
- **POST** `/courses/groups/create/group/` - Create a new group.
- **GET** `/courses/groups/{id}/` - Get group details.
- **POST** `/courses/groups/{id}/add-student/` - Add student to group.
- **POST** `/courses/groups/{id}/add-teacher/` - Add teacher to group.
- **DELETE** `/courses/groups/{id}/delete/group/` - Delete group.
- **POST** `/courses/groups/{id}/remove-student/` - Remove student from group.
- **POST** `/courses/groups/{id}/remove-teacher/` - Remove teacher from group.
- **PUT** `/courses/groups/{id}/update/group/` - Update group.

### Homework Reviews 

- **GET** `/courses/homework-reviews/` - List all homework reviews.
- **POST** `/courses/homework-reviews/create/homework-review/` - Create a new homework review.
- **GET** `/courses/homework-reviews/{id}/` - Get homework review details.
- **DELETE** `/courses/homework-reviews/{id}/delete/homework-review/` - Delete homework review.
- **PUT** `/courses/homework-reviews/{id}/update/homework-review/` - Update homework review.

### Homework Submissions

- **GET** `/courses/homework-submissions/` - List all homework submissions.
- **POST** `/courses/homework-submissions/create/homework-submission/` - Create a new homework submission.
- **GET** `/courses/homework-submissions/{id}/` - Get homework submission details.
- **DELETE** `/courses/homework-submissions/{id}/delete/homework-submission/` - Delete homework submission.
- **PUT** `/courses/homework-submissions/{id}/update/homework-submission/` - Update homework submission.

### Homeworks

- **GET** `/courses/homeworks/` - List all homeworks.
- **POST** `/courses/homeworks/create/homework/` - Create a new homework.
- **GET** `/courses/homeworks/{id}/` - Get homework details.
- **DELETE** `/courses/homeworks/{id}/delete/homework/` - Delete homework.
- **PUT** `/courses/homeworks/{id}/update/homework/` - Update homework.

### Subjects

- **GET** `/courses/subjects/` - List all subjects.
- **POST** `/courses/subjects/create/subject/` - Create a new subject.
- **GET** `/courses/subjects/{id}/` - Get subject details.
- **DELETE** `/courses/subjects/{id}/delete/subject/` - Delete subject.
- **PUT** `/courses/subjects/{id}/update/subject/` - Update subject.

### Table Types

- **GET** `/courses/table-types/` - List all table types.
- **POST** `/courses/table-types/create/tabletype/` - Create a new table type.
- **GET** `/courses/table-types/{id}/` - Get table type details.
- **DELETE** `/courses/table-types/{id}/delete/tabletype/` - Delete table type.
- **PUT** `/courses/table-types/{id}/update/tabletype/` - Update table type.

### Tables

- **GET** `/courses/tables/` - List all tables.
- **POST** `/courses/tables/create/table/` - Create a new table.
- **GET** `/courses/tables/{id}/` - Get table details.
- **DELETE** `/courses/tables/{id}/delete/table/` - Delete table.
- **PUT** `/courses/tables/{id}/update/table/` - Update table.

---

### Payments APIs

- **GET** `/payments/payment/` - List all payments.
- **POST** `/payments/payment/create/payment/` - Create a new payment.
- **GET** `/payments/payment/{id}/` - Get payment details.
- **DELETE** `/payments/payment/{id}/delete/payment/` - Delete a payment.
- **PUT** `/payments/payment/{id}/update/payment/` - Update payment details.

### Payment Types

- **GET** `/payments/payment-type/` - List payment types.
- **POST** `/payments/payment-type/create/payment-type/` - Create new payment type.
- **GET** `/payments/payment-type/{id}/` - Get payment type details.
- **DELETE** `/payments/payment-type/{id}/delete/payment-type/` - Delete payment type.
- **PUT** `/payments/payment-type/{id}/update/payment-type/` - Update payment type.

---

### Statistics APIs

#### Attendance Statistics
- **GET** `/statistics/attendance-statistics/` - Get attendance statistics.

#### Courses Statistics
- **GET** `/statistics/courses-statistics/` - Get courses statistics.

#### Groups Statistics 
- **GET** `/statistics/groups-statistics/` - Get group statistics.

#### Payments Statistics
- **GET** `/statistics/payments-statistics/` - Get payments statistics.

#### Students Statistics
- **GET** `/statistics/students-statistic/` - Get students statistics.

#### Teachers Statistics
- **GET** `/statistics/teachers-statistic/` - Get teachers statistics.

---

## Notes

- `{id}` should be replaced with the actual ID of the resource.
- Use appropriate HTTP methods (GET, POST, PUT, DELETE) as per the endpoint.
- Ensure authentication for protected routes.

---

## Contact

For further questions, contact the developer nematov.uz

