#define  DP_POWER 1 // 开关 |
#define  DP_MODE 2 // 除湿模式 | range:['2', '4', '5', '6', '7']
#define  DP_HUMIDITY 4 // 除湿设置 | min:35 max:80
#define  DP_WINDSPEED 6 // 风速 | range:['1', '2', '3']
#define  DP_FAULT 11 // 故障告警 | label:['E1', 'E2', 'EH', 'E5', 'water_full', 'overload']
#define  DP_GET_TEMP 103 // 室内摄氏温度 | min:0 max:99
#define  DP_GET_HUM 104 // 环境湿度 | min:0 max:99
#define  DP_FUNCTAG 105 // 机型位 | label:['0', '1', '2', '3', '4', '5']
#define  DP_LOCK_BUTTON 106 // 锁键 |
#define  DP_HIDE_BUTTON 107 // 隐显键 |
#define  DP_CLEAN_BUTTON 108 // 清洗键 |
#define  DP_PUMP_BUTTON 109 // 泵浦键 |
#define  DP_SWING_BUTTON 110 // 摆风 |
#define  DP_UV_ION 111 // 负离子 |
#define  DP_GET_TEMP_F 112 // 室内华氏温度 | min:0 max:99
#define  DP_F_C 113 // 温标切换 |
