import os
import time
import zipfile


sourcefile=['"D:\\UNIX Learning Notes"','"D:\翼支付项目"']      #必须用双引号括住目录，因为目录名字有空格
target_dir='D:\\backup'                          # 没用双引号，因为该目录名字没有空格

# 目标存储目录不存在时，创建目录
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today=target_dir+\
      os.sep+time.strftime('%Y%m%d')              # \ 连接符，表明本行与下一行是不可分割的同一个语句
now=time.strftime('%H%M%S')
#target=today+os.sep+time.strftime('%Y%m%d')+now+'.zip'
target=today+os.sep+now+'.zip'

# 目标存储子目录不存在时，创建子目录
if not os.path.exists(today):
    os.mkdir(today)
print('子目录创建成功：',today)

# zip 命令拼装
zip_command='zip -r {0}  {1}'.format(target,' '.join(sourcefile))

print('Zip command is')
print(zip_command)
print('Running')
if os.system(zip_command)==0:
    print('Successful backup to',target)
else:
    print('Backup faliled.')

