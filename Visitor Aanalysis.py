import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# filter 'סכום'
df_visits = df_visits[lambda x: x['visitor_code'] != 105]


def barplot (x,y,label, title, rotate=0):
    # Create the grid
    fig, ax = plt.subplots(figsize=(7, 3.5), dpi=96)
    bar1 = ax.bar(x, y, width=0.6)

    # Create the grid
    ax.grid(which="major", axis='x', color='#DAD8D7', alpha=0.5, zorder=1)
    ax.grid(which="major", axis='y', color='#DAD8D7', alpha=0.5, zorder=1)

    # Reformat x-axis label and tick labels
    ax.set_xlabel('', fontsize=12, labelpad=10)
    ax.xaxis.set_label_position("bottom")
    ax.xaxis.set_major_formatter(lambda s, i: f'{s:,.0f}')
    ax.xaxis.set_tick_params(pad=2, labelbottom=True, bottom=True, labelsize=12, labelrotation=0)
    labels = label
    ax.set_xticks(x, labels)  # Map integers numbers from the series to labels list
    plt.xticks(rotation=rotate)

    # Reformat y-axis
    ax.set_ylabel('Number of Visitors (1,000)', fontsize=12, labelpad=10)
    ax.yaxis.set_label_position("left")
    ax.yaxis.set_major_formatter(lambda s, i: f'{s:,.0f}')
    ax.yaxis.set_tick_params(pad=2, labeltop=False, labelbottom=True, bottom=False, labelsize=12)

    # Add label on top of each bar
    ax.bar_label(bar1, labels=[f'{e:,.1f}' for e in y], padding=3, color='black', fontsize=8)

    # Remove the spines
    ax.spines[['top', 'left', 'bottom']].set_visible(False)

    # Add in title and subtitle
    ax.text(x=0.12, y=.93, s=title, transform=fig.transFigure,
            ha='left', fontsize=14, weight='bold', alpha=.8)

    plt.show()



# region << Plot number of visits in year >>
# Sum visits grouped by year
year_counts = df_visits.groupby('Year')['num_of_visitors'].sum()


barplot (x=year_counts.index,
         y=year_counts.values / 1000,
         label=year_counts.index.tolist(),
         title='Number of Visitors in all Sites')


# endregion

# region << Plot number of visits per month >>
month_counts = df_visits[lambda x: (x['Year'] == '2022')].groupby('Month')['num_of_visitors'].sum()

# plot
barplot (x=month_counts.index,
         y=month_counts.values / 1000,
         label=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
         title='Number of Visitors in all Sites in 2022')
# endregion

# region << Plot number of visits per day of the week >>
day_counts = df_visits[lambda x: (x['Year'] == '2022')].groupby('DayOfWeek')['num_of_visitors'].sum()
day_counts_sorted = day_counts.reindex(['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])

barplot (x=day_counts_sorted.index,
         y=day_counts_sorted.values / 1000,
         label=day_counts_sorted.index.tolist(),
         title='Number of Visitors in all Sites by Day in 2022')

# endregion

# region << Plot Popular sites >>
df_visits_2022 = df_visits[lambda x: x['Year'] == '2022']
grouped_visits = df_visits_2022.groupby('site_name')['num_of_visitors'].sum()

top_15_sites = grouped_visits.sort_values(ascending=False).head(15)
inverted_label = [string[::-1] for string in top_15_sites.index.tolist()]
inverted_label[9] = 'םילשורי תומוח'


barplot(x=top_15_sites.index,
        y=top_15_sites.values/1000,
        label=inverted_label,
        title='15 Most Popular Sited of 2022',
        rotate=45)

# endregion

# region << Extreme Values >>
sns.boxplot(data=df_visits['num_of_visitors'])

plt.hist(df_visits['num_of_visitors'], bins=30, edgecolor='black')

plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Data')

plt.show()
# endregion