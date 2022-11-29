Function new_role
	Dim num
	num = 0
    while 1:
        Dim intM,intN
        FindPic 1418, 904, 1500, 980, "Attachment:new_role_next2.png", "000000", 0, 0.7, intM, intN
        If intM > -1 And intN > -1 Then
            Tap intM + (Rnd() * 60) - 30, intN + (Rnd() * 60) - 30
            Delay ((Rnd() + 2) * 1000) 
            num = num + 1
            TracePrint "num is: ",num

            If num >= 7 Then 
            	FindPic 1405, 810, 1520, 870, "Attachment:1_5.png", "000000", 0, 0.8, intM, intN
        		TracePrint "1_5 出现问答 "
				If intM > -1 And intN > -1 Then 
					Delay ((Rnd() + 1) * 1000)
					Exit While
				End If
			End If 
		End If
    Wend
    Call answer_quest()
    Call 选择头像()
    Call 选择名字()
    Call 选择出生州()
    Call 首次招募()
	Call 编制部队()
	Call 快速分兵()
	Call 跳过剧情_黑()
	Call 回城()
	Delay ((Rnd() + 15) * 1000)
	Call 循环跳过剧情_黑()
	Call 选择主城_入城()
	Call 队伍选择1()
	Call 兵种选择()
	Call 小返回()
	Call 小小返回()
	Call 跳过剧情_黑()
	
	Call 选择目标领地_行军()
	Call 跳过剧情_黑()
	Call 回城()
	
//  关平 剧情
	Call 关平剧情()
	Call 队伍选择1()
	
	Call 下阵主将()
	Call 更换主将()
	Call 快速分兵()
	
	// todo 领取今日签到奖励 加入同盟 霸业剧情
    // 容错  连续多次点击返回按钮位置（如有偏差或剧情弹窗，可以用多次返回跳过）

End Function


Function answer_quest
	Dim num
	num = 0
	While 1
		TracePrint "answer times: ",num
        Dim intM,intN
        FindPic 1405, 810, 1520, 870, "Attachment:1_5.png", "000000", 0, 0.8, intM, intN
        If intM > -1 And intN > -1 Then 
//      	intM intN 1436 827,  	第一条选项 1336 327
			TracePrint "找到1_5坐标为：",intM,intN
        	Tap intM -100 + (Rnd() * 100) - 50, intN - 500 + (Rnd() * 30) - 15
            Delay ((Rnd() + 2) * 1000)
        End If
        
        FindPic 1405, 810, 1520, 870, "Attachment:2_5.png", "000000", 0, 0.8, intM, intN
        If intM > -1 And intN > -1 Then 
			TracePrint "找到2_5坐标为：",intM,intN
        	Tap intM -100 + (Rnd() * 100) - 50, intN - 500 + (Rnd() * 30) - 15
            Delay ((Rnd() + 2) * 1000)
        End If
               
        FindPic 1405, 810, 1520, 870, "Attachment:3_5.png", "000000", 0, 0.8, intM, intN
        If intM > -1 And intN > -1 Then 
			TracePrint "找到3_5坐标为：",intM,intN
        	Tap intM -100 + (Rnd() * 100) - 50, intN - 500 + (Rnd() * 30) - 15
            Delay ((Rnd() + 2) * 1000)
        End If

        FindPic 1405, 810, 1520, 870, "Attachment:4_5.png", "000000", 0, 0.8, intM, intN
        If intM > -1 And intN > -1 Then 
			TracePrint "找到4_5坐标为：",intM,intN
        	Tap intM -100 + (Rnd() * 100) - 50, intN - 500 + (Rnd() * 30) - 15
            Delay ((Rnd() + 2) * 1000)
        End If
                   
        FindPic 1405, 810, 1520, 870, "Attachment:5_5.png", "000000", 0, 0.8, intM, intN
        If intM > -1 And intN > -1 Then 
			TracePrint "找到5_5坐标为：",intM,intN
        	Tap intM -100 + (Rnd() * 100) - 50, intN - 500 + (Rnd() * 30) - 15
            Delay ((Rnd() + 2) * 1000)
        End If       
        
        num = num + 1
        If num >=1 Then
        	FindPic 1418, 904, 1500, 980, "Attachment:new_role_next2.png", "000000", 0, 0.7, intM, intN
        	If intM > -1 And intN > -1 Then
				TracePrint "new_role_next 已回答完成5题 "
                Exit While 
            End If
        End If
        If num >= 5 Then 
        	TracePrint "未能答完5题，需要人工确认原因并处理"
            Exit While
        End If
	Wend
End Function

