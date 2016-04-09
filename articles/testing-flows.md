<properties
    pageTitle="Testing flows flows | Microsoft Flow"
    description="Test your flows before you finish them to verify they behave as you need."
    services=""
    suite="flow"
    documentationCenter="na"
    authors="merwanhade"
    manager="dwrede"
    editor=""
    tags=""/>

<tags
   ms.service="flow"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="04/08/2016"
   ms.author="mhade"/>

# Testing your flows #

Test in Microsoft Flow to make sure your flows will run as expected.

**Prerequisites**
- [Create a flow](get-started-logic-template.md)

1.Create a new flow. You can create one from a template or start from scratch. This tutorial uses a flow where whenever a new tweet appears, an email is sent with details about the tweet.

2.After you've authored your flow, click the **Test flow** button.
[Insert image showing an authored flow with emphasis on the Test flow button]

3.To complete the test, perform the trigger action. e.g. Post a new tweet with a hashtag "azure" (i.e. #azure)
[Insert image showing the prompt of "This flow can't be tested until the trigger action is performed"]

4.Once the trigger condition is met, the rest of your flow will be executed. You can view the results of the execution in the designer.
[Insert image showing success.]

5.Click on an individual trigger or action to see the inputs and outputs of the execution.
[Insert image where the trigger is expanded to show inputs and outputs]

6.You can now finish creating the flow by choosing the **Create** button or go back to editing the flow by choosing the **Edit** button.
[Insert image with emphasis on the Edit flow and Create buttons]
