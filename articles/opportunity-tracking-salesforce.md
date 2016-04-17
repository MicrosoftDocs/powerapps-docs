<properties
	pageTitle="Track Salesforce opportunities | Microsoft PowerApps"
	description="Step-by-step instructions for opening and running a sample app that connects to the user's Salesforce account."
	services=""
	suite="powerapps"
	documentationCenter="na"
	authors="linhtranms"
	manager="erikre"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="04/11/2016"
   ms.author="litran"/>

# Track Salesforce opportunities in Microsoft PowerApps #
The **Opportunity Tracking** app shows the status and details of all your opportunities in Salesforce, and you can add opportunities to your account from within the app. For each opportunity, you can send an email with details, log a call, add a note, or schedule a task.  

## Open the app ##
1. In [powerapps.com](https://web.powerapps.com), select the tile to open **Opportunity Tracking** for Salesforce.

	![Portal Homepage](./media/opportunity-tracker-salesforce/portal-homepage.png)

1. Select the **Phone** option to show the app as if it were running on a phone.

1. Provide the credentials for your Salesforce account, if you have one, or [create an account](http://www.salesforce.com) and provide credentials for it.

	The **Opportunity Tracking** app shows how many opportunities in each status (Open/Prospective, Closed/Won, Closed/Lost) are in your account. If your account is brand new, sample data will appear.

	![Portal Homepage](./media/opportunity-tracker-salesforce/home.png)

## Show opportunities and accounts ##

1. Select a tile to display a list of opportunities in a particular category, or select **Opportunities** at the bottom of the screen to show a list of all your opportunities.

	![Portal Homepage](./media/opportunity-tracker-salesforce/opportunities.png)

	**Note**: To add an opportunity, select **+** in the upper-right corner on the home screen, and then provide details.

1. Select **Add Filter** > **Opportunity** > **Closed/Won** to show only those opportunities.

	![Portal Homepage](./media/opportunity-tracker-salesforce/filter_status_result.png)

1. Select **Filter** > **Account**, and then enter an account name that exists in your data.

	This example shows the result of filtering the sample data for **Burlington Textiles Corp of America**.

	![Portal Homepage](./media/opportunity-tracker-salesforce/filter_account_result.png)

1. Select an account to view its details.

	This example shows the details for **Burlington Textiles Corp of America**.

	![Portal Homepage](./media/opportunity-tracker-salesforce/account_details.png)

1. Select an opportunity to view its details.

	This example shows details for **Burlington Textile Weaving Plant Generator**.

	![Portal Homepage](./media/opportunity-tracker-salesforce/opportunity_details.png)

1. In the details view of an opportunity, select the pencil icon to edit those details, make your change or changes, and then save them.

	![Portal Homepage](./media/opportunity-tracker-salesforce/opportunity_edit.png)

1. Make the changes you desire and save changes.

## Send an email message ##
1. In the details view of an opportunity, select **Send an Email**.

	![Portal Homepage](./media/opportunity-tracker-salesforce/send_email.png)

1. Select someone in your list of Salesforce contacts, and specify a **Title** and **Body** for the message.

1.  (optional) Add a photo if you already have a file, or take a photo if your device has a camera.

1. When you're ready, select **Send email**.

## Add a note ##
1. In the details view of an opportunity, select **Add a note** to show existing notes, and then select **+** in the upper-right corner.

	![Portal Homepage](./media/opportunity-tracker-salesforce/add_note.png)

1. Specify a title for the note and the note itself, and then select **Save note**.

	![Portal Homepage](./media/opportunity-tracker-salesforce/save_note.png)

## Log a call ##
1. In the details view of an opportunity, select **Log a call**.

	![Portal Homepage](./media/opportunity-tracker-salesforce/log_call.png)

1. Select a contact and the person to whom you want to assign the call, specify other details, and then select **Save**.

## Show activity history ##
1. In the details view of an opportunity, select **Activity History** to show the opportunity details, including emails and calls.

	![Portal Homepage](./media/opportunity-tracker-salesforce/activity_history.png)

### Next steps ###
Learn more by opening a few other sample apps, such as [Case Management with Salesforce](case-management-salesforce.md), that can connect to your data.
