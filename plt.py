import datetime
import matplotlib.pyplot as plt

plot_data = [
    [['250620', [392, 400, 450], ['2018.03.29', '2018.03.30', '2018.03.31']]],
    [['27440', [419], ['2018.03.29']]],
    [['329430', [999], ['2018.03.29']]],
    [['448510', [759, 800], ['2018.03.29', '2018.03.30']]],
    [['578080', [899], ['2018.03.29']]]
    ]

# plot_data[0][0][0]  # название
# plot_data[0][0][1]  # цена
# plot_data[0][0][2]  # дата


fig = plt.figure(dpi=128, figsize=(10, 6))
i = 0
plt.plot(plot_data[i][0][2], plot_data[i][0][1])
plt.scatter(plot_data[i][0][2], plot_data[i][0][1], label=plot_data[i][0][0])
i += 1
plt.plot(plot_data[i][0][2], plot_data[i][0][1])
plt.scatter(plot_data[i][0][2], plot_data[i][0][1], label=plot_data[i][0][0])
i += 1
plt.plot(plot_data[i][0][2], plot_data[i][0][1])
plt.scatter(plot_data[i][0][2], plot_data[i][0][1], label=plot_data[i][0][0])
i += 1
plt.plot(plot_data[i][0][2], plot_data[i][0][1])
plt.scatter(plot_data[i][0][2], plot_data[i][0][1], label=plot_data[i][0][0])
i += 1
plt.plot(plot_data[i][0][2], plot_data[i][0][1])
plt.scatter(plot_data[i][0][2], plot_data[i][0][1], label=plot_data[i][0][0])
i += 1
# Форматирование диаграммы.
plt.title('цена игр', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("стоимость (руб.)", fontsize=16)
plt.xlabel("дата замера", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.legend()
plt.show()
