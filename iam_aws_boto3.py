import boto3

#aws configure -> create a default user
#aws configure --profile dev -> create a dev user
#aws configure --profile qa -> create a qa user
#aws configure --profile prod -> create a prod user
aws_mgmt_console = boto3.session.Session(profile_name="default")
iam_console = aws_mgmt_console.resource("iam")

for each_user in iam_console.users.all():
    print (each_user.name)
