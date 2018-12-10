---
title: Email screen template reference | Microsoft Docs
description: Understand, at a low level, how the email screen template works in PowerApps
author: caburk
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: anneta
ms.date: 11/19/2018
ms.author: caburk
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---

# Reference information about the email-screen template for canvas apps

For canvas apps in PowerApps, understand how each significant control in the email-screen template contributes to the screen's overall default functionality. This deep dive presents the behavior formulas and the values of other properties that determine how the controls respond to user input. For a high-level discussion of this screen's default functionality, see the [email-screen overview](email-screen-overview.md).

## Prerequisite

Familiarity with how to add and configure screens and other controls as you [create an app in PowerApps](../data-platform-create-app-scratch.md).

## Default functionality

To add an email screen from the template:

1. [Sign in](http://web.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) to PowerApps, and then create an app or open an existing app in PowerApps Studio.

    This topic shows a phone app, but the same concepts apply to a tablet app.

1. On the **Home** tab of the ribbon, select **New screen** > **Email**.

    By default, the screen resembles this graphic:

    ![Email screen](media/email-screen/email-screen-full.png)

This topic explains the expressions or formulas to which various properties (such as **Items** and **OnSelect**) of significant controls are set. Those controls are presented in this order:

* [Text search box](#text-search-box)
* [Add Icon](#add-icon)
* [People browse gallery](#people-browse-gallery)
* [Email people gallery](#email-people-gallery) (+ child controls)
* [Mail icon](#mail-icon)

## Text search box

   ![TextSearchBox control](media/email-screen/email-search-box.png)

Several other controls in the screen have a dependency on this one:

* If a user starts typing any text, **PeopleBrowseGallery** becomes visible.
* If a user types out a valid email address, **AddIcon** becomes visible.
* When a user selects a person within **PeopleBrowseGallery** the search contents are reset.

## Add icon

   ![AddIcon control](media/email-screen/email-add-icon.png)

The purpose of this control is to allow app users to add people who don't exist inside their org to the recipient list for the email being composed.

* Property: **Visible**<br>
    Value: Logic to show the control only when a user types out a full and valid email address into the search box.

  ```
    !IsBlank(TextSearchBox.Text) &&
    IsMatch(TextSearchBox.Text, Match.Email) &&
    Not(Trim(TextSearchBox.Text) in MyPeople.UserPrincipalName)
  ```
  * Line by line this code block says that the **AddIcon** control will only be visible if:

    1. The text in **TextSearchBox** contains something
    1. The text in **TextSearchBox** is a valid email address
    1. The text in **TextSearchBox** doesn't already exist in the MyPeople collection

* Property: **OnSelect**<br>
    Value: Selecting this adds the valid email address to the **MyPeople** collection. This collection is used by the screen as the recipient list.

  ```
    Collect(MyPeople,
        {DisplayName: TextSearchBox.Text, UserPrincipalName: TextSearchBox.Text, Mail: TextSearchBox.Text});
    Reset(TextSearchBox)
  ```
  
  * This code block adds a row to the **MyPeople** collection and populates three fields with the text in **TextSearchBox**. These 3 fields are DisplayName, UserPrincipalName, and Mail. It then resets the contents of **TextSearchBox**

## People browse gallery

   ![PeopleBrowseGallery control](media/email-screen/email-browse-gall.png)

* Property: **Items**
    Value: The top 15 search results of the search text from the **TextSearchBox** control.
    
    `If(!IsBlank(Trim(TextSearchBox.Text)), 'Office365Users'.SearchUser({searchTerm: Trim(TextSearchBox.Text), top: 15}))`

  * The items of this gallery are populated by search results from the [Office365.SearchUser](https://docs.microsoft.com/en-us/connectors/office365users/#searchuser) operation.
    * The operation takes the text in Trim(**TextSearchBox**) as its search term and returns the top 15 results based on that search.
  * **TextSearchBox** is wrapped in a Trim() function because a user search on spaces is invalid.
  * The `Office365Users.SearchUser` operation is wrapped in an `If(!IsBlank(Trim(TextSearchBox.Text)) ... )` function because you only want to call the operation when the search box has user entered text. Otherwise it will be a performance waste.

### People browse gallery Title control

   ![PeopleBrowseGallery Title control](media/email-screen/email-browse-gall-title.png)

* Property: **Text**<br>
    Value: `ThisItem.DisplayName`

  * Displays the person's display name from their Office365 profile.

* Property: **OnSelect**
    Value: Code to add the user to an app level collection, and select the user.

    ```
    Concurrent(
        Set(_selectedUser, ThisItem),
        Reset(TextSearchBox),
        If(Not(ThisItem.UserPrincipalName in MyPeople.UserPrincipalName), Collect(MyPeople, ThisItem))
    )
    ```
    Selecting this control does 3 things concurrently:

    1. Sets the **_selectedUser** variable to the item selected
    1. Resets the search term in **TextSearchBox**
    1. Adds the selected item to the **MyPeople** collection, a collection of all the selected users which the email screen uses as a set of recipients

## Email people gallery

   ![EmailPeopleGallery control](media/email-screen/email-people-gall.png)

* Property: **Items**<br>
    Value: `MyPeople`

  * This is the collection of people initialized / added to by selecting the **PeopleBrowseGallery Title** control

* Property: **Height**<br>
    Value: Logic to set the height based on the number of items currently in the gallery.

  ```
  Min(
      (EmailPeopleGallery.TemplateHeight + EmailPeopleGallery.TemplatePadding * 2) *
          RoundUp(CountRows(EmailPeopleGallery.AllItems) / 2, 0),
      304
    )
  ```

  * The height of this gallery adjusts to the number of items in the gallery to a maximum height of 304.
  * It takes TemplateHeight + TemplatePadding * 2 as the total height of a single row of the EmailPeopleGallery, then multiplies it by the number of rows. Since WrapCount = 2, the number of true rows is RoundUp(CountRows(EmailPeopleGallery.AllItems) / 2, 0).

* Property: **ShowScrollbar**<br>
    Value: `EmailPeopleGallery.Height >= 304`

  * When the height of the gallery reaches 304, the scrollbar will be visible.

### Email people gallery Title control

   ![EmailPeopleGallery Title control](media/email-screen/email-people-gall-text.png)

* Property: **OnSelect**<br>
    Value: `Set(_selectedUser, ThisItem)`

  * Sets the **_selectedUser** variable to the item selected in the **EmailPeopleGallery**

### Email people gallery iconRemove control

   ![MonthDayGallery Title control](media/email-screen/email-people-gall-delete.png)

* Property: **OnSelect**<br>
    Value: `Remove(MyPeople, LookUp(MyPeople, UserPrincipalName = ThisItem.UserPrincipalName))`

  * Looks up the record in the **MyPeople** collection where the UserPrincipalName matches the UserPrincipalName of the selected item, and removes that record from the collection

## Mail icon

* Property: **OnSelect**<br>
    Value: Logic to send the user's email.

  ```
  Set(_emailRecipientString, Concat(MyPeople, Mail & ";"));
  'Office365'.SendEmail(_emailRecipientString, TextEmailSubject.Text, TextEmailMessage.Text, {Importance:"Normal"});
  Reset(TextEmailSubject);
  Reset(TextEmailMessage);
  Clear(MyPeople)
  ```

  * Sending an email requires a semicolon separated string of email addresses. The first line takes the 'Mail' field from all the rows in the **MyPeople** collection and concatenates them down into a single string of email addresses separated by semicolons, and sets the **_emailRecipientString** variable to that string value.
  * It then uses the [Office365.SendEmail](https://docs.microsoft.com/en-us/connectors/office365/#sendemail) operation to send the email to the recipients.
    * The operation has 3 required parameters and 1 optional parameter: **To**, **Subject**, **Body**, and **Importance**. In this example, these are **_emailRecipientString**, **TextEmailSubject**.Text, **TextEmailMessage**.Text, and Normal, respectively.
  * Finally, it resets the **TextEmailSubject** and **TextEmailMessage** controls and clears the **MyPeople** collection.

* Property: **DisplayMode**<br>
    Value: `If(Len(Trim(TextEmailSubject.Text)) > 0 && !IsEmpty(MyPeople), DisplayMode.Edit, DisplayMode.Disabled)`
  * To send an email, the email subject line must have text, and the recipient (**MyPeople**) collection must not be empty.

## Next steps

* [Learn more about this screen](./email-screen-overview.md)
* [Learn more about the Office365 Outlook connector in PowerApps](../connections/connection-office365-outlook.md)
* [Learn more about the Office365 Users connector in PowerApps](../connections/connection-office365-users.md)