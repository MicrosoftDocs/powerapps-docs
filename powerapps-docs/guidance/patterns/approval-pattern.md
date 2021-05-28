---
title: "Power Apps pattern: Approval | Microsoft Docs"
description: Learn how approval apps make it easier to get reviews and sign off on decisions.
author: topness-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: guidance
ms.date: 01/04/2021
ms.author: phtopnes
ms.reviewer: kathyos
---

# Pattern: Approval

<!--![Collage of approval app screenshots](media/approvals-collage.jpg "Collage of approval app screenshots")-->

Power Apps makers use the approval pattern to ensure that data, decisions,
and documents are reviewed by a stakeholder or multiple stakeholders, either all at
once or in sequence. Although the approval pattern can be valuable on its own, it's
frequently combined with other patterns, especially the [inspection or audit pattern](/inspection-pattern).
Approvals can be easily implemented with [Power Automate approval workflows](/power-automate/modern-approvals), but
can also be implemented with capability you build into your app.

## How to recognize the approval pattern

![Illustration of the approval pattern with request, review, and respond steps](media/approval-illustration.png "Illustration of the project management pattern with request, review, and respond steps")

In a typical approval scenario:

1. Data is collected from user input, external systems, or other sources. The
    data might be a document, multiple documents, a single value, or the results
    from another system. The user initiates a request for approval, or the
    system might automatically initiate an approval based on criteria (for
    example, purchases over \$1,000 require approval) or scenario (for example,
    international travel requires executive approval).

2. An approver, or multiple approvers, evaluates the information and takes
    action that does one of the following:

    - Advances the request to another approver.

    - Approves the request.

    - Reassigns the request to another person.

    - Rejects the request.

3. The system takes action based on the response of the approver.

## How customers are using the approval pattern

### Toyota uses Power Automate for travel approvals

[Read the whole story.](https://preview.flow.microsoft.com/blog/toyota-uses-power-automate-and-microsoft-forms-for-travel-approval/)

Toyota Motor North America sends its team members all around the world to visit
Toyota business locations, dealers, and suppliers. With only a general
understanding of Power Automate, one engineer within Toyota Motor North
America's Quality Division created and deployed a solution to the division in
just two weeks.

When the form is submitted, Power Automate uses the Office 365 Users connector
to step through the reporting structure to find the requester's appropriate
approver in the management hierarchy. In certain conditions, for example
international travel, the logic identifies the secondary approver who's needed to finalize the request.

Approvers and managers get an email with highlights of the request and an
attached PDF detailing the request from Microsoft Forms. The engineer used built-in
Word and OneDrive actions to populate a Word document and convert it to PDF.
The requester and approvers get a summary email with the PDF attached, in
addition to the approval notification over email and in the Microsoft Flow
mobile app. Executive approvers have quickly taken to the ability to approve
requests on their mobile devices.

![Screenshot of a Power Automate flow for finding a manager to approve a travel request](media/toyota-travel-request-flow.png "Screenshot of a Power Automate flow for finding a manager to approve a travel request")

### T-Mobile Orbit app for customer initiative approvals

[Read the whole story.](https://powerapps.microsoft.com/blog/tmobile/)

For T-Mobile to be competitive and a leader in the telecommunications industry,
it constantly runs myriad customer initiatives, such
as device promotions, service offers, and technical initiatives. The complex
customer initiative process, from initial input to final approval, takes months
to complete and involves anywhere from 5 to 15 employees at every stage.

When a project member needs to create a new initiative, such as a promotion for
a new device, they go into the app, input the details, and attach all relevant
documentation for their team leader to review. The app is also used by T-Mobile
executives to review and approve initiatives.

This app uses a customizable view of Power Automate approvals within a canvas
app. [Find out how](https://powerapps.microsoft.com/blog/building-an-approval-experience-in-canvas-apps/)
to deploy this capability in your own apps.

![Screenshot of the T-Mobile Orbit app](media/tmobile-orbit-app.jpg "Screenshot of the T-Mobile Orbit app")

### Virgin Atlantic employee credit card approvals

[Read the whole
story.](https://powerapps.microsoft.com/blog/virgin-atlantic-drives-agile-wins-for-mobile-workforce-with-the-power-platform/)

Virgin Atlantic created an app for employees to request a corporate credit card.
After an employee submits this request, it goes to the relevant
manager to approve. This process was previously managed by using paper forms, which
were printed out and handed to the Procurement team. It has now been digitized
by using Power Apps.

![Screenshot of the Virgin Atlantic credit card application app](media/virgin-atlantic-credt-card-app.png "Screenshot of the Virgin Atlantic credit card application app")

## Template: Microsoft Building Access app

This Building Access app is used by organizations to bring employees back to
the office safely, as organizations plan the gradual reopening of their
office facilities. Facilities teams globally are working to restructure building
layouts and seating arrangements to maintain social distancing norms, and
control building occupancy thresholds. Employees use this app to reserve an
office space to work. If the office space is near capacity, an approval is sent
to their manager before the visit is permitted. Managers approve visits by using a
canvas app custom approval screen or an adaptive card in Microsoft Teams.

[Learn how to deploy this solution within your own
Microsoft Power Platform environment.](https://aka.ms/BuildingAccessApp)

:::row:::
   :::column span="":::
      ![Screenshot of the Building Access app request screen](media/microsoft-building-app-request.png "Screenshot of the Building Access app request screen")
   :::column-end:::
   :::column span="":::
      ![Screenshot of the Building Access app approvals screen](media/microsoft-building-app-approvals.png "Screenshot of the Building Access app approvals screen")
   :::column-end:::
:::row-end:::

### Additional examples

- [Hexion uses Microsoft Power Platform to automate IT request
approvals](https://customers.microsoft.com/story/810656-hexion-manufacturing-power-platform)

- [Microsoft transforms payroll processes with Microsoft Power
Automate](https://www.microsoft.com/en-us/itshowcase/transforming-payroll-processes-with-microsoft-power-automate)

- [How Microsoft used Power Automate to create its new centralized banking
portal](https://www.microsoft.com/itshowcase/blog/how-microsoft-used-power-automate-to-create-its-new-centralized-banking-portal/)

- [Streamlining Microsoft's payment processes with Microsoft Power
Automate](https://www.microsoft.com/itshowcase/blog/streamlining-microsofts-payment-processes-with-microsoft-power-automate/)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]