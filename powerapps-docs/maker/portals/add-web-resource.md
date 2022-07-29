---
title: Add Azure storage web resource to a form
description: Steps to add Azure storage web resource to a form to enable uploading attachments to Azure Storage.
author: gitanjalisingh33msft

ms.topic: conceptual
ms.custom: 
ms.date: 07/29/2022
ms.subservice: portals
ms.author: gisingh
ms.reviewer: ndoelman
contributors:
    - gitanjalisingh33msft
    - nickdoelman
---

# Add the Azure Storage web resource to a form

> [!NOTE]
> The steps in this topic describe adding a component to view and add file attachments to Azure for a model-driven app. The control is not usable on a basic or advanced form component on a portal webpage. It is recommended to use a different Dataverse form for creating basic and advanced forms for the portal. See [Enable Azure storage](enable-azure-storage.md#configure-basic-or-advanced-forms) for more information on configuring portal forms to add and view attachments stored in Azure.

Attachments uploaded to Azure Storage (instead of directly to Microsoft Dataverse) can be managed by using notes in Dataverse.

To enable attachments from a particular form in a model-driven app to be uploaded into Azure Storage, you must add a web resource to that form, and [configure Azure Storage for your organization](enable-azure-storage.md).

When a file (for example, attachments.zip) is uploaded to Azure Storage by using the portal, it's represented by a note on a table and a placeholder for the attachment.

:::image type="content" source="media/enable-azure-storage/dataverse-form.png" alt-text="File attachment added to Dataverse form on a model-driven Power App.":::

The attachment file is now named attachment.zip.txt. By default, Dataverse  has no conception of an Azure file, so this placeholder .txt file is stored in Dataverse  instead. The Azure Storage context for the placeholder file shows details about the file.
```
{
  "Name": "attachment.txt",
  "Type": "text/plain",
  "Size": 379,
  "Url": "https://accountname.blob.core.windows.net/storage/81a9a9491c36e51182760026833bcf82/attachment.txt"
}
```

## Steps to add the Azure Storage web resource to a form

To see and interact with the file stored in Azure, you must add the web resource *adx.annotations.html* to the form. As a pre-requisite, ensure that your users have read access to adx_setting table. Otherwise, the web resource won't render properly.

1. In the form editor for the relevant form, In the **Components** area, in the **Display** section, select the **HTML web Resource**.

1. In the **Add HTML web resource** box, select **adx_annotations/adx.annotations.html** and choose **Add**.

1. Enter a name and label for the resource.

1. Select the **Edit** command on the **Web resource** link.

1. In the **Custom Parameter (data)** box, enter **azureEnabled=true**. 

    :::image type="content" source="media/enable-azure-storage/form-designer.png" alt-text="Form designer to add web resource.":::

1. Select **Done** to save the resource.

1. Save the form, and then publish the changes.

The new control will now be rendered on the page, giving you the ability to manage your attachments in Azure Storage.

:::image type="content" source="media/enable-azure-storage/dataverse-form-azure.png" alt-text="File attachment added to Dataverse form on a model-driven Power App stored in Azure.":::

The paper-clip icon has been replaced with a cloud icon to denote that this file is stored in Azure Storage. You can continue to store attachments in Dataverse; those files will be denoted with the paper-clip icon.

> [!NOTE]
> You must add cross-origin resource sharing (CORS) rule on your Azure Storage account as follows, otherwise you will see the regular attachment icon rather than the cloud icon.
> - **Allowed origins**: Specify your domain. For example, `https://contoso.crm.dynamics.com`  <br> Ensure the allowed origin doesn't have trailing `/`. For example, `https://contoso.crm.dynamics.com/` is incorrect.
> - **Allowed verbs**: GET, PUT, DELETE, HEAD, POST
> - **Allowed headers**: Specify the request headers that the origin domain may specify on the CORS request. For example, x-ms-meta-data\*, x-ms-meta-target\*. For this scenario, you must specify *, otherwise the web resource will not render properly.
> - **Exposed headers**: Specify the response headers that may be sent in the response to the CORS request and exposed by the browser to the request issuer. Examples - \* or x-ms-meta-\*. For this scenario, you must specify *, otherwise the web resource will not render properly.
> - **Maximum age (seconds)**: Specify the maximum amount time that a browser should cache the preflight OPTIONS request. For example, 200.
> 
> [!include[More information](../../includes/proc-more-information.md)] [CORS support for the Azure Storage Services](/rest/api/storageservices/cross-origin-resource-sharing--cors--support-for-the-azure-storage-services).

If the attached file is an image, the control will display the image as a thumbnail whether it's stored in Dataverse  or Azure Storage.

> [!NOTE]
> The thumbnail feature is limited to images under 1 MB in size.

![Notes thumbnail.](media/notes-thumbnail.png "Notes thumbnail")

## Processes for Azure Blob Storage

Several processes are required to upload attachments to Azure Storage that must be activated: **AzureBlobStorageEnabled**, **Azure Blob Storage Url** and **Generate Shared Access Signature**.

![Blob storage processes.](media/blob-storage-processes.png "Blob storage processes")

During migration, the processes may get deactivated. Migration may cause attachments to upload to Dataverse instead of Azure Storage after you follow steps to add web resource. Ensure these processes are activated to upload attachments to Azure Storage.

## CORS protocol support

To learn about CORS protocol support in portals, go to [Configure CORS protocol support](configure/cors-support.md).

