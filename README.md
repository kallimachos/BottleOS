Bottle on OpenShift
===================

A quickstart for Bottle + Python 2.6 running on OpenShift. Based on the OpenShift-authored version here: https://github.com/openshift-quickstart/bottle-openshift-quickstart


Running on OpenShift
----------------------------

Create an account at https://www.openshift.com/

Create a python application based on the code in this repository

    rhc app create bottle python-2.6 --from-code https://github.com/kallimachos/BottleOS.git

That's it, you can now checkout your application at:

    http://bottle-$yournamespace.rhcloud.com