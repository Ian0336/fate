import  sxtwl
import sys
type = sys.getfilesystemencoding()
Gan = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
Zhi = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
ShX = ["鼠", "牛", "虎", "兔", "龍", "蛇", "馬", "羊", "猴", "雞", "狗", "豬"]
numCn = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]
jqmc = ["冬至", "小寒", "大寒", "立春", "雨水", "惊蛰", "春分", "清明", "谷雨", "立夏", "小滿", "芒種", "夏至", "小暑", "大暑", "立秋", "處暑","白露", "秋分", "寒露", "霜降", "立冬", "小雪", "大雪"]
ymc = ["十一", "十二", "正", "二", "三", "四", "五", "六", "七", "八", "九", "十" ]
rmc = ["初一", "初二", "初三", "初四", "初五", "初六", "初七", "初八", "初九", "初十", "十一", "十二", "十三", "十四", "十五", "十六", "十七", "十八", "十九", "二十", "廿一", "廿二", "廿三", "廿四", "廿五", "廿六", "廿七", "廿八", "廿九", "三十", "卅一"]


lunar = sxtwl.Lunar()
listg=[]
listz=[]
listy=[]
listm=[]
listd=[]
listh=[]  #第一个参数为生日的日天干,参数二为出生的时间(小时)





def check():
        g=listg
        z=listz
        
        if g[2]==0:
            for i in range(4):
                if z[i]==1 or z[i]==7:
                    if i==0: listy.append("天乙貴人")
                    elif i==1: listm.append("天乙貴人")
                    elif i==2: listd.append("天乙貴人")
                    else: listh.append("天乙貴人")
                if z[i]==5:
                    if i==0: listy.append("文昌")
                    elif i==1: listm.append("文昌")
                    elif i==2: listd.append("文昌")
                    else: listh.append("文昌")
                if z[i]==2:
                    if i==0: listy.append("十天祿")
                    elif i==1: listm.append("十天祿")
                    elif i==2: listd.append("十天祿")
                    else: listh.append("十天祿")
                if z[i]==3:
                    if i==0: listy.append("羊刃")
                    elif i==1: listm.append("羊刃")
                    elif i==2: listd.append("羊刃")
                    else: listh.append("羊刃")
                if z[i]==6:
                    if i==0: listy.append("紅艷煞")
                    elif i==1: listm.append("紅艷煞")
                    elif i==2: listd.append("紅艷煞")
                    else: listh.append("紅艷煞")
                if z[i]==9:
                    if i==0: listy.append("飛刃")
                    elif i==1: listm.append("飛刃")
                    elif i==2: listd.append("飛刃")
                    else: listh.append("飛刃")
        if g[2]==1:
            for i in range(4):
                if z[i]==0 or z[i]==8:
                    if i==0: listy.append("天乙貴人")
                    elif i==1: listm.append("天乙貴人")
                    elif i==2: listd.append("天乙貴人")
                    else: listh.append("天乙貴人")
                if z[i]==6:
                    if i==0: listy.append("文昌")
                    elif i==1: listm.append("文昌")
                    elif i==2: listd.append("文昌")
                    else: listh.append("文昌")
                if z[i]==3:
                    if i==0: listy.append("十天祿")
                    elif i==1: listm.append("十天祿")
                    elif i==2: listd.append("十天祿")
                    else: listh.append("十天祿")
                if z[i]==4:
                    if i==0: listy.append("羊刃")
                    elif i==1: listm.append("羊刃")
                    elif i==2: listd.append("羊刃")
                    else: listh.append("羊刃")
                if z[i]==6:
                    if i==0: listy.append("紅艷煞")
                    elif i==1: listm.append("紅艷煞")
                    elif i==2: listd.append("紅艷煞")
                    else: listh.append("紅艷煞")
                if z[i]==10:
                    if i==0: listy.append("飛刃")
                    elif i==1: listm.append("飛刃")
                    elif i==2: listd.append("飛刃")
                    else: listh.append("飛刃")
        if g[2]==2:
            for i in range(4):
                if z[i]==11 or z[i]==9:
                    if i==0: listy.append("天乙貴人")
                    elif i==1: listm.append("天乙貴人")
                    elif i==2: listd.append("天乙貴人")
                    else: listh.append("天乙貴人")
                if z[i]==8:
                    if i==0: listy.append("文昌")
                    elif i==1: listm.append("文昌")
                    elif i==2: listd.append("文昌")
                    else: listh.append("文昌")
                if z[i]==5:
                    if i==0: listy.append("十天祿")
                    elif i==1: listm.append("十天祿")
                    elif i==2: listd.append("十天祿")
                    else: listh.append("十天祿")
                if z[i]==6:
                    if i==0: listy.append("羊刃")
                    elif i==1: listm.append("羊刃")
                    elif i==2: listd.append("羊刃")
                    else: listh.append("羊刃")
                if z[i]==2:
                    if i==0: listy.append("紅艷煞")
                    elif i==1: listm.append("紅艷煞")
                    elif i==2: listd.append("紅艷煞")
                    else: listh.append("紅艷煞")
                if z[i]==0:
                    if i==0: listy.append("飛刃")
                    elif i==1: listm.append("飛刃")
                    elif i==2: listd.append("飛刃")
                    else: listh.append("飛刃")
        if g[2]==3:
            for i in range(4):
                if z[i]==11 or z[i]==9:
                    if i==0: listy.append("天乙貴人")
                    elif i==1: listm.append("天乙貴人")
                    elif i==2: listd.append("天乙貴人")
                    else: listh.append("天乙貴人")
                if z[i]==9:
                    if i==0: listy.append("文昌")
                    elif i==1: listm.append("文昌")
                    elif i==2: listd.append("文昌")
                    else: listh.append("文昌")
                if z[i]==6:
                    if i==0: listy.append("十天祿")
                    elif i==1: listm.append("十天祿")
                    elif i==2: listd.append("十天祿")
                    else: listh.append("十天祿")
                if z[i]==7:
                    if i==0: listy.append("羊刃")
                    elif i==1: listm.append("羊刃")
                    elif i==2: listd.append("羊刃")
                    else: listh.append("羊刃")
                if z[i]==7:
                    if i==0: listy.append("紅艷煞")
                    elif i==1: listm.append("紅艷煞")
                    elif i==2: listd.append("紅艷煞")
                    else: listh.append("紅艷煞")
                if z[i]==1:
                    if i==0: listy.append("飛刃")
                    elif i==1: listm.append("飛刃")
                    elif i==2: listd.append("飛刃")
                    else: listh.append("飛刃")
        if g[2]==4:
            for i in range(4):
                if z[i]==7 or z[i]==1:
                    if i==0: listy.append("天乙貴人")
                    elif i==1: listm.append("天乙貴人")
                    elif i==2: listd.append("天乙貴人")
                    else: listh.append("天乙貴人")
                if z[i]==8:
                    if i==0: listy.append("文昌")
                    elif i==1: listm.append("文昌")
                    elif i==2: listd.append("文昌")
                    else: listh.append("文昌")
                if z[i]==5:
                    if i==0: listy.append("十天祿")
                    elif i==1: listm.append("十天祿")
                    elif i==2: listd.append("十天祿")
                    else: listh.append("十天祿")
                if z[i]==6:
                    if i==0: listy.append("羊刃")
                    elif i==1: listm.append("羊刃")
                    elif i==2: listd.append("羊刃")
                    else: listh.append("羊刃")
                if z[i]==4:
                    if i==0: listy.append("紅艷煞")
                    elif i==1: listm.append("紅艷煞")
                    elif i==2: listd.append("紅艷煞")
                    else: listh.append("紅艷煞")
                if z[i]==0:
                    if i==0: listy.append("飛刃")
                    elif i==1: listm.append("飛刃")
                    elif i==2: listd.append("飛刃")
                    else: listh.append("飛刃")
        if g[2]==5:
            for i in range(4):
                if z[i]==0 or z[i]==8:
                    if i==0: listy.append("天乙貴人")
                    elif i==1: listm.append("天乙貴人")
                    elif i==2: listd.append("天乙貴人")
                    else: listh.append("天乙貴人")
                if z[i]==9:
                    if i==0: listy.append("文昌")
                    elif i==1: listm.append("文昌")
                    elif i==2: listd.append("文昌")
                    else: listh.append("文昌")
                if z[i]==6:
                    if i==0: listy.append("十天祿")
                    elif i==1: listm.append("十天祿")
                    elif i==2: listd.append("十天祿")
                    else: listh.append("十天祿")
                if z[i]==7:
                    if i==0: listy.append("羊刃")
                    elif i==1: listm.append("羊刃")
                    elif i==2: listd.append("羊刃")
                    else: listh.append("羊刃")
                if z[i]==4:
                    if i==0: listy.append("紅艷煞")
                    elif i==1: listm.append("紅艷煞")
                    elif i==2: listd.append("紅艷煞")
                    else: listh.append("紅艷煞")
                if z[i]==1:
                    if i==0: listy.append("飛刃")
                    elif i==1: listm.append("飛刃")
                    elif i==2: listd.append("飛刃")
                    else: listh.append("飛刃")
        if g[2]==6:
            for i in range(4):
                if z[i]==1 or z[i]==7:
                    if i==0: listy.append("天乙貴人")
                    elif i==1: listm.append("天乙貴人")
                    elif i==2: listd.append("天乙貴人")
                    else: listh.append("天乙貴人")
                if z[i]==11:
                    if i==0: listy.append("文昌")
                    elif i==1: listm.append("文昌")
                    elif i==2: listd.append("文昌")
                    else: listh.append("文昌")
                if z[i]==8:
                    if i==0: listy.append("十天祿")
                    elif i==1: listm.append("十天祿")
                    elif i==2: listd.append("十天祿")
                    else: listh.append("十天祿")
                if z[i]==9:
                    if i==0: listy.append("羊刃")
                    elif i==1: listm.append("羊刃")
                    elif i==2: listd.append("羊刃")
                    else: listh.append("羊刃")
                if z[i]==10:
                    if i==0: listy.append("紅艷煞")
                    elif i==1: listm.append("紅艷煞")
                    elif i==2: listd.append("紅艷煞")
                    else: listh.append("紅艷煞")
                if z[i]==3:
                    if i==0: listy.append("飛刃")
                    elif i==1: listm.append("飛刃")
                    elif i==2: listd.append("飛刃")
                    else: listh.append("飛刃")
        if g[2]==7:
            for i in range(4):
                if z[i]==2 or z[i]==6:
                    if i==0: listy.append("天乙貴人")
                    elif i==1: listm.append("天乙貴人")
                    elif i==2: listd.append("天乙貴人")
                    else: listh.append("天乙貴人")
                if z[i]==0:
                    if i==0: listy.append("文昌")
                    elif i==1: listm.append("文昌")
                    elif i==2: listd.append("文昌")
                    else: listh.append("文昌")
                if z[i]==9:
                    if i==0: listy.append("十天祿")
                    elif i==1: listm.append("十天祿")
                    elif i==2: listd.append("十天祿")
                    else: listh.append("十天祿")
                if z[i]==10:
                    if i==0: listy.append("羊刃")
                    elif i==1: listm.append("羊刃")
                    elif i==2: listd.append("羊刃")
                    else: listh.append("羊刃")
                if z[i]==9:
                    if i==0: listy.append("紅艷煞")
                    elif i==1: listm.append("紅艷煞")
                    elif i==2: listd.append("紅艷煞")
                    else: listh.append("紅艷煞")
                if z[i]==4:
                    if i==0: listy.append("飛刃")
                    elif i==1: listm.append("飛刃")
                    elif i==2: listd.append("飛刃")
                    else: listh.append("飛刃")  
        if g[2]==8:
            for i in range(4):
                if z[i]==3 or z[i]==5:
                    if i==0: listy.append("天乙貴人")
                    elif i==1: listm.append("天乙貴人")
                    elif i==2: listd.append("天乙貴人")
                    else: listh.append("天乙貴人")
                if z[i]==2:
                    if i==0: listy.append("文昌")
                    elif i==1: listm.append("文昌")
                    elif i==2: listd.append("文昌")
                    else: listh.append("文昌")
                if z[i]==11:
                    if i==0: listy.append("十天祿")
                    elif i==1: listm.append("十天祿")
                    elif i==2: listd.append("十天祿")
                    else: listh.append("十天祿")
                if z[i]==0:
                    if i==0: listy.append("羊刃")
                    elif i==1: listm.append("羊刃")
                    elif i==2: listd.append("羊刃")
                    else: listh.append("羊刃")
                if z[i]==0:
                    if i==0: listy.append("紅艷煞")
                    elif i==1: listm.append("紅艷煞")
                    elif i==2: listd.append("紅艷煞")
                    else: listh.append("紅艷煞")
                if z[i]==6:
                    if i==0: listy.append("飛刃")
                    elif i==1: listm.append("飛刃")
                    elif i==2: listd.append("飛刃")
                    else: listh.append("飛刃")
        if g[2]==9:
            for i in range(4):
                if z[i]==5 or z[i]==3:
                    if i==0: listy.append("天乙貴人")
                    elif i==1: listm.append("天乙貴人")
                    elif i==2: listd.append("天乙貴人")
                    else: listh.append("天乙貴人")
                if z[i]==3:
                    if i==0: listy.append("文昌")
                    elif i==1: listm.append("文昌")
                    elif i==2: listd.append("文昌")
                    else: listh.append("文昌")
                if z[i]==0:
                    if i==0: listy.append("十天祿")
                    elif i==1: listm.append("十天祿")
                    elif i==2: listd.append("十天祿")
                    else: listh.append("十天祿")
                if z[i]==1:
                    if i==0: listy.append("羊刃")
                    elif i==1: listm.append("羊刃")
                    elif i==2: listd.append("羊刃")
                    else: listh.append("羊刃")
                if z[i]==8:
                    if i==0: listy.append("紅艷煞")
                    elif i==1: listm.append("紅艷煞")
                    elif i==2: listd.append("紅艷煞")
                    else: listh.append("紅艷煞")
                if z[i]==7:
                    if i==0: listy.append("飛刃")
                    elif i==1: listm.append("飛刃")
                    elif i==2: listd.append("飛刃")
                    else: listh.append("飛刃")
        
        
        
        
        if z[2]==0:
             for i in range(4):
                if z[i]==0:
                    if i==0: listy.append("將星")
                    elif i==1: listm.append("將星")
                    elif i==2: listd.append("將星")
                    else: listh.append("將星")
                if z[i]==4:
                    if i==0: listy.append("華蓋")
                    elif i==1: listm.append("華蓋")
                    elif i==2: listd.append("華蓋")
                    else: listh.append("華蓋")
                if z[i]==2:
                    if i==0: listy.append("驛馬")
                    elif i==1: listm.append("驛馬")
                    elif i==2: listd.append("驛馬")
                    else: listh.append("驛馬")
                if z[i]==5:
                    if i==0: listy.append("劫煞")
                    elif i==1: listm.append("劫煞")
                    elif i==2: listd.append("劫煞")
                    else: listh.append("劫煞")
                if z[i]==11:
                    if i==0: listy.append("亡神")
                    elif i==1: listm.append("亡神")
                    elif i==2: listd.append("亡神")
                    else: listh.append("亡神")
                if z[i]==9:
                    if i==0: listy.append("桃花")
                    elif i==1: listm.append("桃花")
                    elif i==2: listd.append("桃花")
                    else: listh.append("桃花")
        if z[2]==1:
             for i in range(4):
                if z[i]==9:
                    if i==0: listy.append("將星")
                    elif i==1: listm.append("將星")
                    elif i==2: listd.append("將星")
                    else: listh.append("將星")
                if z[i]==1:
                    if i==0: listy.append("華蓋")
                    elif i==1: listm.append("華蓋")
                    elif i==2: listd.append("華蓋")
                    else: listh.append("華蓋")
                if z[i]==11:
                    if i==0: listy.append("驛馬")
                    elif i==1: listm.append("驛馬")
                    elif i==2: listd.append("驛馬")
                    else: listh.append("驛馬")
                if z[i]==2:
                    if i==0: listy.append("劫煞")
                    elif i==1: listm.append("劫煞")
                    elif i==2: listd.append("劫煞")
                    else: listh.append("劫煞")
                if z[i]==8:
                    if i==0: listy.append("亡神")
                    elif i==1: listm.append("亡神")
                    elif i==2: listd.append("亡神")
                    else: listh.append("亡神")
                if z[i]==6:
                    if i==0: listy.append("桃花")
                    elif i==1: listm.append("桃花")
                    elif i==2: listd.append("桃花")
                    else: listh.append("桃花")
        if z[2]==2:
             for i in range(4):
                if z[i]==6:
                    if i==0: listy.append("將星")
                    elif i==1: listm.append("將星")
                    elif i==2: listd.append("將星")
                    else: listh.append("將星")
                if z[i]==1:
                    if i==0: listy.append("華蓋")
                    elif i==1: listm.append("華蓋")
                    elif i==2: listd.append("華蓋")
                    else: listh.append("華蓋")
                if z[i]==8:
                    if i==0: listy.append("驛馬")
                    elif i==1: listm.append("驛馬")
                    elif i==2: listd.append("驛馬")
                    else: listh.append("驛馬")
                if z[i]==11:
                    if i==0: listy.append("劫煞")
                    elif i==1: listm.append("劫煞")
                    elif i==2: listd.append("劫煞")
                    else: listh.append("劫煞")
                if z[i]==5:
                    if i==0: listy.append("亡神")
                    elif i==1: listm.append("亡神")
                    elif i==2: listd.append("亡神")
                    else: listh.append("亡神")
                if z[i]==3:
                    if i==0: listy.append("桃花")
                    elif i==1: listm.append("桃花")
                    elif i==2: listd.append("桃花")
                    else: listh.append("桃花")    
        if z[2]==3:
             for i in range(4):
                if z[i]==3:
                    if i==0: listy.append("將星")
                    elif i==1: listm.append("將星")
                    elif i==2: listd.append("將星")
                    else: listh.append("將星")
                if z[i]==7:
                    if i==0: listy.append("華蓋")
                    elif i==1: listm.append("華蓋")
                    elif i==2: listd.append("華蓋")
                    else: listh.append("華蓋")
                if z[i]==5:
                    if i==0: listy.append("驛馬")
                    elif i==1: listm.append("驛馬")
                    elif i==2: listd.append("驛馬")
                    else: listh.append("驛馬")
                if z[i]==8:
                    if i==0: listy.append("劫煞")
                    elif i==1: listm.append("劫煞")
                    elif i==2: listd.append("劫煞")
                    else: listh.append("劫煞")
                if z[i]==2:
                    if i==0: listy.append("亡神")
                    elif i==1: listm.append("亡神")
                    elif i==2: listd.append("亡神")
                    else: listh.append("亡神")
                if z[i]==0:
                    if i==0: listy.append("桃花")
                    elif i==1: listm.append("桃花")
                    elif i==2: listd.append("桃花")
                    else: listh.append("桃花")
        if z[2]==4:
             for i in range(4):
                if z[i]==0:
                    if i==0: listy.append("將星")
                    elif i==1: listm.append("將星")
                    elif i==2: listd.append("將星")
                    else: listh.append("將星")
                if z[i]==4:
                    if i==0: listy.append("華蓋")
                    elif i==1: listm.append("華蓋")
                    elif i==2: listd.append("華蓋")
                    else: listh.append("華蓋")
                if z[i]==2:
                    if i==0: listy.append("驛馬")
                    elif i==1: listm.append("驛馬")
                    elif i==2: listd.append("驛馬")
                    else: listh.append("驛馬")
                if z[i]==5:
                    if i==0: listy.append("劫煞")
                    elif i==1: listm.append("劫煞")
                    elif i==2: listd.append("劫煞")
                    else: listh.append("劫煞")
                if z[i]==11:
                    if i==0: listy.append("亡神")
                    elif i==1: listm.append("亡神")
                    elif i==2: listd.append("亡神")
                    else: listh.append("亡神")
                if z[i]==9:
                    if i==0: listy.append("桃花")
                    elif i==1: listm.append("桃花")
                    elif i==2: listd.append("桃花")
                    else: listh.append("桃花")
        if z[2]==5:
             for i in range(4):
                if z[i]==9:
                    if i==0: listy.append("將星")
                    elif i==1: listm.append("將星")
                    elif i==2: listd.append("將星")
                    else: listh.append("將星")
                if z[i]==1:
                    if i==0: listy.append("華蓋")
                    elif i==1: listm.append("華蓋")
                    elif i==2: listd.append("華蓋")
                    else: listh.append("華蓋")
                if z[i]==11:
                    if i==0: listy.append("驛馬")
                    elif i==1: listm.append("驛馬")
                    elif i==2: listd.append("驛馬")
                    else: listh.append("驛馬")
                if z[i]==2:
                    if i==0: listy.append("劫煞")
                    elif i==1: listm.append("劫煞")
                    elif i==2: listd.append("劫煞")
                    else: listh.append("劫煞")
                if z[i]==8:
                    if i==0: listy.append("亡神")
                    elif i==1: listm.append("亡神")
                    elif i==2: listd.append("亡神")
                    else: listh.append("亡神")
                if z[i]==6:
                    if i==0: listy.append("桃花")
                    elif i==1: listm.append("桃花")
                    elif i==2: listd.append("桃花")
                    else: listh.append("桃花")
        if z[2]==6:
             for i in range(4):
                if z[i]==6:
                    if i==0: listy.append("將星")
                    elif i==1: listm.append("將星")
                    elif i==2: listd.append("將星")
                    else: listh.append("將星")
                if z[i]==10:
                    if i==0: listy.append("華蓋")
                    elif i==1: listm.append("華蓋")
                    elif i==2: listd.append("華蓋")
                    else: listh.append("華蓋")
                if z[i]==8:
                    if i==0: listy.append("驛馬")
                    elif i==1: listm.append("驛馬")
                    elif i==2: listd.append("驛馬")
                    else: listh.append("驛馬")
                if z[i]==11:
                    if i==0: listy.append("劫煞")
                    elif i==1: listm.append("劫煞")
                    elif i==2: listd.append("劫煞")
                    else: listh.append("劫煞")
                if z[i]==5:
                    if i==0: listy.append("亡神")
                    elif i==1: listm.append("亡神")
                    elif i==2: listd.append("亡神")
                    else: listh.append("亡神")
                if z[i]==3:
                    if i==0: listy.append("桃花")
                    elif i==1: listm.append("桃花")
                    elif i==2: listd.append("桃花")
                    else: listh.append("桃花")
        if z[2]==7:
             for i in range(4):
                if z[i]==3:
                    if i==0: listy.append("將星")
                    elif i==1: listm.append("將星")
                    elif i==2: listd.append("將星")
                    else: listh.append("將星")
                if z[i]==7:
                    if i==0: listy.append("華蓋")
                    elif i==1: listm.append("華蓋")
                    elif i==2: listd.append("華蓋")
                    else: listh.append("華蓋")
                if z[i]==5:
                    if i==0: listy.append("驛馬")
                    elif i==1: listm.append("驛馬")
                    elif i==2: listd.append("驛馬")
                    else: listh.append("驛馬")
                if z[i]==8:
                    if i==0: listy.append("劫煞")
                    elif i==1: listm.append("劫煞")
                    elif i==2: listd.append("劫煞")
                    else: listh.append("劫煞")
                if z[i]==2:
                    if i==0: listy.append("亡神")
                    elif i==1: listm.append("亡神")
                    elif i==2: listd.append("亡神")
                    else: listh.append("亡神")
                if z[i]==0:
                    if i==0: listy.append("桃花")
                    elif i==1: listm.append("桃花")
                    elif i==2: listd.append("桃花")
                    else: listh.append("桃花")
        if z[2]==8:
             for i in range(4):
                if z[i]==0:
                    if i==0: listy.append("將星")
                    elif i==1: listm.append("將星")
                    elif i==2: listd.append("將星")
                    else: listh.append("將星")
                if z[i]==4:
                    if i==0: listy.append("華蓋")
                    elif i==1: listm.append("華蓋")
                    elif i==2: listd.append("華蓋")
                    else: listh.append("華蓋")
                if z[i]==2:
                    if i==0: listy.append("驛馬")
                    elif i==1: listm.append("驛馬")
                    elif i==2: listd.append("驛馬")
                    else: listh.append("驛馬")
                if z[i]==5:
                    if i==0: listy.append("劫煞")
                    elif i==1: listm.append("劫煞")
                    elif i==2: listd.append("劫煞")
                    else: listh.append("劫煞")
                if z[i]==11:
                    if i==0: listy.append("亡神")
                    elif i==1: listm.append("亡神")
                    elif i==2: listd.append("亡神")
                    else: listh.append("亡神")
                if z[i]==9:
                    if i==0: listy.append("桃花")
                    elif i==1: listm.append("桃花")
                    elif i==2: listd.append("桃花")
                    else: listh.append("桃花")
        if z[2]==9:
             for i in range(4):
                if z[i]==9:
                    if i==0: listy.append("將星")
                    elif i==1: listm.append("將星")
                    elif i==2: listd.append("將星")
                    else: listh.append("將星")
                if z[i]==1:
                    if i==0: listy.append("華蓋")
                    elif i==1: listm.append("華蓋")
                    elif i==2: listd.append("華蓋")
                    else: listh.append("華蓋")
                if z[i]==11:
                    if i==0: listy.append("驛馬")
                    elif i==1: listm.append("驛馬")
                    elif i==2: listd.append("驛馬")
                    else: listh.append("驛馬")
                if z[i]==2:
                    if i==0: listy.append("劫煞")
                    elif i==1: listm.append("劫煞")
                    elif i==2: listd.append("劫煞")
                    else: listh.append("劫煞")
                if z[i]==8:
                    if i==0: listy.append("亡神")
                    elif i==1: listm.append("亡神")
                    elif i==2: listd.append("亡神")
                    else: listh.append("亡神")
                if z[i]==6:
                    if i==0: listy.append("桃花")
                    elif i==1: listm.append("桃花")
                    elif i==2: listd.append("桃花")
                    else: listh.append("桃花")
        if z[2]==10:
             for i in range(4):
                if z[i]==6:
                    if i==0: listy.append("將星")
                    elif i==1: listm.append("將星")
                    elif i==2: listd.append("將星")
                    else: listh.append("將星")
                if z[i]==10:
                    if i==0: listy.append("華蓋")
                    elif i==1: listm.append("華蓋")
                    elif i==2: listd.append("華蓋")
                    else: listh.append("華蓋")
                if z[i]==8:
                    if i==0: listy.append("驛馬")
                    elif i==1: listm.append("驛馬")
                    elif i==2: listd.append("驛馬")
                    else: listh.append("驛馬")
                if z[i]==11:
                    if i==0: listy.append("劫煞")
                    elif i==1: listm.append("劫煞")
                    elif i==2: listd.append("劫煞")
                    else: listh.append("劫煞")
                if z[i]==5:
                    if i==0: listy.append("亡神")
                    elif i==1: listm.append("亡神")
                    elif i==2: listd.append("亡神")
                    else: listh.append("亡神")
                if z[i]==3:
                    if i==0: listy.append("桃花")
                    elif i==1: listm.append("桃花")
                    elif i==2: listd.append("桃花")
                    else: listh.append("桃花")
        if z[2]==11:
             for i in range(4):
                if z[i]==3:
                    if i==0: listy.append("將星")
                    elif i==1: listm.append("將星")
                    elif i==2: listd.append("將星")
                    else: listh.append("將星")
                if z[i]==7:
                    if i==0: listy.append("華蓋")
                    elif i==1: listm.append("華蓋")
                    elif i==2: listd.append("華蓋")
                    else: listh.append("華蓋")
                if z[i]==5:
                    if i==0: listy.append("驛馬")
                    elif i==1: listm.append("驛馬")
                    elif i==2: listd.append("驛馬")
                    else: listh.append("驛馬")
                if z[i]==8:
                    if i==0: listy.append("劫煞")
                    elif i==1: listm.append("劫煞")
                    elif i==2: listd.append("劫煞")
                    else: listh.append("劫煞")
                if z[i]==2:
                    if i==0: listy.append("亡神")
                    elif i==1: listm.append("亡神")
                    elif i==2: listd.append("亡神")
                    else: listh.append("亡神")
                if z[i]==0:
                    if i==0: listy.append("桃花")
                    elif i==1: listm.append("桃花")
                    elif i==2: listd.append("桃花")
                    else: listh.append("桃花")
        
        
        
        
        if z[1]==0:
            if z[2]==5: listd.append("天德")
            elif g[2]==8: listd.append("月德")
        if z[1]==1:
            if g[2]==6: listd.append("天德")
            elif g[2]==6: listd.append("月德")
        if z[1]==2:
            if g[2]==3: listd.append("天德")
            elif g[2]==2: listd.append("月德")
        if z[1]==3:
            if z[2]==8: listd.append("天德")
            elif g[2]==0: listd.append("月德")
        if z[1]==4:
            if g[2]==8: listd.append("天德")
            elif g[2]==8: listd.append("月德")    
        if z[1]==5:
            if g[2]==7: listd.append("天德")
            elif g[2]==6: listd.append("月德")   
        if z[1]==6:
            if z[2]==11: listd.append("天德")
            elif g[2]==2: listd.append("月德")
        if z[1]==7:
            if g[2]==0: listd.append("天德")
            elif g[2]==0: listd.append("月德")
        if z[1]==8:
            if g[2]==9: listd.append("天德")
            elif g[2]==8: listd.append("月德")
        if z[1]==9:
            if z[2]==2: listd.append("天德")
            elif g[2]==6: listd.append("月德")
        if z[1]==10:
            if g[2]==2: listd.append("天德")
            elif g[2]==2: listd.append("月德")    
        if z[1]==11:
            if g[2]==1: listd.append("天德")
            elif g[2]==0: listd.append("月德")   
            
            
            
            
        if z[0]==0 or z[0]==1 or z[0]==11: 
            for i in range(4):
                if z[i]==2:
                    if i==0: listy.append("孤辰")
                    elif i==1: listm.append("孤辰")
                    elif i==2: listd.append("孤辰")
                    else: listh.append("孤辰")
                if z[i]==10:
                    if i==0: listy.append("寡宿")
                    elif i==1: listm.append("寡宿")
                    elif i==2: listd.append("寡宿")
                    else: listh.append("寡宿")
        if z[0]==2 or z[0]==3 or z[0]==4:
            for i in range(4):
                if z[i]==5:
                    if i==0: listy.append("孤辰")
                    elif i==1: listm.append("孤辰")
                    elif i==2: listd.append("孤辰")
                    else: listh.append("孤辰")
                if z[i]==1:
                    if i==0: listy.append("寡宿")
                    elif i==1: listm.append("寡宿")
                    elif i==2: listd.append("寡宿")
                    else: listh.append("寡宿") 
        if z[0]==5 or z[0]==6 or z[0]==7:
            for i in range(4):
                if z[i]==8:
                    if i==0: listy.append("孤辰")
                    elif i==1: listm.append("孤辰")
                    elif i==2: listd.append("孤辰")
                    else: listh.append("孤辰")
                if z[i]==4:
                    if i==0: listy.append("寡宿")
                    elif i==1: listm.append("寡宿")
                    elif i==2: listd.append("寡宿")
                    else: listh.append("寡宿") 
        if z[0]==8 or z[0]==9 or z[0]==10:
            for i in range(4):
                if z[i]==11:
                    if i==0: listy.append("孤辰")
                    elif i==1: listm.append("孤辰")
                    elif i==2: listd.append("孤辰")
                    else: listh.append("孤辰")
                if z[i]==7:
                    if i==0: listy.append("寡宿")
                    elif i==1: listm.append("寡宿")
                    elif i==2: listd.append("寡宿")
                    else: listh.append("寡宿") 
                    
                    
                    
                    
        if z[0]==0 or z[0]==4 or z[0]==8:
            if z[1]==2:
                listm.append("男掃女家")
                   
            if z[1]==1:
                listm.append("女掃男家")
        if z[0]==1 or z[0]==5 or z[0]==9:
            if z[1]==7:
                listm.append("男掃女家")
            if z[1]==10:
                listm.append("女掃男家") 
        if z[0]==2 or z[0]==6 or z[0]==10:
            if z[1]==5:
                listm.append("男掃女家")
            if z[1]==8:
                listm.append("女掃男家")
        if z[0]==3 or z[0]==7 or z[0]==11:
            if z[1]==3:
                listm.append("男掃女家")
            if z[1]==9:
                listm.append("女掃男家")
                    
                    
                    
                    
        
        if 0 in g:
            if 4 in g:
                if 6 in g:
                    listy.append("天上三奇")
        if 1 in g:
            if 2 in g:
                if 3 in g:
                    listy.append("地上三奇")
        if 7 in g:
            if 8 in g:
                if 9 in g:
                    listy.append("人中三奇")
                    
                    
                    
        
            
        if g[2]==6 and z[2]==4: listy.append("魁罡")
        if g[2]==8 and z[2]==4: listy.append("魁罡")
        if g[2]==6 and z[2]==10: listy.append("魁罡")
        if g[2]==4 and z[2]==10: listy.append("魁罡")
        
        
        if g[2]==1 and z[2]==5: listy.append("孤鸞日")
        if g[2]==3 and z[2]==5: listy.append("孤鸞日")
        if g[2]==0 and z[2]==2: listy.append("孤鸞日")
        if g[2]==8 and z[2]==2: listy.append("孤鸞日")
        if g[2]==2 and z[2]==6: listy.append("孤鸞日")
        if g[2]==4 and z[2]==6: listy.append("孤鸞日")
        if g[2]==8 and z[2]==0: listy.append("孤鸞日")
        if g[2]==7 and z[2]==11: listy.append("孤鸞日")
        if g[2]==4 and z[2]==8: listy.append("孤鸞日")
        
        
        
