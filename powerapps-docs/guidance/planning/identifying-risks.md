---
title: Planning - Identifying Power Apps project risks | Microsoft Docs
description: When planning a Power Apps project, identify what might present a risk to your project, what kind of risks are created by the app, and what you'll do to address them.
author: TGrounds
ms.service: powerapps
ms.topic: conceptual
ms.custom: guidance
ms.date: 06/16/2020
ms.subservice: guidance
ms.author: thground
ms.reviewer: kathyos

---

# Identifying the risks

It's a good idea to identify what might present a risk to your project and what kind
of risks are created by the app. It might sound a little over the top,
but your apps could potentially create risks if those apps are mission-critical,
have high business impact, or use or create sensitive data.

Here are some of the examples of risks that you might need to consider:

- **Resource risks**: These includes risks such as a lack of people to work on the app, lack of
    funding to make the apps, and so on.

- **Business risks**: In cases where business frequently changes, it's important to note that
    changes in the business might affect how the app should be made.

- **External risks**: These are risks that depend on factors outside the control of the project
    team. For example, if the app needs to integrate with other external
    systems, there's a risk that the external system might change the way it works.

- **Security risks**: This is a very important factor to consider because it directly relates to how
    you create your solutions with Power Apps.

After you've identified the risks, consider what you'll do to address them. You
might also want to assess their risk level to understand the potential impact.

- **Severe risk**: A risk that might negatively affect the entire company

- **Significant risk**: A risk that might negatively affect this project or a department, and
    needs to be solved before continuing

- **Minor risk**: A risk that might affect the project but won't stop it from
    continuing, or a risk that has negative effects only at an individual level

## Example: Expense report project risks

We created a table like this for our expense report project:

| Risk         | Risk level | Plan to reduce risk       |
|--------------|------------|-------------------------------|
| We can't confidently move data into the finance system without an expert in the system on the team       | Significant    | Move ERP integration to phase 2, when an expert from IT will be available.       |
| To move off the paper system, we need to educate several hundred employees about the new system for filing expense reports. | Significant    | Engage the HR communications team for educational sessions. Create a deck that managers can use at their team meetings. |

> [!div class="nextstepaction"]
> [Next step: Get support from management](gaining-support.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]