<properties
   pageTitle="API functions in PowerApps | Microsoft Azure"
   description="List of out-of-box API functions available in PowerApps"
   services="powerapps"
   documentationCenter="na"
   authors="rajeshramabathiran"
   manager="dwrede"
   editor=""
   tags=""/>
<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="11/17/2015"
   ms.author="rajram"/>

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

Step by step instructions to create an app from data is covered [here][13].

PowerApps provies the following functions for tabular data.

- Get items: This is achieved by binding a control to a datasource
- Update an item: This is achieved through _UpdateContext_ function
- Delete an item: This is achieved through _Remove_ function

All the functions mentioned above are captured as part of [Build a formula][1] article.

##Actions

Actions are functions that can be called on individual APIs. For example, you can post a tweet, send an email, get my manager information, etc.

Following APIs expose one or more actions

- Microsoft Translator
- Office 365 Outlook
- Office 365 Users
- Twitter

###Microsoft Translator

Microsoft Translator is a cloud-based automatic translation service. Connect to Microsoft Translator to perform text translations. You can perform various actions such as detect languages, translate text, etc. 

####Create a new connection for Microsoft Translator
1.  Open an existing PowerApps application or [create a new app from scratch][2].
2.  Click on _File_ and select _Connections_
3.  If you do not have a connection already for _Microsoft Translator_ under _My Connections_ Click on _Available Connections_
![powerapps connections][3]
4.  Under _Available Connections_, select _Microsoft Translator_ from the list and click _Connect_
> TIP: You can use the search box to filter down the specific API
![powerapps connections microsoft translator][4]
5. A new connection to _Microsoft Translator_ is created and it shows up in _My Connections_

####Add Microsoft Translator data source

1. Click on _Content_, and select _Data Sources_
![add data source][5]
2. Select _Insert your data_
3. Select _Microsoft Translator_ under _My Connections_
![add data source - translator][6]
4. Click on _Add Data Source_
![add data source- translator - select][7]
5. A new data source is added for _Microsoft Translator_
![Microsoft Translator data source][8]


Following functions are available in the Microsoft Translator API:

####Get languages
**Syntax**

Languages()

**Description**

Retrieves all languages that Microsoft Translator supports.

**Example usage**

1. On a new screen, click on _Insert_ and select _Controls_
2. From the list of controls available, select _Drop-down_. A drop-down control is created
	1. In the expressions bar, the control's _Items_ is bound to _DropDownSample_ by default
	2. Remove the _DropDownSample_ and replace it with `microsofttranslator!Languages()`
3. Click on the dropdown and notice that the dropdown is populated with the list of available languages from _Microsoft Translator_


####Translate text
**Syntax**

Translate(query, languageTo[, languageFrom, Category])

**Description**

Translates text to a specified language using Microsoft Translator

**Example usage**

1. On a new screen, click on _Insert_ and select _Text_
2. From the list of options available, select _Input Text_. A new text box is added to the screen.
3. Click on _Insert_ and click on _Label_. A new label is added to the screen. 
	1. Drag and drop the label below the input text.
	2. Set its _Text_ property to _"Select destination language"_
4. Click on _Insert_ and select _Controls_
5. From the list of controls available, select _Drop-down_. A drop-down control is created
	1. Drag and drop the control below the label
	2. Set its _Items_ property to _microsofttranslator!Languages()_
6. Click on _Insert_ and select _Text_ 
7. From the list of options available, select _Input Text_. A new text box is added to the screen.
	1. Drag and drop the text box below the drop down
	2. Set its _Default_ property to `microsofttranslator!Translate(Text1!Text, Dropdown1!Selected!Value)`
8. Notice that the second text box automatically updates with the translated text whenever the first text box or the destination language drop down is updated. 

####Detect language
**Syntax**

Detect(query)

**Description**

Detects source language of given text

**Example usage**

1. On a new screen, click on _Insert_ and select _Text_
2. From the list of options available, select _Input Text_. A new text box is added to the screen.
3. Click on _Insert_ and click on _Label_. A new label is added to the screen. 
	1. Drag and drop the label below the input text.
	2. Set its _Text_ property to `microsofttranslator!Detect(Text1!Text)`
4. Notice that the label gets updated automatically with the detected language whenever the text box value changes.

####Get speech languages
**Syntax**

SpeechLanguages()

**Description**

