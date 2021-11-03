---
title: "Localize labels and strings on a custom page (preview)" 
description: "This article outlines how to load resx files with localized content and how to use PowerFx to set content for labels on your custom page.
ms.custom: ""
ms.date: 11/01/2021
ms.reviewer: ""
ms.service: powerapps
ms.subservice: mda-maker
ms.topic: "article"
author: "mspilde"
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
  - D365CE
---
# Localize labels, messages and tooltips on a custom page (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

This article outlines how the common to add localized content to a custom page by uploading web resource resx files for each language into your solution and how to use PowerFX to set the content on a lable of a form.  This also applies to tooltips and any message that uses a text control.

  > [!IMPORTANT]
  > - This is a preview feature, and isn't available in all regions.
  > - [!INCLUDE[cc_preview_features_definition](../../includes/cc-preview-features-definition.md)]

## Localizing labels on a custom page
Providing localized content on a custom page in a model-driven app is vital when building apps that support global users or a multilingual organization.  This can be done by uploading text files in a .resx format as a web resource.  The files will need to contain the translated text that you want to use for labels on your custom pages.
The process has the following steps:
1.	Enable languages for your environment
2.	Adding localized resx web resource files into your solution
3.	Adding localized files to your custom page
4.	Managing localized web resources
5.	Adding localized strings to your label controls
6.	Running your app with localized content

