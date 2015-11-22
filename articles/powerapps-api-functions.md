<properties
   pageTitle="Read about the API functions in PowerApps | Microsoft PowerApps"
   description="How to use the API functions available in PowerApps"
   services=""
   suite="powerapps"
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
   ms.date="11/19/2015"
   ms.author="rajram"/>

# Learn more about the API functions in PowerApps

PowerApps supports native functions, including math, date time operations, and more. See [Build a formula][1] for a complete list of these operations.

PowerApps enables connectivity to different services out-of-the-box. These are managed by Microsoft and are available as soon you sign into PowerApps.

This article describes the functions and actions available with the Microsoft Translator, Office 365 Outlook,  Office 365 Users, and the Twitter APIs. There are also examples of how to use these functions with your PowerApps.

## Types of API functions
PowerApps uses the following types of API functions:

- Tabular data operations
- Actions

#### Tabular data operations
External services include the ability to call other APIs. For example, you can create a new lead in Salesforce, update a row in excel, delete an item in SharePoint Online list, fetch opportunities from Dynamics CRM Online, and more. The entities in each service is determined dynamically.

The following APIs expose tabular data:

- CRM Online
- Salesforce
- SharePoint Online
- SharePoint Server
- SQL Server
- Excel in Dropbox, OneDrive
- Google Sheets


PowerApps provides the following functions for tabular data:

- Get items: Binds a control to a datasource
- Update an item: Uses the _UpdateContext_ function
- Delete an item: Uses the _Remove_ function

All these functions are listed at [Build a formula][1]. To create PowerApps from existing data, go [here][13].

#### Actions

Actions are functions that can be called on individual APIs. For example, you can post a tweet, send an email, get manager information, and so on. The following APIs expose actions:

- Microsoft Translator
- Office 365 Outlook
- Office 365 Users
- Twitter

## Microsoft Translator API

Microsoft Translator is a cloud-based automatic translation service. You can connect to Microsoft Translator to translate text, and complete different actions such as detect languages, translate text, and  more.

In this section:

- Create a new connection to the Microsoft Translator API.
- Add the Microsoft Translator as a data source to your PowerApps.
- See the API functions and how to use them in your PowerApps.

### Create a new connection for Microsoft Translator
1.  Open an existing PowerApp or [create a new app][2].
2.  On the **File** tab, select **Connections**.
3.  If you don't have an existing _Microsoft Translator_ connection under **My Connections**, select **Available Connections**:  
![powerapps connections][3]
4.  In **Available Connections**, select _Microsoft Translator_, and select **Connect**:  
	**Tip**: You can use the search box to filter for a specific API.  
![powerapps connections microsoft translator][4]
5. A new connection to _Microsoft Translator_ is created and is listed in **My Connections**.

#### Add the Microsoft Translator data source

1. In the PowerApps designer, select the **Content** tab, and select **Data Sources**:  
![add data source][5]
2. Select **Insert your data**:  
![][22]
3. Under **My Connections**, select _Microsoft Translator_:  
![add data source - translator][6]
4. Select **Add Data Source**:  
![add data source- translator - select][7]
5. A new data source is added for _Microsoft Translator_:  
![Microsoft Translator data source][8]

The following functions are available in the Microsoft Translator API.

#### Get languages function

Syntax | Description
--- | ---
Languages() | Retrieves all languages that Microsoft Translator supports.

**Usage Example**

1. On a new screen, select the _Insert_ tab, and select _Controls_.
2. In the list of controls, select _Drop-down_. A drop-down control is created. Then:    

	a) In the function bar, the _Items_ property of the drop-down control is bound to _DropDownSample_ by default.  
	b) Remove _DropDownSample_ and replace it with `microsofttranslator!Languages()`.

3. Select the dropdown. Notice that the dropdown is populated with the list of available languages from _Microsoft Translator_.


#### Translate text function

Syntax | Description
--- | ---
Translate(query, languageTo[, languageFrom, Category]) | Translates text to a specified language using Microsoft Translator

**Usage Example**

