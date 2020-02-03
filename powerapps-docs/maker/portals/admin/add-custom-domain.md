---
title: "Add a custom domain name | MicrosoftDocs"
description: "Instructions to add a custom domain name."
author: tapanm-msft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 11/04/2019
ms.author: tapanm
ms.reviewer:
---

# Add a custom domain name

A custom domain can help your customers find your support resources more easily and enhance your brand. Only one custom domain name can be added to a portal. After you've provisioned your portal and acquired your domain name, you'll need an SSL certificate to set up a custom host name. You can use the purchased SSL certificate for your domain to link your portal to a custom domain by using a wizard.

1. Open [Power Apps Portals admin center](admin-overview.md).

2. Go to **Portal Actions** > **Add a Custom Domain Name**. A wizard opens to choose the SSL certificate.

3. On the **Choose a SSL certificate** page, select one of the following options:
   - **Upload a new certificate**: Select this option to upload the .pfx file if you have not yet uploaded it to the organization. Select the upload button underneath **File** to select the .pfx file. After selecting the file, enter the password for your SSL certificate in the **Password** field.
   - **Use an existing certificate**: Select this option to choose the correct certificate from the drop-down list.

     > [!Note]
     > The SSL certificate must meet all the following requirements:
     > - Signed by a trusted certificate authority
     > - Exported as a password-protected PFX file
     > - Contains private key at least 2048 bits long
     > - Contains all intermediate certificates in the certificate chain
     > - Must be SHA2 enabled; SHA1 support is being removed from popular browsers

4. Select **Next**.

5. On the **Choose a host name** page, select one of the following options:
    - **Add a new host name**: Select this option to create a new custom domain. Enter the domain name you want in the **Domain Name** field.
    - **Use an existing host name**: Select this option to choose a host name from the drop-down list. 
   
   > [!Note]
   > - You can only have one custom domain name for a portal. 
   > - To create a custom host name, you will need to create a CNAME with your domain provider that points your domain to the URL of your portal. If you have just added a CNAME with your domain provider, it will take some time to propagate to all DNS servers. If the name is not propagated and you add it here, the following error message will appear: Please add a CNAME record to this domain name. Retry after some time passes.

6. Review the information you have entered, and then select **Next** to begin creating the SSL Binding. You should see the message Custom Domain name has been successfully configured for this Portal. You can now go to {Custom Domain Name} to access this portal. {Custom Domain Name} will be a hyperlink to the Custom Portal URL that was just configured.

7. Select **Finish** to close the wizard.

    > [!Note]
    > If you want to change your existing custom domain name, you must upload a new SSL certificate and follow the steps as mentioned in this section.
    

