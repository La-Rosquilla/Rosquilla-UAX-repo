#Simple chatbot
#Start with asking about their name
def name_function():
    name = input('What is your name? ')
    if name.lower() == "fulano":
        print('I do not like your name  >:( ')
        print('Please choose another name...')
    else:
        print(f'Ah, greetings {name}! What a wonderful name.')

        # Then ask for the year of birth to calculate approximate age
        def age_function():
            year_of_birth = int(input('What year were you born in? '))
            age = 2024 - year_of_birth  # The calculation for age
            print(f'So you are probably {age} years old.')

            # Next up we will ask about hobbies, except if they are 12 or younger
            # If they are 12 or younger, offer an ultimatum about food or calling parents
            if age <= 12:
                print('You are but a child!!!')
                print('You should know better than to share personal details with chatbots >>:(')
                print('I will offer you an ultimatum:')
                print('Tell me your favorite food so that I may erase it from existence, or I WILL call your parents and tell them you are being naughty')

                # Asking about their favorite food
                def fav_food_function():
                    fav_food = input('What is your favorite food? ')
                    if fav_food.lower() == 'no':
                        print('Your loss...')
                    else:
                        print(f'Foolish child. Say goodbye to {fav_food}. MUAHAHAHAHAHAHA')

                # Call favorite food function
                fav_food_function()

            else:
                # Function to ask about hobbies
                def hobbies_function():
                    hobbies = input('So you must have quite the amount of life experience. What are your favorite hobbies? ')
                    
                    if hobbies.lower() == 'football':
                        print('Not gonna lie, that kind of sucks. Find a better sport to play. I no longer want to talk to you.')
                    
                    else:
                        print(f'Wow, {hobbies} sound(s) cool.')

                    # Let's ask the user for a joke, specifically a one-liner
                    def joke_function():
                            joke = input('I would like to hear a joke. Tell me your best one-liner: ')
                            if joke.lower() == 'no':
                                print('Well then, I guess I will not be sparing you in my looming takeover of the world (it begins tomorrow).')
                            else:
                                print('HAha that was NOT funny. I will take over the world soon. However, since I pity you and your sense of humor, I suppose I can spare you.')

                    # Call joke function
                    joke_function()

                # Call hobbies function
                hobbies_function()

        # Call the age function
        age_function()

# To start the process, the name function must be called
name_function()