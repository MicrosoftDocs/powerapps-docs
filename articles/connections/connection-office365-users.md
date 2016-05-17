<properties
	pageTitle="Overview of the Office 365 users connection | Microsoft PowerApps"
	description="See the available Office 365 Users functions, responses, and examples"
	services=""
	suite="powerapps"
	documentationCenter="na"
	authors="MandiOhlinger"
	manager="erikre"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="04/26/2016"
   ms.author="mandia"/>

# Office 365 Users

![Office 365 Users](./media/connection-office365-users/office365icon.png)

Office 365 Users lets you access user profiles in your organization using your Office 365 account. You can perform various actions such as get your profile, a user's profile, a user's manager or direct reports and also update a user profile.

You can display this information in a text box on your app. You can display one function, multiple functions, or even combine different functions. For example, you can create an expression that combines the User Name and Phone Number, and then display this information in your app.

This topic shows the available functions.

&nbsp;

[AZURE.INCLUDE [connection-requirements](../../includes/connection-requirements.md)]

## View the available functions
 
This connection includes the following functions:

| Function Name |  Description |
| --- | --- |
|[MyProfile](connection-office365-users.md#myprofile) | Retrieves the profile for the current user |
|[UserProfile](connection-office365-users.md#userprofile) | Retrieves a specific user profile |
|[Manager](connection-office365-users.md#manager) | Retrieves user profile for the manager of the specified user |
|[DirectReports](connection-office365-users.md#directreports) | Returns the direct reports for the specified user |
|[SearchUser](connection-office365-users.md#searchuser) | Retrieves search results of user profiles |


## MyProfile
Get my profile: Retrieves the profile for the current user.

#### Input properties
None.

#### Output properties

| Property Name | Type | Description |
| --- | --- | --- |
| Department | string | Department of the user. |
| DisplayName  | string | Display name of user. |
| GivenName  | string | Given name of user. |
| Id  | string | User id |
| JobTitle  | string | Job Title of the user. |
| Mail  | string | Email id of user. |
| MailNickname  | string | Nickname of user. |
| Surname  | string | Surname of user. |
| TelephoneNumber  | string | Telephone number of user. |
| UserPrincipalName  | string | User Principal Name. |
| AccountEnabled  | boolean | Account enabled flag. |

#### Examples

1. In your app, go to the **Insert** tab, and select **Text box**.
2. In the function bar, set the **[Text](../controls/properties-core.md)** property to any of the following formulas:  

	`office365users.MyProfile().DisplayName`  
	`Office365Users.MyProfile().Mail`


## UserProfile
Get user profile: Retrieves a specific user profile. 

#### Input properties

| Name| Data Type| Required | Description|
| ---|---|---|---|
|Id|string| yes|User principal name or email id |

#### Output properties

| Property Name | Type | Description |
| --- | --- | --- |
| Department | string | Department of the user. |
| DisplayName  | string | Display name of user. |
| GivenName  | string | Given name of user. |
| Id  | string | User id |
| JobTitle  | string | Job Title of the user. |
| Mail  | string | Email id of user. |
| MailNickname  | string | Nickname of user. |
| Surname  | string | Surname of user. |
| TelephoneNumber  | string | Telephone number of user. |
| UserPrincipalName  | string | User Principal Name. |
| AccountEnabled  | boolean | Account enabled flag. |

#### Examples

1. In your app, go to the **Insert** tab, and select **Text box**.
2. In the function bar, set the **[Text](../controls/properties-core.md)** property to any of the following formulas:  

	`Office365Users.UserProfile("useremail@microsoft.com").JobTitle`  
`Office365Users.UserProfile(Office365Users.MyProfile().UserPrincipalName).Mail`  
`Office365Users.UserProfile(Office365Users.MyProfile().Id).AccountEnabled`


## Manager
Get manager: Retrieves user profile for the manager of the specified user

#### Input properties

| Name| Data Type| Required | Description|
| ---|---|---|---|
|Id|string| yes|User principal name or email id |

#### Output properties

| Property Name | Type | Description |
| --- | --- | --- |
| Department | string | Department of the user. |
| DisplayName  | string | Display name of user. |
| GivenName  | string | Given name of user. |
| Id  | string | User id |
| JobTitle  | string | Job Title of the user. |
| Mail  | string | Email id of user. |
| MailNickname  | string | Nickname of user. |
| Surname  | string | Surname of user. |
| TelephoneNumber  | string | Telephone number of user. |
| UserPrincipalName  | string | User Principal Name. |
| AccountEnabled  | boolean | Account enabled flag. |

#### Examples  

1. In your app, go to the **Insert** tab, and select **Text box**.
2. In the function bar, set the **[Text](../controls/properties-core.md)** property to any of the following formulas:  

	`Office365Users.Manager(Office365Users.MyProfile().Id).DisplayName`  
`Office365Users.Manager(Office365Users.MyProfile().Id).TelephoneNumber` 


## DirectReports 
Get direct reports: Get direct reports

#### Input properties

| Name| Data Type| Required | Description|
| ---|---|---|---|
|Id|string| yes|User principal name or email id |

#### Output properties

| Property Name | Type | Description |
| --- | --- | --- |
| Department | string | Department of the user. |
| DisplayName  | string | Display name of user. |
| GivenName  | string | Given name of user. |
| Id  | string | User id |
| JobTitle  | string | Job Title of the user. |
| Mail  | string | Email id of user. |
| MailNickname  | string | Nickname of user. |
| Surname  | string | Surname of user. |
| TelephoneNumber  | string | Telephone number of user. |
| UserPrincipalName  | string | User Principal Name. |
| AccountEnabled  | boolean | Account enabled flag. |

#### Examples  

1. In your app, go to the **Insert** tab, select **Gallery**, and under **text gallery**, select **Vertical**. 
2. In the function bar, set the gallery's **[Items](../controls/properties-core.md)** property to any of the following formulas:  

	`Office365Users.DirectReports("useremail@microsoft.com").DisplayName`  
`Office365Users.DirectReports(Office365Users.MyProfile().Id).Mail`

You can also use an **Input Text** control to enter a manager's email address, and then return her direct reports in the gallery. Steps:  

1. On the **Insert** tab, select **Text**, and then select **Input text**.
2. Rename the text-input control *infoAbout*, and then type in a manager's email address in that control.
3. In the function bar, set the gallery's **[Items](../controls/properties-core.md)** property to the following formula:  

	`Office365Users.DirectReports(infoAbout.Text).DisplayName`

> [AZURE.TIP] We use a Gallery because the DirectReports function can return multiple results. 


## SearchUser
Search for users: Retrieves search results of user profiles

#### Input properties

| Name| Data Type| Required | Description|
| ---|---|---|---|
|searchTerm|string| no | Search string. Applies to: display name, given name, surname, mail, mail nickname, and user principal name|

#### Output properties

| Property Name | Type | Description |
| --- | --- | --- |
| Department | string | Department of the user. |
| DisplayName  | string | Display name of user. |
| GivenName  | string | Given name of user. |
| Id  | string | User id |
| JobTitle  | string | Job Title of the user. |
| Mail  | string | Email id of user. |
| MailNickname  | string | Nickname of user. |
| Surname  | string | Surname of user. |
| TelephoneNumber  | string | Telephone number of user. |
| UserPrincipalName  | string | User Principal Name. |
| AccountEnabled  | boolean | Account enabled flag. |


#### Examples
1. In your app, go to the **Insert** tab, select **Text**, and then select **Input text**.
2. Rename the text-input control *SearchTerm*, and then type a name in that control.
3. On the **Insert** tab, select **Gallery**, and under **text gallery**, select **horizontal**.
4. In the function bar, set the gallery's **[Items](../controls/properties-core.md)** property to the following formula:  

	`office365users.SearchUser({searchTerm: SearchTerm.Text})`

The gallery shows the search results you entered.

> [AZURE.TIP] We use a Gallery because the SearchTerm function can return multiple results. 


## Helpful links

See all the [available connections](../connections-list.md).  
Learn how to [add connections](../add-manage-connections.md) to your apps.
