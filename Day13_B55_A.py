#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Python functions:


# In[ ]:


paremeters and arguments


# In[ ]:


type of arguments


# In[1]:


def greeting():
    """creating a greeting function """
    print('hello')


# In[2]:


greeting()


# In[ ]:





# In[24]:


def greet_user(username):
    """creating a fun for greeting the user"""
    print(f"hello, {username}")


# In[25]:


greet_user('hema')


# In[ ]:





# In[ ]:


type of arguments:


# In[ ]:


# create a function....


# In[62]:


def describe_pet(animal_type,pet_name):
    """creating a pet function for capturing the deails"""
    print(f"I have a {animal_type}")
    print(f"my {animal_type}'s name is {pet_name}")


# In[63]:


describe_pet('dog','bruno')


# In[64]:


describe_pet('bruno','dog')


# In[65]:


describe_pet('dora')


# In[ ]:


Note: in case of any missing info we will treat the animal_type as a dog


# In[66]:


def describe_pet(animal_type= 'dog',pet_name):
    """creating a pet function for capturing the deails"""
    print(f"I have a {animal_type}")
    print(f"my {animal_type}'s name is {pet_name}")


# In[69]:


def describe_pet(pet_name,animal_type= 'dog'):
    """creating a pet function for capturing the deails"""
    print(f"I have a {animal_type}")
    print(f"my {animal_type}'s name is {pet_name}")


# In[70]:


describe_pet('dora')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




