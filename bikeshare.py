<<<<<<< HEAD
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

    while True:
        city = input('Please enter the city you would like to analyze (chicago, new york city, or washington): ').lower()
        if city.strip() in CITY_DATA:
            break
        else: print('Invalid input, please try again.')


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Please enter the month you would like to filter by (January through June) or type "all" to apply no month filter: ').lower()
        if month.strip() in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            break
        else: print('Invalid input, please try again.')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Please enter the day of the week you would like to filter by, or type "all" to apply no day filter: ').lower()
        if day.strip() in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
            break
        else: print('Invalid input, please try again.')

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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]

    print('Most common month:', popular_month)


    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.day
    popular_day = df['day'].mode()[0]

    print('Most common day of the week:', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]

    print('Most common start hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('The most commonly used start station:', common_start)

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('The most commonly used end station:', common_end)

    # TO DO: display most frequent combination of start station and end station trip
    start_end_combo = df[['Start Station', 'End Station']].mode().loc[0]
    print('The most frequent combination of start station and end station trip: {}, {}'.format(start_end_combo[0], start_end_combo[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User types:\n', user_types)

    # TO DO: Display counts of gender
    try:
        gender_counts = df['Gender'].value_counts()
    # TO DO: Display earliest, most recent, and most common year of birth
        early_birth = df['Birth Year'].min()
        latest_birth = df['Birth Year'].max()
        most_common_birth = df['Birth Year'].mode()[0]
    except KeyError:
        print('Gender column not available.')
        print('Birth year column not available.')
    else:
        print('Gender Types:\n', gender_counts)
        print('Earliest year of birth: {}\n Most recent year of birth: {}\n Most common year of birth: {}'.format(early_birth, latest_birth, most_common_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        record_no = 0

        while True:
            raw_data = input('Would you like 5 lines of raw data? Enter yes or no. \n').lower()
            if raw_data == 'yes':
                print(df.iloc[record_no:record_no + 5])
                record_no += 5
                continue
            else:
                break


        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
    
||||||| merged common ancestors
=======
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

    while True:
        city = input('Would you like to analyze Chicago, New York City, or Washington?: ').lower()
        if city.strip() in CITY_DATA:
            break
        else: print('Invalid input, please try again.')


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Please enter the month you would like to filter by (January through June) or type "all" to apply no month filter: ').lower()
        if month.strip() in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            break
        else: print('Invalid input, please try again.')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Which day of the week you would like to filter by, or type "all" to apply no day filter: ').lower()
        if day.strip() in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
            break
        else: print('Invalid input, please try again.')

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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]

    print('Most popular month:', popular_month)


    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.day
    popular_day = df['day'].mode()[0]

    print('Most popular day of the week:', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]

    print('Most popular start hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('The most commonly used start station:', common_start)

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('The most commonly used end station:', common_end)

    # TO DO: display most frequent combination of start station and end station trip
    start_end_combo = df[['Start Station', 'End Station']].mode().loc[0]
    print('The most frequent combination of start station and end station trip: {}, {}'.format(start_end_combo[0], start_end_combo[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The average travel time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User types:\n', user_types)

    # TO DO: Display counts of gender
    try:
        gender_counts = df['Gender'].value_counts()
    # TO DO: Display earliest, most recent, and most common year of birth
        early_birth = df['Birth Year'].min()
        latest_birth = df['Birth Year'].max()
        most_common_birth = df['Birth Year'].mode()[0]
    except KeyError:
        print('Gender column not available.')
        print('Birth year column not available.')
    else:
        print('Gender Types:\n', gender_counts)
        print('Earliest year of birth: {}\n Most recent year of birth: {}\n Most common year of birth: {}'.format(early_birth, latest_birth, most_common_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        record_no = 0

        while True:
            raw_data = input('Would you like 5 lines of raw data? Enter yes or no. \n').lower()
            if raw_data == 'yes':
                print(df.iloc[record_no:record_no + 5])
                record_no += 5
                continue
            else:
                break


        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
>>>>>>> refactoring
