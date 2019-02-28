import random
fortune = ['情绪波动 慎保胃肝', '慎防侵吞 切勿赌博', '患得患失 多表关怀',
           '看清形势 改善人缘', '钱财易泄 慎勿借贷', '慎保肝肾 平安是福', '酒色伤身 知所节制',
           '年值太岁 凡事留意', '量入为出 慎防侵吞', '切勿涉险 远离利器', '感情随缘 放开怀抱', ]
res = fortune[random.randint(0, len(fortune))]
print(res)