Function 选择头像
    While 1
    	Dim intM,intN
    	For i = 0 To 2
    		TracePrint "i is ",i
        	FindPic 1418, 904, 1500, 980, "Attachment:new_role_next2.png", "000000", 0, 0.7, intM, intN
        	If intM > -1 And intN > -1 Then
            	Tap intM + (Rnd() * 60) - 30, intN + (Rnd() * 60) - 30
            	Delay ((Rnd() + 3) * 1000)
            End If
        FindPic 1595, 788, 1865, 848, "Attachment:quedingxuanze.png", "000000", 0, 0.7, intM, intN
        If intM > -1 And intN > -1 Then 
        	TracePrint "quedingxuanze 坐标：",intM ,intN
        	Delay ((Rnd() + 1) * 1000)
//       	intM, intN 1623 801 	
            Tap intM + (Rnd() * 80) - 10, intN + (Rnd() * 40) - 3
            Delay ((Rnd() + 5) * 1000)
            Exit While
        End If 
    	Next
    Wend
End Function

Function 选择名字
    While 1
    	Dim intM,intN
    	For i = 0 To 1
    		TracePrint "i is ",i
        	FindPic 1671, 670, 1774, 722, "Attachment:suiji.png", "000000", 0, 0.7, intM, intN
        	If intM > -1 And intN > -1 Then
            	Tap intM + (Rnd() * 20) - 5, intN + (Rnd() * 10)
            	Delay ((Rnd() + 2) * 1000)
            End If
        FindPic 1319, 788, 1597, 853, "Attachment:jinruluanshi.png", "000000", 0, 0.7, intM, intN
        If intM > -1 And intN > -1 Then 
//      	intM, intN 1349 800
        	TracePrint "jinruluanshi 坐标：",intM ,intN	
            Tap intM + (Rnd() * 100) - 5, intN + (Rnd() * 30) - 3
            Delay ((Rnd() + 5) * 1000)
            Exit While
        End If 
    	Next
    Wend
//  todo 判断名字重复，请重新输入  
End Function


Function 选择出生州
	TracePrint "选择出生州"
	While 1
		Dim intM,intN
		For i = 0 To 6
    		TracePrint "i is ",i
        	FindPic 1418, 904, 1500, 980, "Attachment:new_role_next2.png", "000000", 0, 0.7, intM, intN
        	If intM > -1 And intN > -1 Then
            	Tap intM + (Rnd() * 60) - 30, intN + (Rnd() * 60) - 30
            	Delay ((Rnd() + 3) * 1000)
            End If
        Next    
		Delay ((Rnd() + 5) * 1000)
        FindPic 1012, 650, 1094, 766, "Attachment:jiangdong.png", "000000", 0, 0.8, intM, intN
        If intM > -1 And intN > -1 Then 
//          intM, intN	 1043 679
//        	TracePrint "intM, intN is :",intM, intN		
            	Tap intM + (Rnd() * 60) - 30, intN + (Rnd() * 60) - 30
            Delay ((Rnd() + 1) * 1000)
            Exit While
        End If
    Wend
    
    FindPic 1486, 904, 1620, 970, "Attachment:ruzhu.png", "000000", 0, 0.7, intM, intN
    If intM > -1 And intN > -1 Then 
     	TracePrint "ruzhu intM, intN is :",intM, intN
        Tap intM + (Rnd() * 60) - 10, intN + (Rnd() * 20)
        Delay ((Rnd() + 40) * 1000)

//     	todo  入驻失败，根据人工输入框输入值确认继续还是退出循环
//        While 1
//      	找图区域坐标待确认 jinruchangjingzhong.png  
//    		FindPic 0, 0, 1920, 1080, "Attachment:jinruchangjingzhong.png", "000000", 0, 0.7, intM, intN
//    		Delay ((Rnd() + 2) * 1000)
//    		If intM > -1 And intN > -1 Then 
//    			TracePrint "intM, intN is :",intM, intN	
//        		TracePrint "入驻失败，需要人工处理"
//        		Delay ((Rnd() + 40) * 1000)
//        		
//        	End If 
//            TracePrint"当前服务器已满或其他原因无法进入，请输入您的选择：1：跳过此步；2：继续查找"
//            choice_op = Call getinput(20)
//            if choice_op == "1":
//                Exit While
//            End If
//        else:
//            Exit While 
//        Wend
         
    End If		

	While 1
    	FindPic 1671, 988, 1822, 1047, "Attachment:xiayibu.png", "000000", 0, 0.7, intM, intN
    	If intM > -1 And intN > -1 Then 
    	 	TracePrint "xiayibu intM, intN is :",intM, intN
        	Tap intM + (Rnd() * 20), intN + (Rnd() * 10)
        	Delay ((Rnd() + 5) * 1000)
        	Exit While
    	End If
	Wend
	
End Function

