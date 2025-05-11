# aws-ebs-snapshot-cleaner
🔄 A Python-based AWS Lambda function that automatically deletes unused EBS snapshots to reduce storage costs. 🚀 Implements cloud resource cleanup using Boto3, EC2, and snapshot volume association logic.

# 🧹 AWS EBS Snapshot Cleaner (Python + Lambda)

This project automates the cleanup of unused **EBS snapshots** in AWS to reduce storage costs and maintain a clean cloud environment. It's built using **Python (Boto3)** and deployed via **AWS Lambda**.

## 🔍 What It Does

- Fetches all EBS snapshots owned by your AWS account
- Identifies if snapshots are tied to:
  - Non-existing volumes
  - Volumes not attached to any **running EC2 instance**
- Automatically deletes such orphaned or unused snapshots

> 💡 Useful for DevOps engineers who want to automate cost optimization and cloud hygiene.

---

## 🧠 Tech Stack

- **AWS Lambda**
- **AWS EC2 & EBS**
- **Python 3.x**
- **Boto3 (AWS SDK)**

---

## 📌 Why This Matters

- Prevents unnecessary AWS billing from leftover snapshots 💸
- Cleans up zombie volumes and resources 👻
- Shows real-world use of automation in cloud DevOps

---

## 🛠️ How to Use

1. Deploy the code as a Lambda function in your AWS environment
2. Set IAM permissions to allow:
   - `ec2:DescribeSnapshots`
   - `ec2:DescribeInstances`
   - `ec2:DescribeVolumes`
   - `ec2:DeleteSnapshot`
3. (Optional) Schedule it using **CloudWatch Events** for periodic cleanup

---



## 🚀 Future Improvements

- Add logging to CloudWatch
- Add tag-based filters (e.g., skip snapshots tagged as `Keep`)
- Add notification via SNS for deleted snapshots

---

## 📬 Feedback

Feel free to fork, contribute, or suggest improvements!  
*Built as part of my DevOps learning journey.*