1. On a new screen, select the _Insert_ tab, and select _Text_.
2. In the list of options, select _Input Text_. A new text box is added to the screen.
3. On the _Insert_ tab, select _Label_. A new label is added to the screen. Then:  

	a) Drag and drop the label below the input text.  
	b) Set its _Text_ property to _"Select destination language"_.

4. On the _Insert_ tab, select _Controls_.
5. In the list of controls, select _Drop-down_. A drop-down control is created. Then:

	a) Drag and drop the control below the label.  
	b) Set its _Items_ property to _microsofttranslator!Languages()_.

6. On the _Insert_ tab, select _Text_.
7. In the list of options, select _Input Text_. A new text box is added to the screen. Then:  

	a) Drag and drop the text box below the drop down list.  
	b) Set its _Default_ property to `microsofttranslator!Translate(Text1!Text, Dropdown1!Selected!Value)`.

8. When the first text box or the destination language drop-down is updated, the second text box automatically updates with the translated text.

#### Detect language function

Syntax | Description
--- | ---
Detect(query) | Detects source language of given text

**Usage Example**

1. On a new screen, select the _Insert_ tab, and select _Text_.
2. In the list of options, select _Input Text_. A new text box is added to the screen.
3. On the _Insert_ tab, select _Label_. A new label is added to the screen. Next:  

	a) Drag and drop the label below the input text.  
	b) Set its _Text_ property to `microsofttranslator!Detect(Text1!Text)`.

4. When the text box value changes, the label is automatically updated with the detected language.

#### Get speech languages function

Syntax | Description
--- | ---
SpeechLanguages() | Retrieves the languages available for speech synthesis

**Usage Example**

1. On a new screen, select the _Insert_ tab, and select _Controls_.
2. In the list of controls, select _drop-down_. A drop-down control is created. Next:  

	a) In the function bar, the control's _Items_ is bound to _DropDownSample_ by default.  
	b) Remove the _DropDownSample_ and replace it with `microsofttranslator!SpeechLanguages()`.

3. Select the drop down. Notice that the drop down is populated with the list of  the available speech languages from _Microsoft Translator_.


## Office 365 Outlook API
Office 365 is a service that uses Office applications and other productivity services over the Internet. Using this API, you can connect to Office 365 Outlook to manage your mail.

In this section:

- Create a new connection to the Office 365 Outlook API.
- Add Office 365 Outlook as a data source to your PowerApps.
- See the API functions and how to use them in your PowerApps.

#### Create a new connection for Office 365 Outlook
1.  Open an existing PowerApps application or [create a new app][2].
2.  On the **File** tab, select **Connections**.
3.  If you don't have an existing connection to _Office 365 Outlook_ under **My Connections**, select **Available Connections**:  
![powerapps connections][3]
4.  Under **Available Connections**, select _Office 365 Outlook_, and select **Connect**.  
	**Tip**: You can use the search box to filter for the specific API.  
![powerapps connections Office 365 Outlook][14]
5. Enter your credentials and select **Authorize**:  
![powerapps Office 365 connection authorize][17]
6. A new connection to _Office 365 Outlook_ is created and is listed in **My Connections**.


#### Add Office 365 Outlook data source
1. Select the **Content** tab, and select **Data Sources**:  
![add data source][5]
2. Select **Insert your data**.
3. Under **My Connections**, select _Office 365 Outlook_:  
![add data source - translator][15]
4. Select **Add Data Source**:  
![add data source- translator - select][7]
5. A new data source is added for _Office 365 Outlook_:  
![Microsoft Translator data source][16]

The following functions are available in the Office 365 Outlook API.

#### Send Email function

Syntax | Description
--- | ---
SendEmail(Subject, Body, To[, Attachments, From, CC, BCC, Importance, IsHtml]) | Sends the message supplied in the request body

**Usage Example**

