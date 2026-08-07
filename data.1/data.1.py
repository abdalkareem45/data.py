import pandas as pd
import os
df = pd.read_csv("adult.data.csv")
print(os.getcwd())


def calculate_demographic_data(print_data=True):
    race_count = df['race'].value_counts()
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)
    advanced = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = round((df[advanced]['salary'] == '>50K').mean() * 100, 1)
    lower_education_rich = round((df[~advanced]['salary'] == '>50K').mean() * 100, 1)
    min_work_hours = df['hours-per-week'].min()
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers['salary'] == '>50K').mean() * 100, 1)
    country_salary = df.groupby('native-country')['salary'].apply(lambda x: (x == '>50K').mean())
    highest_earning_country = country_salary.idxmax()
    highest_earning_country_percentage = round(country_salary.max() * 100, 1)
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_rich['occupation'].value_counts().idxmax()
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }


results = calculate_demographic_data()
print(results)
