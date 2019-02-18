import json
from twitter2 import inform_friends

# main_dict = json.loads(open('user_friends.json').read())
# main_dict = inform_friends('@Khrysty35589984')

account =  str(input("Enter a account: "))
main_dict = inform_friends(account)


def main():
    """
    Return a list of lists of possible parameters.

    Parameters:
    "friend_list" - names
    "nick_list" - names and screen names
    "create_map" - screen names and locations
    "another_list" - another 
    """

    keyword = str(input("Enter a keyword to see the information about followers: "))
    
    if keyword == "friend_list":
        return get_friend_list()
    if keyword == "nick_list":
        return get_user_nick_list()
    if keyword == "create_map":
        return get_data_map()
    if keyword == "another_list":
        return get_another_list()
    return "The keyword is not avaible"
    

def get_friend_list():
    """
    Return a list of names of account's friends.
    """
    return list(key['name'] for key in main_dict['users'])


def get_user_nick_list():
    """
    Return a list of tuples(name, screen name) of account's friends.
    """
    return list((key['name'], key['screen_name']) for key in main_dict['users'])


def get_data_map():
    """
    Return a list of tuples(screen name, location) of account's friends.
    """
    return list((key['screen_name'], key['location']) for key in main_dict['users'])


def get_another_list():
    """
    Return a list of tuples(name and param[value]) of account's friends.

    Paremeters(simple):
    "id_str", "location", "description", "url", "protected", "followers_count",
    "friends_count", "listed_count", "created_at", "favourites_count",
    "utc_offset", "time_zone", "geo_enabled", "verified", "statuses_count",
    "lang", "contributors_enabled", "is_translator", "is_translation_enabled",
    "profile_background_color", "profile_background_image_url", "profile_background_image_url_https"
    "profile_background_tile", "profile_image_url", "profile_image_url_https",
    "profile_link_color", "profile_sidebar_border_color", "profile_sidebar_fill_color",
    "profile_text_color", "profile_use_background_image", "has_extended_profile",
    "default_profile", "default_profile_image", "following", "live_following",
    "follow_request_sent", "notifications", "muting", "blocking", "blocked_by",
    "translator_type"
    Paremeters(complex):
    "entities", "status"
    """
    detailed_key = str(input("Enter a more detailed keyword: "))
    lst = []
    for key in main_dict['users']:
        for nextkey in key:
            if nextkey == detailed_key:
                lst.append((key['name'], key[detailed_key]))  
    if len(lst) != 0:   
        return lst
    return "The keyword is not avaible"


print(main())