1. On a new screen, select the _Insert_ tab, and select _Label_. Set its _Text_ property to _Subject_.
2. On the _Insert_ tab, select _Text_, and select _Input text_. Set its _Default_ property  to "Hi there".
3. On the _Insert_ tab, select _Label_. Set its _Text_ property to _Body_.
4. On the _Insert_ tab, select _Text_, and select _Input text_. Set its _Default_ property  to "Welcome".
5. On the _Insert_ tab, select _Label_. Set its _Text_ property to _To_.
6. On the _Insert_ tab, select _Text_, and select _Input text_. Set its _Default_ property  to "user@domain.com".  
	**Note**: Replace this value with a valid email recipient.
7. On the _Insert_ tab, select _Button_. Then:  

	a) Set its _OnSelect_ property to `office365!SendEmail(text1!text, text2!text, text3!text)`.  
	b) Set its _Text_ property to _Send email_.

8. Run the app and set the values in the text boxes. Select the _Send email_ button to send the email to your recipient.


## Office 365 Users API
Office 365 is a service that uses Office applications and other productivity services over the Internet. You can connect to Office 365 Users to access user profiles in your organization. You can perform various actions such as get a user's profile, get a user's manager or direct reports, and more.

In this section:

- Create a new connection to the Office 365 Users API.
- Add Office 365 Users as a data source to your PowerApps.
- See the API functions and how to use them in your PowerApps.

#### Create a new connection for Office 365 Users
1.  Open an existing PowerApps application or [create a new app][2].
2.  On the **File** tab, select **Connections**.
3.  If you don't have an existing connection to _Office 365 Outlook_ under **My Connections**, select **Available Connections**:  
![powerapps connections][3]
4.  Under **Available Connections**, select _Office 365 Users_, and select **Connect**.  
	**Tip**: You can use the search box to filter for the specific API.  
![powerapps connections Office 365 Outlook][18]
5. Enter your credentials and select **Authorize**:  
![powerapps twitter connection authorize][21]
6. A new connection to _Office 365 Users_ is created and is listed in **My Connections**.

#### Add Office 365 Users data source
1. Select the **Content** tab, and select **Data Sources**:  
![add data source][5]
2. Select **Insert your data**.
3. Under **My Connections**, select **Office 365 Users**:  
![add data source - translator][19]
4. Select **Add Data Source**:  
![add data source- translator - select][7]
5. A new data source is added for _Office 365 Users_:  
![Microsoft Translator data source][20]

The following functions are available in the Office 365 Users API.

#### Get my profile function

Syntax | Description
--- | ---
MyProfile() | Retrieves the profile for the current user

**Usage Example**

1. On a new screen, select the _Insert_ tab, and select _Label_. Set its _Text_ property to `office365users!MyProfile()!JobTitle`.
2. The label is populated with your job title.


#### Get user profile function

Syntax | Description
--- | ---
UserProfile(userId) | Retrieves a specific user profile

**Usage Example**

1. On a new screen, select the _Insert_ tab, and select _Text_.
2. In the list of options, select _Input text_. Set its _Default_ property  to "user@domain.com".  
	**Note**: Change the value to a valid user email in your organization.
3. On the _Insert_ tab, select _Label_. Set its _Text_ property to `office365users!UserProfile(Text1!Text)!DisplayName`.
4. The label is populated with the display name of the user specified in the text box.


#### Get manager function

Syntax | Description
--- | ---
Manager(userId) | Retrieves user profile for the manager of the specified user.

**Usage Example**

1. On a new screen, select the _Insert_ tab, and select _Text_.
2. In the list of options, select _Input text_. Set its _Default_ property  to "user@domain.com".  
	**Note**: Change the value to a valid user email in your organization.
3. On the _Insert_ tab, select _Label_. Set its _Text_ property to `office365users!Manager(Text1!Text)!DisplayName`.
4. The label is populated with the display name of the specified user's manager.


#### Get direct reports function

Syntax | Description
--- | ---
DirectReports(userId) | Gets the direct reports.

**Usage Example**

1. On a new screen, select the _Insert_ tab, and select _Text_.
2. In the list of options, select _Input text_. Set its _Default_ property  to "user@domain.com".  
	**Note**: Set the value to a valid user email in your organization.
