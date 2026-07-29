class StorageException(Exception):
    """Base storage exception."""
    pass


class BucketNotFound(StorageException):
    pass


class UploadFailed(StorageException):
    pass


class DownloadFailed(StorageException):
    pass