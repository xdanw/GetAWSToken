
import os
import boto3
from boto3.session import Session
from botocore.config import Config
from botocore.session import Session as BotocoreSession

botocore_session = BotocoreSession()

session_keywords = {'botocore_session': botocore_session}

session_keywords['aws_access_key_id'] = raw_input('Access Key ID: ');
session_keywords['aws_secret_access_key'] = raw_input('Secret: ');
session_keywords['aws_session_token'] = raw_input('Token: ');

# in XLD Plugin: 
# common/aws_helper.py -> __init__ -> create_session -> __get_session -> return Session(**session_keywords)
ses = Session(**session_keywords)

# in XLD Plugin: 
# ec2/ec2_helper.py  get_instances()  <-  ec2client.describe_instances is from here
#   > ec2_client = get_aws_client(region=deployed.region, resource_name='ec2')
#      > in aws_helper.py:  get_aws_client()  <-  (BotocoreSession).client(resource_name, region_name=region, config=config)

region = 'us-gov-west-1';
ec2_client = ses.client('ec2',region)
DescribeEc2Response = ec2_client.describe_instances(Filters=[])

if DescribeEc2Response['ResponseMetadata']['HTTPStatusCode'] == 200: 
    print '...\r\nSuccess: Retrieved EC2 information from ' + region + '.';

print '-------------------------------------'
print DescribeEc2Response
print '-------------------------------------'


if len(DescribeEc2Response['Reservations']) == 0: 
    print 'You have no reserved instances.'




