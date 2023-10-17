-- convert hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)

-- use hbtn_0c_0
USE hbtn_0c_0;
-- convert the table first_table
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
