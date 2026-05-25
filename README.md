# practice_python_boto3
A collection of lightweight Python scripts designed to automate cloud workflows, interact with AWS resources, and streamline infrastructure management using the official AWS SDK for Python (Boto3).
🛠️ Prerequisites
Before running the scripts, ensure your local environment meets the following requirements:
Python: Version 3.8 or higher.
AWS Account: Active account with programmatic access credentials (Access Key ID and Secret Access Key).
IAM Permissions: Appropriate policies attached to your AWS user (e.g., AmazonS3FullAccess, AmazonEC2ReadOnlyAccess).
📥 Installation & Setup
Follow these steps to set up the project locally:
1. Clone the repository
bash
git clone https://github.com
cd your-repo-name
Use code with caution.
2. Set up a virtual environment
bash
# Create the environment
python -m venv venv

# Activate it (Mac/Linux)
source venv/bin/activate

# Activate it (Windows)
venv\Scripts\activate
Use code with caution.
3. Install dependencies
bash
pip install -r requirements.txt
Use code with caution.
(Ensure your requirements.txt contains at least boto3>=1.34.0)
🔐 AWS Credential Configuration
Boto3 automatically searches for credentials in your environment. The recommended approach is using the AWS CLI.
Option A: Via AWS CLI (Recommended)
Install the AWS CLI and run the configuration wizard:
bash
aws configure
Use code with caution.
Provide your details when prompted:
text
AWS Access Key ID [None]: YOUR_ACCESS_KEY
AWS Secret Access Key [None]: YOUR_SECRET_KEY
Default region name [None]: us-east-1
Default output format [None]: json
Use code with caution.
Option B: Via Environment Variables
Alternatively, export the credentials directly into your terminal session:
bash
# Mac/Linux
export AWS_ACCESS_KEY_ID="YOUR_ACCESS_KEY"
export AWS_SECRET_ACCESS_KEY="YOUR_SECRET_KEY"
export AWS_DEFAULT_REGION="us-east-1"

# Windows (Command Prompt)
set AWS_ACCESS_KEY_ID=YOUR_ACCESS_KEY
set AWS_SECRET_ACCESS_KEY=YOUR_SECRET_KEY
set AWS_DEFAULT_REGION=us-east-1
Use code with caution.
💻 Usage
Run any of the provided automation scripts directly using Python:
bash
# Example: Run the S3 upload script
python s3_upload.py

# Example: Inspect running EC2 instances
python ec2_status.py
Use code with caution.
📁 Project Structure
text
├── .gitignore
├── README.md
├── requirements.txt
├── s3_upload.py       # Handles S3 bucket listing and uploads
├── ec2_status.py      # Filters and reads EC2 instance states
└── dynamodb_put.py    # Adds operational data to DynamoDB
Use code with caution.
