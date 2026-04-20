abusive_words = ['abuse', 'bad', 'hate']
def valid_email(email,abusive_words=abusive_words):
    '''This function checks if email is valid or not. 
    It checks if email sender is not gmail and email body is not empty. 
    It also checks if email body contains any abusive words. 
    If email is valid, it returns True, otherwise it returns False.'''
    # check if gmail is part of email sender
    if ('@gmail.com' not in email['sender']) & (len(email['body'])>5):
        for word in abusive_words:
            if word in email['body']:
                return False
        return True
    return False


def call_llm(email):    
    # call llm to classify email
    return "Billing"
