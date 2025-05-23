---
title: View solution deployments on the deployment page
description: Learn how to view pipeline deployments on the deployment page.
author: asheehi1
ms.author: matp
ms.topic: how-to
ms.date: 4/29/2025
ms.custom: template-how-to
ms.subservice: dataverse-maker
---
# View solution deployments on the deployment page

From the **Solutions** page, makers can navigate to **Deployments** to view all of their solution deployments, across all solutions and pipelines, in one place. If their deployment began from (or was deployed to) the current environment, they're able to view its status and other details.

:::image type="content" source="media/maker-deployment-hub.png" alt-text="Screenshot of the deployment page for makers." lightbox="media/maker-deployment-hub.png":::

## Get started

When you first access the Deployment page, you notice the **Get started** section. This section currently offers several links to relevant documents designed to help makers gain a better understanding of solutions, pipelines, and the in-product Application Lifecycle Management (ALM) process.

## Failed deployments

On the left of the overview, makers can view failed deployments if any. When you select each deployment, a panel appears, highlighting the necessary actions to either retry or revise the solution, ensuring a successful deployment.

## Active deployments

On the right of the overview, makers view their ongoing deployments. When makers select these deployments, they can view the in-progress details of the deployment, such as waiting for a predeployment approval. The active deployments page is useful for makers who work in multiple solutions that are deploying simultaneously.

## Deployment history

At the bottom of the overview, makers view their deployment history. This section provides a comprehensive list of all deployments, including the deployment status, the solution, the pipeline, and the environment. Makers can filter this list by solution, pipeline, and environment to quickly find the deployment they're looking for. This run history view is unique. First it's filtered to only show the current user's deployments specifically to and from this environment, and second it's upleveled to show all the current user's deployments, not just involving one solution or pipeline. Selecting a deployment in this grid shows a details panel, summarizing all the deployment information and displaying the deployment notes as well.

### Retry failed deployments

Deployments shown as **Failed** in the run history view can be deployed by selecting **Retry** in the details panel if the operation was **Deploy**. A confirmation message appears when you confirm the retry.

## Take action with advisor-powered recommendations

Actionable recommendations for improving ALM health within your environment is shown in the **Take action** section at the bottom of the Deployment page. These recommendations help ensure that makers are following the best practices to enable healthy ALM within the organization.

## Why can't I see solution deployments other than those that I initiated?

In order to view others' solution deployments, you must have the Deployment Pipeline Administrator security role or equivalent privileges to view other deployments.

## Related articles

[Use pipelines in Power Platform to deploy solutions](use-pipelines.md)

[View solution deployments on the deployment page for admins](/power-platform/alm/admin-deployment-hub)
