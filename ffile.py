content='''
1. 先从网上下载jdk(jdk-1_5_0_02-linux-i586.rpm) ，推荐SUN的官方网站www.sun.com，下载后放在/home目录中，当然其它地方也行。
进入安装目录
#cd /home
#cp jdk-1_5_0_02-linux-i586.rpm /usr/local
#cd /usr/local
给所有用户添加可执行的权限
#chmod +x jdk-1_5_0_02-linux-i586.rpm.bin
#./jdk-1_5_0_02-linux-i586.rpm.bin
此时会生成文件jdk-1_5_0_02-linux-i586.rpm，同样给所有用户添加可执行的权限
#chmod +x jdk-1_5_0_02-linux-i586.rpm
安装程序
#rpm -ivh jdk-1_5_0_02-linux-i586.rpm
出现安装协议等，按接受即可。
2.设置环境变量。
#vi /etc/profile
在最后面加入
#set java environment
JAVA_HOME=/usr/java/jdk-1_5_0_02
CLASSPATH=.:＄JAVA_HOME/lib.tools.jar
PATH=＄JAVA_HOME/bin:＄PATH
export JAVA_HOME CLASSPATH PATH
保存退出。
要使JDK在所有的用户中使用，可以这样：
vi /etc/profile.d/java.sh
在新的java.sh中输入以下内容：
#set java environment
JAVA_HOME=/usr/java/jdk-1_5_0_02
CLASSPATH=.:＄JAVA_HOME/lib/tools.jar
PATH=＄JAVA_HOME/bin:＄PATH
export JAVA_HOME CLASSPATH PATH
保存退出，然后给java.sh分配权限：chmod 755 /etc/profile.d/java.sh

'''

'''
f=open('部署手册.txt','w')
print('部署手册.txt文件已创建')
f.write(content)
print('部署手册.txt文件内容成功写入')
f.close()
f=open('部署手册.txt')
while True:
    line=f.readline()
    if len(line)==0:
        break
    print(line,end='')
f.close()

'''
# 写入文件
with open('部署手册.txt', 'w') as f:
    f.write(content)


# 读出文件
with open('部署手册.txt', 'r') as f:
    nr = f.read()
    print(nr)
