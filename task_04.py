#  Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
#  Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
#  а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

#  К сожалению из дано не понятно как будут распределяться журавлики если кол-во не кратно 6.

a=int (input("введите кол-во журавликов: "))
petr =0
katia =0
sergei =0

b=a//6
petr =b
katia =4*b
sergei =b

n=a%6
if n !=0:
    petr +=1
    n-=1
    if n>0:
        katia +=n
print (f"{petr}  {katia}  {sergei}")  

