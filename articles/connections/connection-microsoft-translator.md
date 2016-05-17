<properties
	pageTitle="Overview of the Microsoft Translator connection | Microsoft PowerApps"
	description="See the available Microsoft Translator functions, responses, and examples"
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

#  Microsoft Translator

![Microsoft Translator](./media/connection-microsoft-translator/translatoricon.png)

Microsoft Translator lets you translate text.

You can display the translated information in a text box on your app. For example, you can create an input text box that asks the user to enter some text to translate. In another text box, you can display the translated text. 

This topic shows the available functions.

&nbsp;

[AZURE.INCLUDE [connection-requirements](../../includes/connection-requirements.md)]

## View the available functions
 
This connection includes the following functions:

| Function Name |  Description |
| --- | --- |
|[Languages](connection-microsoft-translator.md#languages) | Retrieves all languages that Microsoft Translator supports  |
|[Translate](connection-microsoft-translator.md#translate) | Translates text to a specified language using Microsoft Translator  |
|[Detect](connection-microsoft-translator.md#detect) | Detects source language of given text  |
|[SpeechLanguages](connection-microsoft-translator.md#speechlanguages) | Retrieves the languages available for speech synthesis  |
|[TextToSpeech](connection-microsoft-translator.md#texttospeech) | Converts a given text into speech as an audio stream in wave format  |

## Languages
Get languages: Retrieves all languages that Microsoft Translator supports 

#### Input properties
None.

#### Output properties

| Property Name | Data Type | Required | Description |
|---|---|---|---|
|Code|string|No | |
|Name|string|No | |


## Translate
Translate text: Translates text to a specified language using Microsoft Translator 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|query|string|yes|Text to translate|
|languageTo|string|yes|Target language code (example: 'fr')|
|languageFrom|string|no|Source language (if not provided, Microsoft Translator will try to auto-detect) (example: en)|
|category|string|no|Translation category (default: 'general')|

#### Output properties
None. 


## Detect
Detect language: Detects source language of given text 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|query|string|yes|Text whose language will be identified|

#### Output properties

| Property Name | Data Type | Required | Description |
|---|---|---|---|
|Code|string|No | |
|Name|string|No | |


## SpeechLanguages
Get speech languages: Retrieves the languages available for speech synthesis 

#### Input properties
None.

#### Output properties

| Property Name | Data Type | Required | Description |
|---|---|---|---|
|Code|string|No | |
|Name|string|No | |


## TextToSpeech
Text to speech: Converts a given text into speech as an audio stream in wave format 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|query|string|yes|Text to convert|
|language|string|yes|Language code to generate speech (example: 'en-us')|

#### Output properties
None. 


## Helpful links

See all the [available connections](../connections-list.md).  
Learn how to [add connections](../add-manage-connections.md) to your apps.
