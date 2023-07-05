import argparse
import fnmatch
import os

def findFiles(path,filter = '*'):
    q = []
    for r, d, f in os.walk(path):
        for file in f:
            if fnmatch.fnmatch(file,filter):
                q.append(os.path.join(r, file))
    return sorted(q)

def process(folder,out):
    myYear = ''
    myMonth = ''
    with open(out,'wt') as I:
        I.write('# Blog\n')

        for F in findFiles(folder,'*.md'):
            F = F.replace('\\','/') # convert windows paths to linux
            print(F)
            # -- get the date from the filename
            dte = F[len(folder):].split('/')
            year = dte[1]
            month = dte[2]
            day = dte[3]

            if year != myYear:
                I.write(f'## {year}\n')

            if f"{year}-{month}" != myMonth:
                I.write(f'### {month}\n')

            # -- grab the first line of the file
            title = ''
            with open(F,'rt') as q:
                title = q.readline().replace('# ','')

            I.write(f"{year}-{month}-{day} [{title}]({F})\n")

            myYear = year
            myMonth = f"{year}-{month}"
        

def main():
    parser = argparse.ArgumentParser(description='Blog Index Generator')
    parser.add_argument('-folder', help='Path to the blog index files', required=True)
    parser.add_argument('-output', help='Path to the output file', required=True)
    args = parser.parse_args()

    process(args.folder,args.output)

if __name__ == '__main__':
    main()