Function 首次招募
	Dim intM, intN
	While 1
		For i=1 To 6
		    TracePrint "i is ",i
//        	FindPic 1130, 680, 1300, 735, "Attachment:wolongxiansheng.png", "000000", 0, 0.7, intM, intN
//        	TracePrint "wolongxiansheng.png is ", intM, intN
//        	Delay ((Rnd() + 2) * 1000)
//        	If intM > -1 And intN > -1 Then
//            	Tap intM + (Rnd() * 5) - 5, intN + (Rnd() * 5) - 5
//            	Delay ((Rnd() + 5) * 1000)
//            	Exit While
//            End If
            
//          todo 待确认0.8精度是否能查到  
            FindPic 1689, 816, 1761, 883, "Attachment:heidi_next.png", "000000", 0, 0.8, intM, intN
        	If intM > -1 And intN > -1 Then 
        		TracePrint "heidi_next.png is ", intM, intN
            	Tap intM + (Rnd() * 5) - 5, intN + (Rnd() * 5) - 5
            	Delay ((Rnd() + 5) * 1000)
            End If
        Next
        For i=0 To 3
        	FindPic 1300, 977, 1435, 1065, "Attachment:shouci_zhaomu.png", "000000", 0, 0.7, intM, intN
        	If intM > -1 And intN > -1 Then 
        		TracePrint "shouci_zhaomu.png is ", intM, intN
	            Tap intM + (Rnd() * 10), intN + (Rnd() * 5) - 10
            	Delay ((Rnd() + 5) * 1000)
            	Exit While
        	End If
        Next
    Wend
    
    While 1
    	FindPic 1053, 816, 1256, 879, "Attachment:zhaomu2ci.png", "000000", 0, 0.8, intM, intN
        If intM > -1 And intN > -1 Then 
        	TracePrint "wolong_next.png is ", intM, intN
            Tap intM + (Rnd() * 5) - 5, intN + (Rnd() * 5) - 5
            Delay ((Rnd() + 5) * 1000)
            Exit While
        End If	
    Wend
//  第一个武将曹休 交互动画  
	While 1
    	FindPic 1503, 931, 1576, 1007, "Attachment:zhaomu_next.png", "000000", 0, 0.8, intM, intN
    	If intM > -1 And intN > -1 Then 
    		TracePrint "zhaomu_next2.png is ", intM, intN
        	Tap intM + (Rnd() * 5) - 5, intN + (Rnd() * 5) - 5
        	Delay ((Rnd() + 5) * 1000)
        	Exit While
    	End If	
    Wend
    
	While 1
    	FindPic 777, 1007, 1094, 1066, "Attachment:zhaomu_dianjiqitaquyu_fanhui.png", "000000", 0, 0.8, intM, intN
    	If intM > -1 And intN > -1 Then 
    		TracePrint "zhaomu_dianjiqitaquyu_fanhui.png is ", intM, intN
        	Tap intM + (Rnd() * 50), intN - (Rnd() * 50) + 5
        	Delay ((Rnd() + 5) * 1000)
        	Exit While
    	End If	
    Wend
//  第二个武将孙乾交互  
	While 1
    	FindPic 1503, 931, 1576, 1007, "Attachment:zhaomu_next.png", "000000", 0, 0.8, intM, intN
    	If intM > -1 And intN > -1 Then 
    		TracePrint "zhaomu_next2.png is ", intM, intN
        	Tap intM + (Rnd() * 5) - 5, intN + (Rnd() * 5) - 5
        	Delay ((Rnd() + 5) * 1000)
        	Exit While
    	End If	
    Wend
    
	While 1
    	FindPic 777, 1007, 1094, 1066, "Attachment:zhaomu_dianjiqitaquyu_fanhui.png", "000000", 0, 0.8, intM, intN
    	If intM > -1 And intN > -1 Then 
    		TracePrint "zhaomu_dianjiqitaquyu_fanhui.png is ", intM, intN
        	Tap intM + (Rnd() * 50), intN - (Rnd() * 50) + 5
        	Delay ((Rnd() + 5) * 1000)
        	Exit While
    	End If	
    Wend
    
    For i = 0 To 1
    	Call 小返回()
    Next
    