Retrieves the languages available for speech synthesis

**Example usage**

1. On a new screen, click on _Insert_ and select _Controls_
2. From the list of controls available, select _Drop-down_. A drop-down control is created
	1. In the expressions bar, the control's _Items_ is bound to _DropDownSample_ by default
	2. Remove the _DropDownSample_ and replace it with `microsofttranslator!SpeechLanguages()`
3. Click on the drop down and notice that the drop down is populated with the list of available speech languages from _Microsoft Translator_


###Office 365 Outlook
Office 365 is a service that allows the use of Office applications and other productivity services over the Internet. Connect to Office 365 Outlook to manage your mail. 

####Create a new connection for Office 365 Outlook
1.  Open an existing PowerApps application or [create a new app from scratch][2].
2.  Click on _File_ and select _Connections_
3.  If you do not have a connection already for _Office 365 Outlook_ under _My Connections_ Click on _Available Connections_
![powerapps connections][3]
4.  Under _Available Connections_, select _Office 365 Outlook_ from the list and click _Connect_
> TIP: You can use the search box to filter down the specific API
![powerapps connections Office 365 Outlook][14]
5. Provide your credentials and click on _Authorize_.
![powerapps twitter connection authorize][17]
6. A new connection to _Office 365 Outlook_ is created and it shows up in _My Connections_

####Add Office 365 Outlook data source

1. Click on _Content_, and select _Data Sources_
![add data source][5]
2. Select _Insert your data_
3. Select _Office 365 Outlook_ under _My Connections_
![add data source - translator][15]
4. Click on _Add Data Source_
![add data source- translator - select][7]
5. A new data source is added for _Office 365 Outlook_
![Microsoft Translator data source][16]

Following functions are available in Office 365 Outlook API:

####Send Email

**Syntax**

SendEmail(Subject, Body, To[, Attachments, From, CC, BCC, Importance, IsHtml])

**Description**

Sends the message supplied in the request body

**Example usage**

1. On a new screen, click on _Insert_ and select _Label_
	1. Set its _Text_ property to _Subject_
2. Click on Insert and select _Text_
3. From the list of available options, select _Input text_
	1. Set its _Default_ property  to "Hi there"
4. Click on _Insert_ and select _Label_
	1. Set its _Text_ property to _Body_
5. Click on Insert and select _Text_
6. From the list of options available, select _Input text_
	1. Set its _Default_ property  to "Welcome"
7. Click on _Insert_ and select _Label_
	1. Set its _Text_ property to _To_
8. Click on Insert and select _Text_
9. From the list of options available, select _Input text_
	1. Set its _Default_ property  to "user@domain.com"
	> Note: Replace this value with a valid email recipient.
10. Click on _Insert_ and select _Button_
	1. Set its _OnSelect_ property to `office365!SendEmail(text1!text, text2!text, text3!text)`
	2. Set its _Text_ property to _Send email_
11. Run the app, set the values in the text boxes and click on _Send email_ button to send an email.


###Office 365 Users
Office 365 is a service that allows the use of Office applications and other productivity services over the Internet. Connect to Office 365 Users to access user profiles in your organization. You can perform various actions such as get a user's profile, a user's manager or direct reports, etc. 

####Create a new connection for Office 365 Users
1.  Open an existing PowerApps application or [create a new app from scratch][2].
2.  Click on _File_ and select _Connections_
3.  If you do not have a connection already for _Office 365 Outlook_ under _My Connections_ Click on _Available Connections_
![powerapps connections][3]
4.  Under _Available Connections_, select _Office 365 Users_ from the list and click _Connect_
> TIP: You can use the search box to filter down the specific API
![powerapps connections Office 365 Outlook][18]
5. Provide your credentials and click on _Authorize_.
![powerapps twitter connection authorize][21]
6. A new connection to _Office 365 Users_ is created and it shows up in _My Connections_

####Add Office 365 Users data source

1. Click on _Content_, and select _Data Sources_
![add data source][5]
2. Select _Insert your data_
3. Select _Office 365 Users_ under _My Connections_
![add data source - translator][19]
4. Click on _Add Data Source_
![add data source- translator - select][7]
5. A new data source is added for _Office 365 Users_
![Microsoft Translator data source][20]

Following functions are available in Office 365 Users API:

####Get my profile

**Syntax**

MyProfile()