3. On the _Insert_ tab, select _Label_. Set its _Text_ property to `Concatenate("Direct reports of ", Text1!Text)`.
4. On the _Insert_ tab, select _Gallery_.
5. In the list of options, select _Portrait_ in _Text Galleries_ section. Then:  

	a) Set its _Items_ property to `office365users!DirectReports(Text1!Text)`.  
	b) Select _Options_ in the bottom of the screen.  
	c) In the gallery pane, set _Body1_ to _Department_, _Heading1_ to _DisplayName_, and _Subtitle1_ to _GivenName_.

6. Direct reports of the specified user are displayed.

#### Search for users function

Syntax | Description
--- | ---
SearchUser(searchTerm) | Retrieves search results of user profiles.

**Usage Example**

1. On a new screen, select the _Insert_ tab, and select _Text_.
2. In the list of options, select _Input text_. Set its _Default_ property to "user@domain.com".  
	**Note**: Set the value to a user you want to search in your organization.
3. On the _Insert_ tab, select _Label_. Set its _Text_ property to `"Search results"`.
4. On the _Insert_ tab, select _Gallery_.
5. In the list of options, select _Portrait_ in _Text Galleries_ section. Then:  

	a) Set its _Items_ property to `office365users!SearchUser({searchTerm: Text1!Text})`.  
	b) Select _Options_ in the bottom of the screen.  
	c) In the gallery pane, set _Body1_ to _Department_, _Heading1_ to _DisplayName_, and _Subtitle1_ to _GivenName_.

6. Users matching the search term are displayed.

## Twitter API
Twitter is an online social networking service that enables users to send and receive short messages called 'tweets'.  You can connect to Twitter to manage your tweets. You can also perform various actions such as send tweet, search, view followers, and more.

In this section:

- Create a new connection to the Twitter API.
- Add Twitter as a data source to your PowerApps.
- See the API functions and how to use them in your PowerApps.

#### Create a new connection for Twitter
1.  Open an existing PowerApps application or [create a new app][2].
2.  On the **File** tab, select **Connections**.
3.  If you don't have an existing connection for _Twitter_ under **My Connections**, select **Available Connections**:  
![powerapps connections][3]
4.  Under **Available Connections**, select _Twitter_, and select **Connect**.  
 	**TIP**: You can use the search box to filter for the specific API.  
![powerapps connections twitter][9]
5. Enter your credentials and select **Authorize**:  
![powerapps twitter connection authorize][10]
6. A new connection to _Twitter_ is created and is listed in **My Connections**.

The following functions are available in the Twitter API.

#### Add Twitter data source
1. Select the **Content** tab, and select **Data Sources**:  
![add data source][5]
2. Select **Insert your data**.
3. Under **My Connections**, select **Twitter**:  
![add data source - twitter][11]
4. Select **Add Data Source**:  
![add data source- twitter - select][7]
5. A new data source is added for _Twitter_:  
![Twitter data source][12]

#### Get user timeline function

Syntax | Description
--- | ---
UserTimeline(userName[, maxResults]) | Retrieves a collection of the most recent tweets posted by the specified user.

**Usage Example**

1. On a new screen, select the _Insert_ tab, and select _Text_.
2. In the list of options, select _Input text_. Set its _Default_ property  to "microsoft".  
	**Note**: You can replace _microsoft_ with any valid twitter handle. Do not prefix @ for the twitter handle.
3. On the _Insert_ tab, select _Label_. Set its _Text_ property to `Concatenate("Latest tweets from @", Text1!Text)`.
4. On the _Insert_ tab, select _Gallery_.
5. In the list of options, select _Portrait_ in the _Custom Galleries_ section. Then:  

	a) Set its _Items_ property to `twitter!UserTimeline(Text1!Text)`.  
	b) Select _Insert a visual_ and then select _Label_.  
	c) Set its _Text_ property to `ThisItem!TweetText`.

6. The latest tweets of the specified twitter user are displayed.

#### Get home timeline function

Syntax | Description
--- | ---
HomeTimeline([maxResults]) | Retrieves the most recent tweets and re-tweets posted by me and my followers.

