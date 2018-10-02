def lambda_handler(event, context):
    if event['request']['type'] == "LaunchRequest" :
        return onLaunch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest" :
        return onIntent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest" :
        return onSessionEnd(event['request'], event['session'])

def onLaunch(launchRequest, session):
    return welcomeuser()

def onIntent(intentRequest, session):
             
    intent = intentRequest['intent']
    intentName = intentRequest['intent']['name']
    if intentName == "GetNewProgramIntent":
        return program_day(intent, session)
    elif intentName == "AMAZON.HelpIntent":
        return welcomeuser()
    elif intentName == "AMAZON.CancelIntent" or intentName == "AMAZON.StopIntent":
        return handleSessionEndRequest()
    else:
        raise ValueError("Invalid intent")

def onSessionEnd(sessionEndedRequest, session):
    print("on_session_ended requestId=" + sessionEndedRequest['requestId'] + ", sessionId=" + session['sessionId'])

def welcomeuser():
    sessionAttributes = {}
    cardTitle = " Hello"
    speechOutput =  "Hello , Welcome to the code practice ! " \
                    "You can know your program by saying Tell me  today's program"
    repromptText =   "You can know your program by saying Tell me  today's program"
    shouldEndSession = False
    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def program_day(intent, session):
   
    import random
    index = random.randint(0,len(programs)-1)
    cardTitle = intent['name']
    sessionAttributes = {}
    speechOutput = "Programming is fun and today you have to implement the following code "+ programs[index] 
    repromptText = "You can know your program by saying Tell me  today's program"
    shouldEndSession = True                   
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def handleSessionEndRequest():
    cardTitle = "Session Ended"
    speechOutput = "Thank you for using code practice Alexa Skills Kit. " \
                    "Have a great time! "
    shouldEndSession = True
    return buildResponse({}, buildSpeechletResponse(cardTitle, speechOutput, None, shouldEndSession))

def buildSpeechletResponse(title, output, repromptTxt, endSession):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
            },
            
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
            },
            
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': repromptTxt
                }
            },
        'shouldEndSession': endSession
    }


def buildResponse(sessionAttr , speechlet):
    return {
        'version': '1.0',
        'sessionAttributes': sessionAttr,
        'response': speechlet
    }



programs = [ "Sum of elements of an integer array" ,
          "Implement merge sort using insertion sort" ,
          "Calculate factorial of a number using recursion",
          "Calculate factorial of a number using iteration method" ,
          "Inheritance using concept of abstract classes" ,
          "Program to implement string functions" ,
          "program that asks the user for their name and greets them with their name.",
          "program that prints ‘Hello World’ to the screen." ,
          "program that prints a multiplication table for numbers up to 12." ,
          "function that tests whether a string is a palindrome." ,
          " program that prints the next 20 leap years.",
          "Implement an unbalanced binary search tree" ,
          "Implement a balanced binary search tree of your choice" ,
          "Given two strings, write a program that efficiently finds the longest common subsequence." ,
          "Implement binary search.",
          "Write a function that takes a number and returns a list of its digits.",
          "Write a function that combines two lists by alternatingly taking elements.",
          "Write a function that returns the elements on odd positions in a list.",
          "program to remove duplicate elements from array.",
          "Program to swap two numbers",
          "program to check whether a number is positive or negative.",
          "program to calculate sum of natural numbers.",
          "program to display prime numbers between two intervals.",
          "code to create pattern and structure."
        ]
