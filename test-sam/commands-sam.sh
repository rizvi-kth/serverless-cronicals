
# aws commands
# ============
aws s3 cp ./sample-data.json s3://crawl-data/2020/05/2020-05-01/sample-data.json --profile rz-robot


# SAM CLI
# =======
pipenv install aws-sam-cli
sam init --help

# Create an App
sam init --runtime python3.7 --name test-app

# Start api-geteway locally
sam local start-api

# Package and deploy
sam package --template-file template.yaml --output-template-file out-template.yaml --s3-bucket rz-ds-resources --profile rz-robot --region eu-west-1
sam deploy --template-file out-template.yaml --stack-name rz-stack-lambda --capabilities CAPABILITY_NAMED_IAM --profile rz-robot --region eu-west-1

# Build and local test
# template-build.yaml --> build/template.yaml
sam build --template-file template-build.yaml --manifest ./hello_world/requirements.txt
sam local invoke HelloWorldFunction --no-event
# Package and deploy
# build/template.yaml --> template-deploy.yaml
sam package --template-file ./.aws-sam/build/template.yaml --output-template-file template-deploy.yaml --s3-bucket rz-ds-resources --profile rz-robot --region eu-west-1
sam deploy --template-file template-deploy.yaml

# Invoke the function locally
sam local invoke HelloWorldFunction --no-event
sam local invoke HelloWorldFunction --event ./test.json

# Create project wise config file - edit the samconfig.toml file
sam deploy --guided --stack-name rz-stack-lambda --capabilities CAPABILITY_NAMED_IAM --profile rz-robot --region eu-west-1




# AWS CLI
# =======
# Remove a stack
aws cloudformation delete-stack --stack-name rz-stack-lambda --profile rz-robot