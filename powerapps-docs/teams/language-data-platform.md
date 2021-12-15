---
title: Dataverse for Teams environment language | Microsoft Docs
description: Dataverse for Teams environment language.
author: NHelgren
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 11/16/2020
ms.subservice: teams
ms.author: nhelgren
ms.reviewer: matp
contributors:
  - mattp123
---
# Dataverse for Teams environment language

A Dataverse for Teams environment is automatically created when a Teams user *either* [creates an app](create-first-app.md) in a team using the Power Apps app for the first time *or* installs an app (created using Power Apps app) in a team for the first time from the Teams app catalog. During the environment creation, the environment’s language is set to the tenant default language.

The language settings for the environment define the language, sorting, and search formats of the tables in the environment. The *default* language set during the automatic creation of the environment can't be changed thereafter. 

When a user accesses the Power Apps app within a team in Microsoft Teams, the user’s language setting is compared against the default language of the Dataverse for Teams environment for the team. Depending on the match of the languages, the following happens:
 
- If the user's language setting matches the default language of the environment, the default language is used to display existing information and for creating new tables and columns.

- If the user's language setting is different from the default language of the environment and the environment:

    - Doesn't have the required language pack installed, the new language pack matching the user's language setting will automatically be installed in the environment. It might take up to 15 minutes for the language pack installation to complete. This is a one-time installation, and will only occur the first time a new language is used.

    - Already has the required language pack installed, the environment will use the user’s language.

    Also, this does not change the default language of the environment, but provides a localized user experience for the user when viewing the existing information in the team, and allows all new tables and columns created by the user to have localized labels that match her/his language.