**Usage Example**

1. On a new screen, select the _Insert_ tab, and select _Label_. Set its _Text_ property to `"My latest tweets"`.
2. On the _Insert_ tab, select _Gallery_.
3. In the list of options, select _Portrait_ in the _Custom Galleries_ section. Then:   

	a) Set its _Items_ property to `twitter!HomeTimeline()`.  
	b) Select _Insert a visual_ and then select _Label_.  
	c) Set its _Text_ property to `ThisItem!TweetText`.

4. The latest tweets of the current twitter user are displayed.


#### Search tweet function

Syntax | Description
--- | ---
SearchTweet(searchQuery[, maxResults]) | Retrieves a collection of relevant tweets matching a specified query.

1. On a new screen, select the _Insert_ tab, and select _Text_.
2. In the list of options, select _Input text_. Set its _Default_ property  to "microsoft".  
	**Note**: You can replace _microsoft_ with any search term.
3. On the _Insert_ tab, select _Label_. Set its _Text_ property to `"Search results"`.
4. On the _Insert_ tab, select _Gallery_.
5. In the list of options, select _Portrait_ in the _Custom Galleries_ section. Then:  

	a) Set its _Items_ property to `twitter!SearchTweet(Text1!Text)`.  
	b) Select _Insert a visual_ and then select _Label_.  
	c) Set its _Text_ property to `ThisItem!TweetText`.

6. Tweets matching the specified search term are displayed.

#### Get followers function

Syntax | Description
--- | ---
Followers(userName[, maxResults]) | Retrieves users following the specified user.

**Usage Example**

1. On a new screen, select the _Insert_ tab, and select _Text_.
2. In the list of options, select _Input text_. Set its _Default_ property  to "microsoft".  
	**Note**: You can replace _microsoft_ with any valid twitter handle. Do not prefix @ for the twitter handle.
3. On the _Insert_ tab, select _Label_. Set its _Text_ property to `Concatenate(Text1!Text, " followers")`.
4. On the _Insert_ tab, select _Gallery_.
5. In the list of options, select _Portrait_ in the _Text Galleries_ section. Then:  

	a) Set its _Items_ property to `twitter!Followers(Text1!Text)`.  
	b) Select _Options_ in the bottom of the screen.  
	c) In the gallery pane, set _Body1_ to _Description_, _Heading1_ to _FullName_, and _Subtitle1_ to _UserName_.

6. Followers of the specified user are displayed.

#### Get my followers function

Syntax | Description
--- | ---
MyFollowers([maxResults]) | Retrieves users who are following me.

**Usage Example**

1. On a new screen, select the _Insert_ tab, and select _Label_. Set its _Text_ property to `"My followers"`.
2. On the _Insert_ tab, select _Gallery_.
3. In the list of options, select _Portrait_ in the _Text Galleries_ section. Then:  

	a) Set its _Items_ property to `twitter!MyFollowers()`.  
	b) Select _Options_ in the bottom of the screen.  
	c) In the gallery pane, set _Body1_ to _Description_, _Heading1_ to _FullName_, and _Subtitle1_ to _UserName_.

4. Followers of the current user are displayed.

#### Get following function

Syntax | Description
--- | ---
Following(userName[, maxResults]) | Retrieves users who the specified user is following.

**Usage Example**

1. On a new screen, select the _Insert_ tab, and select _Text_.
2. In the list of options, select _Input text_. Set its _Default_ property  to "microsoft".  
	**Note**: You can replace _microsoft_ with any valid twitter handle. Do not prefix @ for the twitter handle.
3. On the _Insert_ tab, select _Label_. Set its _Text_ property to `Concatenate("Users following ", Text1!Text)`.
4. On the _Insert_ tab, select _Gallery_.
5. In the list of options, select _Portrait_ in the _Text Galleries_ section. Then:  

	a) Set its _Items_ property to `twitter!Following(Text1!Text)`.  
	b) Select _Options_ in the bottom of the screen.  
	c) In the gallery pane, set _Body1_ to _Description_, _Heading1_ to _FullName_, and _Subtitle1_ to _UserName_.

