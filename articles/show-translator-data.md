<properties
   pageTitle="Show data from Microsoft Translator | Microsoft PowerApps"
   description="Translate text into another language and play an audio version of the translation in an app"
   services=""
   suite="powerapps"
   documentationCenter="na"
   authors="aftowen"
   manager="erikre"
   editor=""
   tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="02/11/2016"
   ms.author="anneta"/>

# Show data from Microsoft Translator in PowerApps #

Connect to Microsoft Translator, translate text into another language, and play an audio version of the translation.

**Prerequisites**

Know how to [add and configure a control](add-configure-controls.md).

## Connect to Microsoft Translator ##
1.  Open PowerApps, select **New** on the **File** menu (near the left edge), and then select **Get started** under **Start from scratch**.

	![Open a blank app](./media/show-translator-data/blank-app.png)

1. In the lower-right corner, select **Options**, and then select **Insert your data**.

	![Insert a data source](./media/show-translator-data/insert-data.png)

1. Select **Available connections**, and then select **Microsoft Translator**.

	![Connect to Microsoft Translator](./media/show-translator-data/add-translator.png)

1. Select **Connect**, and then select **Add Data Source**.

	Your connection appears under **Data sources**.

1. Close the **Options** pane by selecting the **X** in its upper-right corner.

	![Close the Options pane](./media/show-translator-data/close-options.png)

## Translate text ##
1. Add a text-input control, and rename it **Source**.

1. Add a drop-down list, rename it **TargetLang**, and move it below the **Source** box.

1. Set the **Items** property of **TargetLang** to this formula:<br>
**microsofttranslator.Languages()**

1. Add a text box, move it below **TargetLang**, and set the text box's **Text** property to this formula:
<br>**microsofttranslator.Translate(Source.Text, TargetLang.Selected.Value)**

1. Type text into **Source**, and select a language in **TargetLang**.

	The text box shows the text that you specified in the language that you specified.

	![Translate text from English to French](./media/show-translator-data/translate-text.png)

## Speak translated text ##
1. If you haven't already, follow the steps in the previous procedure for translating text.

1. Set the **Items** property of the **TargetLang** drop-down list to this formula:<br>
**microsofttranslator.SpeechLanguages()**

1. Rename the text box (not the **Source** box) to **Target**.

1. Add an audio control, and set its **Media** property to this formula:<br>
**microsofttranslator.TextToSpeech(Target.Text, TargetLang.Selected.Value)**

1. Press F5, type text into **Source**, select an option in **TargetLang**, and then select the play button in the audio control.

	The app plays an audio version of the text that you specified in the language that you specified.

1. Press Esc to return to the default workspace.

## Detect the source language ##
1. Add a text-input control, and name it **Source**.

1. Add a text box, and then move it under **Source**.

1. Set the **Text** property of the text box to this formula:
<br>**microsofttranslator.Detect(Source.Text).Name**

1. Type text into **Source**.

	The text box indicates the language of the text that you typed. For example, the text box shows **French** if you type **bonjour** into **Source** or **Italian** if you type **ciao**.
