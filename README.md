aliyun_driver
=============

根据阿里云提供的SDK简单实现了文件上传跟删除。
--------------------------------------------

***
##实例##

    main.py:
    from aliyunoss_driver import *

    HOST = ''
    ACCESS_ID = ''
    SECRET_ACCESS_KEY = ''

    if __name__ == "__main__":
        test = driver_oss(HOST, ACCESS_ID, SECRET_ACCESS_KEY)
        test_upload = test.upload_data("your_bucket_name", "your_object_name", "your_file")
        test_delete = test.delete_data("your_bucket_name", "your_object_name", "your_file")
