# SqLite schema

Tables and fields required:

- Subject
  - subject_id
  - name
  - description
- Book
  - book_id
  - subject_id
  - name
  - author
  - edition
- Section (chapter or subchapter--that which has unique problem sets)
  - section_id
  - book_id
  - name (could be numeric (like 2.6))
  - studied (yes or no -- have I studied that material yet)
  - date_studied
  - description
- Problem
  - problem_id
  - book_id
  - section_id
  - name
  - completed (yes or no)
  - date of completion

Assignment
    list of problems. How to handle this? in a list of pids? 

Relationships between tables:

|  | Subject | Book | Chapter | Problem | Assignment |
| - | ------- | ---- | ------- | ------- | ---------- |
| Subject |---| 1-many |---|1-many|---|
| Book |---|---| 1-many |1-many|---|
| Chapter |---|---|---|1-many|---|
| Problem |---|---|---|---|many-1|
| Assignment |---|---|---|---|---|

Draw diagram that establishes nature of relationship between each table (one-to-one, one-to-many, many-to-many). The way to handle each of these cases is discussed here https://support.office.com/en-us/article/database-design-basics-eb2159cf-1e30-401a-8084-bd4f9c9ca1f5

Then apply normalization rules