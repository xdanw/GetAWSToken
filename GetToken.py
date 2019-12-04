
import boto3
import botocore.session

client = boto3.client('sts')

print ('Uses boto3 to retrieve a time-limited session token (STS token)');
print ('(region is currently hardcoded to us-gov-west-1)');
awsKeyId = raw_input('IAM User Access Key ID: '); 
awsKeySecret = raw_input('IAM Access Secret: ')

# ATTN: MUST specify region when using govcloud
stsClient = boto3.client('sts', region_name='us-gov-west-1', aws_access_key_id=awsKeyId, aws_secret_access_key=awsKeySecret)

stsToken = stsClient.get_session_token()

roleArn = raw_input('Role ARN (optional): ')

if roleArn: 
    roleResponse = stsClient.assume_role(RoleArn=roleArn, RoleSessionName='Session0001')
    # note: optional DurationSeconds, maximum 129600 on get_session_token, maximum 43200 on assume_role
    # boto3 assume_role also accepts ExternalId='corp1'

print '---------------------------------';

print ' ';
print "Token for user.";
print 'STS Temporary Access Key ID: ' + stsToken['Credentials']['AccessKeyId'];
print 'STS Secret Key: ' + stsToken['Credentials']['SecretAccessKey'];
print 'STS Session Token: ' + stsToken['Credentials']['SessionToken'];
exp = stsToken['Credentials']['Expiration']
# print 'Expires: ' + str(exp.year) + '/' + str(exp.month) + '/' + str(exp.day) + ' ' + str(exp.hour) + ':' + str(exp.minute)
print 'Expires: ' + str(exp) + '(UTC)';
print ' ';


if roleArn: 
    print '---------------------------------';

    print ' ';
    print 'Assumed role.'
    print 'Assumed role ID: ' + roleResponse['AssumedRoleUser']['AssumedRoleId'];
    print 'ARN: ' + roleResponse['AssumedRoleUser']['Arn'];
    print 'Temporary Access Key ID (for this role): ' + roleResponse['Credentials']['AccessKeyId'];
    print 'Role Secret Key: ' + roleResponse['Credentials']['SecretAccessKey'];
    print 'Role Session Token: ' + roleResponse['Credentials']['SessionToken'];
    exp = roleResponse['Credentials']['Expiration']
    print 'Expires: ' + str(exp) + '(UTC)';
    print ' ';

    print '---------------------------------';



