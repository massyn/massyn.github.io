---
layout: page
title: Python code snippits
permalink: /python
---

## AWS

### S3

#### Read all objects in a bucket

```python
import boto3

Bucket = "MYBUCKETNAME"
Prefix = "myPrefix"

for P in boto3.client('s3').get_paginator('list_objects').paginate(Bucket=Bucket,Prefix = Prefix):
    for k in P['Contents']:
        print(k['Key'])
        content = boto3.client('s3').get_object(Bucket=Bucket, Key=k['Key'])['Body'].read().decode('utf-8')
```

#### Write to an S3 bucket

```python
boto3.resource('s3').Bucket(os.environ['S3BUCKET']).put_object(
    ACL         = 'bucket-owner-full-control',
    ContentType = 'application/json',
    Key         = key,
    Body        = json.dumps(newstate,indent=2,default=str)
)
```

#### Read an S3 object

```python
state = json.loads(boto3.client('s3').get_object(Bucket=os.environ['S3BUCKET'], Key=key)['Body'].read().decode('utf-8'))
```

### SNS

#### Publish a topic

```python
boto3.client('sns',region_name = 'ap-southeast-2').publish(TopicArn=os.environ['MonitorTopicSNS'],Message = msg, Subject = subject)
```

## Date and time

Convert epoch time to date time

```python
import datetime

x = datetime.datetime.fromtimestamp(epoch).strftime('%Y-%m-%d %H:%M:%S')
```

Convert Python datetime to a string

```python
import datetime

def datestamp_to_string(t):
    return datetime.datetime.strptime(t, '%Y-%m-%d %H:%M:%S')
```

Get the current datestamp

```python
import datetime

def datestamp():
    return datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

```

Find the first day of the week
```python
import datetime

def firstDayoftheWeek(dte):
    FDW = dte - datetime.timedelta(days = dte.weekday())

    return FDW
    # return FDW.strftime('%Y-%m-%d')
```
## Email

Send email through Outlook

```python
import win32com.client

def send_email(to,cc,subject,body):
    outlook = win32com.client.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = to
    mail.Subject = subject
    mail.HTMLBody = body
    mail.cc = cc
    mail.Display()
    #mail.Send()
```

## Files

### Find all files in a directory

```python
import os
import fnmatch

def findFiles(path,filter = '*'):
    q = []
    for r, d, f in os.walk(path):
        for file in f:
            if fnmatch.fnmatch(file,filter):
                q.append(os.path.join(r, file))
    return q
```

### Find the path of my script

```python
import os.path

file_path = os.path.dirname(os.path.realpath(__file__))
```

## Files

### Write a file to disk or S3

```python
import json
import boto3
import botocore

def writeFile(filename,data):
    # -- what type of data is it?
    if(type(data) != str):
        Body = json.dumps(data,default=str)
        ContentType = 'application/json'
    else:
        Body = data
        ContentType = 'application/text'

    # - is it local, or s3?
    if filename.startswith('s3://'):
        bucket = filename.split('/')[2]
        key = '/'.join(filename.split('/')[3:])
        
        print(f"bucket = {bucket}")
        print(f"key = {key}")
        try:
            boto3.resource('s3').Bucket(bucket).put_object(
                ACL         = 'bucket-owner-full-control',
                ContentType = ContentType,
                Key         = key,
                Body        = Body
            )
        except botocore.exceptions.ClientError as error:
            print(f"WARNING - s3.put_object - {error.response['Error']['Code']}")

    else:
        print(f"filename = {filename}")
        with open(filename,'wt') as f:
            f.write(Body)



if __name__=='__main__':
    x = { 'some' : 'data'}

    writeFile('myfile.txt',x)

    writeFile('s3://mybucket/2023/05/02/myfile.txt',x)
```

## CSV

### Write a CSV file

```python
import csv

def writeCSV(file,data):
    headers = list(data[0])
    with open(file, 'wt', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(headers)
       
        for x in data:
            row = []
            for h in headers:
                row.append(x.get(h))
            csvwriter.writerow(row)

if __name__ == '__main__':
    data = [
        { "header1" : "data1", "header2" : "data2" },
        { "header1" : "data3", "header2" : "data4" }
    ]
    writeCSV('output.csv',data)
```

### Read a CSV file

```python
import chardet
import csv,codecs

def readCSV(file):
    output = []
    # -- detect the file encoding first
    with open(file, 'rb') as f:
        result = chardet.detect(f.read())  

    with open(file, 'rb') as csvfile:		
        # = read the file line by line
        reader = csv.DictReader(codecs.iterdecode(csvfile, result['encoding']))
        for row in reader:
            output.append(row)

    return output
    
if __name__ == '__main__':
    for x in readCSV('c:/temp/test.csv'):
        print(x)
```

## Slack or Discord