**Description**

Retrieves the profile for the current user

**Example usage**

1. On a new screen, click on _Insert_ and select _Label_
	1. Set its _Text_ property to `office365users!MyProfile()!JobTitle`
2 The label will be populated with your job title.


####Get user profile

**Syntax**

UserProfile(userId)

**Description**

Retrieves a specific user profile

**Example usage**

1. On a new screen, click on _Insert_ and select _Text_
2. From the list of options available, select _Input text_
	1. Set its _Default_ property  to "user@domain.com"
	> Note: Change the value to a valid user email in your organization
3. Click on _Insert_ and select _Label_
	1. Set its _Text_ property to `office365users!UserProfile(Text1!Text)!DisplayName`
4. The label will be populated with the display name of the user specified in the text box.


####Get manager

**Syntax**

Manager(userId)

**Description**

Retrieves user profile for the manager of the specified user

**Example usage**

1. On a new screen, click on _Insert_ and select _Text_
2. From the list of options available, select _Input text_
	1. Set its _Default_ property  to "user@domain.com"
	> Note: Change the value to a valid user email in your organization
3. Click on _Insert_ and select _Label_
	1. Set its _Text_ property to `office365users!Manager(Text1!Text)!DisplayName`
4. The label will be populated with the display name of the specified user's manager.



####Get direct reports

**Syntax**

DirectReports(userId)

**Description**

Get direct reports

**Example usage**

1. On a new screen, click on _Insert_ and select _Text_
2. From the list of options available, select _Input text_
	1. Set its _Default_ property  to "user@domain.com"
	> Note: Set the value to a valid user email in your organization
3. Click on _Insert_ and select _Label_
	1. Set its _Text_ property to `Concatenate("Direct reports of ", Text1!Text)`
4. Click on _Insert_ and select _Gallery_
5. From the list of options available, select _Portrait_ in _Text Galleries_ section
	1. Set its _Items_ property to `office365users!DirectReports(Text1!Text) `
	2. Click on _Options_ in the bottom of the screen
		1. In the gallery pane, set _Body1_ to _Department_, _Heading1_ to _DisplayName_ and _Subtitle1_ to _GivenName_
6. Direct reports of the specified user will be displayed.

####Search for users

**Syntax**

SearchUser(searchTerm)

**Description**

Retrieves search results of user profiles

**Example usage**

1. On a new screen, click on _Insert_ and select _Text_
2. From the list of options available, select _Input text_
	1. Set its _Default_ property  to "user@domain.com"
	> Note: Set the value to a user you want to search in your organization
3. Click on _Insert_ and select _Label_
	1. Set its _Text_ property to `"Search results"`
4. Click on _Insert_ and select _Gallery_
5. From the list of options available, select _Portrait_ in _Text Galleries_ section
	1. Set its _Items_ property to `office365users!SearchUser({searchTerm: Text1!Text}) `
	2. Click on _Options_ in the bottom of the screen
		1. In the gallery pane, set _Body1_ to _Department_, _Heading1_ to _DisplayName_ and _Subtitle1_ to _GivenName_
6. Users matching the search term will be displayed.

###Twitter
Twitter is an online social networking service that enables users to send and receive short messages called 'tweets'. Connect to Twitter to manage your tweets. You can perform various actions such as send tweet, search, view followers, etc. Following functions are available in Twitter API:

####Create a new connection for Twitter
1.  Open an existing PowerApps application or [create a new app from scratch][2].
2.  Click on _File_ and select _Connections_
3.  If you do not have a connection already for _Twitter_ under _My Connections_ Click on _Available Connections_
![powerapps connections][3]
4.  Under _Available Connections_, select _Twitter_ from the list and click _Connect_
> TIP: You can use the search box to filter down the specific API
![powerapps connections microsoft translator][9]
5. Provide your credentials and click on _Authorize_.
![powerapps twitter connection authorize][10]
6. A new connection to _Twitter_ is created and it shows up in _My Connections_

####Add Twitter data source

1. Click on _Content_, and select _Data Sources_
![add data source][5]
2. Select _Insert your data_
3. Select _Twitter_ under _My Connections_
![add data source - twitter][11]
4. Click on _Add Data Source_
![add data source- twitter - select][7]
5. A new data source is added for _Twitter_
![Twitter data source][12]

####Get user timeline

**Syntax**

