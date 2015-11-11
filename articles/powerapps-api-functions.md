<properties
   pageTitle="API functions"
   description="List of out-of-box API functions available in PowerApps"
   services="na"
   documentationCenter="na"
   authors="AFTOwen"
   manager=""
   editor=""
   tags=""/>
<tags
   ms.service="kratosapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="11/08/2015"
   ms.author="anneta"/>

#API functions

PowerApps has support for native functions like math, date time operations, etc. An exhaustive list of these operations is captured in the [Build a formula][1] article.

PowerApps platform also enables connectivity to different services out of the box. These are managed by Microsoft and are available as soon you sign into PowerApps. This documents walks through the actions that can be performed in each of the APIs.

##Types of API functions
The different types of API functions in PowerApps are

- Tabular data operations
- Actions

###Tabular data operations
External services provide capabilities to invoke over entities. For example, you can create a new lead in Salesforce, update a row in excel, delete an item in SharePoint Online list, fetch opportunities from Dynamics CRM Online, etc. The entities in each service is determined dynamically.

Following APIs expose tabular data

- CRM Online
- Salesforce
- SharePoint Online
- SharePoint Server
- SQL Server
- Excel in Dropbox, OneDrive
- Google Sheets

PowerApps provies the following functions for tabular data.

- Get items -- This is achieved by binding a control to a datasource
- Update an item -- This is achieved through UpdateContext function
- Delete an item -- This is achieved through Remove function

All the functions mentioned above are captured as part of [Build a formula][1] article.

##Actions

Actions are functions that can be called on individual APIs. For example, you can post a tweet, send an email, get my manager information, etc.

Following APIs expose one or more actions

- Microsoft Translator
- Office 365 Outlook
- Office 365 Users
- Twitter

###Microsoft Translator

Microsoft Translator is a cloud-based automatic translation service. Connect to Microsoft Translator to perform text translations. You can perform various actions such as detect languages, translate text, etc. Following functions are available in the Microsoft Translator API:

####Get languages
**Syntax**
Languages()

**Description**
Retrieves all languages that Microsoft Translator supports

####Translate text
**Syntax**
Translate(query, languageTo[, languageFrom, Category])

**Description**
Translates text to a specified language using Microsoft Translator

####Detect language
**Syntax**
Detect(query)

**Description**
Detects source language of given text

####Get speech languages
**Syntax**
SpeechLanguages()

**Description**
Retrieves the languages available for speech synthesis

####Text to speech
**Syntax**
TextToSpeech(query, language)

**Description**
Converts a given text into speech as an audio stream in wave format

###Office 365 Outlook
Office 365 is a service that allows the use of Office applications and other productivity services over the Internet. Connect to Office 365 Outlook to manage your mail. Following functions are available in Office 365 Outlook API:

####Send Email
**Syntax**
SendEmail(Subject, Body, To[, Attachments, From, CC, BCC, Importance, IsHtml])

**Description**
Sends the message supplied in the request body

###Office 365 Users
Office 365 is a service that allows the use of Office applications and other productivity services over the Internet. Connect to Office 365 Users to access user profiles in your organization. You can perform various actions such as get a user's profile, a user's manager or direct reports, etc. Following functions are available in Office 365 Users API:

####Get my profile
**Syntax**
MyProfile()

**Description**
Retrieves the profile for the current user

####Get user profile
**Syntax**
UserProfile(userId)

**Description**
Retrieves a specific user profile

####Update profile
**Syntax**
UpdateProfile(userId, DisplayName, GivenName, Surname, Mail, MailNickname, TelephoneNumber, AccountEnabled, UserPrincipalName, Department, JobTitle)

**Description**
Updates the profile of the specified user

####Get manager
**Syntax**
Manager(userId)

**Description**
Retrieves user profile for the manager of the specified user

####Get direct reports
**Syntax**
DirectReports(userId)

**Description**
Get direct reports

####Search for users
**Syntax**
SearchUser(searchTerm)

**Description**
Retrieves search results of user profiles

###Twitter
Twitter is an online social networking service that enables users to send and receive short messages called 'tweets'. Connect to Twitter to manage your tweets. You can perform various actions such as send tweet, search, view followers, etc. Following functions are available in Twitter API:

####Get user timeline
**Syntax**
UserTimeline(userName[, maxResults])

**Description**
Retrieves a collection of the most recent tweets posted by the specified user

####Get home timeline
**Syntax**
HomeTimeline([maxResults])

**Description**
Retrieves the most recent tweets and re-tweets posted me and my followers

####Search tweet
**Syntax**
SearchTweet(searchQuery[, maxResults])

**Description**
Retrieves a collection of relevant tweets matching a specified query

####Get followers
**Syntax**
Followers(userName[, maxResults])

**Desription**
Retrieves users following the specified user

####Get my followers
**Syntax**
MyFollowers([maxResults])

**Description**
Retrieves users who are following me

####Get following
**Syntax**
Following(userName[, maxResults])

**Description**
Retrieves users who the specified user is following

####Get my following
**Syntax**
MyFollowing([maxResults])

**Description**
Retrieves users that I am following

####Get user
**Syntax**
User(userName)

**Description**
Retrieves details about the specified user (example: user name, description, followers count, etc.)

####Post a tweet
**Syntax**
Tweet([tweetText, body])

**Description**
Tweet




<!--References-->
[1]: reference-functions.md