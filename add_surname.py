# Author: Aubrey Floyd
# GitHub username: aubreyfloyd2
# Date: 2/13/2023
# Description: Function that checks names for letter "K" and returns those first names with
#              "K" in a list that adds last name Kardashian.

def add_surname(first_name):
    """Returns only K first names with surname added"""
    full_name = [n+ " Kardashian" for n in first_name if n[0]=="K"]
    return full_name

# first_name = ["Kiki", "Krystal", "Pavel", "MaryKay", "Annie", "Koala"]
# print(add_surname(first_name))