6. Followers of the specified user are displayed.


#### Get my following function

Syntax | Description
--- | ---
MyFollowing([maxResults])| Retrieves users that I am following.

**Usage Example**

1. On a new screen, select the _Insert_ tab, and select _Label_. Set its _Text_ property to `"Users following me"`.
2. On the _Insert_ tab, select _Gallery_.
3. In the list of options, select _Portrait_ in the _Text Galleries_ section. Then:  

	a) Set its _Items_ property to `twitter!MyFollowing()`.  
	b) Select _Options_ in the bottom of the screen.  
	c) In the gallery pane, set _Body1_ to _Description_, _Heading1_ to _FullName_, and _Subtitle1_ to _UserName_.

4. Followers of the current user are displayed.

#### Get user function

Syntax | Description
--- | ---
User(userName) | Retrieves details about the specified user, including user name, description, followers count, and so on.

**Usage Example**

1. On a new screen, select the _Insert_ tab, and select _Text_.
2. In the list of options, select _Input text_. Set its _Default_ property  to "microsoft".  
	**Note**: You can replace _microsoft_ with any valid twitter handle. Do not prefix @ for the twitter handle.
3. On the _Insert_ tab, select _Label_. Set its _Text_ property to `twitter!User(Text1!Text)!FollowersCount`.
4. The followers count of the specified user are displayed.


#### Post a tweet function

Syntax | Description
--- | ---
Tweet([tweetText, body])| Tweets a post.

**Example usage**

1. On a new screen, select the _Insert_ tab, and select _Text_.
2. In the list of options, select _Input text_. Set its _Default_ property  to "Hi there".  
	**Note**: You can replace _Hi there_ with any tweet.
3. On the _Insert_ tab, select _Button_. Then:  

	a) Set its _OnSelect_ property to `twitter!Tweet({tweetText: Text1!Text})`.  
	b) Set its _Text_ property to _Tweet_.

4. Run the app and select the _Tweet_ button to send a tweet.



<!--References-->
[1]: reference-functions.md
[2]: get-started-create-from-blank.md
[3]: ./media/powerapps-api-functions/powerapps-connections.PNG
[4]: ./media/powerapps-api-functions/powerapps-connections-microsoft-translator.PNG
[5]: ./media/powerapps-api-functions/powerapps-connections-add-datasource.PNG
[6]: ./media/powerapps-api-functions/powerapps-connections-add-datasource-translator.PNG
[7]: ./media/powerapps-api-functions/powerapps-connections-add-datasource-translator-select.PNG
[8]: ./media/powerapps-api-functions/powerapps-connections-datasource-microsoft-translator.PNG
[9]: ./media/powerapps-api-functions/powerapps-connections-twitter.PNG
[10]: ./media/powerapps-api-functions/powerapps-connections-twitter-authorize.PNG
[11]: ./media/powerapps-api-functions/powerapps-connections-add-datasource-twitter.PNG
[12]: ./media/powerapps-api-functions/powerapps-connections-datasource-twitter.PNG
[13]: get-started-create-from-data.md
[14]: ./media/powerapps-api-functions/powerapps-connections-o365-outlook.PNG
[15]: ./media/powerapps-api-functions/powerapps-connections-add-datasource-o365-outlook.PNG
[16]: ./media/powerapps-api-functions/powerapps-connections-datasource-o365-outlook.PNG
[17]: ./media/powerapps-api-functions/powerapps-connections-o365-outlook-authorize.PNG
[18]: ./media/powerapps-api-functions/powerapps-connections-o365-users.PNG
[19]: ./media/powerapps-api-functions/powerapps-connections-add-datasource-o365-users.PNG
[20]: ./media/powerapps-api-functions/powerapps-connections-datasource-o365-users.PNG
[21]: ./media/powerapps-api-functions/powerapps-connections-o365-users-authorize.PNG

[22]: ./media/powerapps-api-functions/insertdata.png