> [!IMPORTANT]
> - Any existing tables or columns at the time of the language change will not be translated to another language. They will continue to use the existing names.
>- In some cases, a language supported by Teams might not be available in Dataverse for Teams and other Power Platform features. When this happens, the nearest fallback language is used for the interface. More information: [Supported languages and fallbacks](#supported-languages-and-fallbacks) later in this topic. 

### Example

User A’s language is English (United States) in Teams and they create an app in a team called Team 1. 

User B’s language is set to French in Teams and they access the Power Apps app in Team 1.
- If the Dataverse for Teams environment doesn't have the French language pack installed, it will be automatically installed in the environment for Team 1. The user interface for User B immediately changes to French while the language pack is installed. After the language pack is installed, any new tables and columns will be created in the French language.
- If the Dataverse for Teams environment for Team 1 already has the French language pack installed, no additional installation is required.
 
If the User B changes her/his language in Teams again and accesses the Power Apps app in the team next time, the new language pack will be installed if the language isn't already installed in Dataverse for Teams environment.

## Supported languages and fallbacks

The languages supported across Teams, Dataverse for Teams, and other Power Platform features vary slightly. When a language is not supported by Dataverse for Teams and other Power Platform features, these will use an identified fallback language. Here is a list of the languages supported across Teams, Dataverse for Teams, and other Power Platform features and their fallback languages. 

The fallback languages are denoted in *italics*.


| Teams             | Dataverse for Teams           | Power Apps Studio | Power Automate    | Power Virtual Agents | Power BI           |
|-----------------------|-----------------------|------------------------------|-----------------------|-------------------------|-----------------------|
| Arabic                | Arabic                | *English US*                   | *English US*            | *English US*              | Arabic                |
| Brazilian Portuguese  | Brazilian Portuguese  | Brazilian Portuguese         | Brazilian Portuguese  | Brazilian Portuguese    | Brazilian Portuguese  |
| Bulgarian             | Bulgarian             | Bulgarian                    | Bulgarian             | *English US*              | Bulgarian             |
| Catalan               | Catalan               | Catalan                      | Catalan               | *Spanish*                 | Catalan               |
| Croatian              | Croatian              | Croatian                     | Croatian              | *English US*              | Croatian              |
| Czech                 | Czech                 | Czech                        | Czech                 | *English US*              | Czech                 |
| Danish                | Danish                | Danish                       | Danish                | Danish                  | Danish                |
| Dutch                 | Dutch                 | Dutch                        | Dutch                 | Dutch                   | Dutch                 |
| English (Canada)      | *English US*            | *English US*                   | *English US*            | *English US*              | *English US*            |
| English UK            | English UK            | *English US*                   | *English US*            | *English US*              | *English US*            |
| English US            | English US            | English US                   | English US            | English US              | English US            |
| Estonian              | Estonian              | Estonian                     | Estonian              | *English US*              | Estonian              |
| Finnish               | Finnish               | Finnish                      | Finnish               | *Swedish*                 | Finnish               |
| French                | French                | French                       | French                | French                  | French                |
| French (Canada)       | French (Canada)       | *French*                       | *French*                | *French*                  | *French*                |
| German Standard       | German Standard       | German Standard              | German Standard       | German Standard         | German Standard       |
| Greek                 | Greek                 | Greek                        | Greek                 | *English US*              | Greek                 |
| Hebrew                | Hebrew                | *English US*                   | *English US*            | *English US*              | Hebrew                |
| Hindi                 | Hindi                 | Hindi                        | Hindi                 | Hindi                   | Hindi                 |
| Hungarian             | Hungarian             | Hungarian                    | Hungarian             | *English US*              | Hungarian             |
| Icelandic             | *English UK*            | *English US*                   | *English US*            | *English US*              | English UK            |
| Indonesian            | Indonesian            | Indonesian                   | Indonesian            | *English US*              | Indonesian            |
| Italian               | Italian               | Italian                      | Italian               | Italian                 | Italian               |
| Japanese              | Japanese              | Japanese                     | Japanese              | Japanese                | Japanese              |
| Korean                | Korean                | Korean                       | Korean                | Korean                  | Korean                |
| Latvian               | Latvian               | Latvian                      | Latvian               | *English US*              | Latvian               |
| Lithuanian            | Lithuanian            | Lithuanian                   | Lithuanian            | *English US*              | Lithuanian            |
| Norwegian - NB        | Norwegian - NB        | Norwegian - NB               | Norwegian - NB        | Norwegian - NB          | Norwegian - NB        |
| Norwegian - NN        | *Norwegian - NB*        | *Norwegian - NB*               | *Norwegian - NB*        | *Norwegian - NB*          | *Norwegian - NB*        |
| Philipino             | *English UK*            | *English US*                   | *English US*            | *English US*              | *English UK*            |
| Polish                | Polish                | Polish                       | Polish                | Polish                  | Polish                |
| Portuguese (Portugal) | Portuguese (Portugal) | Portuguese (Portugal)        | Portuguese (Portugal) | *Brazilian Portuguese*    | Portuguese (Portugal) |
| Romanian              | Romanian              | Romanian                     | Romanian              | *English US*              | Romanian              |
| Russian (cyrillic)    | Russian (cyrillic)    | Russian (cyrillic)           | Russian (cyrillic)    | Russian (cyrillic)      | Russian (cyrillic)    |
| Serbian (Latin)       | Serbian (Latin)       | Serbian (Latin)              | Serbian (Latin)       | *English US*              | Serbian (Latin)       |
| Simplified Chinese    | Simplified Chinese    | Simplified Chinese           | Simplified Chinese    | Simplified Chinese      | Simplified Chinese    |
| Slovak                | Slovak                | Slovak                       | Slovak                | *English US*              | Slovak                |
| Slovenian             | Slovenian             | Slovenian                    | Slovenian             | *English US*              | Slovenian             |
| Spanish               | Spanish               | Spanish                      | Spanish               | Spanish                 | Spanish               |
| Spanish (Mexico)      | *Spanish*               | *Spanish*                      | *Spanish*               | *Spanish*                 | *Spanish*               |
| Swedish               | Swedish               | Swedish                      | Swedish               | Swedish                 | Swedish               |
| Thai                  | Thai                  | Thai                         | Thai                  | English US              | Thai                  |
| Traditional Chinese   | Traditional Chinese   | Traditional Chinese          | Traditional Chinese   | Traditional Chinese     | Traditional Chinese   |
| Turkish               | Turkish               | Turkish                      | Turkish               | Turkish                 | Turkish               |
| Ukrainian             | Ukrainian             | Ukrainian                    | Ukrainian             | *English US*              | Ukrainian             |
| Vietnamese            | Vietnamese            | Vietnamese                   | *English US*            | *English US*              | Vietnamese            |
| Welsh                 | *English UK*            | *English US*                   | *English US*            | *English US*              | *English UK*            | 

### See also

[What is Dataverse for Teams?](overview-data-platform.md) <br />
[Create tables](create-table.md)<br/>
[About the Dataverse for Teams environment](/power-platform/admin/about-teams-environment)


[!INCLUDE[footer-include](../includes/footer-banner.md)]