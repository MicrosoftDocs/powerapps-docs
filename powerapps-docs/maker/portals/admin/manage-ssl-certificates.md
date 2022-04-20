---
title: Add SSL certificates
description: Learn how to add an SSL custom certificate to enable custom domain names for your portal.
author: neerajnandwana-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 03/16/2022
ms.subservice: portals
ms.author: nenandw
ms.reviewer: ndoelman
contributors:
    - neerajnandwana-msft
    - nickdoelman
---

# Manage SSL certificates

You'll need an SSL certificate to set up a [custom host name](add-custom-domain.md). You can upload and update your own custom certificates by using the Power Apps portals admin center.

**To add a new certificate**
<!--note from editor: If you only have one H2, it's an orphan and you don't need it.-->
1. Open the [Power Apps portals admin center](admin-overview.md).

1. Select **Manage SSL certificates**. The certificate's subject name is displayed along with expiration date and thumbprint.

1. Select **Add new**.

1. Select the upload button underneath **File** to select a .pfx certificate file. After selecting the file, enter the password for your SSL certificate in the **Password** field.

1. Select **OK**.

    :::image type="content" source="media/manage-custom-certificates/upload-custom-certificate.png" alt-text="Upload a Certificate window with an Upload file button and password field.":::

     > [!NOTE]
     > The SSL certificate must meet all the following requirements:
     > - Be signed by a trusted certificate authority
     > - Be [exported](/powershell/module/pki/export-pfxcertificate) as a password-protected PFX file.
     > - Contain a private key at least 2,048 bits long
     > - Contain all intermediate certificates in the certificate chain
     > - Be SHA2-enabled; SHA1 support is being removed from popular browsers
     > - Be encrypted with Triple DES encryption; Power Apps portals doesn't support AES-256 encryption
     > - Contain<!--note from editor: Edit assumes that the certificate must be a PFX file.--> an [Extended Key Usage](https://en.wikipedia.org/w/index.php?title=X.509&section=4#Extensions_informing_a_specific_usage_of_a_certificate) for server authentication (OID = 1.3.6.1.5.5.7.3.1)
     > 
     > The steps to export an SSL certificate as a password-protected PFX file can vary depending on your certificate provider. Check with your certificate provider for recommendations. For example, certain providers might suggest using an OpenSSL third-party tool from the [OpenSSL](https://www.openssl.org/) or [OpenSSL Binaries](https://wiki.openssl.org/index.php/Binaries) sites. 

    :::image type="content" source="media/manage-ssl-certificates/ssl-certificates.png" alt-text="Manage SSL certificates tab in the Power Apps portals admin center." :::

### See also

[Add a custom domain name](add-custom-domain.md)<br>
[Microsoft Learn: Configure SSL certificates and custom domain names](/learn/modules/portals-administration/2-custom-domain)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
