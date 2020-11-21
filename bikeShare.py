import time
import calendar as caldr
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    city,day = '',''
    month = -1
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while city not in CITY_DATA.keys():
        print("\nEnter name of the city to analyze (chicago, new york city, washington):")
        city = input().lower()

        if city not in CITY_DATA.keys():
            print("Invalid City.")

    # TO DO: get user input for month (all, january, february, ... , june)
    while type(month) != int  or int(month) > 12 or int(month) < 0:
        print("\nEnter number of the month to filter by, or 0 to apply no month filter: ")
        
        try:
            month = int(input())
            if month > 12 or month < 0:
                print("Invalid number")
        except ValueError:
            print("This is not a number.")
        
        

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter name of the day of week to filter by, or '"'all'"' to apply no day filter: ")


    # print('-'*40)
    return city, month, day


def load_data(city, month, day):
    
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
 

    #Get month and day from Start Time
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    #Filter by month
    if month != 0:
        df = df[df['month'] == month]

    #Filter by day 
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    # start_time = time.time()

    # TO DO: display the most common month
    commonMonth = caldr.month_name[df['month'].mode()[0]]
    print("The most common month: {}".format(commonMonth))


    # TO DO: display the most common day of week
    commonDay = df['day_of_week'].mode()[0]
    print("The most common day of week: {}".format(commonDay))


    # TO DO: display the most common start hour
    df['hours'] = df['Start Time'].dt.hour
    commonHour = df['hours'].mode()[0]
    print("The most common start hour: {}".format(commonHour))

    # print("\nThis took %s seconds." % (time.time() - start_time))
    # print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...')
    # start_time = time.time()

    # TO DO: display most commonly used start station
    commonStartStation = df['Start Station'].mode()[0]
    print("The most commonly used start station: {}".format(commonStartStation))


    # TO DO: display most commonly used end station
    commonEndStation = df['End Station'].mode()[0]
    print("The most commonly used end station: {}".format(commonEndStation))

    # TO DO: display most frequent combination of start station and end station trip
    df['combo'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    combo = df['combo'].mode()[0]
    print("The most frequent trips from {}".format(combo))

    # print("\nThis took %s seconds." % (time.time() - start_time))
    # print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    # start_time = time.time()

    # TO DO: display total travel time


    # TO DO: display mean travel time


    # print("\nThis took %s seconds." % (time.time() - start_time))
    # print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    # start_time = time.time()

    # TO DO: Display counts of user types


    # TO DO: Display counts of gender


    # TO DO: Display earliest, most recent, and most common year of birth


    # print("\nThis took %s seconds." % (time.time() - start_time))
    # print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
