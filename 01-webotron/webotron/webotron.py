import boto3
import click

session = boto3.Session(profile_name='shotty')
s3 = session.resource('s3')

@click.group()
def cli():
    "Webotron deploys website to AWS"
    pass


@cli.command('list-buckets')
def list_buckets():
    "List all S3 buckets"
    for bucket in s3.buckets.all():
        print(bucket)

# note that the single quotation in the command will replace the command name when you call it
@cli.command('list-bucket-objects')
def list_bucket_objects(bucket):
    "List Objects in the bucket"
    for obj in s3.Bucket(bucket).objects.all():
        print(obj)
        

if __name__ == '__main__':
    cli()
