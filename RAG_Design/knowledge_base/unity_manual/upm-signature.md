--- 
Source: Unity 6 Manual (upm-signature.md)
---

# Package signatures
Starting with Unity 6.3, the Package Manager checks for digital package signatures on all tarball packages used in the Unity ecosystem.
A package signature is a cryptographic identifier that helps verify where a package came from and ensures it wasn’t changed after the developer created it. Package signatures make it easier for everyone to confirm a package’s origin and integrity, and spot any unauthorized changes or tampering. The recommended best practice is for all publishers to sign their packages. Taking this simple step helps members of the Unity community feel more confident when using your packages.
The Package Manager window shows the status of a package’s signature. If the package has signature issues, the Package Manager window flags that package. The following table explains each status and what you can do to resolve issues.
| **Status icon** | **Contains a signature** | **Signing channel** | **Additional information** | **Recommended action** |
| --- | --- | --- | --- | --- |
| Icon showing signed package | Yes | Official Unity channels or your own organization. | N/A | Package is safe to use in your project. |
| Icon showing package signature FULL | Yes | Public channel or an organization you don’t belong to. | Make sure you understand where the package originates from. | Use these packages only if you’re certain of their source. If possible, try to get added to the organization that signed the package. |
| Icon showing package signature error | Yes, but is invalid. | Various | An invalid signature might indicate that the package has been tampered with, is unsafe, or malicious. | Consider removing this package from your project. |
| Icon showing package signature warning | No | N/A | To protect your project, the recommended best practice is to use only signed packages. | As a package consumer, ask the package owner to publish a version of the package with a signature, then install the signed version. As a package publisher, [sign your package](cus-export.html), then distribute the signed version. |
## Considerations for companies with multiple organizations defined in Unity Cloud
When a company has multiple organizations defined in [Unity Cloud](https://cloud.unity.com/), the Package Manager assigns package signature indicators based on the organization that signed each package. Company members outside that signing organization can still use the package, but they won’t get the same safety signals as those who belong to the signing organization.
To address this uneven experience that members might encounter, create a broader, shared organization and add all relevant members (or groups) to the new organization. Then, use [export](cus-export.html) to re-sign your packages using the new organization. For information about creating organizations, refer to [Create an organization](https://docs.unity.com/en-us/cloud/organizations/create-organization).
## Additional resources
* [Export and sign your UPM package](cus-export.html)
* [Share your package](cus-share.html)
* [Unity Editor command line arguments](EditorCommandLineArguments.html)