<properties
    pageTitle="Create Logic Flows from a template | Microsoft PowerApps"
    description="Create Logic Flows from any of several built-in templates."
    services=""
    suite="powerapps"
    documentationCenter="na"
    authors="aftowen"
    manager="dwrede"
    editor=""
    tags=""
 />

<tags
  ms.service="powerapps"
    ms.devlang="na"
    ms.topic="article"
    ms.tgt_pltfrm="na"
    ms.workload="na"
    ms.date="02/01/2016"
   ms.author="aftowen"/>

# Create Logic Flows from a template #
Create Logic Flows from any of several built-in templates that can, for example, send you an email message when anyone sends a tweet that includes a particular keyword.

**Note:** [Create a logic flow from scratch](get-started-logic-flow.md) if you want to start from a blank canvas.

**Prerequisites**

- An account on [powerapps.com](http://go.microsoft.com/fwlink/?LinkId=708209)
- A Twitter account
- Office 365 credentials

## Choose a template

1. In [powerapps.com](http://go.microsoft.com/fwlink/?LinkId=708209), select **Logic flows** in the left navigation bar, and then select **Create a logic flow**.

	![Logic flows option in the left navigation bar](./media/get-started-logic-template/create-logic-flow.png)

1. Select a template, such as **Get Email Notification for Tweets**.

	![New option in the left navigation bar](./media/get-started-logic-template/select-template.png)

1. If prompted, connect to one or more data sources, such as Twitter, by selecting **Add new connection** in the drop-down list and then following the prompts.

	![List of connections that the template requires](./media/get-started-logic-template/confirm-connections.png)

1. Select **Open logic flow**.

	Your logic flow appears, showing each event with a blue title bar and each action with an orange title bar.

	![Default events and actions from template](./media/get-started-logic-template/template-default.png)

## Customize your logic flow ##

1. Select the title bar for an event to expand it, and then customize it (for example, by specifying a keyword that interests you).

	![Specify keyword for tweets](./media/get-started-logic-template/specify-keyword.png)

1. Expand and customize the template's action or actions.

	For example, expand the **Send Email** action, and then customize the subject line, the body, and the recipient fields.

	Customize the subject line and the body by following either or both of these steps:

	- Type any text that you want to appear in every message that this logic flow sends.
	- Select one or more placeholders to add information that's specific to each tweet. (Select the button with the ellipsis to show more placeholders.)

	![Customize the subject line of the notification mail](./media/get-started-logic-template/customize-subject.png)

	In the **To** field, leave your address as the default, or specify one or more other addresses in addition to or instead of your own.

1. Near the bottom of the screen, specify a name for your logic flow, and then select **Done**.

	![Done button](./media/get-started-logic-template/done.png)

When a tweet is sent with the keyword that you specified, you'll receive email notification according to the information that you specified.

## Next steps ##

- [Add steps](multi-step-logic-flow.md), such as different ways to be notified, to your logic flow.
