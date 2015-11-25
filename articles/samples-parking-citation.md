<properties
    pageTitle="Parking Citation Sample App | Microsoft PowerApps"
    description="Sample app with SharePoint Online as a data source"
    services=""
    suite="powerapps"
    documentationCenter="na"
    authors="merwanhade"
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
   ms.author="mhade"/>

# Parking Citation #
##NOTE - This page is under construction and may contain inaccuracies.

This PowerApps sample demonstrates how to create an app that stores and retrieves data from a SharePoint Online list. In addition, the app also demonstrates key PowerApps concepts such as:

- Using the pen control for annotations
- Using card galleries to create a grid of images
- Using checkboxes and galleries to create a multi-select listbox
- Using the image control to show latitude and longitude coordinates on a map

The app enables Parking Citation officers to capture infraction details such as vehicle make, vehicle color, and a series of images. Each image can include notes and annotations.

## How to run this sample ##
To run this sample, you will need:

- [Install PowerApps](http://aka.ms/powerappsinstall)
- SharePoint Online site


### 1. [Download the sample as .zip](http://aka.ms/parkingcitationsample)
To get started, download this sample. In the zip, you'll find:

- Parking-Citation.msapp
- parkingcitationsampledata.xlsx
- Sample images
- Address Lookup API

### 2. Upload sample data to your SharePoint Online site


### 3. Run the sample in PowerApps on Windows
- To run the app, open PowerApps on Windows.
- Navigate to the **File**->**Open** menu and Browse to the Parking-Citation.msapp file
- Once the app is open, go to the **File**->**Connections** menu and click **Add Connection**
- Select SharePoint Online and click **Connect**
- Select the first screen of the app and click **Options** followed by **Insert your data**
- From a list of **My connections**, select the SharePoint Online connection you just created.
- Now select **New site** and enter in your **Site URL**
- Select the two lists you set up in the second step of this tutorial and you're good to go.

### 4. (Optional): Ask your IT Admin to register the Address Lookup API in your organization's ASE
Instead of requiring users to type in an address, you can use the Address Lookup API included in the sample to calculate an address based on the user's latitude and longitude.

- Ask your IT admin to register the Address Lookup API in your organization's ASE following this [tutorial](www.powerapps.com/en-us/articles/powerapps-register-api-hosted-in-app-service).
- Add a connection to the registered API
