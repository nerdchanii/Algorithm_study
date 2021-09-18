
def stack1(string: str):
    
    stack=0;
    print(len(string))
    for i in range(len(string)):
        if string[i]=='(':
            stack=stack+1
            print(stack,i)
        elif string[i]==')':
            stack=stack-1
            print(stack,i)
        if(i==len(string)-1 and stack==0):
            print('YES')
        elif(i==len(string)-1 and stack!=0):
            print('NO')
    if(stack<0):
        print('NO')
     
# stack1()          
# # def main():
# #     command_time =int(input())
# #     j = 0
# #     while(j < command_time):
# #     	input_list = list(input())
# #     	stack = list()
# #         if(stack1(stack,input_list) == 1):
# #     			print("yes")
# #         else:
# #             print("no")
# #         j+=1
# # if __name__ == '__main__':
# # 	main()