//  进入主城  
    While 1
    	FindPic 1700, 814, 1756, 875, "Attachment:bianjibudui_next.png", "000000", 0, 0.7, intM, intN
    	If intM > -1 And intN > -1 Then 
        	TracePrint "bianjibudui_next: ",intM, intN
        	Tap intM + (Rnd() * 5) - 5, intN + (Rnd() * 5) - 5
        	Delay ((Rnd() + 3) * 1000)
    	End If
    	
    	FindPic 857, 685, 1038, 746, "Attachment:xuanzezhucheng.png", "000000", 0, 0.7, intM, intN
    	If intM > -1 And intN > -1 Then 
        	TracePrint "xuanzezhucheng: ",intM, intN
        	Tap intM + (Rnd() * 50), intN + (Rnd() * 15)
        	Delay ((Rnd() + 3) * 1000)
    	End If
    	
    	FindPic 877, 435, 1027, 535, "Attachment:rucheng.png", "000000", 0, 0.7, intM, intN
    	If intM > -1 And intN > -1 Then 
        	TracePrint "rucheng: ",intM, intN
        	Tap intM + (Rnd() * 50), intN + (Rnd() * 15)
        	Delay ((Rnd() + 3) * 1000)
        	Exit While
    	End If
    	
    Wend     
End Function

Function 小返回
	Dim intM, intN
	While 1
    	FindPic 1730, 0, 1889, 71, "Attachment:fanhui_xiao.png", "000000", 0, 0.8, intM, intN
    	If intM > -1 And intN > -1 Then 
    		TracePrint "fanhui_xiao.png is ", intM, intN
        	Tap intM + (Rnd() * 5) - 5, intN + (Rnd() * 5) - 5
        	Delay ((Rnd() + 5) * 1000)
        	Exit While
    	End If	
    Wend 	
End Function

Function 小小返回
	Dim intM, intN
	While 1
    	FindPic 1798, 0, 1918, 71, "Attachment:xiaoxiao_fanhui.png", "000000", 0, 0.7, intM, intN
    	If intM > -1 And intN > -1 Then 
    		TracePrint "xiaoxiao_fanhui.png is ", intM, intN
        	Tap intM + (Rnd() * 5), intN + (Rnd() * 5)
        	Delay ((Rnd() + 5) * 1000)
        	Exit While
    	End If	
    Wend 	
End Function

Function 编制部队
	//  点击编制部队  
	Dim intM, intN
    While 1
    FindPic 61, 914, 303, 988, "Attachment:dianjibianzhibudui.png", "000000", 0, 0.7, intM, intN
    If intM > -1 And intN > -1 Then 
        TracePrint "dianjibianzhibudui: ",intM, intN
        Tap intM + (Rnd() * 150), intN + (Rnd() * 50)-25
        Delay ((Rnd() + 3) * 1000)
        Exit While
    End If
    Wend
    
//  配置主将加号
	While 1
    	FindPic 580, 350, 676, 436, "Attachment:peizhizhujiang_jiahao.png", "000000", 0, 0.7, intM, intN
    	If intM > -1 And intN > -1 Then 
        	TracePrint "peizhizhujiang_jiahao: ",intM, intN
        	Tap intM + (Rnd() * 50)-25, intN + (Rnd() * 50)-25
        	Delay ((Rnd() + 3) * 1000)
        	Exit While
    	End If
    Wend
 //  上阵
	While 1
    	FindPic 1786, 309, 1895, 363, "Attachment:shangzhen.png", "000000", 0, 0.7, intM, intN
    	If intM > -1 And intN > -1 Then 
        	TracePrint "shangzhen: ",intM, intN
        	Tap intM + (Rnd() * 50)-25, intN + (Rnd() * 50)-25
        	Delay ((Rnd() + 3) * 1000)
        	Exit While
    	End If
    Wend
    
//  配置副将加号
	While 1
    	FindPic 888, 350, 1003, 436, "Attachment:peizhizhujiang_jiahao.png", "000000", 0, 0.7, intM, intN
    	If intM > -1 And intN > -1 Then 
        	TracePrint "peizhizhujiang_jiahao: ",intM, intN
        	Tap intM + (Rnd() * 50)-25, intN + (Rnd() * 50)-25
        	Delay ((Rnd() + 3) * 1000)
        	Exit While
    	End If
    Wend
 //  上阵
	While 1
    	FindPic 1786, 430, 1895, 480, "Attachment:shangzhen.png", "000000", 0, 0.7, intM, intN
    	If intM > -1 And intN > -1 Then 
        	TracePrint "shangzhen: ",intM, intN
        	Tap intM + (Rnd() * 50)-25, intN + (Rnd() * 50)-25
        	Delay ((Rnd() + 3) * 1000)
        	Exit While
    	End If
    Wend    

End Function


Function 快速分兵
	Dim intM, intN
	While 1
    	FindPic 108, 984, 309, 1037, "Attachment:kuaisufenbing.png", "000000", 0, 0.7, intM, intN
    	If intM > -1 And intN > -1 Then 
        	TracePrint "kuaisufenbing: ",intM, intN
        	Tap intM + (Rnd() * 80), intN + (Rnd() * 20)
        	Delay ((Rnd() + 3) * 1000)
        	Exit While
    	End If
    Wend
    
	While 1
    	FindPic 1595, 824, 1743, 957, "Attachment:querenfenbing.png", "000000", 0, 0.7, intM, intN
    	If intM > -1 And intN > -1 Then 
        	TracePrint "querenfenbing: ",intM, intN
        	Tap intM + (Rnd() * 80), intN + (Rnd() * 20)
        	Delay ((Rnd() + 3) * 1000)
        	Exit While
    	End If
    Wend
    
    Call 小返回()
    Call 小小返回()
    
