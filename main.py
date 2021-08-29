from boto3.session import Session
import boto3
from datetime import datetime

def get_s3():
    ACCESS_KEY = 'AKIARX7DSUMEMFVL267C'
    SECRET_KEY = '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'
    session = Session(aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)
    s3 = session.resource('s3')
    your_bucket = s3.Bucket('stellar.health.test.srikar.vedula')
    for s3_file in your_bucket.objects.all():
        print(s3_file.key)
    your_bucket.download_file('patients.log', 'C:/Users/srika/PycharmProjects/stellar_assignment/patients.log')

def log_parse():
    get_s3()
    file='patients.log'
    list_of_lists = []
    with open(file) as f:
        f = f.readlines()

    for line in f:
       # print(line)
        stripped_line = line.strip()

        line_list = stripped_line.split()
        list_of_lists.append(line_list)
    print(list_of_lists[0])
    list_of_lists.pop(0)
    list_of_lists = list_of_lists[:len(list_of_lists) - 5]

    #print(type(list_of_lists[1]))
    new_strings=[]
    for i in list_of_lists:
        #print(i)
        dob_str="DOB"
        for ele in i:
            if dob_str in ele:
                # print(ele)
                # print(type(ele[0]))
                index = i.index(ele)
                print(index)
                print(ele)
                splt_char = "/"

                K = 2

                temp = ele.split(splt_char)
                res = splt_char.join(temp[:K]), splt_char.join(temp[K:])
                print(list(res))
                re=list(res)
                year=re[1]
                print(year)
                new_str="DOB=X/X/"+str(year)
                print(new_str)
                i[index]=new_str

    for i in list_of_lists:
        print(i)

    with open('newpatients.txt', 'w') as filehandle:
        for listitem in list_of_lists:
            filehandle.write('%s\n' % listitem)

def upload_file():
    ACCESS_KEY = 'AKIARX7DSUMEMFVL267C'
    SECRET_KEY = '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'
    session = boto3.Session(
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY
    )

        # Creating S3 Resource From the Session.
    s3 = session.resource('s3')
    s3.Object('stellar.health.test.srikar.vedula', 'newpatients.txt').upload_file(Filename='C:/Users/srika/PycharmProjects/stellar_assignment/newpatients.txt')
if __name__ == '__main__':
    log_parse()
    upload_file()
    print("completed")