def five_g(i):
    if(i==1 or i==0):return "木"
    if(i==3 or i==2):return "火"
    if(i==5 or i==4):return "土"
    if(i==7 or i==6):return "金"
    if(i==9 or i==8):return "水"
    
def five_z(i):
    if(i==3 or i==2):return "木"
    if(i==6 or i==5):return "火"
    if(i==4 or i==10 or i==1 or i==7):return "土"
    if(i==8 or i==9):return "金"
    if(i==1 or i==11):return "水"
    
        
def mm(year,month,date,hour):


    day = lunar.getDayBySolar(year, month, date)
    gz = lunar.getShiGz(day.Lday2.tg,  hour)


    listg.append(day.Lyear2.tg)
    listg.append(day.Lmonth2.tg)
    listg.append(day.Lday2.tg)
    listg.append(gz.tg)

    listz.append(day.Lyear2.dz)
    listz.append(day.Lmonth2.dz)
    listz.append(day.Lday2.dz)
    listz.append(gz.dz)
    check()
    listg.clear()
    listz.clear()
    listg.append(Gan[day.Lyear2.tg])
    listg.append(five_g(day.Lyear2.tg))
    listg.append(Gan[day.Lmonth2.tg])
    listg.append(five_g(day.Lmonth2.tg))
    listg.append(Gan[day.Lday2.tg])
    listg.append(five_g(day.Lday2.tg))
    listg.append(Gan[gz.tg])
    listg.append(five_g(gz.tg))

    listz.append(Zhi[day.Lyear2.dz])
    listz.append(five_z(day.Lyear2.dz))
    listz.append(Zhi[day.Lmonth2.dz])
    listz.append(five_z(day.Lmonth2.dz))
    listz.append(Zhi[day.Lday2.dz])
    listz.append(five_z(day.Lday2.dz))
    listz.append(Zhi[gz.dz])
    listz.append(five_z(gz.dz))
    
    print(f"年柱: {Gan[day.Lyear2.tg]}{Zhi[day.Lyear2.dz] }  >>{listy} ")
    print(f"月柱: {Gan[day.Lmonth2.tg]}{Zhi[day.Lmonth2.dz] }  >>{listm} ")
    print(f"日柱: {Gan[day.Lday2.tg]}{Zhi[day.Lday2.dz] } >>{listd} ")
    print(f"時柱: {Gan[gz.tg]}{Zhi[gz.dz] }  >>{listh} ")
    return
        
    
if __name__ == '__main__':
    
    mm(2003,3,6,12)
    
        
        