End Function

Function 攻占中心地块
	TracePrint "攻占中心地块"
//  点击中心地块中心	
	Tap 955 - (Rnd() * 30) + 30, 485 - (Rnd() * 30) + 30
	Delay ((Rnd() + 2) * 1000)
	Dim intM, intN
//	查找并点击攻占	
	While 1
//		查找范围比实际有所扩大，考虑通用的可能性	
    	FindPic 1169, 227, 1423, 295, "Attachment:gongzhan_daidao.png", "000000", 0, 0.7, intM, intN
    	If intM > -1 And intN > -1 Then 
        	TracePrint "gongzhan_daidao: ",intM, intN
        	Delay ((Rnd() + 1) * 1000)
        	Tap intM + (Rnd() * 80), intN + (Rnd() * 20)
        	Delay ((Rnd() + 3) * 1000)
        	Exit While
    	End If
    Wend
//  选择出征部队  
	While 1	
    	FindPic 1040, 826, 1134, 873, "Attachment:xuanzechuzhengbudui_daiming.png", "000000", 0, 0.7, intM, intN
    	If intM > -1 And intN > -1 Then 
        	TracePrint "xuanzechuzhengbudui_daiming: ",intM, intN
        	Delay ((Rnd() + 1) * 1000)
        	Tap intM - (Rnd() * 100), intN + (Rnd() * 100)
        	Delay ((Rnd() + 3) * 1000)
        	Exit While
    	End If
    Wend
    
//  点击圆形攻占按钮_黄底  
	While 1	
    	FindPic 1407, 652, 1602, 822, "Attachment:gongzhan.png", "000000", 0, 0.7, intM, intN
    	If intM > -1 And intN > -1 Then 
        	TracePrint "gongzhan: ",intM, intN
        	Delay ((Rnd() + 1) * 1000)
        	Tap intM + (Rnd() * 80), intN + (Rnd() * 80)
        	Delay ((Rnd() + 3) * 1000)
        	Exit While
    	End If
    Wend
//  delay 时间待定  
    Delay (30 * 1000)
    
//  跳过战斗剧情
	While 1
    	FindPic 74, 1006, 181, 1054, "Attachment:tiaoguo.png", "000000", 0, 0.7, intM, intN
    	If intM > -1 And intN > -1 Then 
        	TracePrint "tiaoguo: ",intM, intN
        	Delay ((Rnd() + 1) * 1000)
        	Tap intM + (Rnd() * 80), intN + (Rnd() * 80)
        	Delay ((Rnd() + 3) * 1000)
        	Exit While
    	End If
    Wend
     
//  领取首战奖励
	While 1	
    	FindPic 904, 467, 1005, 566, "Attachment:shouzhanjiangli_ziyuan.png", "000000", 0, 0.7, intM, intN
    	If intM > -1 And intN > -1 Then 
        	TracePrint "shouzhanjiangli_ziyuan: ",intM, intN
        	Delay ((Rnd() + 1) * 1000)
        	Tap intM + (Rnd() * 10), intN + (Rnd() * 10)
        	Delay ((Rnd() + 3) * 1000)
        	Exit While
    	End If
    Wend
    
    Call 跳过剧情_黑()
    Call 跳过剧情_黑()
End Function


Function 回城
	Dim intM, intN
//  回城
	While 1	
    	FindPic 1721, 356, 1837, 408, "Attachment:huicheng.png", "000000", 0, 0.7, intM, intN
    	If intM > -1 And intN > -1 Then 
        	TracePrint "huicheng: ",intM, intN
        	Delay ((Rnd() + 1) * 1000)
        	Tap intM + (Rnd() * 20)-10, intN + (Rnd() * 10)
        	Delay ((Rnd() + 5) * 1000)
        	Exit While
    	End If
    Wend	
End Function


Function 跳过剧情_黑
	Dim intM, intN
	While 1
//		查找范围比实际有所扩大，考虑通用的可能性	
    	FindPic 1382, 740, 1848, 994, "Attachment:zhaomu_next.png", "000000", 0, 0.7, intM, intN
    	If intM > -1 And intN > -1 Then 
        	TracePrint "zhaomu_next: ",intM, intN
        	Tap intM - (Rnd() * 80), intN - (Rnd() * 80)
        	Delay ((Rnd() + 3) * 1000)
        	Exit While
    	End If
    Wend 
