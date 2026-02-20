---
title: "Power Apps pattern: Approval"
description: Learn how to use the Power Apps approval pattern to automate workflows, streamline processes, and ensure efficient decision-making.
#customer intent: As a Power Apps maker, I want to learn how to use Power Automate for approval workflows so that I can streamline decision-making processes.
author: topness-msft
ms.topic: concept-article
ms.custom: guidance
ms.date: 02/20/2026
ms.subservice: guidance
ms.author: phtopnes
ms.reviewer: kathyos
---

# Pattern: Approval

<!--![Collage of approval app screenshots.](media/approvals-collage.jpg "Collage of approval app screenshots")-->

Power Apps makers use the approval pattern to ensure that stakeholders review data, decisions, and documents, either all at once or in sequence. Although valuable on its own, the approval pattern is frequently combined with other patterns, especially the [inspection or audit pattern](/powerapps/guidance/patterns/inspection-pattern). Approvals can be easily implemented with [Power Automate approval workflows](/power-automate/modern-approvals), but can also be implemented with capability you build into your app.

## How to recognize the approval pattern

:::image type="content" source="media/approval-illustration.png" alt-text="Screenshot of the approval pattern illustration showing request, review, and respond steps.":::

In a typical approval scenario:

1. Data is collected from user input, external systems, or other sources. The data might be a document, multiple documents, a single value, or the results from another system. The user initiates a request for approval. Alternatively, the system might automatically initiate an approval based on criteria (for example, purchases over $1,000 require approval) or scenario (for example, international travel requires executive approval).

1. An approver, or multiple approvers, evaluates the information and takes action based on that information. The approver might:
 
    - Advance the request to another approver.
    - Approve the request.
    - Reassign the request to another person.
    - Reject the request.

1. The system takes action based on the response of the approver.

## How customers are using the approval pattern

Customers across industries use the approval pattern to streamline processes.

### Toyota uses Power Automate for travel approvals

[Read the whole story.](https://www.microsoft.com/power-platform/blog/power-automate/toyota-uses-power-automate-and-microsoft-forms-for-travel-approval)

Toyota Motor North America sends its team members all around the world to visit Toyota business locations, dealers, and suppliers. With only a general understanding of Power Automate, one engineer within Toyota Motor North America's Quality Division created and deployed a solution to the division in just two weeks.
When the form is submitted, Power Automate uses the Office 365 Users connector to step through the reporting structure to find the requester's appropriate approver in the management hierarchy. In certain conditions, for example international travel, the logic identifies the secondary approver needed to finalize the request.

Approvers and managers get an email with highlights of the request and an attached PDF detailing the request from Microsoft Forms. The engineer used built-in Word and OneDrive actions to populate a Word document and convert it to PDF. The requester and approvers get a summary email with the PDF attached, in addition to the approval notification over email and in the Microsoft Flow mobile app. Executive approvers quickly adopted the ability to approve requests on their mobile devices.

:::image type="content" source="media/toyota-travel-request-flow.png" alt-text="Screenshot of a Power Automate flow for finding a manager to approve a travel request.":::

### T-Mobile Orbit app for customer initiative approvals

[Read the whole story.](https://www.microsoft.com/power-platform/blog/power-apps/tmobile)

For T-Mobile to be competitive and a leader in the telecommunications industry, it constantly runs myriad customer initiatives, such as device promotions, service offers, and technical initiatives. The complex customer initiative process, from initial input to final approval, takes months to complete and involves anywhere from 5 to 15 employees at every stage.

When a project member needs to create a new initiative, such as a promotion for a new device, they go into the app, input the details, and attach all relevant documentation for their team leader to review. The app is also used by T-Mobile executives to review and approve initiatives.

This app uses a customizable view of Power Automate approvals within a canvas app. [Find out how](https://powerapps.microsoft.com/blog/building-an-approval-experience-in-canvas-apps/) to deploy this capability in your own apps.

:::image type="content" source="media/tmobile-orbit-app.jpg" alt-text="Screenshot of the T-Mobile Orbit app showing the customer initiative approval interface.":::

### Virgin Atlantic employee credit card approvals

[Read the whole story.](https://www.microsoft.com/power-platform/blog/power-apps/virgin-atlantic-drives-agile-wins-for-mobile-workforce-with-the-power-platform/)

Virgin Atlantic created an app for employees to request a corporate credit card. After an employee submits this request, it goes to the relevant approver. Previously, approvers were printed and handed to the Procurement team. The process has now been digitized with Power Apps.

:::image type="content" source="media/virgin-atlantic-credt-card-app.png" alt-text="Screenshot of the Virgin Atlantic credit card application app.":::

## Template: Microsoft Building Access app

Organizations use this Building Access app to bring employees back to the office safely, as they plan the gradual reopening of their office facilities. Facilities teams globally are working to restructure building layouts and seating arrangements to maintain social distancing norms, and control building occupancy thresholds. Employees use this app to reserve an office space to work. If the office space is near capacity, an approval is sent to their manager before the visit is permitted. Managers approve visits by using a canvas app custom approval screen or an adaptive card in Microsoft Teams.

[Learn how to deploy this solution within your own Microsoft Power Platform environment.](https://aka.ms/BuildingAccessApp)

:::row:::
   :::column span="":::
      :::image type="content" source="media/microsoft-building-app-request.png" alt-text="Screenshot of the Building Access app request screen.":::
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/microsoft-building-app-approvals.png" alt-text="Screenshot of the Building Access app approvals screen.":::
   :::column-end:::
:::row-end:::

## More examples

- [Hexion uses Microsoft Power Platform to automate IT request approvals](https://customers.microsoft.com/story/810656-hexion-manufacturing-power-platform)
- [EY uses Power Platform to automate customer payment processing](/power-platform/guidance/case-studies/global-finance)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
