```markdown
# ✉️ Automated Email System - Motivational and Love Letters

This repository showcases Python scripts for automating the creation and delivery of motivational emails and love letters. 

Each script combines random message generation with SMTP integration for seamless email automation. 

A testing module ensures quality and consistency.

---

## 📁 Files Overview

1. **mmain.py** ✨ Automates the sending of motivational quotes via email.

   - **Email Setup:** Configures SMTP settings for Gmail.

   - **Random Message Generation:** Creates motivational quotes using predefined word lists.

   - **Automation Ready:** Includes functionality for scheduling emails.

2. **main.py** 💌 Automates the sending of love letters with a similar structure.

   - **Email Setup:** Uses Gmail SMTP for email delivery.

   - **Personalized Messages:** Generates love letters with creative and heartfelt messages.

   - **Automation Friendly:** Supports scheduled email sending.

3. **TestGenerateMessage.py** 🛠️ Tests the structure of generated messages.

   - **Validation:** Ensures messages are grammatically correct and include key phrases.

   - **Reusability:** Built for verifying message formats across different email scripts.

---

## **Setups:**

- **Install Python:** [Download here](https://www.python.org/downloads/)

- **Install Dependencies:**  
  ```bash
  pip install schedule
  ```

- **Set Up Email Credentials:**  
  Update `sender`, `recipient`, and `pw` variables in `mmain.py` and `main.py` with your credentials.

---

## **Run Programs:**

**mmain.py ✨ (Motivational Quotes):**

- ```bash
  python mmain.py
  ```

**main.py 💌 (Love Letters):**

- ```bash
  python main.py
  ```

**TestGenerateMessage.py 🛠️ (Testing):**

- ```bash
  python -m pytest TestGenerateMessage.py
  ```

---

Enjoy these programs as a showcase of Python's capabilities for automation and SMTP integration!
```