End Function

// 循环10次 跳过剧情，直到出现“选择主城”
Function 循环跳过剧情_黑
	Dim intM, intN
	While 1
		For i = 0 To 9
			FindPic 1382, 740, 1848, 994, "Attachment:zhaomu_next.png", "000000", 0, 0.7, intM, intN
    		If intM > -1 And intN > -1 Then 
        		TracePrint "zhaomu_next: ",intM, intN
        		Delay ((Rnd() + 2) * 1000)
        		If i = 3 Then
        			Delay ((Rnd() + 3) * 1000)
        		End If
        		If i = 4 Then
        			Delay ((Rnd() + 16) * 1000)
        		End If
        		        		
        		Tap intM - (Rnd() * 80), intN - (Rnd() * 80)
        		Delay ((Rnd() + 3) * 1000)
        	End If
        	
 		FindPic 1382, 740, 1848, 994, "Attachment:xuanzezhucheng.png", "000000", 0, 0.7, intM, intN
    	If intM > -1 And intN > -1 Then 
        	TracePrint "xuanzezhucheng: ",intM, intN
        	Tap intM - (Rnd() * 80), intN - (Rnd() * 80)
        	Delay ((Rnd() + 3) * 1000)       	
        	Exit While
    	End If
		Next
	Wend
End Function

Function 关平剧情
	Dim intM, intN
	While 1
		For i = 0 To 3
			FindPic 1382, 740, 1848, 994, "Attachment:zhaomu_next.png", "000000", 0, 0.7, intM, intN
    		If intM > -1 And intN > -1 Then 
        		TracePrint "zhaomu_next: ",intM, intN
        		Delay ((Rnd() + 2) * 1000)
        		If i = 3 Then
        			Delay ((Rnd() + 3) * 1000)
        		End If
        		If i = 4 Then
        			Delay ((Rnd() + 16) * 1000)
        		End If
        		        		
        		Tap intM - (Rnd() * 80), intN - (Rnd() * 80)
        		Delay ((Rnd() + 3) * 1000)
        	End If
        Next	
		While 1
    		FindPic 777, 1007, 1094, 1066, "Attachment:zhaomu_dianjiqitaquyu_fanhui.png", "000000", 0, 0.8, intM, intN
    		If intM > -1 And intN > -1 Then 
    			TracePrint "zhaomu_dianjiqitaquyu_fanhui.png is ", intM, intN
        		Tap intM + (Rnd() * 50), intN - (Rnd() * 50) + 5
        		Delay ((Rnd() + 5) * 1000)
        		Exit While
    		End If	
    	Wend
    	
		For i = 0 To 3
			FindPic 1382, 740, 1848, 994, "Attachment:zhaomu_next.png", "000000", 0, 0.7, intM, intN
    		If intM > -1 And intN > -1 Then 
        		TracePrint "zhaomu_next: ",intM, intN
        		Delay ((Rnd() + 2) * 1000)
        		If i = 3 Then
        			Delay ((Rnd() + 3) * 1000)
        		End If
        		If i = 4 Then
        			Delay ((Rnd() + 16) * 1000)
        		End If
        		        		
        		Tap intM - (Rnd() * 80), intN - (Rnd() * 80)
        		Delay ((Rnd() + 3) * 1000)
        	End If
        Next
	Wend
	Call 选择主城_入城()
End Function

Function 选择主城_入城
	Dim intM, intN
	While 1
//		FindPic 857, 685, 1038, 746, "Attachment:xuanzezhucheng.png", "000000", 0, 0.7, intM, intN		
		FindPic 820, 685, 1038, 746, "Attachment:xuanzezhucheng_yijun.png", "000000", 0, 0.7, intM, intN
    	If intM > -1 And intN > -1 Then 
        	TracePrint "xuanzezhucheng_yijun: ",intM, intN
        	Tap intM + (Rnd() * 50), intN + (Rnd() * 15)
        	Delay ((Rnd() + 3) * 1000)
    	End If
    	
    	FindPic 877, 435, 1027, 535, "Attachment:rucheng.png", "000000", 0, 0.7, intM, intN
    	If intM > -1 And intN > -1 Then 
        	TracePrint "rucheng: ",intM, intN
        	Tap intM + (Rnd() * 50), intN + (Rnd() * 15)
        	Delay ((Rnd() + 3) * 1000)
        	Exit While
    	End If
    Wend 
End Function

Function 队伍选择1
	Dim intM, intN
	While 1
