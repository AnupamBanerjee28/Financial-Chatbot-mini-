#!/usr/bin/env python
# coding: utf-8

# In[1]:


# chatbot.py

def get_response(query):
    responses = {
        "Total Revenue for Tesla in Fiscal Year 2023": "The Total Revenue for Tesla in Fiscal Year 2023 is $96,773 million.",
        "Net Income for Microsoft in Fiscal Year 2022": "The Net Income for Microsoft in Fiscal Year 2022 is $72,738 million.",
        "Company with the Highest Total Assets in Fiscal Year 2021": "The company with the highest Total Assets in Fiscal Year 2021 is Apple with $3,51,002 million  in assets.",
        "Total Liabilities and Total Assets for Apple in Fiscal Year 2023": "For Apple in Fiscal Year 2023, the Total Liabilities are $2,90,437 million and the Total Assets are $3,52,583 million.",
           }
    
    return responses.get(query, "Sorry, I don't have information for that query.")

def main():
    print("Welcome to the Financial Chatbot!")
    while True:
        user_input = input("Please enter your query: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = get_response(user_input)
        print(response)

if __name__ == "__main__":
    main()


# In[ ]:




