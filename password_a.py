password = "a123"
i = 3
while i > 0 :
	i = i -1 
	pwd = input(" Please input your password : ")
	if pwd == password :
		print(" 登入成功 ")
		break
	else :
		print("密碼錯誤啦")
		if i > 0 :
			print("還有" ,  i  ,  "次機會")
		else :
			print("沒有機會了喔")

