# 📧 Automated Daily Status Email Reporting

A **Python-based automation solution** that replaces **manual status update emails** with a **fully automated, scheduled reporting system**.  
The application reads project tracker data, generates a **clean and structured status summary**, and **automatically sends the email every day at 8:00 PM** using **Windows Task Scheduler** — with **zero manual intervention**.

This project demonstrates practical **workflow automation**, **report generation**, and **email automation** commonly used in enterprise environments.

---

## 🔧 Key Features

- 📊 **Automated Data Extraction**
  - Reads project tracker updates (Excel / CSV)
  - Filters and structures relevant status information

- 📝 **Clean Status Summary Generation**
  - Formats data into a professional, readable email
  - Ensures consistency across all reports

- 📬 **Automated Email Delivery**
  - Sends emails automatically using Python
  - No manual triggering required

- ⏰ **Daily Scheduling**
  - Integrated with **Windows Task Scheduler**
  - Runs every day at **8:00 PM**

- 🔁 **Zero Manual Effort**
  - Fully unattended execution
  - Reliable and repeatable process

---

## 🛠 Tech Stack

- **Python**
- **Pandas** – Data processing
- **SMTP / Email Libraries** – Email delivery
- **Windows Task Scheduler** – Job scheduling
- **Excel / CSV** – Project tracker input

---

## 📦 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/Automated-Status-Email.git
   cd Automated-Status-Email
2. **Install dependencies**
    ```bash
    pip install -r requirements.txt

3. **Configure email settings**

Update sender email credentials

Configure recipient list

Set tracker file path

4. **Test the script manually**

      ```bash
     python main.py

5. **Schedule using Task Scheduler**

Create a daily task

Set trigger time to 8:00 PM

Point to the Python executable and script


