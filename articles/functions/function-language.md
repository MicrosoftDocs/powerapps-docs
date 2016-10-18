<properties
	pageTitle="Language function | Microsoft PowerApps"
	description="Reference information, including syntax and examples, for the Language function in PowerApps"
	services=""
	suite="powerapps"
	documentationCenter="na"
	authors="gregli-msft"
	manager="anneta"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="10/16/2016"
   ms.author="gregli"/>

# Language function in PowerApps #

Returns the language tag of the current user.

## Description ##

The **Language** function returns the language and region of the current user as a language tag.

Use the language information to tailor your app across locales.  For example, if you are creating an app that will be used in Italy and France, you can use **Language** to automatically display Italian and French strings to your users in those different locations. 

### Lanugage tags ###

The return value of this function is a language tag text in the format:

**"*xx*-*YY*"**

where *xx* is the two character abbreviation for the language and *YY* is the two character abbreviation for the region.  This format is the same as the [IETF BCP-47 language tag](https://tools.ietf.org/html/bcp47) format.  

For example, English in the United States uses the language tag "en-US".  To see the list of supported language tags, type **Value( "1", ** in the formula bar or advanced view and scroll through the list of locales suggested for the second argument.  

The **Text** and **Value** functions also use language tags.  Use these functions for translating to and from text strings in a globally aware manner.

## Syntax ##

**Language**()

## Example ##

### User's locale ###

It is assumed that the host operating system and/or browser are using the default locale for the location.

| Formula | Location | Return Value |
|---------|----------|--------------|
| **Language()** | Rio de Janeiro, Brazil | "pt-BR" |
| **Language()** | Lisbon, Portugal | "pt-PT" |
| **Language()** | Washington DC, USA | "en-US" |
| **Language()** | Manchester, Great Britain | "en-GB" |
| **Language()** | Paris, France | "fr-FR" |

### Localization table ###

A simple approach to localization is to create an Excel spreadsheet mapping an author defined **TextID** to an appropriate text string based on the user's language.  Although you could use a collection or any other data source for this table, we chose Excel because it is easy to edit and manage outside of the app by translators.

1. Create the following table in Excel: 

	![](media/function-language/loc-table.png)

	The entry with *blank* for the **Language** column will be used as the default if there is no specific text string found for a given language. This entry must appear after all other entries for a given **TextID**.

	For our purposes, we only need to look at the language of the locale and not the region.  If regional considerations were important, we could have included the full language tag value in the table above. 

1. Use the **Insert** ribbon, **Table** command, to make this into a proper Excel table.  By default, it will be named **Table1** but you can name it whatever you like with the **Table Tools/Design** ribbon and the **Table Name:** text box on the far left hand side.
 
1. Save the Excel file to your local file system.   

1. In PowerApps, in the right-hand pane, click or tap the **Data Sources** tab, and then click or tap **Add data source**.

1. Click or tap **Add static data to your app**, click or tap the Excel file that you saved, and then click or tap **Open**.

1. Select the table that you created, and then click or tap **Connect**.

In your app, wherever you would have used the text **"Hello"** before, use this formula instead:

* **First( Filter( Table1, TextID = "Hello" && (LanguageTag = Left( Language(), 2 ) || IsBlank( LanguageTag )))).LocalizedText**  

This formula will lookup the appropriate **LocalizedText** value for the language of the user, and if that is not found, will fall back on the default *blank* version. 

### Translation service ###

You can translate text on demand using a translation service, such as the Microsoft Translator service:  

1. In PowerApps, in the right-hand pane, click or tap the **Data Sources** tab, and then click or tap **Add data source**.

1. Click or tap **Microsoft Translator**.

In your app, wherever you would have used the text **"Hello"** before, use this formula instead:

* **MicrosoftTranslator.Translate( "Hello", Language() )**

The Microsoft Translator service uses the same language tags that the **Language** function returns.

This approach comes with some drawbacks when compared to the previous example which utilized a pre-translated table of text strings:

* The translation will take time to complete, requiring a call to a service across the network.  This will result in a lag to see the translated text in your app. 
* The translation will be mechanical and may not be what you anticipate or be the best choice for the situation within your app.



  

 



