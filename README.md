✉️ Automated Email System - Motivational and Love Letters

This repository showcases Python scripts for automating the creation and delivery of motivational quotes and love letters. Each script features random message generation, SMTP integration for email delivery, and a testing module for message validation.


## 📁 Files Overview

1. **mmain.py** ✨ Automates the sending of motivational quotes via email.

   - **Email Setup:** Configures SMTP settings for Gmail.  

   - **Random Message Generation:** Creates motivational quotes using predefined word lists.  

   - **Automation Ready:** Includes functionality for scheduling emails.  

   - **How to Use:** Run the script to start sending motivational quotes.

2. **main.py** 💌 Automates the sending of love letters via email.

   - **Email Setup:** Uses Gmail SMTP for email delivery.  

   - **Personalized Messages:** Generates love letters with creative and heartfelt phrases.  

   - **Automation Friendly:** Supports scheduling for regular email dispatch.  

   - **How to Use:** Run the script to send personalized love letters.

3. **TestGenerateMessage.py** 🛠️ Tests the structure and quality of generated messages.

   - **Validation:** Ensures messages are grammatically correct and include key phrases.  

   - **Reusability:** Works with both motivational and love letter scripts.  

   - **How to Use:** Run tests to validate message structure and content.

---

## **Setups:** 

- **Install Python:** [Download here](https://www.python.org/downloads/)  

- **Install Dependencies:**  
  ```bash
  pip install schedule
  ```

- **Set Up Email Credentials:**  
  Update the `sender`, `recipient`, and `pw` variables in `mmain.py` and `main.py` with your email credentials.

---

## **Run each script:**

**mmain.py ✨:**

- ```bash
  python mmain.py
  ```

**main.py 💌:**

- ```bash
  python main.py
  ```

**TestGenerateMessage.py 🛠️:**

- ```bash
  python -m pytest TestGenerateMessage.py
  ```