## Enable languages for your environment
To add languages for your custom page you need to first enable the languages you want to support in the model-driven app where your custom page will be running.  Please make sure you have followed the steps outlined in the [docs](https://docs.microsoft.com/en-us/powerapps/developer/model-driven-apps/resx-web-resources) to enable languages in the Power Apps admin center .

After completing the steps to enable language(s) in the environment, you will need to upload a resx file for each language in the proper format for the strings you want localized on your custom page. Please read the doc on how to [use resx files as a web resource](https://docs.microsoft.com/en-us/powerapps/developer/model-driven-apps/resx-web-resources) for your model-driven Power App.

After you have the created the files with the localized strings you can upload them into your solution.  There are two ways to accomplish this task, the first is to open your solution in make.powerapps.com and click on the option to add a web resource to your solution in your environment or you can add a web resource while working on a custom page.  Adding while working on a custom page will be covered in the section on adding localized files to your custom page.

## Add localized resx Web Resource files to your solution
Open your solution in make.powerapps.com and click on +New->More->Web Resource
It will open a new tab with a dialog to add resx web resource files.

All files added to your solution need to follow a specific format that includes **{filename}.LanguageID.resx** where the language id is the numeric value for that language.  This is done because the framework relies on this naming convention to identify which resource file should be used to associate the appropriate localized string to a label control.  The {filename} **must be the same** for all your files.  

In this example all localized string files will have the name CustomPageLoc.LanguageID.resx, which means for English it would be **CustomPageLoc.1033.resx**, for French it will be **CustomPageLoc.1036.resx**, for Arabic it will be **CustomPageLoc.1025.resx**, etc.  The display name for every file added must be the same name.

In the example below all files have CPLoc as the display name.  The **display name must be the same** to ensure all loc content is used properly on a custom page for each language.  It is recommended that you add the corresponding name for the language in the description field to help identify the content when viewing the files in the page designer and you will need to load the same language that you working in the maker portal (make.powerapps.com).  For example, if you are **authoring in English, be sure to add the English resx file**.
:::image type="content" source="media/page-localization/studio-web-resource-dialog.png"alt-text="Power Apps Studio web resource dialog.":::

After you have added your file to your solution make sure you publish your changes to ensure the file is included and available for your custom page to reference and add to the page.  The following is a screen shot of the resx files that have been added to a solution and are now available to add to a custom page.
:::image type="content" source="media/page-localization/studio-web-resource-panel.png"alt-text="Power Apps Studio web resource panel.":::

## Adding localized files to your custom page
You can add localized files to your custom page when you are creating the page or when editing a page.  Please refer to the doc to learn more about [creating and using custom pages](https://docs.microsoft.com/en-us/powerapps/maker/model-driven-apps/model-app-page-overview) in your model-driven Power App.

To add a language to your page, click on the resource icon in the left hand to open the Resources pane.
:::image type="content" source="media/page-localization/studio-page-resource-pointer.png "alt-text="Power Apps Studio custom page resources.":::

Click on the + Add resource or the Add resource button
:::image type="content" source="media/page-localization/studio-page-resource-add-resource.png"alt-text="Power Apps Studio custom page add web resource.":::

A dialog will open and list all the available web resources in your solution.  To find your files quickly you can use the search at the top of the dialog to **search for the display name** that will show all your localized resx files.  You only need to select and **add the file that matches the language that you are authoring your page**, in this example the English file should be the only one you need to add.

**It is not necessary to add every file**, you only need to add one file.  The solution and platform will map the uploaded languages based on the display name to the language web resource files that you added to your solution.  If you add multiple files a dialog will be displayed with an error stating that files have already been loaded to your page.

:::image type="content" source="media/page-localization/studio-page-web-resource-add-resource-dialog.png" alt-text="Power Apps Studio custom page add web resource dialog.":::

If you do not see the Resx with the language you want to add in the dialog you will need to add the file to your solution.  You can add a resource to your solution by clicking on the + New Web Resource in the dialog.  This will open a new tab with a dialog to add a resx file.  Please make sure you have read the through and understand the section on adding resx web resources and follow the instructions on how to add localized files to your solution.

After clicking on the Add button, the dialog will close, and the web resource will be listed in the Resource Pane.
:::image type="content" source="media/page-localization/studio-page-web-resource-add-resource-dialog-resx.png"alt-text="Power Apps Studio custom page web resource with resx file.":::

## Managing localized web resources
After a web resource language has been added to your page you can quickly and easily manage the file by simply clicking on the ellipses next to the file.  A flyout will open and you can refresh the web resource if it has been changed, updated or you can remove the resource from your page.  You will need to refresh the ResX resources on your page if the display name has changed or any of the string keys have been updated in the resx file and has been published to your solution. Please note that updating the translations in the resx file and publishing the solution does not require the Resx on your page to be refreshed.
:::image type="content" source="media/page-localization/studio-page-web-resource-add-resource-dialog-refresh.png"alt-text="Power Apps Studio custom page web resource with resx file.":::

## Adding localized string to your label controls

To add localized content to your label control you will need to select the label and set the function to the resource using the text function of the control.  Click on or select the label control and select the text function.
:::image type="content" source="media/page-localization/studio-page-text-option.png"alt-text="Power Apps Studio custom page text option on a control.":::

Using the text function set the value to the web resource and the value you want that is in your web resource resx file.  After setting the expression the content will show in the preview for the page.
:::image type="content" source="media/page-localization/studio-page-text-function.png"alt-text="Power Apps Studio custom page text function for a control.":::

Save and publish your changes to the page and make sure you **also save and publish your changes to the app**.  Both are needed to ensure your localized labels will render with the appropriate strings at runtime.

## Running your app with localized content

After publishing your page and your app, click on play in app designer to open the app in a browser.
Click on your custom page on the sitemap.
:::image type="content" source="media/page-localization/studio-page-runtime-1.png"alt-text="Power Apps Studio custom page runtime.":::

The label(s) for your control(s) will show the localized content.  You can test all languages added to your app and your page(s) by clicking on Personal settings under the gear icon at the top of the page and setting the User Interface Language to the language you would like to test.

:::image type="content" source="media/page-localization/studio-page-runtime-2.png"alt-text="Power Apps Studio custom page runtime setting options.":::

:::image type="content" source="media/page-localization/studio-page-runtime-3.png"alt-text="Power Apps Studio custom page runtime setting dialog.":::