---
title: Add SSL certificates
description: Learn how to to add a SSL custom certificate to enable custom domain names for your portal.
author: neerajnandwana-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 02/11/2022
ms.subservice: portals
ms.author: nenandw
ms.reviewer: ndoelman
contributors:
    - neerajnandwana-msft
    - nickdoelman
---

# Manage SSL certificates

You'll need an SSL certificate to set up a [custom host name](add-custom-domain.md). You can upload and update you own custom certificates using the Power Apps portals admin center.

## Add new certificate

1. Open the [Power Apps portals admin center](admin-overview.md).

1. Select **Manage SSL certificates**. The certificate’s subject name is displayed along with expiration date and thumbprint.

1. Select **Add new** to upload a new certificate.

1. Select the upload button underneath **File** to select a .pfx certificate file. After selecting the file, enter the password for your SSL certificate in the **Password** field.

1. Select **OK** to upload the certificate.

    :::image type="content" source="media/manage-custom-certificates/upload-custom-certificate.png" alt-text="Upload a Certificate window with Upload file button and password box.":::

     > [!NOTE]
     > The SSL certificate must meet all of the following requirements:
     > - Signed by a trusted certificate authority
     > - [Exported](/powershell/module/pki/export-pfxcertificate) as a password-protected PFX file.
     > - Contains private key at least 2048 bits long
     > - Contains all intermediate certificates in the certificate chain
     > - Must be SHA2 enabled; SHA1 support is being removed from popular browsers
     > - PFX file must be encrypted with TripleDES encryption; Power Apps portals doesn't support AES-256 encryption
     > - Contains an [Extended Key Usage](https://en.wikipedia.org/w/index.php?title=X.509&section=4#Extensions_informing_a_specific_usage_of_a_certificate) for server authentication (OID = 1.3.6.1.5.5.7.3.1).
     > 
     > The steps to export SSL certificate as a password-protected PFX file may vary depending on your certificate provider. Check with your certificate provider for recommendation. For example, certain providers may suggest using an OpenSSL third-party tool from [OpenSSL](https://www.openssl.org/) or [OpenSSL Binaries](https://wiki.openssl.org/index.php/Binaries) sites. 

    :::image type="content" source="media/manage-ssl-certificates/ssl-certificates.png" alt-text="Manage SSL certificates tab in the Power Apps portals admin center." :::

### See also
[Add a custom domain name](add-custom-domain.md)<br>
[Microsoft Learn: Configure SSL certificates and custom domain names](/learn/modules/portals-administration/2-custom-domain)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
