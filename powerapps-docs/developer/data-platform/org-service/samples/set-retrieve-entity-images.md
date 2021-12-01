---
title: " Set and retrieve entity images (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample showcases how to set and retrieve entity images." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 12/20/2019
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "samples"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Set and retrieve entity images

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

This sample shows how to set and retrieve data for entity images. You can download the sample from [here](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/SetRetrieveImages).

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

This sample shows how to create a connection role that can be used for accounts and contacts.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

Checks the current version of the org.

### Demonstrate

1. Uses the CreateImageAttributeDemoEntity method to create a custom table with the schema name `sample_ImageAttributeDemo` and a primary column with the schema name `sample_Name`.
2. Create an image column with the schema name `EntityImage`. All image columns use this name.

3. Retrieve and update the main form for the `sample_ImageAttributeDemo` table to set the `showImage` column to true so that the image is displayed in the form.

4. Publish the `sample_ImageAttributeDemo` table.

5. Creates five new records for the `sample_ImageAttributeDemo` table using five different sized images located in the Images folder as shown here.After each record is created you have the opportunity to view the record in the web browser application using the `ShowEntityFormInBrowser` method so that you can see how the source images are resized to fit the space available in the form.
6. Retrieves the records with the `entityimage` column and saves the resized files. After you run the sample you can find the files saved in the `\bin\Debug` folder.
7. Retrieves the records with the `entityimage_url` column and displays the relative URL values you can include in your application to access the images. This query should be more responsive because the amount of data transferred is smaller.

### Clean up

Display an option to delete the records in [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]