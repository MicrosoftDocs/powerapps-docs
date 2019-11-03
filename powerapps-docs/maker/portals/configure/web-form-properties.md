---
title: "Configure web form properties for a portal | MicrosoftDocs"
description: "Instructions to configure web form properties for a portal."
author: sbmjais
manager: shujoshi
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 11/04/2019
ms.author: shjais
ms.reviewer:
---

# Define web form properties for portals

The web form contains relationships to webpages and a start step to control the initialization of the form within the portal. The relationship to the webpage allows dynamic retrieval of the form definition for a given page node within the website.  

The other options on the web form record itself control top-level preferences for the multiple-step process as a whole, for example whether you'd like to display a progress bar.

To view existing Web forms or to create new web forms, open the [Portal Management app](configure-portal.md) and go to **Portals** > **Web Forms**.

> [!Note]
> A **Web Form** must be associated with a webpage for a given website for the form to be viewable within the site.  

When creating or editing a webpage from the the [Portal Management app](configure-portal.md), a **Web Form** can be specified in the lookup field provided on the **New Web Page** form.

## Web form attributes

The following attributes and relationships determine the functionality of the Web form.


|                Name                 |                                                                                                                                                                                        Description                                                                                                                                                                                         |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                Name                 |                                                                                                                                                                          A title of the form used for reference.                                                                                                                                                                           |
|             Start Step              |                                                                                The first step of the form. A Web form will consist of one or more steps. For more information about these steps please refer to the section titled Web Form Step found below. The first step cannot be of type Condition.                                                                                |
|       Authentication Required       |                                                                              If checked, when a user who is not signed in visits the page that contains the form, they will be redirected to the sign-in page. Upon successful sign-in, the user will be redirected back to the page that contains the form.                                                                               |
|      Start New Session On Load      |              Selecting **Yes** indicates that if the user opens the form in a new browser or new tab, or closes the browser or page and returns, the form will start a completely new session and begin at the first step. Otherwise the session will be persisted and the user can close the browser or page and resume later exactly where they left off. Default: **No**.               |
| Multiple Records Per User Permitted |                                                                                                  Selecting **Yes** indicates that a user is permitted to create more than one submission. This assists the form in determining what to do when a user revisits a form. Default: **Yes**.                                                                                                   |
|       Edit Expired State Code       |                                                                                                                    The target entity's state code integer value that, when combined with the status reason, indicates when an existing record can no longer be edited.                                                                                                                     |
|     Edit Expired Status Reason      |                                                                       The target entity's status code integer value that, when combined with the state code, indicates that when an existing record has these values the record is not to be edited anymore&mdash;for example, when a record is updated as complete.                                                                       |
|        Edit Expired Message         | The message displayed when the existing record's state code and status reason match the values specified. For each language pack installed and enabled for the organization, a field will be available to enter the message in the associated language. Default message; You have already completed a submission. Thank you! |
|                                     |                                                                                                                                                                                                                                                                                                                                                                                            |

## Progress indicator settings

| Name                              | Description                                                                                          |
|-----------------------------------|------------------------------------------------------------------------------------------------------|
| Enabled                           | Check to display the progress indicator. Default: **Disabled**.                                      |
| Type                              | One of the following: Title, Numeric (Step x of n), and Progress Bar. Default: **Title**                                                                                    |
| Position                          | One of the following: Top, Bottom, Left, Right. Position is relative to the form. Default: **Top**.                                                   |
| Prepend Step Number to Step Title | Check to add the number of the step to the beginning of the title of the step. Default is unchecked. |
||

Example of the various progress indicator types:

**Title**

![Track progress using a title](media/track-progress-title.png "Track progress by using a title")  

**Title with Step Number prepended**

![Track progress using a step number](media/track-progress-step-number.png "Track progress by using a step number")  

**Numeric**

![Track progress using a numeral](media/track-progress-numeral.png "Track progress by using a numeral")  

**Progress Bar**

![Track progress using a bar](media/track-progress-bar.png "Track progress by using a bar")  

## “Save changes” warning 

|                 Name                  |                                                                                                                                Description                                                                                                                                |
|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Display Save Changes Warning On Close |                         Select to display a warning message if the user has made changes to field(s) and they try to reload the page, close the browser, select the browser's back button, or select the previous button in a multiple step form.                         |
|     Save Changes Warning Message      | For each language pack installed and enabled for the organization, a field will be available to enter the message in the associated language. If no message is specified, the browser's default will be used. |
|                                       |                                                                                                                                                                                                                                                                           |

Example:

![Save changes warning](media/save-changes-warning.png "Save changes warning")  

>[!Note]
> Firefox does not provide the ability to specify a custom message.

## Geolocation configuration for web form

A managed form can be configured to display a map control to either display an existing location as a pin on a map or to provide the ability for the user to specify a location. See [Add Geolocation](add-geolocation.md).

The form's map control requires additional configuration to tell it what the IDs of the various location fields are, to assign values to them or retrieve values from them. The Web Form Step record has a section that defines these field mappings that you must assign values for. The field names will vary depending on the schema you have created.

![Geolocation data in web form](media/geolocation-managed-form.png "Geolocation data in web form")

> [!Note]
> The Geolocation section is not visible in the German Sovereign Cloud environment. If a user has enabled geolocation by using a different form, it will not be displayed during rendering on portal.

### See also

[Configure a portal](configure-portal.md)  
[Define entity forms](entity-forms.md)  
[Web Form steps for portals](web-form-steps.md)  
[Web Forms metadata for portals](configure-web-form-metadata.md)  
[Web Form subgrid configuration for portals](configure-web-form-subgrid.md)  
[Notes configuration for Web Forms for portals](../configure-notes.md)  
