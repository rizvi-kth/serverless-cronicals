# Serverless
# ==========

serverless deploy --aws-profile rz-robot

# Check the templates
sls create --help

# Create a project with a templete
sls create -t aws-python3 -p pysls
sls create --template aws-python3 --path pysls

# In the project directory
cd pysls

sls deploy --aws-profile rz-robot
sls remove --aws-profile rz-robot
sls invoke --function hello --aws-profile rz-robot
sls create function -f testFunction



# aws commands
# ============
aws s3 cp ./sample-data.json s3://crawl-data/2020/05/2020-05-01/sample-data.json --profile rz-robot





