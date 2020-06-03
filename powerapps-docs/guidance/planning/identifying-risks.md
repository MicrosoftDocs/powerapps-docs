---
title: Identifying the risks | Microsoft Docs
description: Identifying the project members
author: TGrounds
ms.service: powerapps
ms.topic: conceptual
ms.custom: guidance
ms.date: 06/02/2020
ms.author: thground
ms.reviewer: kathyos
searchScope:  
  - PowerApps
---

# Identifying the risks

It’s a good idea to identify risk to your project. You should identify what kind
of risks are involved when making the app. It may sound a little over the top,
but your apps could potentially create risks if those apps are mission critical,
have high business impact, or use/create sensitive data.

Here are some of the examples of risks that may need to be considered:

-   **Resource risks**: These includes risks such as lack of people to work on the app, lack of
    funding to make the apps etc.

-   **Business risks**: In cases where business frequently change, it is important to take note that
    there is going to be a risk of changes in the business that may affect how
    the app should be made.

-   **External risks**: These are risks that depend on factors outside the control of the project
    team. For example, if the app needs to integrate with other external
    systems, the external system may change how it works.

-   **Security risks**: This is a very important factor to consider as it directly relates to how
    you create your solutions with the Power Apps.

Once you’ve identified the risks, consider what you will do to address them. You
might also want to include the risk level to understand the potential impact.

-   **Severe risk**: A risk that may impact the entire company

-   **Significant risk**: A risk that may impact this project, or a department that
    needs to be solved before continuing

-   **Minor risk**: A risk that may impact the project but will not stop it from
    continuing, or a risk that affects only at an individual level.

## Example: Expense report project risks


We created a table like this for our expense report project:

| **Risk**                                                                                                               | **Risk Level** | **Plan to reduce risk**                                                                                        |
|------------------------------------------------------------------------------------------------------------------------|----------------|----------------------------------------------------------------------------------------------------------------|
| We can’t confidently move data into the finance system without an expert in the system on the team                     | Significant    | Move ERP integration to phase 2, when an expert from IT will be available                                      |
| To move off paper system, we need to educate several hundred employees about the new system for filing expense reports | Significant    | Engage HR communications team for educational comms Create a deck that managers can use at their team meetings |
