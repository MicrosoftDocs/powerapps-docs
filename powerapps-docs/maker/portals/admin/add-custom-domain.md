---
title: Add a custom domain name
description: Learn how to to add a custom domain name to your portal.
author: neerajnandwana-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 04/21/2021
ms.subservice: portals
ms.author: nenandw
ms.reviewer: tapanm
contributors:
    - neerajnandwana-msft
    - tapanm-msft
---

# Add a custom domain name

A custom domain can help your customers find your support resources more easily and enhance your brand. Only one custom domain name can be added to a portal. After you've provisioned your portal and acquired your domain name, you'll need an SSL certificate to set up a custom host name. You can use the purchased SSL certificate for your domain to link your portal to a custom domain by using a wizard.

> [!IMPORTANT]
> You can add a custom domain name to a portal only when the portal is in production state. For more information about portal stages, go to [portal lifecycle](portal-lifecycle.md).

To learn about the roles required to perform this task, read [Admin roles required for portal administrative tasks](portal-admin-roles.md).

1. Open [Power Apps portals admin center](admin-overview.md).

2. Go to **Portal Actions** > **Add a Custom Domain Name**. A wizard opens to choose the SSL certificate.

3. On the **Choose a SSL certificate** page, select one of the following options:
   - **Upload a new certificate**: Select this option to upload the .pfx file if you haven't yet uploaded it to the organization. Select the upload button underneath **File** to select the .pfx file. After selecting the file, enter the password for your SSL certificate in the **Password** field.
   - **Use an existing certificate**: Select this option to choose the correct certificate from the drop-down list.

     > [!NOTE]
     > The SSL certificate must meet all the following requirements:
     > - Signed by a trusted certificate authority.
     > - [Exported](/powershell/module/pkiclient/export-pfxcertificate?preserve-view=true&view=win10-ps) as a password-protected PFX file.
     > - Contains private key at least 2048 bits long.
     > - Contains all intermediate certificates in the certificate chain.
     > - Must be SHA2 enabled; SHA1 support is being removed from popular browsers.
     > - PFX file must be encrypted with TripleDES encryption. Power Apps portals doesn't support AES-256 encryption.
     > - Contains an [Extended Key Usage](https://en.wikipedia.org/w/index.php?title=X.509&section=4#Extensions_informing_a_specific_usage_of_a_certificate) for server authentication (OID = 1.3.6.1.5.5.7.3.1).
     > 
     > The steps to export SSL certificate as a password-protected PFX file may vary depending on your certificate provider. Check with your certificate provider for recommendation. For example, certain providers may suggest to use OpenSSL 3rd party tool from [OpenSSL](https://www.openssl.org/) or [OpenSSL Binaries](https://wiki.openssl.org/index.php/Binaries) sites. 

4. Select **Next**.

5. On the **Choose a host name** page, select one of the following options:
    - **Add a new host name**: Select this option to create a new custom domain. Enter the domain name you want in the **Domain Name** field.
    - **Use an existing host name**: Select this option to choose a host name from the drop-down list. 
   
   > [!NOTE]
   > - You can only have one custom domain name for a portal. 
   > - To create a custom host name, you will need to create a CNAME with your domain provider that points your domain to the URL of your portal. If you have just added a CNAME with your domain provider, it will take some time to propagate to all DNS servers. If the name is not propagated and you add it here, the following error message will appear: Please add a CNAME record to this domain name. Retry after some time passes.

6. Review the information you've entered, and then select **Next** to begin creating the SSL Binding. You should see the message Custom Domain name has been successfully configured for this Portal. You can now go to {Custom Domain Name} to access this portal. {Custom Domain Name} will be a hyperlink to the Custom Portal URL that you configured.

7. Select **Finish** to close the wizard.

    > [!NOTE]
    > If you want to change your existing custom domain name, you must upload a new SSL certificate and follow the steps as mentioned in this section.
    
### See also

[Microsoft Learn: Configure SSL certificates and custom domain names](/learn/modules/portals-administration/2-custom-domain)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]