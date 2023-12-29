class Solution:
    def smallestNumber(self, num: int) -> int:
        if num > 0:
            str_num=sorted(str(num))
            # if str_num[0]=="0":
            #     str_num[0],str_num[1]=str_num[1],str_num[0]
            i=0
            while str_num[i]=="0":
                i += 1
            if i != 0:
                str_num[0],str_num[i]=str_num[i],str_num[0]
            
            return int("".join(str_num))
        elif num < 0:
            str_num=sorted(str(num),reverse=True)
            x="-" + "".join(str_num[:-1])
            return int(x)
        else:
            return 0
