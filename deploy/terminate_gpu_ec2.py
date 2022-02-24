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

logger.info("Getting instance information - use this to terminate instance")

instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
for instance in instances:
    logger.info(f"Terminating instance: {instance.id}, {instance.instance_type}")
    instance.terminate()
    instance.wait_until_terminated()
    logger.info("Termination complete")