//		队伍1 "兵种" 坐标查找区域 160, 845, 240, 896	
    	FindPic 160, 845, 240, 896, "Attachment:bingzhong.png", "000000", 0, 0.7, intM, intN
    	If intM > -1 And intN > -1 Then 
        	TracePrint "bingzhong_duiwu1: ",intM, intN
        	Delay ((Rnd() + 1) * 1000)
        	Tap intM + (Rnd() * 40)-20, intN + (Rnd() * 100)
        	Delay ((Rnd() + 5) * 1000)
        	Exit While
    	End If
    Wend	
End Function

Function 兵种选择
	Dim intM, intN
//  兵种选择
	While 1
//		队伍1 兵种坐标查找区域 160, 845, 240, 896	
    	FindPic 1655, 584, 1811, 635, "Attachment:bingzhongxuanze.png", "000000", 0, 0.7, intM, intN
    	If intM > -1 And intN > -1 Then 
        	TracePrint "bingzhongxuanze: ",intM, intN
        	Delay ((Rnd() + 1) * 1000)
        	Tap intM + (Rnd() * 100), intN + (Rnd() * 10)
        	Delay ((Rnd() + 3) * 1000)
        	Exit While
    	End If
    Wend
    
//  选择枪兵  
	While 1
    	FindPic 1327, 160, 1614, 629, "Attachment:qiangbing.png", "000000", 0, 0.7, intM, intN
    	If intM > -1 And intN > -1 Then 
        	TracePrint "qiangbing: ",intM, intN
        	Delay ((Rnd() + 1) * 1000)
        	Tap intM + (Rnd() * 100), intN + (Rnd() * 10)
        	Delay ((Rnd() + 3) * 1000)
        	Exit While
    	End If
    Wend
End Function


Function 选择目标领地_行军
	Dim intM, intN
//  选择目标领地_义军
	While 1
    	FindPic 449, 453, 707, 518, "Attachment:xuanzemubiaolingdi.png", "000000", 0, 0.7, intM, intN
    	If intM > -1 And intN > -1 Then 
        	TracePrint "xuanzemubiaolingdi: ",intM, intN
        	Delay ((Rnd() + 1) * 1000)
//  intM, intN  474 480
// 目标领地 960 480 ，计算偏移量 	
        	Tap intM + 486 + (Rnd() * 10)-10, intN + (Rnd() * 10) -10
        	Delay ((Rnd() + 3) * 1000)
        	Exit While
    	End If
    Wend
    // 行军
	While 1
    	FindPic 1185, 336, 1431, 391, "Attachment:xingjun.png", "000000", 0, 0.7, intM, intN
    	If intM > -1 And intN > -1 Then 
        	TracePrint "xingjun: ",intM, intN
        	Delay ((Rnd() + 1) * 1000)
        	Tap intM + (Rnd() * 50), intN + (Rnd() * 10)
        	Delay ((Rnd() + 3) * 1000)
        	Exit While
    	End If
    Wend
       	
//  点击选择出征部队  
	While 1	
    	FindPic 1040, 826, 1134, 873, "Attachment:xuanzechuzhengbudui_daiming.png", "000000", 0, 0.7, intM, intN
    	If intM > -1 And intN > -1 Then 
        	TracePrint "xuanzechuzhengbudui_daiming: ",intM, intN
        	Delay ((Rnd() + 1) * 1000)
        	Tap intM - (Rnd() * 100), intN + (Rnd() * 100)
        	Delay ((Rnd() + 3) * 1000)
        	Exit While
    	End If
    Wend
    
 //  行军_黄底  
	While 1	
    	FindPic 1400, 660, 1589, 818, "Attachment:xingjun_huangdi.png", "000000", 0, 0.7, intM, intN
    	If intM > -1 And intN > -1 Then 
        	TracePrint "xingjun_huangdi: ",intM, intN
        	Delay ((Rnd() + 1) * 1000)
        	Tap intM + (Rnd() * 30), intN + (Rnd() * 20)
        	Delay ((Rnd() + 3) * 1000)
        	Exit While
    	End If
    Wend   
    Delay ((Rnd() + 20) * 1000)
    //  跳过战斗剧情
	While 1
    	FindPic 74, 1006, 181, 1054, "Attachment:tiaoguo.png", "000000", 0, 0.7, intM, intN
    	If intM > -1 And intN > -1 Then 
        	TracePrint "tiaoguo: ",intM, intN
        	Delay ((Rnd() + 1) * 1000)
        	Tap intM + (Rnd() * 80), intN + (Rnd() * 80)
        	Delay ((Rnd() + 3) * 1000)
        	Exit While
    	End If
    Wend
End Function

Function 下阵主将
	Dim intM, intN
	While 1
//		下阵主将	
    	FindPic 668, 134, 770, 200, "Attachment:xiazhen.png", "000000", 0, 0.7, intM, intN
    	If intM > -1 And intN > -1 Then 
        	TracePrint "xiazhen: ",intM, intN
        	Delay ((Rnd() + 1) * 1000)
        	Tap intM + (Rnd() * 5), intN + (Rnd() * 5)
        	Delay ((Rnd() + 3) * 1000)
        	Exit While
    	End If
    Wend
    
	While 1
