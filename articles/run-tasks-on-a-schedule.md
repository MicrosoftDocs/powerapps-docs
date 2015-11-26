<properties
    pageTitle="Run Logic Flows on a schedule | Microsoft PowerApps"
    description="Automate recurring tasks by running Logic Flows on a schedule, such as every day or every hour."
    services=""
    suite="powerapps"
    documentationCenter="na"
    authors="stepsic-microsoft-com"
    manager="dwrede"
    editor=""
    tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="11/14/2015"
   ms.author="stepsic"/>

# Run Logic Flows on a schedule #
Create a logic flow that performs the same task or tasks, such as sending reports in email, every day, hour, or minute. As an alternative, create a logic flow that waits a certain number of minutes or until a certain date before performing a task or tasks.

## Prerequisites ##
- An account on [powerapps.com](http://go.microsoft.com/fwlink/?LinkId=708209)

## Run a logic flow every day, hour, or minute

1. In [powerapps.com](http://go.microsoft.com/fwlink/?LinkId=708209), select **Get started** under **Make a logic flow**.

	![Create a logic flow from blank](./media/run-tasks-on-a-schedule/create-flow.png)

1. Select **Create from blank**.

	![Create a logic flow from blank](./media/run-tasks-on-a-schedule/create-from-blank.png)

1. In the box that says **How would you like to start?** select **Every day**, **Every hour**, or **Every minute**.

	![Every day](./media/run-tasks-on-a-schedule/every-day.png)

1. Add the action or actions that you want the logic flow to take, as [Create a logic flow from scratch](get-started-logic-flow) describes.

## Run a logic flow after a certain number of minutes or on a particular date ##

1. In [powerapps.com](http://go.microsoft.com/fwlink/?LinkId=708209), select **Get started** under **Make a logic flow**.

	![Create a logic flow from blank](./media/run-tasks-on-a-schedule/create-flow.png)

1. Select **Create from blank**.

	![Create a logic flow from blank](./media/run-tasks-on-a-schedule/create-from-blank.png)

1. Specify an event as [Create a logic flow from scratch](get-started-logic-flow) describes.

1. Select the plus icon, and then select **Add action**.

	![Option to add an action to a logic flow](./media/run-tasks-on-a-schedule/add-action.png)

1. In the list of actions, do either of the following:
	- Select **Delay**, and then specify a number of minutes,
	- Select **Delay until**, and then specify a date.

	![Option to add an action to a logic flow](./media/run-tasks-on-a-schedule/add-delay.png)
