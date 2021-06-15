import random as rand
import plotly.express as px
import plotly.figure_factory as ff

diceresult = []
count = []
for i in range(0,100):
    dice1 = rand.randint(1,6)
    dice2 = rand.randint(1,6)
    diceresult.append(dice1+dice2)
    count.append(i)

#fig=px.bar(x=diceresult, y=count)
fig = ff.create_distplot(
    [diceresult],["sum"]
)
fig.show()
print(count,diceresult)