//		确认下阵
    	FindPic 730, 670, 862, 736, "Attachment:queren_xiazhen.png", "000000", 0, 0.7, intM, intN
    	If intM > -1 And intN > -1 Then 
        	TracePrint "queren_xiazhen: ",intM, intN
        	Delay ((Rnd() + 1) * 1000)
        	Tap intM + (Rnd() * 50), intN + (Rnd() * 15)
        	Delay ((Rnd() + 3) * 1000)
        	Exit While
    	End If
    Wend
End Function

Function 更换主将
	Dim intM, intN
//  配置主将加号
	While 1
    	FindPic 580, 350, 676, 436, "Attachment:peizhizhujiang_jiahao.png", "000000", 0, 0.7, intM, intN
    	If intM > -1 And intN > -1 Then 
        	TracePrint "peizhizhujiang_jiahao: ",intM, intN
        	Tap intM + (Rnd() * 50)-25, intN + (Rnd() * 50)-25
        	Delay ((Rnd() + 3) * 1000)
        	Exit While
    	End If
    Wend
    
  //  关平上阵
	While 1
    	FindPic 1786, 427, 1902, 478, "Attachment:shangzhen.png", "000000", 0, 0.7, intM, intN
    	If intM > -1 And intN > -1 Then 
        	TracePrint "shangzhen: ",intM, intN
        	Tap intM + (Rnd() * 50)-25, intN + (Rnd() * 50)-25
        	Delay ((Rnd() + 3) * 1000)
        	Exit While
    	End If
    Wend       
End Function

//Call new_role()
//Call 日常招募()
//Call 容错()


//Call 跳过剧情_黑()
//Call 队伍选择1()
//Call test()

Function test
	Dim intM, intN
  //  关平上阵
	While 1
    	FindPic 1786, 427, 1902, 478, "Attachment:shangzhen.png", "000000", 0, 0.7, intM, intN
    	If intM > -1 And intN > -1 Then 
        	TracePrint "shangzhen: ",intM, intN
        	Tap intM + (Rnd() * 50)-25, intN + (Rnd() * 50)-25
        	Delay ((Rnd() + 3) * 1000)
        	Exit While
    	End If
    Wend   
End Function

Function 


Function 大返回
	Dim intM, intN
	While 1
    	FindPic 1503, 931, 1576, 1007, "Attachment:fanhui_da.png", "000000", 0, 0.8, intM, intN
    	If intM > -1 And intN > -1 Then 
    		TracePrint "zhaomu_next2.png is ", intM, intN
        	Tap intM + (Rnd() * 5) - 5, intN + (Rnd() * 5) - 5
        	Delay ((Rnd() + 5) * 1000)
        	Exit While
    	End If	
    Wend	
End Function


Function 日常招募
	Dim intM, intN
	FindPic 1300, 977, 1435, 1065, "Attachment:zhaomu_wuhong.png", "000000", 0, 0.7, intM, intN
        
        If intM > -1 And intN > -1 Then 
        	TracePrint "zhaomu_wuhong.png is ", intM, intN
//          Tap intM + (Rnd() * 5) - 5, intN + (Rnd() * 5) - 5
            Delay ((Rnd() + 5) * 1000)
    End If
    
//  招募到橙有交互动画  
	For i=0 To 10
    	FindPic 1503, 931, 1576, 1007, "Attachment:zhaomu_next.png", "000000", 0, 0.8, intM, intN
    	If intM > -1 And intN > -1 Then 
    		TracePrint "zhaomu_next.png is ", intM, intN
        	Tap intM + (Rnd() * 5) - 5, intN + (Rnd() * 5) - 5
        	Delay ((Rnd() + 5) * 1000)
        	Exit While
    	End If	
    Next
    
	While 1
    	FindPic 777, 1007, 1094, 1066, "Attachment:zhaomu_dianjiqitaquyu_fanhui.png", "000000", 0, 0.8, intM, intN
    	If intM > -1 And intN > -1 Then 
    		TracePrint "zhaomu_dianjiqitaquyu_fanhui.png is ", intM, intN
        	Tap intM + (Rnd() * 50), intN - (Rnd() * 50) + 5
        	Delay ((Rnd() + 5) * 1000)
        	Exit While
    	End If	
    Wend    
    
End Function


Function 容错
	// 1730, 0, 1889, 71
	Tap 1860 + (Rnd() * 5) - 5, 40 + (Rnd() * 5) - 5
	Delay ((Rnd() + 2) * 1000)
End Function
