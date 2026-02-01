--- 
Source: Unity 6 Manual (accelerator-monitor.md)
---

# Monitor Unity Accelerator
Unity **Accelerator**The Unity Accelerator is an external tool that provides an asset cache that keeps copies of a team’s imported assets. The goal of the Accelerator is to speed up teamwork and reduce iteration time by coordinating asset sharing so that you don’t need to reimport portions of your project. [More info](UnityAccelerator.html)
See in [Glossary](Glossary.html#Accelerator) has a built-in dashboard to monitor and configure changes.
The URL to access your dashboard is `http://hostname[:port]/dashboard` where `hostname:port` is the hostname/IP and port number of the Unity Accelerator you have installed. Note that the default port is `80` for http and `443` for https but you can change this after the installation.
Each Unity Accelerator hosts [Prometheus metric reports](https://prometheus.io/) as `http://hostname[:port]/metrics`, which you can query from the local network. For a full list of metrics monitoring, refer to [Unity Accelerator Prometheus metrics reference](accelerator-metrics-reference.html). The full configuration of Unity Accelerator is available through its unity-accelerator.cfg file.
## Additional resources
* [Unity Accelerator Prometheus metrics reference](accelerator-metrics-reference.html)
* [Configure Unity Accelerator in the Editor](accelerator-configure.html)