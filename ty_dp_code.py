# -*- coding: UTF-8 -*-
import sys
import os
import json

# 属性里需要拉取的字段
property_list =["min","max","range","label"]

dp_json = [{"attr":1,"canTrigger":True,"code":"Power","defaultRecommend":False,"defaultValue":"False","desc":"0 关机\n1 开机","editPermission":False,"executable":True,"extContent":"","iconname":"icon-dp_power","id":1,"mode":"rw","name":"开关","property":{"type":"bool"},"type":"obj"},{"attr":0,"canTrigger":True,"code":"mode","defaultRecommend":False,"defaultValue":"2","desc":"2.SLEEPING   (55%湿度)\n4.LIVING   (50%湿度)\n5.BASEMENT   (45%湿度)\n6.CONTINUOUS   (连续模式)\n7.自由模式   (35%-80%)","editPermission":False,"executable":True,"extContent":"","iconname":"icon-dp_mode","id":2,"mode":"rw","name":"除湿模式","property":{"range":["2","4","5","6","7"],"type":"enum"},"type":"obj"},{"attr":0,"canTrigger":True,"code":"humidity","defaultRecommend":False,"defaultValue":"35","desc":"","editPermission":False,"executable":True,"extContent":"","iconname":"icon-dp_wash","id":4,"mode":"rw","name":"除湿设置","property":{"unit":"％","min":35,"max":80,"scale":0,"step":5,"type":"value"},"type":"obj"},{"attr":0,"canTrigger":True,"code":"windspeed","defaultRecommend":False,"defaultValue":"1","desc":"1：低风\n2：中风\n3：高风","editPermission":False,"executable":True,"extContent":"","iconname":"icon-dp_wind","id":6,"mode":"rw","name":"风速","property":{"range":["1","2","3"],"type":"enum"},"type":"obj"},{"attr":0,"canTrigger":True,"code":"fault","defaultRecommend":False,"defaultValue":"0","desc":"1：E1：排气管温传感器\n2：E2：盘管温传感器\n3：EH：湿度传感器\n4：E5：水泵故障:\n5：water_full：水满\n6：overload：过流保护","editPermission":False,"executable":True,"extContent":"","iconname":"icon-dp_warming","id":11,"mode":"ro","name":"故障告警","property":{"label":["E1","E2","EH","E5","water_full","overload"],"type":"bitmap","maxlen":6},"scope":"fault","type":"obj"},{"attr":0,"canTrigger":True,"code":"get_temp","defaultRecommend":False,"defaultValue":"0","desc":"当前设备温度","editPermission":False,"executable":True,"extContent":"","id":103,"mode":"ro","name":"室内摄氏温度","property":{"unit":"摄氏度","min":0,"max":99,"scale":0,"step":1,"type":"value"},"type":"obj"},{"attr":0,"canTrigger":True,"code":"get_hum","defaultRecommend":False,"defaultValue":"0","desc":"获取当前设备的湿度测量值","editPermission":False,"executable":True,"extContent":"","id":104,"mode":"ro","name":"环境湿度","property":{"unit":"%","min":0,"max":99,"scale":0,"step":1,"type":"value"},"type":"obj"},{"attr":0,"canTrigger":True,"code":"funcTag","defaultRecommend":False,"defaultValue":"0","desc":"第一位：UV ION功能 0：无、1：有 \n第二位：UV ION机型 0：无、1：有 \n第三位：0：摄氏度、1：华氏度 \n第四位：0：二档风机型、1：三档风机型 \n第五位：0：仅除湿模式、1：D025,、D026机型\n第六位：0：无摆风、1：有摆风","editPermission":False,"executable":True,"extContent":"","id":105,"mode":"ro","name":"机型位","property":{"label":["0","1","2","3","4","5"],"type":"bitmap","maxlen":6},"scope":"fault","type":"obj"},{"attr":0,"canTrigger":True,"code":"lock_button","defaultRecommend":False,"defaultValue":"False","desc":"","editPermission":False,"executable":True,"extContent":"","id":106,"mode":"rw","name":"锁键","property":{"type":"bool"},"type":"obj"},{"attr":0,"canTrigger":True,"code":"hide_button","defaultRecommend":False,"defaultValue":"False","desc":"","editPermission":False,"executable":True,"extContent":"","id":107,"mode":"rw","name":"隐显键","property":{"type":"bool"},"type":"obj"},{"attr":0,"canTrigger":True,"code":"clean_button","defaultRecommend":False,"defaultValue":"False","desc":"","editPermission":False,"executable":True,"extContent":"","id":108,"mode":"rw","name":"清洗键","property":{"type":"bool"},"type":"obj"},{"attr":0,"canTrigger":True,"code":"pump_button","defaultRecommend":False,"defaultValue":"False","desc":"","editPermission":False,"executable":True,"extContent":"","id":109,"mode":"rw","name":"泵浦键","property":{"type":"bool"},"type":"obj"},{"attr":0,"canTrigger":True,"code":"swing_button","defaultRecommend":False,"defaultValue":"False","desc":"关闭：无摆风、打开：有摆风","editPermission":False,"executable":True,"extContent":"","id":110,"mode":"rw","name":"摆风","property":{"type":"bool"},"type":"obj"},{"attr":0,"canTrigger":True,"code":"UV_ION","defaultRecommend":False,"defaultValue":"False","desc":"","editPermission":False,"executable":True,"extContent":"","id":111,"mode":"rw","name":"负离子","property":{"type":"bool"},"type":"obj"},{"attr":0,"canTrigger":True,"code":"get_temp_F","defaultRecommend":False,"defaultValue":"0","desc":"","editPermission":False,"executable":True,"extContent":"","id":112,"mode":"rw","name":"室内华氏温度","property":{"unit":"华氏度","min":0,"max":99,"scale":0,"step":1,"type":"value"},"type":"obj"},{"attr":0,"canTrigger":True,"code":"F_C","defaultRecommend":False,"defaultValue":"False","desc":"dp 105中第三位：\n上报1时：切换成华氏度\n上报0时：切换成摄氏度","editPermission":False,"executable":True,"extContent":"","id":113,"mode":"rw","name":"温标切换","property":{"type":"bool"},"type":"obj"}]

