from name_function import Employee
def test_give_default_raise():
    formatted_name= Employee("janis", "joplin",1000000000)
    assert formatted_name=="Janis Joplin 10000"

# def test_give_custom_raise():