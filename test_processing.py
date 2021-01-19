#!/usr/bin/env python
# coding: utf-8

# In[39]:


def normalize(input_string):
    normalized_string = ' '.join(input_string.lower().strip().split())
    return normalized_string


# In[38]:


def no_vowels(input_string):
    vowel = ['a','e','i','o','u']
    temp = ''
    for string in input_string:
        if string.lower() in vowel:
            continue
        temp = temp + string
        
    no_vowel_string = temp
    return no_vowel_string