Sending messages via [Slack](https://slack.com) or [Discord](https://discord.com/)

```python
import json
import urllib.request
import urllib.parse

def slackdiscord(webHook,message):
    if 'discord' in webHook:
        msg = { 'content' : message }
    else:
        msg = { 'text' : message }
    req = urllib.request.Request(
        webHook,
        json.dumps(msg).encode('utf-8'),
        {   
            'Content-Type': 'application/json',
            'User-Agent' : 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'
        }
    )
    resp = urllib.request.urlopen(req)
    return resp.read()
```

## Web monitoring

```python
import urllib.request

def website_monitor(url):
    #print(f'URL : {url}')
    try:
        req = urllib.request.Request(url, method='HEAD')
        resp = urllib.request.urlopen(req, timeout=10)
        #print(resp.getcode())
        return resp.getcode() == 200
    except:
        return False
    return False
```

## Excel

### Write an Excel file from a dictionary

```python
import xlsxwriter

def dict2xls(L,F,fmt = {}):
    print(f"Writing {F}")
    workbook = xlsxwriter.Workbook(F)
    
    COLOURS = {
        'darkblue'  : { 'bold': True,  'font_color' : 'white', 'bg_color' : '#44546A', 'align' : 'center' },
        'green'     : { 'bold': True,  'font_color' : 'white', 'bg_color' : '#00B050', 'align' : 'center' },
        'red'       : { 'bold': True,  'font_color' : 'white', 'bg_color' : '#C00000', 'align' : 'center' },
        'gray'      : { 'bold': False, 'font_color' : 'black', 'bg_color' : '#C0C0C0', 'align' : 'center' }
    }
    
    heading = workbook.add_format(COLOURS['darkblue'])

    for sheet in L:
        worksheet = workbook.add_worksheet(sheet)
        
        row = 0
        col = 0
        for H in L[sheet][0]:
            worksheet.write(row,col,H,heading)
            col += 1

        for a in L[sheet]:
            row += 1
            col = 0
            for H in L[sheet][0]:
                # -- is there formatting involved?
                cellformat = None
                if H in fmt:
                    F = fmt[H].get(a[H])
                    if F != None:
                        cellformat = workbook.add_format(COLOURS[F])

                worksheet.write(row,col,a[H],cellformat)
                col += 1

        worksheet.autofilter(0,0,row,col-1)
        worksheet.freeze_panes(1, 1)

    workbook.close()

if __name__ == '__main__':

    data = { 'Sheet1' : [
        {
            'Heading 1' : 'Data 1',
            'Heading 2' : 'Data 2'
        },
        {
            'Heading 1' : 'Data 3',
            'Heading 2' : 'Data 4'
        },
    ]}
    dict2xls(data, 'c:/temp/myexcelfile.xlsx')
```

## Reporting

### crosstab

```python
import json

def add(matrix,x,y,z):
    # -- index X
    if not 'x' in matrix:
        matrix['x'] = []
    if not x in matrix['x']:
        matrix['x'].append(x)

    # -- index Y
    if not 'y' in matrix:
        matrix['y'] = []
    if not y in matrix['y']:
        matrix['y'].append(y)

    # -- index z
    if not 'z' in matrix:
        matrix['z'] = {}

    if not x in matrix['z']:
        matrix['z'][x] = {}
    
    matrix['z'][x][y] = z

def render_markdown(matrix):

    matrix['x'].sort()
    matrix['y'].sort()

    out = "||**" + "**|**".join(matrix['x']) + "**|\n"
    out += "|--" * (len(matrix['x']) + 1) + "|\n"
    for y in matrix['y']:
        out += f"|**{y}**|"
        for x in matrix['x']:
            out += f"{matrix['z'][x].get(y,'')}|"
        out += "\n"

    return out

def render_html(matrix):

    matrix['x'].sort()
    matrix['y'].sort()

    out = '<table>\n'
    out += "<tr><th>&nbsp;</th><th>" + "</th><th>".join(matrix['x']) + "</th></tr>\n"

    for y in matrix['y']:
        out += f"<tr><th>{y}</th>"
        for x in matrix['x']:
            out += f"<td>{matrix['z'][x].get(y,'')}</td>"
        out += "</tr>\n"

    out += '</table>\n'
    return out

def main():

    x = {}

    add(x,'X1','Y1','hello')
    add(x,'X2','Y1','there')

    add(x,'X1','Y2','Is')
    add(x,'X2','Y2','this')
    add(x,'X3','Y2','working')

    add(x,'X4','Y3','Howdy')

    # render markdown
    with open('output.md','wt') as F:
        F.write('# The main thing\n\n')
        F.write(render_markdown(x))

    # render HTML
    with open('output.html','wt') as F:
        F.write('<html>\n')
        F.write('<head><style>body { font-family:verdana;} th { background-color: #0047AB; color: #FFFFFF } td { background-color: ##B2FFFF; } table,th,td { border: 1px solid gray; border-collapse: collapse; padding: 5px; } </style></head>')
        F.write('<h1>The HTML thing</h1>\n\n')
        F.write(render_html(x))
        F.write('</html>')

main()
```

## Command-line arguments

```python
import argparse
parser = argparse.ArgumentParser(description='CloudFormation Helper')

# -- read a variable
parser.add_argument('-desc',help='Set a description for the CloudFormation file')

# -- Mandatory variable
parser.add_argument('-cf', help='Path to the CloudFormation json file', required=True)

# -- Provide multiple variables in a list
parser.add_argument('-add',help='Add a new resource to the CloudFormation file',nargs='+')

# -- Make it a toggle switch
parser.add_argument('-overwrite', help='Forces an overwrite of a resource if it already exists', action='store_true')

# -- consume the data
args = parser.parse_args()
print(args.desc)

```
