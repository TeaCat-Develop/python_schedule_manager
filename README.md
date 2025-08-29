# 🗓️ Schedule Manager

**Python + MySQL 기반 CLI 일정 관리 프로그램**
사용자가 간단하게 일정 추가, 조회, 완료 가능.

---

## 📌 주요 기능
- ✅ 일정 추가 (INSERT)
- ✅ 일정 조회 (SELECT)
- ✅ 일정 완료 처리 (UPDATE)
- ✅ 프로그램 종료

---

## 🛠 기술 스택
- **Python 3.11**
- **MySQL** (pymysql)

---

## ⚙️ 설치 및 실행 방법

### 1️⃣ 저장소 클론
```bash
git clone https://github.com/<your-username>/schedule-python.git
cd schedule-python```

### 2️⃣ 가상환경 생성 및 활성화
```python3 -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows```

### 3️⃣ 필요 라이브러리 설치
```pip install -r requirements.txt```

### 4️⃣ MySQL 데이터베이스 준비
```CREATE DATABASE schedule_db;```

```USE schedule_db;```

```
CREATE TABLE schedules (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    start_datetime VARCHAR(14) NOT NULL,
    end_datetime VARCHAR(14),
    is_completed BOOLEAN DEFAULT FALSE
);```

### 5️⃣ 프로그램 실행
```
python schedule_manager.py
