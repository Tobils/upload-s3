import boto3


class S3Client:
    def __init__(self) -> None:
        self.__s3Client = boto3.client('s3',
                                       region_name='*******',
                                       aws_access_key_id="*******",
                                       aws_secret_access_key="*******")
        self.__bucket_name = "*******"
        self.__uri = "*******"
        pass

    def upload(self, file):
        try:
            self.__s3Client.upload_fileobj(
                file,
                self.__bucket_name,
                file.filename,
                ExtraArgs={
                    "ACL": "public-read",
                    "ContentType":  file.content_type
                }
            )
            return self.__uri + "/" + self.__bucket_name + "/" + file.filename
        except Exception as e:
            return e
