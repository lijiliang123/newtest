"""
该程序实现：人民币的大写金额
by Thomas Lee on 2019-10-22
   Modified on 2019-10-23

数级的划分标准，四位一个数级
1-4:  个级
5-8： 万级
9-12：亿级
"""

#构建字典数据结构，存储0~9的大写字符
daxie = {0: '零', 1: '壹', 2: '贰', 3: '叁', 4: '肆', 5: '伍',
         6: '陆', 7: '柒', 8: '捌', 9: '玖'}
#构建列表数据结构，存储计数单位，因为按数级分级时，每级只有4个数位，个、十、百、千，个可省略，因后面加“元”
#通过list的区间操作方法[a:b]，实现级数的划分
shuwei = ['', '十', '佰', '千']


#主函数定义
def trans_to_dx(number):
    result1 = ''  #存储亿级数字的大写金额--亿级
    result2 = ''  #存储亿级数字的大写金额--万级
    result3 = ''  #存储亿级数字的大写金额--个级
    result4 = ''  #存储万级数字的大写金额--万级
    result5 = ''  #存储万级数字的大写金额--个级
    result6 = ''  #存储个级数字的大写金额--个级
    resulth1 = ''  #亿级数，亿级位结束后，带上'亿'位
    resulth2 = ''  #亿级数，万级位结束后，带上'万'位
    resulth3 = ''  #亿级数，个级位结束后，带上'元'位
    resulth4 = ''  #万级数，万级位结束后，带上'万'位
    resulth5 = ''  #万级数，个级位结束后，带上'元'位
    resulth6 = ''  #个级数，个级位结束后，带上'元'位
    resulth7 = ''

    num_int = str(int(float(number)))  #获取输入数字的整数部分,转为str，因str才能转化为list对象
    num_digt = str(round((float(number)-int(float(number)))*100))  #获取输入数字的小数部分，只取2位小数，四舍五入

    nmls = list(num_int)  #输入的数值的整数部分转为list对象存放，便于运用list区间方法截取数级
    dgls = list(num_digt)  #输入的数值的小数部分转为list对象存放

    if len(nmls) > 12:
        print('数字太大，暂不支持！系统返回 None.')
        return

    #以下是亿级数的判断
    elif len(nmls) >= 9:
        subls1 = nmls[:-8]  #亿级数位截取，区间不包括右端数位，实际截取:右数第9位至左边第1位
        for i in range(len(subls1)):
            result1 = result1 + daxie[int(subls1[i])] + shuwei[len(subls1)-i-1]
        resulth1 = result1 + '亿'  #亿级数位结束后，加上'亿'级数分割符
        subls2 = nmls[-8:-4]  #万级数位截取, 实际截取:右数第5位至右数第8位
        for i in range(len(subls2)):
            result2 = result2 + daxie[int(subls2[i])] + shuwei[len(subls2)-i-1]
        resulth2 = result2 + '万'  #万级数位结束后，加上'万'级数分割符
        subls3 = nmls[-4:]  #个级数位截取，实际截取:右数第1位至右数第4位
        for i in range(len(subls3)):
            result3 = result3 + daxie[int(subls3[i])] + shuwei[len(subls3)-i-1]
        resulth3 = result3 + '元'  #个级数位结束后，加上'元'级数分割符

    #以下是万级数的判断
    elif len(nmls) >= 5:
        subls4 = nmls[:-4]
        for i in range(len(subls4)):
            result4 = result4 + daxie[int(subls4[i])] + shuwei[len(subls4)-i-1]
        resulth4 = result4 + '万'
        subls5 = nmls[-4:]
        for i in range(len(subls5)):
            result5 = result5 + daxie[int(subls5[i])] + shuwei[len(subls5)-i-1]
        resulth5 = result5 + '元'

    #以下是个级数的判断
    else:
        subls6 = nmls[:]  #代表列表元素全部取出
        for i in range(len(subls6)):
            result6 = result6 + daxie[int(subls6[i])] + shuwei[len(subls6)-i-1]
        resulth6 = result6 + '元'

    #以下是小数位的角、分的判断
    if len(dgls) == 0:
        resulth7 = ''
    elif len(dgls) == 1:
        resulth7 = daxie[int(dgls[0])] + '角' + '零分'
    else:
        resulth7 = daxie[int(dgls[0])] + '角' + daxie[int(dgls[1])] + '分'

    return resulth1 + resulth2 + resulth3 + resulth4 + resulth5 + resulth6 + resulth7


num = input('请输入一个数字:')
print('您输入的数字转为大写是：', trans_to_dx(num))




