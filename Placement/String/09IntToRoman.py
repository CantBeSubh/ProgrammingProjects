# 1<=a<=3999
def solve(a):
    ans=''
    m=a//1000
    if a!=0:
        ans+='M'*m
    a-=1000*m

    c=a//100
    if c!=0:
        if c<=3:
            ans+='C'*c
        elif c==4:
            ans+='CD'
        elif c==9:
            ans+='CM'
        else:
            ans+='D'+'C'*(c-5)
    a-=100*c

    l=a//10
    if l!=0:
        if l<=3:
            ans+='X'*l
        elif l==4:
            ans+='XL'
        elif l==9:
            ans+='XC'
        else:
            ans+='L'+'X'*(l-5)
    a-=10*l

    if a!=0:
        if a<=3:
            ans+='I'*a
        elif a==4:
            ans+='IV'
        elif a==9:
            ans+='IX'
        else:
            ans+='V'+'I'*(a-5)
    
    return ans

print(solve(58))


# Random Internet Solution

# public class Solution {
#     public String intToRoman(int A) {
#         int i=0;
#        String arr[][]={{"I","II","III","IV","V","VI","VII","VIII","IX"},
#                       {"X","XX","XXX","XL","L","LX","LXX","LXXX","XC"},
#                       {"C","CC","CCC","CD","D","DC","DCC","DCCC","CM"},
#                       {"M","MM","MMM"}};
#                       String ans="";
#                 while(A>0){
#                 int sum=A%10;
#                 if(sum!=0) ans=arr[i][sum-1]+ans;
#                 A=A/10;   i++;
#                 }
#                 return ans;
#                 }}