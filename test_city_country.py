# from city_functions import get_city_function


# def test_city_country():
#     """能够正确地处理像城市和国家这样的名称吗？"""
#     city_function = get_city_function("Shanghai", "China")
#     if city_function == "Shanghai, China":
#         assert city_function == "Shanghai, China"
#     else:
#         assert city_function == "Shanghai, China--population:"

from city_functions import get_city_function


def test_city_country_population():
    """能够正确地处理像城市和国家这样的名称吗？"""
    city_function = get_city_function("Shanghai", "China",21)
    if city_function == "Shanghai, China":
        assert city_function == "Shanghai, China"
    else:
        assert city_function == "Shanghai, China--Population:21"
