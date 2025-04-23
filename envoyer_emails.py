# ---------------------------
# BULLETPROOF EMAIL SENDER v3.4 (FINAL)
# ---------------------------
import smtplib
import time
import random
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

class EmailCommando:
    def __init__(self):
        # ================= CONFIG =================
        self.SENDER_EMAIL = "your-email@gmail.com" # 👤 Your Gmail address
        self.APP_PASSWORD = "your-app-password"    # 🔑 App-specific password
        self.SMTP_SERVER = "smtp.gmail.com"        # 🌐 SMTP server for Gmail
        self.SMTP_PORT = 465                       # 🔒 Port for SSL
        self.CV_PATH = "CV_PATH"                          # 📄 Path to your CV
        self.MAX_RETRIES = 3                       # 🔄 Max retries for connection
        self.TIMEOUT = 30                          # ⏳ Timeout for SMTP
        self.BATCH_SIZE = 8                        # 📦 Emails per batch
        
        # ========= SANITIZED RECIPIENT LIST ========
        self.TARGET_LIST = [  
            # Add more sanitized email addresses here
        ]
        
        # ========== EMAIL CONTENT VARIANTS ============
        self.SUBJECT_VARIANTS = [
            
        ]

        self.EMAIL_BODIES = [
            """Hello, ...""",
            """Bonjour, ..."""

            
        ]

    def establish_connection(self):
        for attempt in range(self.MAX_RETRIES):
            try:
                server = smtplib.SMTP_SSL(
                    self.SMTP_SERVER, 
                    self.SMTP_PORT,
                    timeout=self.TIMEOUT
                )
                server.login(self.SENDER_EMAIL, self.APP_PASSWORD)
                print("🔐 Secure SMTP Tunnel Established")
                return server
            except Exception as e:
                print(f"🔥 Connection Attempt {attempt+1} Failed: {str(e)}")
                time.sleep(2**attempt)
        return None

    def craft_email(self, recipient):
        msg = MIMEMultipart()
        msg['From'] = self.SENDER_EMAIL
        msg['To'] = recipient
        msg['Subject'] = Header(f"{random.choice(self.SUBJECT_VARIANTS)} | YouCode", 'utf-8')
        msg['X-Priority'] = '3'  # Normal priority
        
        # Random body selection
        body = random.choice(self.EMAIL_BODIES)
        msg.attach(MIMEText(body, 'plain', 'utf-8'))
        
        # Anonymous CV attachment
        with open(self.CV_PATH, "rb") as f:
            cv_part = MIMEApplication(f.read(), Name="CV.pdf")
        cv_name = f"Candidature_{random.randint(2024,9999)}.pdf"
        cv_part['Content-Disposition'] = f'attachment; filename="{cv_name}"'
        msg.attach(cv_part)
        
        return msg.as_string()

    def execute_mission(self, dry_run=False):
        print("""
        ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
        █▓▒░ EMAIL DEPLOYMENT SYSTEM v3.4 ░▒▓█
        ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
        """)
        
        if dry_run:
            print("🚧 DRY RUN MODE ACTIVATED")
            for i, target in enumerate(self.TARGET_LIST):
                print(f"📨 [Mock] Email {i+1} to {target}")
                print(f"📎 Attachment: Candidature_{random.randint(1000,9999)}.pdf")
                print("⏲️ Simulating delay...\n")
                time.sleep(0.5)
            return

        server = self.establish_connection()
        if not server:
            print("☠️ CRITICAL FAILURE: Unable to establish connection")
            return

        total_sent = 0
        batches = [self.TARGET_LIST[i:i+self.BATCH_SIZE] 
                 for i in range(0, len(self.TARGET_LIST), self.BATCH_SIZE)]
        
        for batch_num, batch in enumerate(batches):
            print(f"\n=== BATCH {batch_num+1}/{len(batches)} ===")
            batch_sent = 0
            
            for idx, target in enumerate(batch):
                try:
                    email_content = self.craft_email(target)
                    server.sendmail(self.SENDER_EMAIL, target, email_content)
                    batch_sent += 1
                    total_sent += 1
                    print(f"✅ [{total_sent}] Success: {target}")
                    time.sleep(random.randint(110, 190))  # Random delay
                    
                except Exception as e:
                    print(f"❌ Failed {target}: {str(e)}")
            
            # Batch cooldown
            if batch_num < len(batches)-1:
                print(f"⏳ Cooling down for {self.BATCH_SIZE} minutes...")
                server.quit()
                time.sleep(self.BATCH_SIZE * 60)
                server = self.establish_connection()
                if not server: break

        server.quit()
        print(f"\n🎯 MISSION COMPLETE - {total_sent}/{len(self.TARGET_LIST)} emails delivered")

if __name__ == "__main__":
    agent = EmailCommando()
    agent.execute_mission(dry_run=False)