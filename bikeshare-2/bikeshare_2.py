import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input('Please choose one of the following cities: chicago, new york city, washington: ')
    city = city.lower()

    while city not in CITY_DATA.keys():
        city = input('Something went wrong. Please enter one of the following cities: \n chicago, new york city, washington \n')
        city = city.lower()

    print('You have chosen ',city)

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Please choose \'all\' or one of the following months: january, february, march, april, may, june: ')
    month = month.lower()

    while month not in ['all','january', 'february', 'march', 'april', 'may', 'june']:
        month = input('Something went wrong. Please enter one of the following months: \n all, january, february, march, april, may, june:\n')
        month = month.lower()

    print('You have chosen ', month)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please choose \'all\' or one of the following day: monday, tuesday, wednesday, thursday, friday, saturday, sunday: ')
    day = day.lower()

    while day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        day = input('Something went wront. Please enter one of the following days: \n all, mon, tue, wed, thu, fri, sat, sun\n')
        day.lower()


    print('You have chosen ', day)


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #Loading data
    df = pd.read_csv(CITY_DATA[city])

    #Convert the starttime column to Datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #Extract month and day of week from Start Time to create new column
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    print(df.head())
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most common month in index numbers: ', popular_month)

    # TO DO: display the most common day of week
    popular_weekday = df['day_of_week'].mode()[0]
    print('Most common day of week: ', popular_weekday)

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most common start hour: ', popular_hour)

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print('The most commonly used start station: ', popular_start)

    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print('The most commonly used end station: ', popular_end)

    # TO DO: display most frequent combination of start station and end station trip
    df['start_to_end'] = 'Start Station' + ' ' + 'End Station'
    frequent_route = df['start_to_end'].mode()[0]
    print('The most frequent combination of start station and end station trip: ', frequent_route)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print('The total travel time: ', total_travel)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('The mean travel time: ', mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_user = df['User Type'].value_counts()
    print('Counts of user type: ',counts_user)

    # TO DO: Display counts of gender. Display earliest, most recent, and most common year of birth

    if city != 'washington':
        counts_gender = df['Gender'].value_counts()
        print('Counts of gender: ', counts_gender)
        print('Earliest year of birth: ', df['Birth Year'].min())
        print('Most recent year of birth: ', df['Birth Year'].max())
        print('Most common year of birth: ', df['Birth Year'].mode()[0])
    else:
        print('The list for Washington does not contain a Gender and Birth Year column.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    """ Asks whether the user wants to raw data. If 'yes' the script prints 5 rows and asks again if the user wants to see 5 more rows. Once the user chooses'no' the script goes to the next section of the script"""

    raw_data = input('Would you like to see raw_data? Enter yes or no\n').lower()
    count = 0
    while raw_data not in ['yes', 'no']:
        raw_data = input('Please try again: yes or no?').lower()

    if raw_data == 'yes':
        print(df.head())

    while raw_data == 'yes':
        raw_data = input('Would you like to see 5 more rows?\n').lower()
        if raw_data == 'yes':
            count +=5
            print(df[count:count+5])



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