UserTimeline(userName[, maxResults])

**Description**

Retrieves a collection of the most recent tweets posted by the specified user

**Example usage**

1. On a new screen, click on _Insert_ and select _Text_
2. From the list of options available, select _Input text_
	1. Set its _Default_ property  to "microsoft"
	> Note: You can replace _microsoft_ with any valid twitter handle. Do not prefix @ for the twitter handle.
3. Click on _Insert_ and select _Label_
	1. Set its _Text_ property to `Concatenate("Latest tweets from @", Text1!Text)`
4. Click on _Insert_ and select _Gallery_
5. From the list of options available, select _Portrait_ in _Custom Galleries_ section
	1. Set its _Items_ property to `twitter!UserTimeline(Text1!Text)`
	2. Click on _Insert a visual_ and then select _Label_
		1. Set its _Text_ property to `ThisItem!TweetText`
6. The latest tweets of the specified twitter user will be displayed.

####Get home timeline

**Syntax**

HomeTimeline([maxResults])

**Description**

Retrieves the most recent tweets and re-tweets posted me and my followers

**Example usage**

1. On a new screen, click on _Insert_ and select _Label_
	1. Set its _Text_ property to `"My latest tweets"`
2. Click on _Insert_ and select _Gallery_
3. From the list of options available, select _Portrait_ in _Custom Galleries_ section
	1. Set its _Items_ property to `twitter!HomeTimeline()`
	2. Click on _Insert a visual_ and then select _Label_
		1. Set its _Text_ property to `ThisItem!TweetText`
4. The latest tweets of the current twitter user will be displayed.


####Search tweet

**Syntax**
SearchTweet(searchQuery[, maxResults])

**Description**

Retrieves a collection of relevant tweets matching a specified query

1. On a new screen, click on _Insert_ and select _Text_
2. From the list of options available, select _Input text_
	1. Set its _Default_ property  to "microsoft"
	> Note: You can replace _microsoft_ with any search term.
3. Click on _Insert_ and select _Label_
	1. Set its _Text_ property to `"Search results"`
4. Click on _Insert_ and select _Gallery_
5. From the list of options available, select _Portrait_ in _Custom Galleries_ section
	1. Set its _Items_ property to `twitter!SearchTweet(Text1!Text)`
	2. Click on _Insert a visual_ and then select _Label_
		1. Set its _Text_ property to `ThisItem!TweetText`
6. Tweets matching the specified search term will be displayed.

####Get followers

**Syntax**

Followers(userName[, maxResults])

**Desription**

Retrieves users following the specified user

**Example usage**

1. On a new screen, click on _Insert_ and select _Text_
2. From the list of options available, select _Input text_
	1. Set its _Default_ property  to "microsoft"
	> Note: You can replace _microsoft_ with any valid twitter handle. Do not prefix @ for the twitter handle.
3. Click on _Insert_ and select _Label_
	1. Set its _Text_ property to `Concatenate(Text1!Text, " followers")`
4. Click on _Insert_ and select _Gallery_
5. From the list of options available, select _Portrait_ in _Text Galleries_ section
	1. Set its _Items_ property to `twitter!Followers(Text1!Text)`
	2. Click on _Options_ in the bottom of the screen
		1. In the gallery pane, set _Body1_ to _Description_, _Heading1_ to _FullName_ and _Subtitle1_ to _UserName_
6. Followers of the specified user will be displayed.

####Get my followers

**Syntax**

MyFollowers([maxResults])

**Description**

Retrieves users who are following me

**Example usage**

1. On a new screen, click on _Insert_ and select _Label_
	1. Set its _Text_ property to `"My followers"`
2. Click on _Insert_ and select _Gallery_
3. From the list of options available, select _Portrait_ in _Text Galleries_ section
	1. Set its _Items_ property to `twitter!MyFollowers()`
	2. Click on _Options_ in the bottom of the screen
		1. In the gallery pane, set _Body1_ to _Description_, _Heading1_ to _FullName_ and _Subtitle1_ to _UserName_
4. Followers of the current user will be displayed.

####Get following

**Syntax**

Following(userName[, maxResults])

**Description**

Retrieves users who the specified user is following


**Example usage**

1. On a new screen, click on _Insert_ and select _Text_
2. From the list of options available, select _Input text_
	1. Set its _Default_ property  to "microsoft"
	> Note: You can replace _microsoft_ with any valid twitter handle. Do not prefix @ for the twitter handle.
