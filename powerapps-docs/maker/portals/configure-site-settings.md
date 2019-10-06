---
title: "Configure site settings for a portal | MicrosoftDocs"
description: "Instructions to add and configure site settings for a portal and global settings for all portals in your organization."
author: sbmjais
manager: shujoshi
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 07/18/2019
ms.author: shjais
ms.reviewer:
---

# Configure site settings for portals

[!include[cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

A site setting is a configurable, named value that is used by website code to modify the behavior or visual style of the portal. Typically when a developer creates the website code, they will reference site settings for various components to enable an end user to modify the setting values to alter the website without having to change the code, recompile, and redeploy the website.

The sample portals that are provided with the installation of [!INCLUDE[pn-dynamics-crm](../../includes/pn-dynamics-crm.md)] portals contain several configurable site settings for various styles used to modify many visual elements within the site such as background style, text color, and layout width.
You can manage the following types of site settings:

- **Global Portal settings**: These settings apply to all portals associated with the [!INCLUDE[pn-dynamics-crm](../../includes/pn-dynamics-crm.md)] organization in which they are being added.
- **Portal site settings**: These settings apply to specific portals (website records) that are associated with the [!INCLUDE[pn-dynamics-crm](../../includes/pn-dynamics-crm.md)] organization in which they are being added.


## Manage portal site settings

1. Go to [portal settings](manage-existing-portals.md#settings) and select **Site settings**.

2. To create a new setting, select **New**.

3. To edit an existing setting, select the **Site Setting** listed in the grid.

4. Specify values for the fields provided: 

    - **Name**:  A label referenced by website code to retrieve the appropriate setting. The name should be unique for the associated website, because the code retrieving the setting will take the first record found with the matching name.
    
    - **Website**:  The associated website. 
    
    - **Value**: The setting
    
    - **Description**: The purpose of the setting or special instructions.

5. Select **Save & Close**.

> [!NOTE] 
> Bing Maps integration is not supported in the German Sovereign Cloud. If you try to create the Bingmaps/credentials setting in this environment, an error message will be displayed.

## Portal site settings

|Name|Value|Description|
|----|-----|-----------|
|Authentication/Registration/RequiresConfirmation|FALSE |A boolean value of true enables email confirmation and disables open registration. Default: False |
|Authentication/Registration/RequiresInvitation|FALSE |A boolean value of true enables invitation code feature and disables open registration. Default: False |
|conference-name|Portals Conference|The name of an adx_conference record that represents the conference for a given portal.|
|HelpDesk/CaseEntitlementEnabled|TRUE|A Boolean value indicating if the Help Desk Case Entitlement is enabled. Default: false|
|HelpDesk/Deflection/DefaultSelectedProductName| |The name of a Product record that is the default selected product in dropdown displayed on the Help Desk Case Deflection if there are more than one product where the producttypecode equals 100000001.|
|Profile/ForceSignUp|FALSE|A Boolean value when set to "True" will force the user to update their profile information before they will be given access to the website contents. Default: False|
|Profile/ShowMarketingOptionsPanel|TRUE|A Boolean value that indicates whether to show the panel that lists the fields to specify the marketing communication preferences on the profile. Default: False|
|Search/Enabled|TRUE|A Boolean value that indicates if search is enabled or not.|
|search/filters|Content:adx_webpage;Events:adx_event,adx_eventschedule;<br>Blogs:adx_blog,adx_blogpost,adx_blogpostcomment;<br>Forums:adx_communityforum,adx_communityforumthread,adx_communityforumpost;<br>Ideas:adx_ideaforum,adx_idea,adx_ideacomment;<br>Issues:adx_issueforum,adx_issue,adx_issuecomment;Help Desk:incident|A collection of search logical name filter options. Defining a value here will add dropdown filter options to site-wide search. This value should be in the form of name/value pairs, with name and value separated by a colon, and pairs separated by a semicolon.<br>For example: "Forums:adx_communityforum,adx_communityforumthread,adx_communityforumpost;Blogs:adx_blog,adx_blogpost,adx_blogpostcomment".|
|Search/IndexQueryName|Portal Search|The name of the system view used by the portal search query. Default: Portal Search|
|search/query|+(@Query) _title:(@Query) _logicalname:adx_webpage~0.9^0.2<br> -_logicalname:adx_webfile~0.9 adx_partialurl:(@Query)<br> _logicalname:adx_blogpost~0.9^0.1 -_logicalname:adx_communityforumthread~0.9|Override query for site search, to apply additional weights and filters. @Query is the query text entered by a user. Lucene query syntax reference: [http://lucene.apache.org/core/old_versioned_docs/versions/2_9_1/queryparsersyntax.html](http://lucene.apache.org/core/old_versioned_docs/versions/2_9_1/queryparsersyntax.html)| 
|Search/Stemmer|English|The language used by the portal search's stemming algorithm. Default: English|
|CustomerSupport/DisplayAllUserActivitiesOnTimeline|FALSE| |
|||

For site settings related to various portal features, see:

- [Authentication identity](https://docs.microsoft.com/en-us/dynamics365/customer-engagement/portals/set-authentication-identity)
- [Azure AD B2C provider](https://docs.microsoft.com/en-us/dynamics365/customer-engagement/portals/azure-ad-b2c)
- [OAuth 2.0](https://docs.microsoft.com/en-us/dynamics365/customer-engagement/portals/configure-oauth2-settings)
- [Open ID Connect](https://docs.microsoft.com/en-us/dynamics365/customer-engagement/portals/configure-openid-settings)
- [WS-Federation](https://docs.microsoft.com/en-us/dynamics365/customer-engagement/portals/configure-ws-federation-settings)
- [SAML 2.0](https://docs.microsoft.com/en-us/dynamics365/customer-engagement/portals/configure-saml2-settings)
- [Migrate identity providers to Azure AD B2C](https://docs.microsoft.com/en-us/dynamics365/customer-engagement/portals/migrate-identity-providers)
- [Search within file attachment content](https://docs.microsoft.com/en-us/dynamics365/customer-engagement/portals/search-file-attachment)
- [Behavior and format of the date and time field](https://docs.microsoft.com/en-us/dynamics365/customer-engagement/portals/behavior-format-date-time-field)
- [Add geolocation](https://docs.microsoft.com/en-us/dynamics365/customer-engagement/portals/add-geolocation)
- [Integrate Field Service](https://docs.microsoft.com/en-us/dynamics365/customer-engagement/portals/integrate-field-service)
- [Implementing General Data Protection Regulations](https://docs.microsoft.com/en-us/dynamics365/customer-engagement/portals/implement-gdpr)
- [Enable header and footer output caching](https://docs.microsoft.com/en-us/dynamics365/customer-engagement/portals/enable-header-footer-output-caching)

## Manage global portal settings

1. Go to [portal settings](manage-existing-portals.md#settings) and select **Site settings**.

2. Go to **Settings** &gt; **Settings**.

3. To create a new setting, select **New**.

4. To edit an existing setting, select the **Site Setting** listed in the grid.

5. Specify values for the fields provided: 

    - **Name**:  A unique name referenced by code to retrieve the appropriate setting.

    - **Value**: The setting

    - **Description**: The purpose of the setting or special instructions.

6. Select **Save & Close**.

> [!NOTE] 
> Bing Maps integration is not supported in the German Sovereign Cloud. If you try to create the BinMap/Key or Adxstudio/ProductivityPack/BingMap/Key setting in this environment, an error message will be displayed.


