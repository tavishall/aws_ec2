import logging
import boto3

# create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

# See https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#client
ec2 = boto3.resource(
    'ec2',
    region_name='us-west-1'
)

# Can either have LaunchTemplateName or LaunchTemplateId, not both.
launch_template = {
    "LaunchTemplateName": "Basic_GPU_template",
    "Version": "2"
}

# Note that I have my credentials stored in ~/.aws/credentials with the
# following format (see # https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)
#
# [default]
# aws_access_key_id=BLAHBLAH
# aws_secret_access_key=BLAHBLAHBLAH
#
# Generate this by going to account in AWS, security credentials, access keys
# Then create new access key, download the file and move it to correct
# place/format
instances = ec2.create_instances(LaunchTemplate=launch_template, MinCount=1, MaxCount=1)

instances[0].wait_until_running()
instances[0].reload()

logger.info(f"IP for instance = {instances[0].public_ip_address}")
logger.info(f"Can run instances[0].terminate() to end it - or use Console")
logger.info(f"Note that you can run instances[0].wait_until_terminated() as well")

"""
Might be cool to have this as a basic while looping on user input with a 
timeout that auto-terminates after X hours of inactivity or something.
"""