3. Click on _Insert_ and select _Label_
	1. Set its _Text_ property to `Concatenate("Users following ", Text1!Text)`
4. Click on _Insert_ and select _Gallery_
5. From the list of options available, select _Portrait_ in _Text Galleries_ section
	1. Set its _Items_ property to `twitter!Following(Text1!Text)`
	2. Click on _Options_ in the bottom of the screen
		1. In the gallery pane, set _Body1_ to _Description_, _Heading1_ to _FullName_ and _Subtitle1_ to _UserName_
6. Followers of the specified user will be displayed.


####Get my following

**Syntax**

MyFollowing([maxResults])

**Description**

Retrieves users that I am following

**Example usage**

1. On a new screen, click on _Insert_ and select _Label_
	1. Set its _Text_ property to `"Users following me"`
2. Click on _Insert_ and select _Gallery_
3. From the list of options available, select _Portrait_ in _Text Galleries_ section
	1. Set its _Items_ property to `twitter!MyFollowing()`
	2. Click on _Options_ in the bottom of the screen
		1. In the gallery pane, set _Body1_ to _Description_, _Heading1_ to _FullName_ and _Subtitle1_ to _UserName_
4. Followers of the current user will be displayed.

####Get user

**Syntax**

User(userName)

**Description**

Retrieves details about the specified user (example: user name, description, followers count, etc.)

**Example usage**

1. On a new screen, click on _Insert_ and select _Text_
2. From the list of options available, select _Input text_
	1. Set its _Default_ property  to "microsoft"
	> Note: You can replace _microsoft_ with any valid twitter handle. Do not prefix @ for the twitter handle.
3. Click on _Insert_ and select _Label_
	1. Set its _Text_ property to `twitter!User(Text1!Text)!FollowersCount`
4. Followers count of the specified user will be displayed.


####Post a tweet

**Syntax**

Tweet([tweetText, body])

**Description**

Tweet

**Example usage**

1. On a new screen, click on _Insert_ and select _Text_
2. From the list of options available, select _Input text_
	1. Set its _Default_ property  to "Hi there"
	> Note: You can replace _Hi there_ with any tweet.
3. Click on _Insert_ and select _Button_
	1. Set its _OnSelect_ property to `twitter!Tweet({tweetText: Text1!Text})`
	2. Set its _Text_ property to _Tweet_
4. Run the app and click on _Tweet_ button to send a tweet.



<!--References-->
[1]: reference-functions.md
[2]: get-started-create-from-blank.md
[3]: /media/powerapps-api-functions/powerapps-connections.PNG
[4]: /media/powerapps-api-functions/powerapps-connections-microsoft-translator.PNG
[5]: /media/powerapps-api-functions/powerapps-connections-add-datasource.PNG
[6]: /media/powerapps-api-functions/powerapps-connections-add-datasource-translator.PNG
[7]: /media/powerapps-api-functions/powerapps-connections-add-datasource-translator-select.PNG
[8]: /media/powerapps-api-functions/powerapps-connections-datasource-microsoft-translator.PNG
[9]: /media/powerapps-api-functions/powerapps-connections-twitter.PNG
[10]: /media/powerapps-api-functions/powerapps-connections-twitter-authorize.PNG
[11]: /media/powerapps-api-functions/powerapps-connections-add-datasource-twitter.PNG
[12]: /media/powerapps-api-functions/powerapps-connections-datasource-twitter.PNG
[13]: get-started-create-from-data.md
[14]: /media/powerapps-api-functions/powerapps-connections-o365-outlook.PNG
[15]: /media/powerapps-api-functions/powerapps-connections-add-datasource-o365-outlook.PNG
[16]: /media/powerapps-api-functions/powerapps-connections-datasource-o365-outlook.PNG
[17]: /media/powerapps-api-functions/powerapps-connections-o365-outlook-authorize.PNG
[18]: /media/powerapps-api-functions/powerapps-connections-o365-users.PNG
[19]: /media/powerapps-api-functions/powerapps-connections-add-datasource-o365-users.PNG
[20]: /media/powerapps-api-functions/powerapps-connections-datasource-o365-users.PNG
[21]: /media/powerapps-api-functions/powerapps-connections-o365-users-authorize.PNG