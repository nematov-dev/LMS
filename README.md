# API Documentation

## Authentication APIs

### Change Password

**POST** `/auth/change-password/`

- Change user password.

### Login

**POST** `/auth/login/`

- Authenticate user and return access token.

### Logout

**POST** `/auth/logout/`

- Logout user by invalidating the token.

### Get User Info

**GET** `/auth/me/`

- Retrieve logged-in user information.

### Reset Password

**POST** `/auth/reset-password/`

- Request password reset.

### Set New Password

**POST** `/auth/set-new-password/`

- Set a new password after reset.

### Refresh Token

**POST** `/auth/token/refresh/`

- Refresh authentication token.

### Verify OTP

**POST** `/auth/verify-otp/`

- Verify OTP for authentication.

---

## Attendance APIs

### List Attendances

**GET** `/attendances/attendance/`

- Retrieve all attendance records.

### Create Attendance

**POST** `/attendances/attendance/create/attendance/`

- Create a new attendance record.

### Retrieve Attendance by ID

**GET** `/attendances/attendance/{id}/`

- Retrieve attendance details by ID.

### Delete Attendance

**DELETE** `/attendances/attendance/{id}/delete/attendance/`

- Delete an attendance record.

### Update Attendance

**PUT** `/attendances/attendance/{id}/update/attendance/`

- Update an attendance record.

### Attendance Status APIs

- **GET** `/attendances/status/` - List all statuses.
- **POST** `/attendances/status/create/status/` - Create new status.
- **GET** `/attendances/status/{id}/` - Get status details.
- **DELETE** `/attendances/status/{id}/delete/status/` - Delete status.
- **PUT** `/attendances/status/{id}/update/status/` - Update status.

---

## Courses APIs

### Courses

- **GET** `/courses/courses/` - List all courses.
- **POST** `/courses/courses/create/course/` - Create a new course.
- **GET** `/courses/courses/{id}/` - Get course details.
- **DELETE** `/courses/courses/{id}/delete/course/` - Delete a course.
- **PUT** `/courses/courses/{id}/update/course/` - Update course.

### Groups

- **GET** `/courses/groups/` - List all groups.
- **POST** `/courses/groups/create/group/` - Create a new group.
- **GET** `/courses/groups/{id}/` - Get group details.
- **POST** `/courses/groups/{id}/add-student/` - Add student to group.
- **POST** `/courses/groups/{id}/add-teacher/` - Add teacher to group.
- **DELETE** `/courses/groups/{id}/delete/group/` - Delete group.
- **POST** `/courses/groups/{id}/remove-student/` - Remove student from group.
- **POST** `/courses/groups/{id}/remove-teacher/` - Remove teacher from group.
- **PUT** `/courses/groups/{id}/update/group/` - Update group.

---

## Payments APIs

### Payment Management

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

## Statistics APIs

### Attendance Statistics

**GET** `/statistics/attendance-statistics/`

- Get attendance statistics.

### Courses Statistics

**GET** `/statistics/courses-statistics/`

- Get courses statistics.

### Groups Statistics

**GET** `/statistics/groups-statistics/`

- Get group statistics.

### Payments Statistics

**GET** `/statistics/payments-statistics/`

- Get payments statistics.

### Students Statistics

**GET** `/statistics/students-statistic/`

- Get students statistics.

### Teachers Statistics

**GET** `/statistics/teachers-statistic/`

- Get teachers statistics.

---

## Users APIs

### User Management

- **GET** `/users/` - List all users.
- **POST** `/users/create/student/` - Create a new student.
- **POST** `/users/create/teacher/` - Create a new teacher.
- **POST** `/users/create/user/` - Create a new user.
- **DELETE** `/users/delete/user/{id}/` - Delete user.

### Get Users by ID

- **POST** `/users/get-students-by-ids/` - Get students by IDs.
- **POST** `/users/get-teachers-by-ids/` - Get teachers by IDs.

### Student Management

- **GET** `/users/students/` - List all students.
- **GET** `/users/student/{id}/` - Get student details.
- **PUT** `/users/update/student/{id}/` - Update student.

### Teacher Management

- **GET** `/users/teachers/` - List all teachers.
- **GET** `/users/teacher/{id}/` - Get teacher details.
- **PUT** `/users/update/teacher/{id}/` - Update teacher.

---

## Notes

- `{id}` should be replaced with the actual ID of the resource.
- Use appropriate HTTP methods (GET, POST, PUT, DELETE) as per the endpoint.
- Ensure authentication for protected routes.

---

## Contact

For further questions, contact the developer nematov.uz