def dp_to_code():
    """使用本地列表dp_json"""
    myfile1 = open("dp.h", 'w',encoding='utf-8')

    for i in dp_json:
        json_str = json.dumps(i)
        json_obj=json.loads(json_str)

        #英文标示符
        code = str(json_obj["code"])
        code = code.upper()

        id =int(json_obj["id"])#DPID
        name=str(json_obj["name"])#名字
        mode=str(json_obj["mode"])#上下发模式

        # 备注
        desc = str(json_obj["desc"])
        desc=desc.replace("\n",",").strip()

        #属性
        property = json_obj["property"]
        pro_str=""
        for i in property_list:
            if i in property:
                #print(i, property[i], end=",")
                # pro_str = pro_str + i + str(property[i])
                pro_str = "%s %s %s"%(pro_str,i,str(property[i]))
                # print(pro_str)

        myfile1.write("#define  DP_%s %d // %s |%s\n"%(code,id,name,desc))

    print("finish")
    myfile1.close()


def dp_to_code_file():
    """读取json文件"""
    myfile1 = open("dp.h", 'w',encoding='utf-8')

    with open("dp.json","r",encoding='utf8')as fp:
        json_data = json.load(fp)
        # print('这是文件中的json数据：',json_data)
        print("type of json file", type(json_data))

    for json_obj in json_data:

        #英文标示符
        code = str(json_obj["code"])
        code = code.upper()

        id =int(json_obj["id"])#DPID
        name=str(json_obj["name"])#名字
        mode=str(json_obj["mode"])#上下发模式

        # 备注
        desc = str(json_obj["desc"])
        desc=desc.replace("\n",",").strip()

        #属性
        property = json_obj["property"]
        pro_str=""
        for i in property_list:
            if i in property:
                #print(i, property[i], end=",")
                # pro_str = pro_str + i + str(property[i])
                pro_str = "%s %s:%s"%(pro_str,i,str(property[i]))
                print(pro_str)

        myfile1.write("#define  DP_%s %d // %s |%s\n"%(code,id,name,pro_str))

    print("finish")
    # myfile1.close()

# dp_to_code()
dp_to_code_file()


