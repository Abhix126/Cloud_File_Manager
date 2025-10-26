# ⚙️ Cloud File Manager (Local ↔ AWS S3) — How to Run

This guide explains how to install, configure, and run the Cloud File Manager GUI to manage files between your **local system** and an **AWS S3 bucket**.

```bash
# -------------------------------
Step 1: Clone Repository
# -------------------------------
git clone https://github.com/yourusername/cloud-file-manager.git
cd cloud-file-manager

# -------------------------------
Step 2: Install Dependencies
# -------------------------------
pip install boto3

# -------------------------------
Step 3: Create AWS IAM User
# -------------------------------
# 1. Go to https://aws.amazon.com/console/
# 2. Navigate to IAM → Users → Add User
# 3. Enter a username, e.g., cloud-file-manager-user
# 4. Select Programmatic access
# 5. Click Next → Attach existing policies → AmazonS3FullAccess
# 6. Create user and copy Access Key ID and Secret Access Key
# 7. Keep credentials secure

# -------------------------------
Step 4: Configure AWS Credentials
# -------------------------------
Create a file creds.py in the project root:

creds.py 
AWS_ACCESS_KEY_ID = "YOUR_ACCESS_KEY_ID"
AWS_SECRET_ACCESS_KEY = "YOUR_SECRET_ACCESS_KEY"
AWS_REGION = "us-east-1"  # Your AWS region
S3_BUCKET = "your-s3-bucket-name"


# -------------------------------
Step 5: Run the Application
# -------------------------------
python gui_app.py

# -------------------------------
Step 6: Using the GUI
# -------------------------------
# Left Panel: Local filesystem
# Right Panel: S3 bucket
# Bottom Panel: Buttons, progress bar, activity log

# Features:
# - Upload → S3: Upload selected local files to S3
# - Download from S3: Download S3 files to local folder
# - Create S3 Folder: Make a new folder in S3
# - Delete S3 Object(s): Remove selected objects from S3
# - View Object (URL): Open S3 object in browser
# Logs are written to logs.txt

# -------------------------------
Step 7: Project Structure
# -------------------------------
# cloud-file-manager/
# │
# ├── gui_app.py         # Main GUI
# ├── s3_manager.py      # AWS S3 operations
# ├── local_manager.py   # Local file browsing
# ├── logger.py          # Thread-safe logging
# ├── creds.py           # AWS credentials
# ├── logs.txt           # Operation logs
# └── images/            # GUI snapshots

# -------------------------------
Step 8: Troubleshooting
# -------------------------------
# - Module 'boto3' not found: pip install boto3
# - AWS credentials invalid: check creds.py values
# - GUI doesn’t open: ensure Tkinter installed (sudo apt install python3-tk)
# - Upload/Download fails: check IAM permissions (s3:PutObject, s3:GetObject, s3:DeleteObject)
