# # 11.2_前半部分
# def get_city_function(city, country, population):
#     """生成格式规范的国家名字"""
#     if population == None:
#         full_name = f"{city}, {country}"
#     else:
#         full_name = f"{city}, {country}--population:{population}"
#     return full_name.title()


# 11.2_后半部分
def get_city_function(city, country, population=None):
    """生成格式规范的国家名字"""
    if population == None:
        full_name = f"{city}, {country}"
    else:
        full_name = f"{city}, {country}--population:{population}"
    return full_name.title()
