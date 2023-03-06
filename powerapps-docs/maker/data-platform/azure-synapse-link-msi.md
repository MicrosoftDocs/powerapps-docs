---
title: Use managed identities for Azure with your Azure data lake storage
description: This article explains how to use Azure Managed identity for your Microsoft Dataverse data in Azure.
author: "JasonHQX"
ms.author: jasonhuang
ms.reviewer: matp
ms.service: powerapps
ms.topic: how-to
ms.date: 03/06/2023
ms.custom: template-how-to 
---
# Use managed identities for Azure with your Azure data lake storage

Azure Data Lake Storage provides a layered security model. This model enables you to secure and control the level of access to your storage accounts that your applications and enterprise environments demand, based on the type and subset of networks or resources used. When network rules are configured, only applications requesting data over the specified set of networks or through the specified set of Azure resources can access a storage account. You can limit access to your storage account to requests originating from specified IP addresses, IP ranges, subnets in an Azure Virtual Network (VNet), or resource instances of some Azure services.

Managed identities for Azure, formerly know as Managed service Identity (MSI), help with the management of secrets. Microsoft Dataverse customers using Azure capabilities create a managed identity (part of Enterprise Policy creation) which can be used for one or more Dataverse environments. This managed identity that will be provisioned in the your tenant is then used by Dataverse to access your Azure data lake.

With managed identities, access to your storage account is restricted to requests originating from the Dataverse environment associated with your tenant. When Dataverse connects to storage on behalf of you, it includes additional context information to prove that the request originates from a secure, trusted environment. This allows storage to grant Dataverse access to your storage account. Managed identities are used to sign the context information in order to establish trust. This adds application-level security in addition to the network and infrastructure security provided by Azure for connections between Azure services.

## Prerequisites

- <!-- prerequisite 1 -->
- <!-- prerequisite 2 -->
- <!-- prerequisite n -->
<!-- remove this section if prerequisites are not needed -->

<!-- 4. H2s 
Required. A how-to article explains how to do a task. The bulk of each H2 should be 
a procedure.
-->

## [Section 1 heading]
<!-- Introduction paragraph -->
1. <!-- Step 1 -->
1. <!-- Step 2 -->
1. <!-- Step n -->

## [Section 2 heading]
<!-- Introduction paragraph -->
1. <!-- Step 1 -->
1. <!-- Step 2 -->
1. <!-- Step n -->

## [Section n heading]
<!-- Introduction paragraph -->
1. <!-- Step 1 -->
1. <!-- Step 2 -->
1. <!-- Step n -->

<!-- 5. Next steps
Required. Provide at least one next step and no more than three. Include some 
context so the customer can determine why they would click the link.
-->

## Next steps
<!-- Add a context sentence for the following links -->
- [Write how-to guides](contribute-how-to-write-howto.md)
- [Links](links-how-to.md)

<!--
Remove all the comments in this template before you sign-off or merge to the 
main branch.
-->
