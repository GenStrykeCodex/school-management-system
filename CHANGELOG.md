# School Management System

**Project Status**: Stable initial release with full core functionality implemented.

---
## v1.0 Changelog – Initial Stable Release
### Title: Full CLI-Based School Management System  

### Highlights:
- Completed CLI menu integration (`main.py`)
- Connected all service modules with interactive handlers
- Implemented full Student Management system:
  - Add, search by ID and roll number
  - View students by class
  - Update marks
  - Delete records
- Implemented full Teacher Management system:
  - Add teachers
  - View all teachers
  - Search by ID
  - Update salary
  - Delete records
- Integrated Academic Reports module:
  - Individual student report
  - Class topper
  - Class average percentage
  - Pass/Fail class statistics
- Added input validation and error handling across application
- Implemented persistent JSON-based data storage
- Improved CLI output formatting and user experience
- Completed layered architecture (models, services, utils, controller)

---

## v0.6 Changelog - 23 Jan 2026
### Title: `main.py` reworked

**Features Added**:

- CLI Menu reworked
- Connection of modules established
- `validators.py` updated

---

## v0.5 Changelog – 21 Jan 2026
### Title:  Report Services Module Completed

**Features Added**:

- `report_service.py` implemented
- Student percentage calculation utility added
- Individual student report generation added
- Class topper identification feature added
- Class average percentage calculation added
- Pass/fail statistics report for classes added
- Report module with validators and JSON storage integrated

---

## v0.4 Changelog – 21 Jan 2026
### Title: Teacher Services Module Completed

Features Added:

- `teacher_service.py` implemented
- Teacher add operation added
- Teacher search by ID implemented
- View all teachers functionality added
- Teacher salary update feature added
- Teacher deletion by ID implemented
- Teacher ID validation (TCH_ prefix) integrated
- Connected teacher services with JSON storage and validators

---

## v0.3 Changelog - 20 Jan 2026
### Title: Student Services Module Completed

Features added:

- `student_service.py` implemented
- Student add operation added
- Class-wise student listing implemented
- Student search by ID and Class+Roll implemented
- Student marks update feature added
- Student deletion by ID implemented

---

## v0.2 Changelog - 19 Jan 2026
### Title: Updated `utils/` folder

Features added:
- `id_generator.py` fixed
- `validators.py` added for input validation

---

## v0.1 Changelog - 18 Jan 2026
### Title: Initialized Project

Features added:
- Student and Teacher model built
- Main menu designed
- `file_handler.py` and `id_generator.py` added
- Project Initialized
