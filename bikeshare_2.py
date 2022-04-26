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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities =['chicago', 'new york city', 'washington']
    while True:
      city= input("Please choose a city: chicago, new york city, washington \n").lower()
      if city in cities:
           break
      else:
        print('Invalid input. Please enter a valid city from the options given.\n')
            

    # get user input for month (all, january, february, ... , june)
    months=['january', 'february','march', 'april', 'may', 'june', 'all']
    while True:
        month= input("\nPlease select a month in which you would like to see data for: january, february, march, april, may, june, all?\n").lower()
        if month in months:
          break
        else:
          print("Invalid input.Please enter a valid month from the option given.\n")
      
            # get user input for day of week (all, monday, tuesday, ... sunday)
    days= ['sunday', 'monday', 'tuesday','wednesday','thursday','friday', 'saturday', 'sunday', 'all']
    while True:
        day= input("\nPlease slect a day of the week in which you would like to see data for: sunday, monday, tuesday, wednesday, thursday, friday, saturday,all\n").lower()
        if day in days:
          break
        else:
           print("Invalid input.Please enter a valid day of the week from the options given\n")
        
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
   # load data file into dataframe
    df = pd.read_csv(CITY_DATA[city])   
    
   # convert the Start Time column to datetime
    df['Start Time']=pd.to_datetime(df['Start Time'])
    
   # extract month and day of week from Start Time to create new columns
    df['month']=df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    # filter by month if applicable 
    if month != 'all':
        months = ['january', 'february','march', 'april', 'may', 'june']
        month = month.index(month) + 1
    
     # filter by month to create the new dataframe
        df = df[df['month'] == month]
    
     # filter by day of week if applicable
    if day!= 'all':
       df=df[df['day_of_week']== day.title()]    
     # filter by day of the week to create the new dataframe
       
              
    return df
def show_data(df):
# The user asks to see some rows of data upon request
  view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no")
  start_loc = 0
  continue_asking= True
  while(continue_asking):
    print(df.iloc[0:5])
    start_loc += 5
    view_data= input("Do you wish to continue?").lower()
    if view_data == 'no':
        continue_asking= False
    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('The most common day of the week: ', common_month)
   
    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The most common day of the week: ', common_day)

    # display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print('The most common start hour: ', common_start_hour)
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station= df['Start Station'].mode()[0]
    print('The most commonly used start station: ',common_start_station)
         
   
    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most common end station: ',common_end_station)
           
  
    # display most frequent combination of start station and end station trip
    frequent_combination= df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('The most frequent combination of start station and end station trip: ', frequent_combination)
   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time= df['Trip Duration'].sum()
    print('The total travel time: ', total_travel_time)     
    # display mean travel time
    mean_travel_time= df['Trip Duration'].mean()
    print('The mean travel time: ' , mean_travel_time)      

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_info_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print('Count of User Types: ' , user_type_count)  
          
    # Display counts of gender
    if city!= 'washington':
       gender_count = df['Gender'].value_counts()
       print('Gender Count: ' , gender_count)
                           
    # Display earliest, most recent, and most common year of birth
       earliest_dob = df['Birth Year'].min()
       print('Earliest Year of Birth: ' , earliest_dob)
                            
       most_recent_dob = df['Birth Year'].max()
       print('Most recent Year of Birth: ' , most_recent_dob)
                            
       most_common_dob = df['Birth Year'].mode()
       print('Most common year of Birth: ' , most_common_dob)
                          
    else:
        print('Sorry, this information is not  available for the city of Washington')                 
                            


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
  


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
